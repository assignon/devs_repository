<template>
  <div class="skills-core">
    <v-layout row justify-space-around align-center class="skills-layout">
      <v-flex xs12 sm12 md2 lg2 xl2 class="skills-flex">
        <h2 class="mt-5 mb-5">My Skills</h2>

        <div class="languages">
          <h4 class="mb-5">Languages</h4>
          <v-list rounded>
            <v-list-item-group v-model="skillsMenu" color="#41b883">
              <v-list-item
                v-for="(lang, i) in skills[0].language"
                :key="i"
                class="animated fadeInUp"
                :style="{ animationDelay: i * 0.3 + 's' }"
              >
                <v-list-item-icon>
                  <!-- <img
                    :src="
                      require(`../../../media/prog_langs/${getProgLangName(
                        lang.prog_lang_id
                      )}.svg`)
                    "
                    alt=""
                    :class="getProgLangName(lang.prog_lang_id)"
                  /> -->
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div>

        <!-- <div class="frameworks">
          <h4 class="mb-5">Frameworks</h4>
          <v-list rounded>
            <v-list-item-group v-model="skillsMenu" color="#41b883">
              <v-list-item
                v-for="(f, i) in skills[1].framework"
                :key="i"
                @click="
                  $vuetify.goTo(`#${getProgLangName(f.prog_lang_id)}`, options)
                "
                class="animated fadeInUp"
                :style="{ animationDelay: i * 0.3 + 's' }"
              >
                <v-list-item-icon>
                  <img
                    :src="
                      require(`../../../media/prog_langs/${getProgLangName(
                        f.prog_lang_id
                      )}.svg`)
                    "
                    alt=""
                    :class="getProgLangName(f.prog_lang_id)"
                  />
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title
                    v-text="getProgLangName(f.prog_lang_id)"
                  ></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div> -->

        <!-- <div class="pro-langs category mt-5">
                    <h3 class="animated fadeInUp" style="">Languages</h3>
                    <p
                            v-for="(lang, i) in skills[0].languages"
                            :key="i"
                            class="animated zoomIn"
                            :style="{animationDelay: `${i*0.5}s`,}"
                    >
                        <v-icon style="font-size: 7px;" class="mr-1">fas fa-circle</v-icon>
                        {{lang}}
                    </p>
                </div>
                <div class="frameworks category">
                    <h3 class="animated fadeInUp" style="animation-delay: 1s;">Frameworks</h3>
                    <p
                            v-for="(framework, i) in skills[1].frameworks"
                            :key="i"
                            class="animated zoomIn"
                            :style="{animationDelay: `${(i*0.5)+1}s`,}"
                    >
                        <v-icon style="font-size: 7px;" class="mr-1">fas fa-circle</v-icon>
                        {{framework}}
                    </p>
                </div>
                <div class="database category">
                    <h3 class="animated fadeInUp" style="animation-delay: 1.2s;">DataBase</h3>
                    <p
                            v-for="(db, i) in skills[2].databases"
                            :key="i"
                            class="animated zoomIn"
                            :style="{animationDelay: `${(i*1)+1}s`,}"
                    >
                        <v-icon style="font-size: 7px;" class="mr-1">fas fa-circle</v-icon>
                        {{db}}
                    </p>
                </div>
                <div class="other category">
                    <h3 class="animated fadeInUp" style="animation-delay: 1.5s;">Other</h3>
                    <p
                            v-for="(other, i) in skills[3].others"
                            :key="i"
                            class="animated zoomIn"
                            :style="{animationDelay: `${(i*1.5)+1}s`,}"
                    >
                        <v-icon style="font-size: 7px;" class="mr-1">fas fa-circle</v-icon>
                        {{other}}
                    </p>
                </div> -->
      </v-flex>

      <v-flex xs12 sm12 md10 lg10 xl10 class="skills-content-flex"> </v-flex>
    </v-layout>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import * as easings from "vuetify/es5/services/goto/easing-patterns";
export default {
  name: "Skills",

  data() {
    return {
      skillsMenu: 0, //v-list model
      // scrolling options
      duration: 400,
      offset: 50,
      easing: "easeInOutCubic",
      easings: Object.keys(easings)
      //   skills: [
      //     { languages: ["Python", "JavaScript"] },
      //     { frameworks: ["VueJs", "Django", "Flask"] },
      //     { databases: ["MySQL", "SQLite", "FireBase"] },
      //     { others: ["Html5", "CSS3", "Vuetify", "Git"] }
      //   ]
    };
  },

  computed: {
    ...mapGetters({
      skills: "skills/getSkills",
      progLangs: "skills/getProgLangs"
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
    this.allSkills();
  },

  mounted() {
    let self = this;
    console.log(self.getProgLangName(2));
  },

  methods: {
    allSkills() {
      /*
        get all skills from the DB
     */
      let self = this;
      this.$store.dispatch("skills/allSkills", {
        url: "skills/all_skills",
        params: {},
        callback: function(data) {
          console.log(data);
          self.$store.getters["skills/setSkills"](data.skills);
          self.$store.getters["skills/setProgLangs"](data.prog_langs);
        }
      });
    },

    getProgLangName(plId) {
      let self = this;
      this.allSkills();
      this.$store.dispatch("progLangName", {
        progLangId: plId,
        callback: function(data) {
          console.log(data);
          self.$store.getters["setProgLang"](data);
          console.log(self.$store.state.progLangArr);
        }
      });

      return self.$store.getters["getProgLang"][0]["name"];
    }
  }
};
</script>

<style scoped>
.skills-core {
  width: 100%;
  height: 95vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.skills-layout {
  width: 100%;
  height: 100%;
}

.skills-flex {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-end;
  background-color: #f5f5f5;
}
.theme--light.v-sheet {
  background-color: #f5f5f5;
  /* margin-top: 120px; */
}
.languages {
  width: 90%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  border: 1px solid red;
}
.skills-flex h2 {
  width: 100%;
  text-align: center;
  color: #16032c;
}

.skills-content-flex {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /*background-color: lightgray;*/
}

.category {
  width: 70%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}

.category h3 {
  color: #fff;
  text-align: left;
  margin-bottom: 7px;
  margin-top: 5px;
}

.category p {
  color: #fff;
  text-align: left;
  font-size: 16px;
  margin: 0px;
  margin-bottom: 7px;
  margin-left: 15px;
  cursor: pointer;
  font-weight: bold;
}

.category p .v-icon {
  color: white;
}

.category p:hover {
  color: #00ff8e;
}

.category p:hover .v-icon {
  color: #00ff8e;
  font-size: 3px;
}
/***************************  programminmg languages style  ***********************************/
.python {
  width: 25px;
  height: 25px;
}
.php {
  width: 30px;
  /* height: 40px; */
}
.vue {
  width: 30px;
  height: 30px;
}
.django {
  width: 30px;
  height: 30px;
}
.laravel {
  width: 30px;
  height: 30px;
}
.html5 {
  width: 30px;
  height: 30px;
}
.css3 {
  width: 30px;
  height: 30px;
}
.flask {
  width: 30px;
  height: 30px;
}
.flutter {
  width: 30px;
  height: 30px;
}
.javascript {
  width: 30px;
  height: 30px;
}
.dart {
  width: 30px;
  height: 30px;
}
.vuetify {
  width: 30px;
  height: 30px;
}
.git {
  width: 30px;
  height: 30px;
}
/**********************************************************************************************/
</style>