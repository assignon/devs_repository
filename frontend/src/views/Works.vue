<template>
  <div class="works-core">
    <v-layout column align-center class="works-layout">
      <v-flex xs12 sm12 md8 lg10 xl10 class="filter-flex">
        <div class="works-head">
          <div class="works-titel">
            <!-- <h2 class>My Works</h2>
            <v-divider width="5%" color="#16032c" style></v-divider>-->
            <div
              class="input-container animated fadeInUp"
              style="animation-delay:0.2s"
            >
              <input
                type="search"
                placeholder="search..."
                class="search-project"
                v-model="searchQuery"
                @focusin="startSearch()"
                @focusout="(searchMode = false), (searchEnter = false)"
                @keyup.enter="searchWorks()"
              />
              <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                  <div
                    class="question-icon-container"
                    v-bind="attrs"
                    v-on="on"
                    @click.stop="searchDialog = true"
                  >
                    <v-icon
                      style="cursor:pointer;font-size:18px;"
                      class="animated bounceIn"
                      >fas fa-question</v-icon
                    >
                  </div>
                </template>
                <span>How to use the search</span>
              </v-tooltip>
            </div>

            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-icon
                  medium
                  class="asc-icon ml-3 hidden-sm-and-down animated bounceIn"
                  v-bind="attrs"
                  v-on="on"
                  @click="orderByAsc()"
                  >fas fa-sort-amount-up</v-icon
                >
              </template>
              <span>old to newest</span>
            </v-tooltip>

            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-icon
                  medium
                  class="desc-icon ml-3 hidden-sm-and-down animated bounceIn"
                  v-bind="attrs"
                  v-on="on"
                  @click="orderByDesc()"
                  >fas fa-sort-amount-down</v-icon
                >
              </template>
              <span>newest to old</span>
            </v-tooltip>

            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-icon
                  medium
                  class="ml-3 hidden-sm-and-down animated bounceIn"
                  v-bind="attrs"
                  v-on="on"
                  @click="filtersVisible = !filtersVisible"
                  >fas fa-filter</v-icon
                >
              </template>
              <span>filter</span>
            </v-tooltip>
          </div>
        </div>
      </v-flex>

      <v-flex
        xs12
        sm12
        md8
        lg10
        xl10
        class="pl-flex animated"
        v-if="filtersVisible"
      >
        <v-radio-group v-model="filter" row>
          <div
            class="pl-container ml-5"
            v-for="(progLang, i) in progLangs"
            :key="i"
          >
            <!-- <v-radio label :color="progLang.color" :value="progLang.icon"></v-radio> -->
            <v-checkbox
              v-model="selected"
              class
              label
              :value="progLang.icon"
            ></v-checkbox>
            <v-icon medium>{{ progLang.icon }}</v-icon>
          </div>
        </v-radio-group>
      </v-flex>

      <WorksTemp
        :works="works"
        :h="height"
        :w="width"
        :reload="false"
        v-if="searchMode == false && foundedWorks.length == 0"
      />
      <div v-if="searchMode" class="nothing-founded-container">
        <div
          class="nothing-founded"
          v-if="foundedWorks.length == 0 && searchEnter"
        >
          <img
            src="../assets/projects/not-found.svg"
            alt
            class="animated fadeInUp"
          />
          <h2 class="animated fadeInUp" style="animation-delay:0.5s;">
            No works founded
          </h2>
        </div>

        <div class="focus-in" v-if="searchEnter == false">
          <!-- <WaitingLoader /> -->
          <TextAnimation
            :textArray="searchQueries"
            w="auto"
            h="auto"
            animation="bounceIn"
            color="#54bf8e"
            fs="30px"
            ta="center"
            :random="true"
            interval="7000"
            timeout="4000"
            display="flex"
          />
          <h2 class="animated fadeInUp" style="animation-delay:0.5s;">
            Waiting for your query
          </h2>
        </div>

        <!-- <WorksTemp :works="foundedWorks" v-if="foundedWorks.length != 0" /> -->
      </div>

      <WorksTemp
        :works="foundedWorks"
        :h="height"
        :w="width"
        :reload="false"
        v-if="foundedWorks.length != 0 || searchEnter"
      />

      <!-- <v-flex 12 xs sm12 md8 lg10 xl10 class="pagination-flex">
        <v-pagination v-model="page" :length="1" :total-visible="7"></v-pagination>
      </v-flex>-->
      <v-dialog v-model="searchDialog" max-width="700px">
        <div class="search-dialog-container" style="background-color: white;">
          <h4 class="mb-3">
            The search engine offers different ways and combinations to make
            more efficient searching and finding projects.
          </h4>
          <v-list>
            <v-list-item-group v-model="descMenu" color="#41b883">
              <v-list-item>
                <v-list-item-content>
                  <p>
                    project
                    <strong>type(s)</strong>,
                    <strong>programming language(s)</strong>,
                    <strong>tags</strong>
                    <br />e.g.
                    <br />
                    <kbd>website</kbd>
                  </p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p>
                    <strong>Combining</strong> queries <br />e.g.
                    <br />
                    <kbd>website+app+...</kbd> or
                    <kbd>website,app,pwa,...</kbd>
                  </p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p>
                    Search projects
                    <strong>before (&lt;)</strong>,
                    <strong>after (>)</strong> or on a
                    <strong>specific (=)</strong> date <br />e.g.
                    <br />
                    <kbd>>2020,09,13</kbd> or <kbd>&lt;2020</kbd> or
                    <kbd>=2020,09</kbd>
                  </p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p>
                    <strong>Combining</strong> queries and dates <br />e.g.
                    <br />
                    <kbd>website,pwa> 2020,09,13</kbd> or
                    <kbd>website&lt;2020</kbd> or
                    <kbd>website+pwa=2020,09</kbd>
                  </p>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <p>
                    <strong>built-in</strong> key words <br />e.g.
                    <br />
                    <kbd>newest</kbd> and
                    <kbd>oldest</kbd>
                  </p>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
          <p>
            <span style="color: magenta,font-weight:bold">i:</span> avoid
            putting spaces between words during combined searches. <br />Do:
            <span style>website,app,cli,...</span>
            <br />Not:
            <span style="text-decoration: line-through"
              >website, app, api, ...</span
            >
            <br />
          </p>
          <p>
            projects
            <strong>types</strong> values: website, mobile, app, cli, desktop
            app, ...
          </p>
          <p>
            projects
            <strong>tags</strong> values: cli, command line, cmd, terminal,
            site, pwa, responsive, programming language packages(e.g. colorama,
            pillow, vuetify, ...)
          </p>
        </div>
      </v-dialog>
    </v-layout>
  </div>
</template>

<script>
// import snackBar from "../../components/modals/snackBar";
import { mapGetters } from "vuex";
import WorksTemp from "../components/layouts/WorksTemp";
// import WaitingLoader from "../components/loaders/Waiting.loader";
import TextAnimation from "@/components/loaders/TextAnimation.vue";
export default {
  name: "Works",

  data() {
    return {
      valid: true, // search form v-model
      desc: true, // check if the projects are sorted order by desc
      page: 9, // pagination
      filter: "plFilter", // radio input model
      filtersVisible: false, // check if the radio iput div display is none orr not
      searchDialog: false, // search explaination dialog model
      selected: [], // selected checkboxes
      searchMode: false, // when user is searching
      searchEnter: false, // when the user hit enter key to search works
      searchQuery: "", // search field value
      descMenu: "", // search engine doc v model
      width: "300px", // works div container width
      height: "300px", // works div container height
      progLangs: [
        { icon: "fab fa-python", color: "black" },
        { icon: "fab fa-php", color: "black" },
        { icon: "fab fa-vuejs", color: "black" },
        { icon: "fas fa-terminal", color: "black" }
      ],
      searchQueries: [
        [`website or website+app+...`],
        ["pwa>2020 or webapp,cli,...<2020/09"],
        [">2020 or <2020/09 or >2020/09/14"]
      ]
    };
  },

  components: {
    WorksTemp: WorksTemp,
    // WaitingLoader: WaitingLoader,
    TextAnimation: TextAnimation
  },

  computed: {
    ...mapGetters({
      works: "work/getWorks",
      foundedWorks: "work/getSearchedWorks"
    })
  },

  created() {
    this.allWorks("default");
    this.$store.getters["work/getSearchedWorks"].length = 0;
    this.screenWidthChange();
    // let arr = this.$store.dispatch("splitToArray", "project,fields,work_type");
    console.log(this.splitToArray("project"));
  },

  methods: {
    screenWidthChange() {
      window.addEventListener("resize", function() {
        let screenSize = window.innerWidth;
        if (screenSize <= 500) {
          this.fontSize = "15px";
          this.width = "170px";
          this.height = "170px";
        }
      });

      let screenSize = window.innerWidth;
      if (screenSize <= 500) {
        this.fontSize = "15px";
        this.width = "170px";
        this.height = "170px";
      }
    },

    splitToArray(str) {
      /*
      split a string words in to array
      params:
        str: [str]: [string to split]
      returns: return array
      */
      let arr;
      if (str.includes("cli")) {
        let newStr = str.replace("cli", "terminal");
        arr = newStr.split(",");
        // arr = [];
        // split.forEach(function(item) {
        //   console.log(item);
        //   arr.push({ original: "cli", new: newStr });
        // });
      } else if (str.includes("website")) {
        let newStr = str.replace("website", "globe-africa");
        arr = newStr.split(",");
        // arr = [];
        // split.forEach(function(item) {
        //   console.log(item);
        //   arr.push({ original: "website", new: newStr });
        // });
      } else if (str.includes("app")) {
        let newStr = str.replace("app", "mobile");
        arr = newStr.split(",");
        // arr = [];
        // split.forEach(function(item) {
        //   console.log(item);
        //   arr.push({ original: "mobile", new: newStr });
        // });
      } else {
        arr = str.split(",");
      }
      return arr;
    },

    allWorks(orderBy) {
      /*
        get all works from the DB
        params:
          orderBy: [str]: [define the order of the data (ex: default=desc, desc, asc)]
      */
      let self = this;
      this.$store.dispatch("work/allWorks", {
        url: "works/all_works",
        params: { order_by: orderBy },
        callback: function(data) {
          console.log(JSON.parse(data));
          self.$store.getters["work/setWorks"](JSON.parse(data));
        }
      });
    },

    startSearch() {
      // when search field focus in
      this.$store.getters["work/getSearchedWorks"].length = 0;
      this.searchMode = true;
    },

    searchWorks() {
      /* when enter key hited */
      let self = this;
      this.searchEnter = true;
      // empty search field
      document.querySelector(".search-project").value = "";
      // send request
      this.$store.dispatch("work/searchWorks", {
        url: "works/search_works",
        params: { query: self.searchQuery },
        callback: function(data) {
          console.log(JSON.parse(data));
          if (self.$store.getters["work/getSearchedWorks"].length == 0) {
            self.searchMode = false;
          }
          // push founded works data to setSearchedWorks array
          self.$store.getters["work/setSearchedWorks"](JSON.parse(data));
        }
      });
    },

    orderByAsc() {
      // get works order by ascending
      document.querySelector(".asc-icon").style.display = "none";
      document.querySelector(".desc-icon").style.display = "block";
      this.allWorks("asc");
    },

    orderByDesc() {
      // get works order by descending
      document.querySelector(".desc-icon").style.display = "none";
      document.querySelector(".asc-icon").style.display = "block";
      this.allWorks("desc");
    }
  }
};
</script>

<style scoped>
.works-core {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-top: 70px;
  padding-bottom: 30px;
}
.works-layout {
  width: 100%;
  height: auto;
  justify-content: center;
}
.filter-flex {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
}
.works-head {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.works-titel {
  width: 70%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.input-container {
  border-radius: 50px;
  width: 60%;
  height: 45px;
  /* border: 1px solid #e0e0e0; */
  background-color: #e0e0e0;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.search-project {
  border-radius: 50px;
  border: 1px solid #e0e0e0;
  background-color: #fff;
  width: 93%;
  height: 100%;
  padding-left: 20px;
  text-align: left;
  font-size: 16px;
  font-weight: bold;
  color: #16032c;
}
.question-icon-container {
  width: 7%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.question-icon-container .v-icon:hover {
  color: #54bf8e;
}
.filter {
  width: 50%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
}
.desc-icon {
  display: none;
}
.pl-flex {
  width: 70%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
}
.pl-container {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
}
.pl-container .v-radio {
  margin-right: 0px;
}
.nothing-founded-container {
  width: 100%;
  height: 75vh;
  display: flex;
  /* flex-direction: row; */
  justify-content: center;
  align-items: center;
}
.nothing-founded,
.focus-in {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.nothing-founded img {
  width: 70px;
  height: 70px;
}
.focus-in h2 {
  position: relative;
  bottom: -40px;
}
/*.works-flex {*/
/*  width: 80%;*/
/*  height: auto;*/
/*  display: flex;*/
/*  flex-direction: row;*/
/*  flex-wrap: wrap;*/
/*  justify-content: space-around;*/
/*  align-items: center;*/
/*  margin-top: 80px;*/
/*}*/
/*.works-container {*/
/*  width: 300px;*/
/*  height: 300px;*/
/*  display: flex;*/
/*  flex-direction: column;*/
/*  justify-content: flex-start;*/
/*  align-items: center;*/
/*  border: 2px solid #16032c;*/
/*  background-color: #16032c;*/
/*  border-radius: 5px;*/
/*  margin-bottom: 45px;*/
/*  cursor: pointer;*/
/*}*/
/*.works-container:hover {*/
/*  transition: transform 0.2s linear 0s;*/
/*  transform: scale(0.9, 0.9);*/
/*}*/
/*.works-img {*/
/*  width: 100%;*/
/*  height: 80%;*/
/*  background-repeat: no-repeat;*/
/*  background-position: center;*/
/*  background-size: cover;*/
/*  border-radius: 3px;*/
/*}*/
/*.prog-langs-container {*/
/*  width: 95%;*/
/*  height: auto;*/
/*  display: flex;*/
/*  flex-direction: row;*/
/*  justify-content: flex-end;*/
/*  align-items: center;*/
/*}*/
/*.prog-langs {*/
/*  width: 30px;*/
/*  height: 30px;*/
/*  !* background-repeat: no-repeat;*/
/*  background-position: center;*/
/*  background-size: cover; *!*/
/*}*/
/*.works-name {*/
/*  width: 100%;*/
/*  height: 20%;*/
/*  display: flex;*/
/*  flex-direction: column;*/
/*  justify-content: center;*/
/*  align-items: center;*/
/*}*/
/*.works-name h4 {*/
/*  text-align: center;*/
/*  color: white;*/
/*}*/
/*.type-icon {*/
/*  width: 100%;*/
/*  height: auto;*/
/*  display: flex;*/
/*  flex-direction: row;*/
/*  justify-content: center;*/
/*  align-items: center;*/
/*}*/
.search-dialog-container {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-content: center;
  padding: 20px;
}
.v-list-item__content {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-content: center;
  padding: 0px;
}
.v-list-item__content p {
  width: 90%;
  text-align: left;
  font-size: 16px;
  color: #1b1127;
}
.v-application kbd {
  background-color: #54bf8e;
  padding: 2px;
  margin: 2px 0px 2px 0px;
}
.search-dialog-container p {
  color: #1b1127;
}
@media only screen and (max-width: 500px) {
  .works-core {
    padding-top: 40px;
  }
  .works-titel {
    width: 100%;
  }
  .input-container {
    width: 90%;
  }
  .search-project {
    width: 90%;
  }
  .question-icon-container {
    width: 10%;
  }
}
</style>
