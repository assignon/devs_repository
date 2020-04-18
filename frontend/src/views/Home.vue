<template>
  <div class="home-core">

    <v-layout
      row
      justify-space-around
      align-center
      class="home-layout"
    >

      <v-flex xs12 sm12 md12 xl12 class="landing-flex" id="homeTop">
        <div class="landing-first">
            <v-img
                alt=""
                class=""
                contain
                min-width="100"
                src='../assets/home/progr.png'
                width="100%"
                height="100%"
              />
        </div>
        <div class="landing-second">
            <h1 class="display-3 font-weight-bold mb-5 animated fadeInUp">Welcom in my world</h1>
            <p class="'mb-5 animated fadeInUp">
                Le Lorem Ipsum est simplement du faux
                texte employé dans la composition et la mise en page avant impression.
                texte employé dans la composition et la mise en page avant impression.
            </p>
            <div class="prog-langs">
                <v-icon
                        v-for="(tech, i) in technics" :key="i"
                        medium
                        color="white"
                        class="animated fadeInUp"
                        :style="{animationDelay: `${i/3}s`}">fab {{tech}}
                </v-icon>
            </div>
        </div>
        <div class="landing-last">
            <p>
                @main.command()<br>
                @click.option('--operatingsys', '-os', is_flag=True, help='Your operatingssystem, don t use it in a venv')<br>
                def install_yanr(operatingsys):<br>
                    <span style="margin-left: 20px;">if operatingsys:</span><br>
                    <span style="margin-left: 40px;">os.system('pip install --editable . --user')</span><br>
                    <span style="margin-left: 20px;">else:</span><br>
                        <span style="margin-left: 40px;">os.system('pip install --editable .')</span><br>
            </p>
        </div>
      </v-flex>

      <v-flex xs12 sm12 md12 xl12 class="skills-flex">
        <h2 class="skill-title">Hallo there</h2>
        <p class="skill-subtext">Is me Yanick</p>
        <div class="skills-container">
          <div class="skills" v-for="(skill, i) in skills" :key="i">
<!--              <div class="skills-img"-->
<!--                   :style="{backgroundImage: `url(${skill.imge})`}"-->
<!--              ></div>-->
              <v-img
                alt=""
                class="skills-img"
                contain
                min-width="100"
                :src="skill.imge"
                width="100"
                data-aos="zoom-in" :data-aos-delay="i*150" data-aos-duration="500"
              />
              <h3 data-aos="fade-up" :data-aos-delay="i*(160*4)" data-aos-duration="500">
                  {{skill.name}}
              </h3>
              <p data-aos="fade-up" :data-aos-delay="i*(170*4)" data-aos-duration="500">
                  {{skill.content}}
              </p>
            </div>
        </div>
      </v-flex>

      <v-flex xs12 sm12 md12 xl12 class="about-flex" id="about">
          <div class="about-overlay">
              <h1 class="about-title display-3 font-weight-bold" data-aos="fade-up" data-aos-duration="500">About me</h1>
          </div>
          <About/>
      </v-flex>

      <v-flex xs12 sm12 md12 xl12 class="contact-flex" id="contact">
<!--          <h3>Contact Me</h3>-->
          <Contact/>
      </v-flex>

    </v-layout>

  </div>
</template>

<script>
// @ is an alias to /src
import About from "@/components/layouts/About.vue";
import Contact from "@/components/layouts/Contact.vue";

export default {
  name: "Home",
  components: {
      About: About,
      Contact: Contact
  },

  data() {
    return{
      skills: [
        {name: 'Web Development', imge: require('../assets/home/wd.svg'), content: 'Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. '},
        {name: 'Scripting/CLI', imge: require('../assets/home/cmdline.svg'), content: 'Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression.'},
        {name: 'Api', imge: require('../assets/home/api.svg'), content: 'Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression.'}
      ],
       technics: [
           'fa-python',
           'fa-js-square',
           'fa-vuejs',
           'fa-python',
           'fa-html5',
           'fa-html5',
           'fa-css3-alt',
           'fa-php',
       ]
    }
  },

  created(){

  },

  methods:{

  }
};
</script>

<style scoped>
  .home-core{
    width: 100%;
    height: auto;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .home-layout{
    width: 100%;
    height: auto;
  }

  .landing-flex{
    width: 100%;
    height: 90vh;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    background-color: #16032c;
  }

  /*.landing-flex div{*/
  /*    width: 30%;*/
  /*    !*border: 1px solid white;*!*/
  /*}*/

  .landing-first{
      width: 33%;
      /*background-image: url('../assets/home/progr.png');*/
      background-repeat: no-repeat;
      background-size: cover;
      background-position: center;
      /*width: 150px;*/
      height: 100%;
  }

  .landing-second{
      width: 35%;
      height: 80%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
  }

  .landing-second h1, .landing-second p{
      color: #00FF8E;
      text-align: center;
  }

  .prog-langs{
      width: 100%;
      height: auto;
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      justify-content: center;
      align-items: center;
  }

  .prog-langs .v-icon{
      font-size: 25px;
      margin-right: 10px;
      margin-left: 10px;
  }

  .skills-flex{
    width: 100%;
    height: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 100px;
    margin-bottom: 100px;
    /*background-color: lightgray;*/
  }

  .landing-last{
      width: 30%;
      border: 1px solid white;
  }

  .landing-last p{
      font-size: 17px;
      color: white;
      text-align: left;
      width: 100%;
      height: auto;
  }

  .skill-title{
    text-align: center;
  }

  .skill-subtext{
    text-align: center;
    font-size: 15px;
  }

  .skills-container{
    width: 100%;
    height: auto;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    align-items: flex-start;
  }

   .skills{
    width: 27%;
    height: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-left: 20px;
    margin-right: 20px;
  }

  .skills .skills-img{
    /*background-repeat: no-repeat;*/
    /*background-size: contain;*/
    /*background-position: center;*/
    /*width: 150px;*/
    /*height: 150px;*/
    margin-bottom: 10px;
  }

  .skills h3{
    text-align: center;
    margin-bottom: 10px;
  }

  .skills p{
    text-align: center;
    font-size: 15px;
  }

  .about-flex{
      width: 100%;
      height: auto;
      min-height: 100vh;
      background-color: #FAFAFA;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      /*margin-top: 10vh;*/
      /*border: 1px solid red;*/
  }

  .about-overlay{
      width: 100%;
      height: 450px;
      background-image: url('../assets/home/about.jpg');
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
      display: flex;
      justify-content: center;
      align-items: center;
  }

  .about-flex .about-title{
      color: white;
      /*margin-top: 100px;*/
      /*margin-bottom: 50px;*/
  }

    .contact-flex{
      width: 100%;
      height: 100vh;
      /*background-color: #FAFAFA;*/
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
</style>
