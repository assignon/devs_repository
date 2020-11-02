<template>
  <div class="skills-core">
    <v-layout class="skills-layout">
      <v-flex xs12 sm12 md4 lg4 xl4 class="skills-flex">
        <!-- mobile version -->
        <div class="mobile-menu hidden-md-and-up">
          <div
            class="mobile-menu-container"
            v-for="(item, i) in progLangs"
            :key="i"
          >
            <v-chip
              @click="
                $vuetify.goTo(
                  `#${item.name}`,
                  options,
                  (active = true),
                  clickedChip()
                )
              "
              class="mr-2 animated fadeInUp pl-5 pr-5"
              :style="{ animationDelay: i * 0.3 + 's' }"
            >
              <img
                :src="require(`../../../media/prog_langs/${item.name}.svg`)"
                alt=""
                :class="item.name"
              />

              <p style="margin:auto; text-transform: capitalize;" class="ml-3">
                {{ item.name }}
              </p>
            </v-chip>
          </div>
        </div>
        <!-- laptop, desktop version -->
        <h2 class="mt-5 mb-5 hidden-sm-and-down">My Skills</h2>
        <!-- programming languages skills -->
        <div class="languages  hidden-sm-and-down">
          <h4 class="mb-5">Languages</h4>
          <v-list rounded>
            <v-list-item-group v-model="skillsMenu" color="#41b883">
              <v-list-item
                v-for="(lang, i) in skills[0].language"
                :key="i"
                @click="$vuetify.goTo(`#${lang.prog_lang}`, options)"
                class="animated fadeInUp"
                :style="{ animationDelay: i * 0.3 + 's' }"
              >
                <v-list-item-icon>
                  <img
                    :src="
                      require(`../../../media/prog_langs/${lang.prog_lang}.svg`)
                    "
                    alt=""
                    :class="lang.prog_lang"
                  />
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title
                    v-text="lang.prog_lang"
                  ></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div>
        <!-- frameworks skills -->
        <div class="frameworks hidden-sm-and-down">
          <h4 class="mb-5">Frameworks</h4>
          <v-list rounded>
            <v-list-item-group color="#41b883">
              <v-list-item
                v-for="(f, i) in skills[1].framework"
                :key="i"
                @click="$vuetify.goTo(`#${f.prog_lang}`, options)"
                class="animated fadeInUp"
                :style="{ animationDelay: i * 0.3 + 's' }"
              >
                <v-list-item-icon>
                  <img
                    :src="
                      require(`../../../media/prog_langs/${f.prog_lang}.svg`)
                    "
                    alt=""
                    :class="f.prog_lang"
                  />
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="f.prog_lang"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div>
        <!-- other skills -->
        <div class="others hidden-sm-and-down">
          <h4 class="mb-5">DataBase</h4>
          <v-list rounded>
            <v-list-item-group color="#41b883">
              <v-list-item
                v-for="(db, i) in skills[2].database"
                :key="i"
                @click="$vuetify.goTo(`#${db.prog_lang}`, options)"
                class="animated fadeInUp"
                :style="{ animationDelay: i * 0.3 + 's' }"
              >
                <v-list-item-icon>
                  <img
                    :src="
                      require(`../../../media/prog_langs/${db.prog_lang}.svg`)
                    "
                    alt=""
                    :class="db.prog_lang"
                  />
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="db.prog_lang"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div>
        <!-- database skills -->
        <div class="db hidden-sm-and-down">
          <h4 class="mb-5">Other</h4>
          <v-list rounded>
            <v-list-item-group color="#41b883">
              <v-list-item
                v-for="(o, i) in skills[3].other"
                :key="i"
                @click="$vuetify.goTo(`#${o.prog_lang}`, options)"
                class="animated fadeInUp"
                :style="{ animationDelay: i * 0.3 + 's' }"
              >
                <v-list-item-icon>
                  <img
                    :src="
                      require(`../../../media/prog_langs/${o.prog_lang}.svg`)
                    "
                    alt=""
                    :class="o.prog_lang"
                  />
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="o.prog_lang"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div>
      </v-flex>

      <v-flex xs12 sm12 md8 lg8 xl8 class="skills-content-flex">
        <div v-for="(skill, s) in skills" :key="s">
          <div v-for="(obj, o) in skill" :key="o">
            <div
              class="skills-content"
              :id="item.prog_lang"
              v-for="(item, i) in obj"
              :key="i"
            >
              <h3>{{ item.prog_lang }}</h3>
              <p v-html='item.content'></p>
            </div>
          </div>
        </div>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import * as easings from "vuetify/es5/services/goto/easing-patterns";
// import Vue from "vue";
export default {
  name: "Skills",

  data() {
    return {
      skillsMenu: 0, //v-list model
      // scrolling options
      duration: 400,
      offset: 120,
      easing: "easeInOutCubic",
      easings: Object.keys(easings),
      skillsCategories: ["language", "framework", "other", "database"],
      active: false, // click outside model(refere to vuetify click outside directive)
    };
  },

  computed: {
    ...mapGetters({
      skills: "skills/getSkills",
      progLangs: "skills/getProgLangs",
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
        easing: this.easing,
      };
    },
  },

  created() {
    // let self = this;
    this.allSkills().then();
  },

  mounted() {},

  methods: {
    clickedChip() {
      if (this.active) {
        // change children color and background-color
        event.currentTarget.style.backgroundColor = "#e0eee7";
        let child = event.currentTarget.childNodes[0];
        child.children[0].style.color = "#42b883";
        child.children[1].style.color = "#42b883";
      }
    },

    async allSkills() {
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
        },
      });
    },

    // getProgLangName(plId) {
    //   let self = this;
    //   this.allSkills();
    //   this.$store.dispatch("progLangName", {
    //     progLangId: plId,
    //     callback: function(data) {
    //       console.log(data);
    //       self.$store.getters["setProgLang"](data);
    //       // console.log(self.$store.state.progLangArr);
    //     }
    //   });

    //   return self.$store.getters["getProgLang"][0]["name"];
    // }
  },
};
</script>

<style scoped>
.skills-core {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

.skills-layout {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: space-around;
  align-items: center;
  height: auto;
}
.skills-flex {
  width: 15%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-end;
  background-color: #f5f5f5;
  position: fixed;
  top: 0px;
  left: 0px;
  overflow-y: scroll;
  padding-top: 80px;
}
.mobile-menu {
  width: auto;
  height: auto;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  overflow-x: scroll;
  margin-top: 20px;
}
.menu-container {
  width: auto;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
  position: fixed;
  top: 0px;
  left: 0px;
}
.mobile-menu-container {
  width: auto;
  height: auto;
  padding-bottom: 10px;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: flex-start;
}
::-webkit-scrollbar {
  width: 0px;
}
.theme--light.v-sheet {
  background-color: #f5f5f5;
  /* margin-top: 120px; */
}
::-webkit-scrollbar {
  width: 0px;
}
.languages,
.db,
.others,
.frameworks {
  width: 90%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
}
.skills-flex h2 {
  width: 100%;
  text-align: center;
  color: #16032c;
}

.skills-content-flex {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: flex-end;
  margin-top: 10px;
  /*background-color: lightgray;*/
}

/* .skills-content-flex div {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
} */

.skills-content-flex .skills-content {
  width: 70%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  margin-left: 70px;
}

.skills-content h3 {
  text-align: left;
  margin-bottom: 7px;
  margin-top: 30px;
  text-transform: capitalize;
}

.skills-content p {
  text-align: left;
  font-size: 16px;
}

/***************************  programminmg languages style  ***********************************/
.python {
  width: 25px;
  height: 20px;
}
.php {
  width: 30px;
  height: 20px;
}
.vue {
  width: 30px;
  height: 20px;
}
.django {
  width: 30px;
  height: 20px;
}
.laravel {
  width: 30px;
  height: 20px;
}
.html5 {
  width: 30px;
  height: 20px;
}
.css3 {
  width: 30px;
  height: 20px;
}
.flask {
  width: 30px;
  height: 20px;
}
.flutter {
  width: 30px;
  height: 20px;
}
.javascript {
  width: 30px;
  height: 20px;
}
.dart {
  width: 30px;
  height: 20px;
}
.vuetify {
  width: 30px;
  height: 20px;
}
.git,
.sqlite,
.firebase,
.mysql {
  width: 30px;
  height: 20px;
}
/**********************************************************************************************/
@media only screen and (max-width: 500px) {
  .skills-layout {
    flex-direction: column;
  }
  .skills-flex {
    flex-direction: row;
    /* position: relative; */
    padding-top: 60px;
    height: auto;
    width: 100%;
    background-color: #fff;
  }
  .skills-content-flex {
    padding-top: 50px;
  }
  .git,
  .sqlite,
  .firebase,
  .mysql,
  .vuetify,
  .dart,
  .javascript,
  .flutter,
  .flask,
  .css3,
  .html5,
  .laravel,
  .django,
  .vue,
  .php,
  .python {
    width: 20px;
    height: 20px;
  }
  .skills-content-flex .skills-content {
    width: 80%;
    margin-left: 30px;
  }
}
</style>
