<template>
  <div class="desc-core animated fadeIn">
    <v-layout row justify-center align-center class="desc-layout">
      <v-flex xs10 sm10 md2 lg2 xl2 class="desc-side-flex">
        <div class="menu-container">
          <!-- <ul>
            <li v-for="(item, i) in splitToArray(desc[0].menu)" :key="i">{{item}}</li>
          </ul>-->
          <v-list rounded>
            <!-- <v-subheader>REPORTS</v-subheader> -->
            <v-list-item-group v-model="descMenu" color="#41b883">
              <v-list-item
                v-for="(item, i) in splitToArray(desc[0].menu)"
                :key="i"
                @click="$vuetify.goTo(`#${item}`, options)"
                class="animated fadeInUp"
                :style="{animationDelay: i*0.3+'s',}"
              >
                <v-list-item-icon>
                  <v-icon>{{iconTransformer(item)}}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                  <v-list-item-title v-text="item"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </div>
      </v-flex>

      <!-- <v-flex xs10 sm10 md10 lg10 xl10 class="desc-content-flex">{{desc[0].description}}</v-flex> -->
      <v-flex xs10 sm10 md10 lg10 xl10 class="desc-content-flex">
        <div id="install">
          <h2>Install</h2>
          <p>
            Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le
            faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme
            assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte.
            Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique,
            sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente
            de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion
            dans des applications de mise en page de texte, comme Aldus PageMaker. assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte.
            Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique,
            sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente
            de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion
            dans des applications de mise en page de texte, comme Aldus PageMake assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte.
            Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique,
            sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente
            de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion
            dans des applications de mise en page de texte, comme Aldus PageMake
          </p>
        </div>
        <div id="idea">
          <h2>Idea</h2>
          <p>
            Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le
            faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme
            assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte.
            Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique,
            sans que son contenu n'en soit modifié.faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme
            assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte.
            Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique,
            sans que son contenu n'en soit modifié.
          </p>
        </div>
        <div id="content">
          <h2>Content</h2>
          <p>
            Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique,
            sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente
            de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion
            dans des applications de mise en page de texte,sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente
            de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion
            dans des applications de mise en page de texte,
          </p>
        </div>
        <div id="technics">
          <h2>Technics</h2>
          <p>
            e Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le
            faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme
            assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte.
            Il n'a pas fait que ssans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente
            de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion
            dans des applications de mise en page de texte,sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente
            de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion
            dans des applications de mise en page de texte,
          </p>
        </div>
        <div id="use">
          <h2>Use</h2>
          <p>
            Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique,
            sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente
            de feuilles Letraset contenant des passages du Losans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à la vente
            de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus récemment, par son inclusion
            dans des applications de mise en page de texte,
          </p>
        </div>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import * as easings from "vuetify/es5/services/goto/easing-patterns";
export default {
  name: "Description",

  data() {
    return {
      workName: this.$route.params.name,
      descMenu: 1, //v-list model
      // scrolling options
      duration: 400,
      offset: 50,
      easing: "easeInOutCubic",
      easings: Object.keys(easings)
    };
  },

  computed: {
    ...mapGetters({
      desc: "description/getDesc"
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
    this.getDescription(); //get cuurent work descrion
  },

  methods: {
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

    getDescription() {
      let self = this;
      this.$store.dispatch("description/getDescription", {
        url: "description/work_desc",
        params: { work_name: self.workName },
        callback: function(data) {
          console.log(data);
          self.$store.getters["description/setDesc"](data);
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
  background-color: #f5f5f5;
}
.menu-container {
  width: 15%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  background-color: #f5f5f5;
  position: fixed;
  top: 0px;
  left: 0px;
}
.theme--light.v-sheet {
  background-color: #f5f5f5;
  margin-top: 120px;
}
.menu-container ul {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  margin-top: 120px;
  /* margin-left: 30px; */
}
.menu-container ul li {
  list-style: none;
  font-size: 17px;
  font-weight: bold;
  margin-bottom: 50px;
  text-transform: capitalize;
}
.desc-content-flex {
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 70px;
}
.desc-content-flex div {
  width: 70%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  margin-bottom: 20px;
}
.desc-content-flex div h2 {
  text-align: left;
  margin-bottom: 10px;
}
.desc-content-flex div p {
  text-align: left;
  font-size: 16px;
  width: 70%;
}
</style>