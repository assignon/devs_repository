<template>
  <div class="works-core">
    <v-layout column justify-center align-center class="works-layout">
      <v-flex xs12 sm12 md8 lg10 xl10 class="filter-flex">
        <div class="works-head">
          <div class="works-titel">
            <h2 class>My Works</h2>
            <v-divider width="5%" color="#16032c" style></v-divider>
          </div>

          <div class="filter">
            <v-icon medium v-if="desc">fas fa-sort-amount-up</v-icon>
            <v-icon medium v-if="!desc">fas fa-sort-amount-down</v-icon>
            <v-icon medium>fab fa-python</v-icon>
          </div>
        </div>
      </v-flex>

      <v-flex xs12 sm12 md8 lg10 xl10 class="pl-flex">
        <v-radio-group v-model="ex7" row>
          <div class="pl-container" v-for="(progLang, i) in progLangs" :key="i">
            <v-radio label :color="progLang.color" :value="progLang.icon"></v-radio>
            <v-icon medium>fab fa-{{progLang.icon}}</v-icon>
          </div>
        </v-radio-group>
      </v-flex>

      <!-- <div class="works-container"> -->
      <v-flex xs10 sm10 md4 lg4 xl4 class="works-flex">
        <div class="works-container" v-for="(project, i) in projects" :key="i">
          <div class="works-img" :style="{backgroundImage: `url(${project.img})`}">
            <v-icon medium v-for="(progicon, pi) in project.progIcon" :key="pi">fab fa-{{progicon}}</v-icon>
          </div>
          <div class="works-name">
            <h3 class="mb1">{{project.name}}</h3>
            <v-divider width="10%" color="#fff" style></v-divider>
            <div class="type-icon mt-2">
              <v-icon
                style="font-size:15px;color:white;"
                class="ml-2 mr-2"
                v-for="(typeicon, ti) in project.typeIcon"
                :key="ti"
              >fas fa-{{typeicon}}</v-icon>
            </div>
          </div>
        </div>
      </v-flex>
      <!-- </div> -->

      <v-flex 12 xs sm12 md8 lg10 xl10 class="pagination-flex">
        <v-pagination v-model="page" :length="15" :total-visible="7"></v-pagination>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
export default {
  name: "Works",

  data() {
    return {
      valid: true, // search form v-model
      desc: true, // check if the projects are sorted order by desc
      page: 1, // pagination
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

  created() {},

  methods: {}
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
}
.works-layout {
  width: 100%;
  height: auto;
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
  width: 50%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: flex-end;
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
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.pl-container {
  width: auto;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: flex-start;
  border: 1px solid red;
}
.works-flex {
  width: 80%;
  height: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
}
.works-container {
  width: 30%;
  height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  border: 2px solid #16032c;
  background-color: #16032c;
  border-radius: 5px;
  margin-bottom: 45px;
}
.works-img {
  width: 100%;
  height: 320px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  border-radius: 3px;
}
.works-name {
  width: 100%;
  height: 80px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.works-name h3 {
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