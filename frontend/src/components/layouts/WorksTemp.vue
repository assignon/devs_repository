<template>
  <v-flex xs10 sm10 md4 lg4 xl4 class="works-flex">
    <div
      class="works-container animated fadeInUp"
      :style="{ animationDelay: i * 0.3 + 's', width: w, height: h }"
      v-for="(project, i) in works"
      :key="i"
      @click.stop="$router.push(`/work/${project.fields.name}`), reloadState()"
    >
      <div
        class="works-img"
        :style="{
          backgroundImage: `url(${require(`../../../../media/${project.fields.image}`)})`,
        }"
      >
        <div class="prog-langs-container pt-3">
          <img
            class="prog-langs"
            :src="require(`../../../../media/prog_langs/${progicon}.svg`)"
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
        <h4 class="mb1">
          {{ project.fields.name }}
          <!-- <span class="date-added">2W ago</span> -->
        </h4>
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
                class="ml-2 mr-2 hidden-sm-and-down"
                v-bind="attrs"
                v-on="on"
                >fas fa-{{ typeicon }}</v-icon
              >
            </template>
            <span></span>
          </v-tooltip>
        </div>
      </div>
    </div>
  </v-flex>
</template>

<script>
// import { mapGetters } from "vuex";
export default {
  name: "worksTemp",

  data() {
    return {
      progLangs: [
        { icon: "fab fa-python", color: "black" },
        { icon: "fab fa-php", color: "black" },
        { icon: "fab fa-vuejs", color: "black" },
        { icon: "fas fa-terminal", color: "black" },
      ],
    };
  },

  props: ["works", "w", "h", "reload"],

  computed: {
    // ...mapGetters({
    //   works: "work/getWorks"
    // })
  },

  created() {},

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

    reloadState() {
      if (this.reload) {
        location.reload();
      }
    },

    // worksDate(datetime) {
    //   let dateSplited = datetime.split("T");
    //   let date = dateSplited[0];
    //   let splitedTime = dateSplited[1].split(".");
    //   let time = splitedTime[0];

    //   let calculateDate = null;
    //   let calculateTime = null;

    //   if (calculateDate < 7) {
    //     // days
    //   } else if (calculateDate >= 7 && calculateDate < 30) {
    //     // weeks
    //     let weekModulo = calculateDate % 7;
    //     if (weekModulo == 0) {
    //       //round week(1, 2, 3week)
    //     } else {
    //       // float week
    //       let getWeek = weekModulo.toString().split(",");
    //       //return week +(1+week)
    //     }
    //   } else if (calculateDate > 30) {
    //     // years
    //     let yearModulo = calculateDate % 30;
    //     if (yearModulo == 0) {
    //       // round year
    //     } else {
    //       let getYear = yearModulo.toString().split(",");
    //     }
    //   } else if (calculateDate == 0) {
    //     // hours
    //   }
    // },
  },
};
</script>

<style scoped>
.works-flex {
  width: 80%;
  height: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
  margin-top: 80px;
}
.works-container {
  /* width: 300px;
  height: 300px; */
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
.date-added {
  font-size: 12px;
  padding: 0px 5px 0px 5px;
  border: 1px solid white;
  border-radius: 50px;
  color: #16032c;
  background-color: white;
  position: relative;
  left: 10px;
  font-weight: bold;
}
.type-icon {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
@media only screen and (max-width: 500px) {
  .works-container {
    margin-bottom: 20px;
  }
  .works-flex {
    width: 100%;
    margin-top: 50px;
  }
  .works-container h4 {
    font-size: 13px;
  }
}
</style>
