<template>
  <v-app>
    <!--        <v-img-->
    <!--          alt="Vuetify Name"-->
    <!--          class="shrink mt-1 hidden-sm-and-down"-->
    <!--          contain-->
    <!--          min-width="100"-->
    <!--          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"-->
    <!--          width="100"-->
    <!--        />-->
    <Nav />
    <v-content>
      <router-view class="'animated fadeIn"></router-view>
    </v-content>
  </v-app>
</template>

<script>
import Nav from "./components/layouts/Nav";

export default {
  name: "App",

  components: {
    Nav
  },

  data: () => ({
    //
  }),

  created() {
    this.$root.log = function log() {
      for (let i = 0; i < arguments.length; i += 1) {
        if (typeof arguments[i] === "object") {
          try {
            arguments[i] = JSON.parse(JSON.stringify(arguments[i]));
          } catch (e) {
            console.error(e);
          }
        }
      }
      console.log(...arguments);
    };
  },

  methods: {
    scrollTopAnimation() {
      let scrollValue = document.documentElement.scrollTop;
      while (scrollValue > 0) {
        document.documentElement.scrollTop--;
      }
    }
  }
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Amita");
@import url("https://fonts.googleapis.com/css?family=Arbutus+Slab");
html,
body {
  scroll-behavior: smooth;
  overflow-x: hidden;
  width: 100%;
  margin: 0px;
  padding: 0px;
  font-family: "Arbutus Slab", Helvetica, Arial, sans-serif;
}
#app {
  /* scroll-behavior: smooth; */
  font-family: "Arbutus Slab", Helvetica, Arial, sans-serif;
  margin: 0px;
  padding: 0px;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  /* overflow-x: hidden; */
}
</style>
