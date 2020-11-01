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

    <!-- <v-tab-item
      class="tab-item interess-tab tabs"
      style="background-color: #FAFAFA;box-shadow: none;"
      v-for="(content, c) in about"
      :key="c"
    >
      <p class="animated fadeInUp">
        {{ content.fields.content }}
      </p>
    </v-tab-item> -->

    <!-- interes tab content -->
    <v-tab-item
      class="tab-item interess-tab tabs"
      style="background-color: #FAFAFA;box-shadow: none;"
    >
      <p class='mb-5 interess-intro'>
          After going through all the things I could do and realize with the programming languages,
          two things caught my curiosity and interest. These two things that I spend most of my time
          to learn more about and become a specialist.
        </p>
      <div class='interess-container mt-5'>
        <div v-for='(interess, i) in interesses' :key='i' class='interesses'>
          <v-icon style='font-size: 50px;color:#16032c' class='mb-3'> fas fa-{{interess.icon}}</v-icon>
          <h4 class='mb-5'>{{interess.titel}}</h4>
          <p>{{interess.content}}</p>
        </div>
      </div>
      <!-- <p class="animated fadeInUp">
        {{about[0].fields.content}}
      </p> -->
    </v-tab-item>
    <!-- study tab content -->
    <v-tab-item
      class="tab-item interess-tab tabs"
      style="background-color: #FAFAFA;box-shadow: none;"
    >
      <p class="animated fadeInUp">
        <Timeline />
      </p>
    </v-tab-item>
    <!-- hobby tab content -->
    <v-tab-item
      class="tab-item hobby-tab tabs"
      style="background-color: #FAFAFA;box-shadow: none;"
    >
      <!-- <p class="animated fadeInUp">
        {{about[2].fields.content}}
      </p> -->
      <div v-for="(hobby, i) in hobbies" :key='i' class='hobby-container'>
        <v-icon style='font-size: 50px' class='mb-3'>fas fa-{{hobby.icon}}</v-icon>
        <h4>{{hobby.name}}</h4>
      </div>
    </v-tab-item>
  </v-tabs>
</template>

<script>
import { mapGetters } from "vuex";
import Timeline from "@/components/layouts/Timeline.vue";
export default {
  name: "About",

  data() {
    return {
      tab: null,
      interesses: [
        {
          icon: 'brain',
          titel: 'AI',
          content: ''
        },
        {
          icon: 'robot',
          titel: 'Robotic',
          content: ''
        }
      ],
      hobbies:[
        {
          icon: 'futbol',
          name: 'Footbal',
          content: ''
        },
        {
          icon: 'pencil-ruler',
          name: 'Drawing',
          content: ''
        },
      ]
    };
  },

  components:{
    Timeline: Timeline
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
.interess-tab{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.hobby-tab{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}
.interess-container{
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.interesses{
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.interess-intro{
width:70%;
}
.interesses p{
  font-size: 16px;
  text-align: center;
}
@media only screen and (max-width: 500px) {
  .about-tab {
    width: 100%;
  }
  .tabs p {
    width: 80%;
    text-align: left;
  }
  .interess-intro{
    width: 100%;
  }
}
</style>