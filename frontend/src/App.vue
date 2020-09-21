<template>
  <v-app id="app" app>
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
  })
};
</script>

<style scoped>
html,
body {
  scroll-behavior: smooth;
  overflow-x: hidden;
  width: 100%;
  margin: 0px;
  padding: 0px;
}
#app {
  /* scroll-behavior: smooth; */
  margin: 0px;
  padding: 0px;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  /* overflow-x: hidden; */
}
</style>
