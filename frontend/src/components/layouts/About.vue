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
           v-for="(name, i) in tabsName"
           :ripple="false"
           :key="i"
           style="background: transparent; color: black;"
           class="font-weight-bold tabs-name"
        >
            {{name.name}}
            <v-icon medium>{{name.icon}}</v-icon>
        </v-tab>

        <v-tab-item
           class="tab-item interess-tab"
           style="background-color: #FAFAFA;box-shadow: none;"
        >
            <p class="animated fadeInUp">
                Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise
                en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie
                depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de
                texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que
                survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans
                que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 grâce à
                la vente de feuilles Letraset contenant des passages du Lorem Ipsum, et, plus
                récemment, par son inclusion dans des applications de mise en page de texte, comme
                Aldus PageMaker.
            </p>
        </v-tab-item>

        <v-tab-item>

        </v-tab-item>

        <v-tab-item>

        </v-tab-item>
    </v-tabs>
</template>

<script>
    export default {
        name: "About",

        data(){
            return {
                tab: null,
                tabsName: [
                    {name:'Interess', icon: ''},
                    {name:'Study', icon: ''},
                    {name:'Hobby', icon: ''}
                ]
            }
        }
    }
</script>

<style scoped>
    .about-tab{
        width: 70%;
        height: auto;
        margin: auto;
    }

    .tabs-name{
        text-transform: capitalize;
        font-size: 16px;
    }

    .interess-tab{
        padding-top: 50px;
    }

    .interess-tab p{
        text-align: center;
        font-size: 16px;
    }
</style>