<template>
    <div class="skills-core">
        <v-layout row justify-space-around align-center class="skills-layout">
            <v-flex xs12 sm12 md2 lg2 xl2 class="skills-flex">
                <h2 class="mt-5 mb-2">My Skills</h2>
                <div class="pro-langs category mt-5">
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
                </div>
            </v-flex>

            <v-flex xs12 sm12 md10 lg10 xl10 class="skills-content-flex">

            </v-flex>
        </v-layout>
    </div>
</template>

<script>
    export default {
        name: "Skills",

        data(){
            return{
                skills:[
                    {languages: ['Python', 'JavaScript']},
                    {frameworks: ['VueJs', 'Django', 'Flask']},
                    {databases: ['MySQL', 'SQLite', 'FireBase']},
                    {others: ['Html5', 'CSS3', 'Vuetify', 'Git']}
                ]
            }
        }
    }
</script>

<style scoped>
  .skills-core{
    width: 100%;
    height: 95vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .skills-layout{
    width: 100%;
    height: 100%;
  }

  .skills-flex{
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-end;
    background-color: #222;
  }

  .skills-flex h2{
      width: 100%;
      text-align: center;
      color: white;
  }

  .skills-content-flex{
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    /*background-color: lightgray;*/
  }

    .category{
        width: 70%;
        height: auto;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: flex-start;
    }

    .category h3{
        color: #fff;
        text-align: left;
        margin-bottom: 7px;
        margin-top: 5px;
    }

    .category p{
        color: #fff;
        text-align: left;
        font-size: 16px;
        margin: 0px;
        margin-bottom: 7px;
        margin-left: 15px;
        cursor: pointer;
        font-weight: bold;
    }

    .category p .v-icon{
        color: white;
    }

    .category p:hover{
        color: #00FF8E;
    }

    .category p:hover .v-icon{
        color: #00FF8E;
        font-size: 3px;
    }
</style>