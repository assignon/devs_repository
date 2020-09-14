<template>
  <div class="works-core">
    <v-layout column align-center class="works-layout">
      <v-flex xs12 sm12 md8 lg10 xl10 class="filter-flex mb-5">
        <div class="works-head">
          <div class="works-titel">
            <!-- <h2 class>My Works</h2>
            <v-divider width="5%" color="#16032c" style></v-divider>-->
            <div class="input-container animated fadeInUp" style="animation-delay:0.2s">
              <input
                type="search"
                placeholder="search..."
                class="search-project"
                @keyup.enter="searchWorks()"
              />
              <v-icon
                style="position:relative;right:20px;cursor:pointer;font-size:18px;"
                class="animated bounceIn"
              >fas fa-question</v-icon>
            </div>

            <v-icon medium v-if="desc" class="ml-3 animated bounceIn">fas fa-sort-amount-up</v-icon>
            <v-icon medium v-if="!desc" class="ml-3 animated bounceIn">fas fa-sort-amount-down</v-icon>
            <v-icon medium class="ml-3 animated bounceIn">fas fa-filter</v-icon>
          </div>
        </div>
      </v-flex>

      <v-flex xs12 sm12 md8 lg10 xl10 class="pl-flex animated" v-if="filtersVisible">
        <v-radio-group v-model="filter" row>
          <div class="pl-container" v-for="(progLang, i) in progLangs" :key="i">
            <v-radio label :color="progLang.color" :value="progLang.icon"></v-radio>
            <v-icon medium>fab fa-{{ progLang.icon }}</v-icon>
          </div>
        </v-radio-group>
      </v-flex>

      <!-- <div class="works-container"> -->
      <v-flex xs10 sm10 md4 lg4 xl4 class="works-flex">
        <div
          class="works-container animated fadeInUp"
          :style="{animationDelay: i*0.3+'s',}"
          v-for="(project, i) in works"
          :key="i"
          @click.stop="$router.push(`/work/${project.fields.name}`)"
        >
          <div
            class="works-img"
            :style="{ backgroundImage: `url(${require(`../../../media/${project.fields.image}`)})` }"
          >
            <div class="prog-langs-container pt-3">
              <img
                class="prog-langs"
                :src="require(`../../../media/prog_langs/${progicon}.svg`)"
                v-for="(progicon, pi) in splitToArray(project.fields.prog_lang)"
                :key="pi"
                alt
              />
              <!-- <div
                class="prog-langs"
                v-for="(progicon, pi) in splitToArray(project.fields.prog_lang)"
                :key="pi"
                :style="{ backgroundImage: `url(${require(`../../../media/prog_langs/${progicon}.svg`)})` }"
              ></div>-->
            </div>
          </div>
          <div class="works-name">
            <h4 class="mb1">{{ project.fields.name }}</h4>
            <v-divider width="10%" color="#fff" style></v-divider>
            <div class="type-icon mt-2">
              <v-tooltip
                bottom
                v-for="(typeicon, ti) in splitToArray(project.fields.work_type)"
                :key="ti"
              >
                <template v-slot:activator="{ on, attrs }">
                  <v-icon
                    style="font-size:15px;color:white;"
                    class="ml-2 mr-2"
                    v-bind="attrs"
                    v-on="on"
                  >fas fa-{{ typeicon }}</v-icon>
                </template>
                <span></span>
              </v-tooltip>
            </div>
          </div>
        </div>
      </v-flex>
      <!-- </div> -->

      <!-- <v-flex 12 xs sm12 md8 lg10 xl10 class="pagination-flex">
        <v-pagination v-model="page" :length="1" :total-visible="7"></v-pagination>
      </v-flex>-->
    </v-layout>
  </div>
</template>

<script>
// import snackBar from "../../components/modals/snackBar";
import { mapGetters } from "vuex";
export default {
  name: "Works",

  data() {
    return {
      valid: true, // search form v-model
      desc: true, // check if the projects are sorted order by desc
      page: 9, // pagination
      filter: "plFilter", // radio input model
      filtersVisible: false, // check if the radio iput div display is none orr not
      progLangs: [
        { icon: "python", color: "black" },
        { icon: "php", color: "black" },
        { icon: "vuejs", color: "black" },
        { icon: "terminal", color: "black" }
      ],
      projects: [
        {
          img: require("../assets/projects/test.jpg"),
          progIcon: ["python", "vuejs"],
          name: "Co2ok",
          typeIcon: ["globe-africa"]
        },
        {
          img: require("../assets/projects/test.jpg"),
          progIcon: ["vuejs"],
          name: "Define Shipping",
          typeIcon: ["mobile", "globe-africa"]
        },
        {
          img: require("../assets/projects/test.jpg"),
          progIcon: ["php"],
          name: "Podium De Flux",
          typeIcon: ["globe-africa"]
        },
        {
          img: require("../assets/projects/test.jpg"),
          progIcon: ["python"],
          name: "Project Creator",
          typeIcon: ["terminal"]
        },
        {
          img: require("../assets/projects/test.jpg"),
          progIcon: ["python", "vuejs"],
          name: "Co2ok",
          typeIcon: ["mobile", "terminal", "globe-africa"]
        },
        {
          img: require("../assets/projects/test.jpg"),
          progIcon: ["python", "vuejs"],
          name: "Co2ok",
          typeIcon: ["mobile", "terminal", "globe-africa"]
        },
        {
          img: require("../assets/projects/test.jpg"),
          progIcon: ["python", "vuejs"],
          name: "Co2ok",
          typeIcon: ["mobile", "terminal", "globe-africa"]
        },
        {
          img: require("../assets/projects/test.jpg"),
          progIcon: ["python", "vuejs"],
          name: "Co2ok",
          typeIcon: ["mobile", "terminal", "globe-africa"]
        },
        {
          img: require("../assets/projects/test.jpg"),
          progIcon: ["python", "vuejs"],
          name: "Co2ok",
          typeIcon: ["mobile", "terminal", "globe-africa"]
        }
      ]
    };
  },

  computed: {
    ...mapGetters({
      works: "work/getWorks"
    })
  },

  created() {
    this.allWorks();
    // let arr = this.$store.dispatch("splitToArray", "project,fields,work_type");
    console.log(this.splitToArray("project"));
  },

  methods: {
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

    allWorks() {
      let self = this;
      this.$store.dispatch("work/allWorks", {
        url: "works/all_works",
        params: {},
        callback: function(data) {
          console.log(JSON.parse(data));
          self.$store.getters["work/setWorks"](JSON.parse(data));
        }
      });
    },

    searchWorks() {
      console.log("hallo there");
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
.filter {
  width: 50%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
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
  align-items: flex-start;
}
.works-flex {
  width: 80%;
  height: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
  margin-top: 70px;
}
.works-container {
  width: 300px;
  height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 2px solid #16032c;
  background-color: #16032c;
  border-radius: 5px;
  margin-bottom: 45px;
  cursor: pointer;
}
.works-container:hover {
  transition: transform 0.2s linear 0s;
  transform: scale(0.9, 0.9);
}
.works-img {
  width: 100%;
  height: 80%;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  border-radius: 3px;
}
.prog-langs-container {
  width: 95%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
}
.prog-langs {
  width: 30px;
  height: 30px;
  /* background-repeat: no-repeat;
  background-position: center;
  background-size: cover; */
}
.works-name {
  width: 100%;
  height: 20%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.works-name h4 {
  text-align: center;
  color: white;
}
.type-icon {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
</style>
