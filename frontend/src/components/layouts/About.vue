<template>
  <v-tabs
    v-model="tab"
    background-color="transparent"
    dark
    icons-and-text
    fixed-tabs
    slider-color="#16032c"
    style="box-shadow: none;background-color: #fafafa;"
    class="about-tab"
  >
    <v-tab
      v-for="(name, i) in about"
      :ripple="false"
      :key="i"
      style="background: transparent; color: black;"
      class="font-weight-bold tabs-name"
    >
      {{ name.fields.tab_name }}
      <!-- <v-icon medium>{{ name.icon }}</v-icon> -->
    </v-tab>

    <v-tab-item
      class="tab-item interess-tab tabs"
      style="background-color: #FAFAFA;box-shadow: none;"
      v-for="(content, c) in about"
      :key="c"
    >
      <p class="animated fadeInUp">
        {{ content.fields.content }}
      </p>
    </v-tab-item>
  </v-tabs>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "About",

  data() {
    return {
      tab: null
    };
  },

  computed: {
    ...mapGetters({
      about: "getAbout"
    })
  },

  created() {
    this.aboutContent();
  },

  methods: {
    aboutContent() {
      let self = this;
      this.$store.dispatch("about", {
        params: {},
        callback: function(data) {
          self.$store.getters["setAbout"](JSON.parse(data));
        }
      });
    }
  }
};
</script>

<style scoped>
.about-tab {
  width: 70%;
  height: auto;
  margin: auto;
}

.tabs-name {
  text-transform: capitalize;
  font-size: 16px;
}

.tabs {
  padding-top: 50px;
}

.tabs p {
  text-align: center;
  font-size: 16px;
  margin: auto;
}
@media only screen and (max-width: 500px) {
  .about-tab {
    width: 100%;
  }
  .tabs p {
    width: 80%;
    text-align: left;
  }
}
</style>