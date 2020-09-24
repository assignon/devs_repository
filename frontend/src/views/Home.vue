<template>
  <div class="home-core">
    <v-layout row justify-space-around align-center class="home-layout">
      <v-flex xs12 sm12 md12 xl12 class="landing-flex" id="homeTop">
        <div class="landing-cover"></div>

        <div class="landing-container">
          <div class="container-one">
            <div>
              <h1
                class="display-3 font-weight-bold mb-5 animated fadeInUp"
                style="animation-delay: 0.2s"
              >Welcome in my world</h1>
              <p class="mb-5 animated fadeInUp" style="animation-delay: 0.6s">
                Le Lorem Ipsum est simplement du faux texte employé dans la
                composition et la mise en page avant impression. texte employé
                dans la composition et la mise en page avant impression.
              </p>
              <router-link to="works" style="text-decoration:none">
                <v-btn
                  class="works-btn animated bounceIn"
                  style="animation-delay: 1s"
                  large
                  color="#00FF8E"
                >My Works</v-btn>
              </router-link>
            </div>
            <!-- <div class="prog-langs">
              <v-icon
                v-for="(tech, i) in technics"
                :key="i"
                medium
                color="white"
                class="animated fadeInUp"
                :style="{ animationDelay: `${i / 3}s` }"
                >fab {{ tech }}
              </v-icon>
            </div>-->
          </div>

          <TextAnimation
            :textArray="codes"
            w="50%"
            h="100%"
            animation="bounceIn"
            color="white"
            fs="25px"
            ta="left"
            :random="true"
            interval="60000"
            timeout="90000"
            display="inline-block"
          />
        </div>
        <!-- <div class="landing-first">
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
        </div>-->
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
              alt
              class="skills-img"
              contain
              min-width="100"
              :src="skill.imge"
              width="100"
              data-aos="zoom-in"
              :data-aos-delay="i * 150"
              data-aos-duration="500"
            />
            <h3
              data-aos="fade-up"
              :data-aos-delay="i * (160 * 4)"
              data-aos-duration="500"
            >{{ skill.name }}</h3>
            <p
              data-aos="fade-up"
              :data-aos-delay="i * (170 * 4)"
              data-aos-duration="500"
            >{{ skill.content }}</p>
          </div>
        </div>
      </v-flex>

      <v-flex xs12 sm12 md12 xl12 class="about-flex" id="about">
        <h1
            class="about-title display-3 font-weight-bold mb-5"
            data-aos="fade-up"
            data-aos-duration="500"
          >About me</h1>
        <About />
      </v-flex>

      <v-flex xs12 sm12 md12 xl12 class="contact-flex" id="contact">
        <!--          <h3>Contact Me</h3>-->
        <Contact />
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
// @ is an alias to /src
import About from "@/components/layouts/About.vue";
import Contact from "@/components/layouts/Contact.vue";
import TextAnimation from "@/components/loaders/TextAnimation.vue";

export default {
  name: "Home",

  components: {
    About: About,
    Contact: Contact,
    TextAnimation: TextAnimation
  },

  data() {
    return {
      skills: [
        {
          name: "Web Development",
          imge: require("../assets/home/wd.svg"),
          content:
            "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. "
        },
        {
          name: "Scripting/CLI",
          imge: require("../assets/home/cmdline.svg"),
          content:
            "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression."
        },
        {
          name: "Api",
          imge: require("../assets/home/api.svg"),
          content:
            "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression."
        }
      ],
      technics: [
        "fa-python",
        "fa-js-square",
        "fa-vuejs",
        "fa-python",
        "fa-html5",
        "fa-html5",
        "fa-css3-alt",
        "fa-php"
      ],
      codes: [
        [
          `
        def python(str):?
          if  "name"  ==  "__main__":|
            user_input  =  input("give your name")|
            print(user_input)
        `
        ],
        [
          `function% javascript(str){?
          let% userInput = document.getElementById('input');?
          if%(userInput != ''){|
            console.log(userInput.value);?
          }else{|
            alert('field is empty')?
          }#
        }
        `
        ],
        [
          ` @csrf_exempt#
            @action(methods=['get'], detail=False)#
            def all_works(self, request):#
            """?
            get all works from DB?#

            Args:|
                request ([get]): [get works]#
            """?
            order_by = request.query_params.get('order_by')?
            if order_by == 'default':|
                works = Works.objects.all().order_by('-pk')?
            elif order_by == 'asc':|
                works = Works.objects.all().order_by('pk')?
            else:|
                works = Works.objects.all().order_by('-pk'))#?

            return Response(serializers.serialize('json', works))
        `
        ]
      ]
    };
  },

  created() {
    // this.animateText();
  },

  mounted() {
    // this.animateText();
  },

  methods: {
    // animateText() {
    //   let textContainer = document.querySelector(".container-two");
    //   // let counter = 0;
    //   this.texts[1].forEach((t, index) => {
    //     // counter++;
    //     let p = document.createElement("p");
    //     p.className = "code-line animated fadeIn";
    //     p.style.animationDelay = `${index}s`;
    //     p.style.fontSize = "20px";
    //     p.style.textAlign = "left";
    //     p.style.textTransform = "bold";
    //     for (let i = 0; i < t.length; i++) {
    //       let spans = document.createElement("span");
    //       spans.textContent = t[i];
    //       spans.className = "animated bounceIn";
    //       spans.style.animationDelay = `${i / 7}s`;
    //       p.appendChild(spans);
    //       if (t[i] == "?") {
    //         p.innerHTML += "<br/>";
    //         p.innerHTML += "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
    //       } else if (t[i] == "|") {
    //         p.innerHTML += "<br/>";
    //         p.innerHTML +=
    //           "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
    //       } else if (t[i] == "#") {
    //         p.innerHTML += "<br/>";
    //       }
    //     }
    //     textContainer.appendChild(p);
    //     console.log(p);
    //   });
    // }
  }
};
</script>

<style scoped>
.home-core {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

.home-layout {
  width: 100%;
  height: auto;
}

.landing-flex {
  width: 100%;
  height: 95vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: url("../assets/home/homeBackground.jpg");
  background-position: cente;
  background-size: cover;
  background-repeat: no-repeat;
}

.landing-cover {
  width: 100%;
  height: 95vh;
  display: flex;
  background-color: #16032c;
  opacity: 0.8;
  position: absolute;
  top: 0px;
}

.landing-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.container-one {
  width: 50%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.container-one div {
  width: 70%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
}

.container-one h1,
.container-one p {
  color: #fff;
  text-align: left;
}

.container-one p {
  width: 100%;
  font-size: 17px;
}

.works-btn {
  color: #16032c;
  font-size: 20px;
  font-weight: bold;
  text-transform: capitalize;
}

.container-two {
  width: 50%;
  height: 100%;
  display: flex;
  color: white;
  border: 1px solid whitesmoke;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  /* background-image: url("../assets/home/homeBackground.jpg");
  background-position: cente;
  background-size: cover;
  background-repeat: no-repeat; */
}
.code-line {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: flex-start;
}

.prog-langs {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: flex-start;
  border: 1px solid white;
}

.prog-langs .v-icon {
  font-size: 25px;
  margin-right: 10px;
  margin-left: 10px;
}

/*.landing-flex div{*/
/*    width: 30%;*/
/*    !*border: 1px solid white;*!*/
/*}*/

.landing-first {
  width: 33%;
  /*background-image: url('../assets/home/progr.png');*/
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  /*width: 150px;*/
  height: 100%;
}

.skills-flex {
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

.landing-last {
  width: 30%;
  border: 1px solid white;
}

.landing-last p {
  font-size: 17px;
  color: white;
  text-align: left;
  width: 100%;
  height: auto;
}

.skill-title {
  text-align: center;
}

.skill-subtext {
  text-align: center;
  font-size: 15px;
}

.skills-container {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
}

.skills {
  width: 27%;
  height: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-left: 20px;
  margin-right: 20px;
}

.skills .skills-img {
  /*background-repeat: no-repeat;*/
  /*background-size: contain;*/
  /*background-position: center;*/
  /*width: 150px;*/
  /*height: 150px;*/
  margin-bottom: 10px;
}

.skills h3 {
  text-align: center;
  margin-bottom: 10px;
}

.skills p {
  text-align: center;
  font-size: 15px;
}

.about-flex {
  width: 100%;
  height: auto;
  /*min-height: 100vh;*/
  background-color: #fafafa;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-bottom: 50px;
  padding-top: 50px;
  /*margin-top: 10vh;*/
}

.about-overlay {
  width: 100%;
  height: 450px;
  background-image: url("../assets/home/about.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.about-flex .about-title {
  color: #17102d;
  /*margin-top: 100px;*/
  /*margin-bottom: 50px;*/
}

.contact-flex {
  width: 100%;
  height: 100vh;
  /*background-color: #FAFAFA;*/
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
