<template>
  <div class="desc-core animated fadeIn">
    <v-layout row justify-center align-center class="desc-layout">
      <v-flex xs12 sm12 md2 lg2 xl2 class="desc-side-flex">
        <div class="mobile-menu">
          <div class="mobile-menu-container hidden-md-and-up pa-5">
            <v-chip
              v-for="(item, i) in splitToArray(desc[0].menu)"
              :key="i"
              @click="
                $vuetify.goTo(
                  `#${item}`,
                  options,
                  (active = true),
                  clickedChip()
                )
              "
              class="mr-2 animated fadeInUp pl-5 pr-5"
              :style="{ animationDelay: i * 0.3 + 's' }"
            >
              <v-icon left small>
                {{ iconTransformer(item) }}
              </v-icon>
              <a
                :href="desc[0].url"
                target="_blank"
                style="text-decoration: none; color:#717171"
                v-if="item == 'url'"
                >url</a
              >
              <p
                v-if="item != 'url' && item != 'github'"
                style="margin:auto; text-transform: capitalize;"
              >
                {{ item }}
              </p>
              <a
                :href="desc[0].repository"
                target="_blank"
                style="text-decoration: none; color: #717171"
                v-if="item == 'github'"
                >github</a
              >
            </v-chip>
          </div>
        </div>

        <div class="menu-container hidden-sm-and-down">
          <router-link to="/works" style="text-decoration: none;">
            <div class="back-to-container animated fadeInUp">
              <v-icon color="#16032c">fas fa-chevron-left</v-icon>
              <p>Works</p>
            </div>
          </router-link>

          <v-list rounded>
            <!-- <v-subheader>REPORTS</v-subheader> -->
            <v-list-item-group v-model="descMenu" color="#41b883">
              <v-list-item
                v-for="(item, i) in splitToArray(desc[0].menu)"
                :key="i"
                @click="$vuetify.goTo(`#${item}`, options)"
                class="animated fadeInUp"
                :style="{ animationDelay: i * 0.3 + 's' }"
              >
                <v-list-item-icon>
                  <v-icon>{{ iconTransformer(item) }}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                  <a
                    :href="desc[0].url"
                    target="_blank"
                    style="text-decoration: none; color:#717171"
                    v-if="item == 'url'"
                    >url</a
                  >
                  <v-list-item-title
                    v-text="item"
                    v-if="item != 'url' && item != 'github'"
                  ></v-list-item-title>
                  <a
                    :href="desc[0].repository"
                    target="_blank"
                    style="text-decoration: none; color: #717171"
                    v-if="item == 'github'"
                    >github</a
                  >
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>

          <!-- <div
            class="related-works animated fadeInUp"
            @click.stop="(drawer = !drawer), worksRelated()"
          >
            <v-btn
              rounded
              large
              color="#42b883"
              dark
              outlined
              class="related-works-btn"
            >
              Related Works
            </v-btn>
          </div> -->
        </div>
      </v-flex>

      <!-- <v-flex xs10 sm10 md10 lg10 xl10 class="desc-content-flex">{{desc[0].description}}</v-flex> -->
      <v-flex xs10 sm10 md10 lg10 xl10 class="desc-content-flex mb-5">
        <div
          class="desc-content-header animated fadeInUp"
          style="animation-delay: 0.4s"
        >
          <h2>
            <span style="color: #54bf8e;">{{ workName }}</span> Work Description
          </h2>
          <v-divider width="5%" color="#16032c" style></v-divider>
        </div>
        <div class="desc-container animated fadeIn"></div>
      </v-flex>

      <v-navigation-drawer
        absolute
        v-model="drawer"
        temporary
        overlay-color="#54bf8e"
        right
        class="related-works-drawer"
        :width="rwdw"
      >
        <div v-if="relatedWorks.length == 0" class="nothing-founded-container">
          <div class="nothing-founded">
            <img
              src="../assets/projects/not-found.svg"
              alt
              class="animated fadeInUp"
            />
            <h2 class="animated fadeInUp" style="animation-delay:0.5s;">
              No related works founded
            </h2>
          </div>
        </div>

        <div class="related-works" v-else>
          <WorksTemp :works="relatedWorks" h="250px" w="250px" :reload="true" />
        </div>
      </v-navigation-drawer>
    </v-layout>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import * as easings from "vuetify/es5/services/goto/easing-patterns";
import WorksTemp from "../components/layouts/WorksTemp";
export default {
  name: "Description",

  data() {
    return {
      workName: this.$route.params.name,
      descMenu: 0, //v-list model
      // scrolling options
      duration: 400,
      offset: 50,
      easing: "easeInOutCubic",
      easings: Object.keys(easings),
      drawer: false, // related works drawer model
      active: false, // click outside model(refere to vuetify click outside directive)
      rwdw: "50%" // related works drawer width
    };
  },

  components: {
    WorksTemp: WorksTemp
  },

  computed: {
    ...mapGetters({
      desc: "description/getDesc",
      relatedWorks: "work/getRelatedWorks"
    }),

    target() {
      const value = this[this.type];
      if (!isNaN(value)) return Number(value);
      else return value;
    },

    options() {
      return {
        duration: this.duration,
        offset: this.offset,
        easing: this.easing
      };
    }
  },

  created() {
    let self = this;
    this.getDescription().then(); //get cuurent work descrion
    setTimeout(() => {
      self.descriptionContent();
    }, 500);

    if (window.innerWidth <= 500) {
      // change related works drawer width on mobile
      this.rwdw = "100%";
    }

    // window.addEventListener("scroll", self.displayMenuBar);
  },

  mounted() {
    // let self = this;
    // window.addEventListener("scroll", self.displayMenuBar());
  },

  methods: {
    onClickOutside() {
      this.active = false;
    },

    clickedChip() {
      // let scrollValue = document.documentElement.scrollTop;
      let self = this;
      let mobileNav = document.querySelector(".mobile-menu-layout");
      if (this.active) {
        // ]hide menu bar if chip clicked
        mobileNav.style.display = "none";
        mobileNav.style.transition = "opacity 0.5s linear 0.1s";
        mobileNav.classList.add("slideInUp");

        // change chips container position to fixed
        let grandParent = event.currentTarget.parentNode.parentNode;

        // change children color and background-color
        event.currentTarget.style.backgroundColor = "#e0eee7";
        let child = event.currentTarget.childNodes[0];
        child.children[0].style.color = "#42b883";
        child.children[1].style.color = "#42b883";
        // hide and show menu bar base on scroll value
        window.addEventListener("scroll", function() {
          self.displayMenuBar(grandParent);
        });
      }
    },

    displayMenuBar(grandParent) {
      let scrollValue = document.documentElement.scrollTop;
      let mobileNav = document.querySelector(".mobile-menu-layout");

      if (scrollValue == 0) {
        mobileNav.style.display = "flex";
        mobileNav.style.transition = "opacity 0.5s linear 0.1s";
        mobileNav.classList.remove("slideInUp");
        mobileNav.classList.add("slideInDown");
        // change chip granparent position to relative
        grandParent.style.position = "relative";
        grandParent.style.top = "0px";
        grandParent.style.backgroundColor = "none";
      } else {
        mobileNav.style.display = "none";
        mobileNav.style.transition = "opacity 0.5s linear 0.1s";
        mobileNav.classList.remove("slideInDown");
        mobileNav.classList.add("slideInUp");
        // check if menu bar is visible
        grandParent.style.position = "fixed";
        grandParent.style.top = "-20px";
        grandParent.style.zIndex = "5";
        grandParent.style.backgroundColor = "white";
      }
    },

    splitToArray(str) {
      let arr = str.split(",");
      return arr;
    },

    iconTransformer(str) {
      let icon;
      if (str == "install") {
        icon = str.replace(str, "fas fa-download");
      } else if (str == "content") {
        icon = str.replace(str, "fas fa-align-right");
      } else if (str == "technics") {
        icon = str.replace(str, "fas fa-tools");
      } else if (str == "use") {
        icon = str.replace(str, "fas fa-question");
      } else if (str == "idea") {
        icon = str.replace(str, "fas fa-lightbulb");
      } else if (str == "github") {
        icon = str.replace(str, "fab fa-github");
      } else if (str == "url") {
        icon = str.replace(str, "fas fa-link");
      } else {
        icon = str.replace(str, str);
      }
      return icon;
    },

    async getDescription() {
      let self = this;
      this.$store.dispatch("description/getDescription", {
        url: "description/work_desc",
        params: { work_name: self.workName },
        callback: function(data) {
          console.log(data);
          self.$store.getters["description/setDesc"](data);
        }
      });
    },

    descriptionContent() {
      /*
        loop throught description file content get back from de DB
        and append it into the html
      */
      let descContent = this.desc; // get descriptiom obj array
      let descContainer = document.querySelector(".desc-container");
      descContent.forEach(data => {
        descContainer.innerHTML += data.description;
      });
    },

    worksRelated() {
      let self = this;
      this.$store.dispatch("work/getRelatedWorks", {
        url: "works/related_works",
        params: { work_name: self.workName },
        callback: function(data) {
          console.log(data);
          self.$store.getters["work/setRelatedWorks"](JSON.parse(data));
          console.log(self.$store.getters["work/getRelatedWorks"]);
        }
      });
    }
  }
};
</script>

<style scoped>
.desc-core {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  /* z-index: 6; */
}
.desc-layout {
  width: 100%;
  height: 100%;
}
.desc-side-flex {
  height: 95vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  /* background-color: #f5f5f5; */
}
.mobile-menu {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  overflow-x: scroll;
  margin-top: 20px;
}
.mobile-menu-container {
  width: auto;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: flex-start;
}
::-webkit-scrollbar {
  width: 0px;
}
.menu-container {
  width: 15%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
  background-color: #f5f5f5;
  position: fixed;
  top: 0px;
  left: 0px;
}
.back-to-container {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  position: relative;
  top: 50px;
  margin-left: 20px;
  cursor: pointer;
}
.back-to-container p {
  font-size: 16px;
  text-align: left;
  margin: auto;
  margin-left: 10px;
  font-weight: bold;
  color: #16032c;
}
.theme--light.v-sheet {
  background-color: #f5f5f5;
  /* margin-top: 120px; */
}
.related-works {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  /* position: relative;
  top: 100px; */
  margin-left: 20px;
  cursor: pointer;
}
.related-works-btn {
  font-size: 16px;
  text-transform: capitalize;
}
.related-works p {
  font-size: 16px;
  text-align: left;
  margin: auto;
  margin-left: 10px;
  font-weight: bold;
  color: #16032c;
}
.desc-content-flex {
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* margin-top: 70px; */
}
.desc-content-flex .desc-content-header {
  width: 100%;
  height: 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.desc-container {
  width: 70%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}
.desc-container #install {
  width: 70%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  margin-bottom: 20px;
}
.desc-container h2 {
  text-align: left;
  margin-bottom: 10px;
}
.desc-container p {
  text-align: left;
  font-size: 16px;
  width: 70%;
}
.related-works-drawer {
  display: flex;
  /* flex-direction: column; */
  justify-content: flex-start;
  align-items: center;
  overflow-y: scroll;
  top: 0px;
  /* z-index: 5; */
  /* margin: 0px;
  padding: 0px; */
}
.related-works {
  width: 100%;
  height: auto;
  display: flex;
  /* flex-direction: row;
  flex-wrap: wrap; */
  justify-content: space-around;
  align-items: center;
}
.related-works .works-flex {
  width: 100%;
  justify-content: center;
  border: 1px solid green;
}
.nothing-founded-container {
  width: 100%;
  height: 75vh;
  display: flex;
  /* flex-direction: row; */
  justify-content: center;
  align-items: center;
}
.nothing-founded {
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
@media only screen and (max-width: 500px) {
  .desc-side-flex {
    height: auto;
  }
  .desc-container {
    width: 100%;
  }
  .desc-container h2 {
    font-size: 15px;
  }
  .desc-content-flex .desc-content-header {
    height: 70px;
  }
}
</style>