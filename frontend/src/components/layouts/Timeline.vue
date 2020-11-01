<template>
    <div class='timeline-core'>
        <v-timeline
    align-top
    :dense="$vuetify.breakpoint.smAndDown"
  >
    <v-timeline-item
      v-for="(item, i) in items"
      :key="i"
      :color="item.color"
      medium
    >
      <template v-slot:opposite>
        <span
          :style='{color: item.color}'
          v-text="item.year"
        ></span>
      </template>

      <v-card
        :color="item.color"
        dark
      >
        <v-card-title class="title">
          {{item.title}}
        </v-card-title>
        <v-card-text class="white text--primary">
          <p class='hidden-md-and-up'>{{item.year}}</p>
        </v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
    </div>
</template>

<script>
export default {
    name: 'Timeline',

    data(){
        return{
            items: [
        {
          color: 'red',
          icon: 'mdi-star',
          title: 'MBO-2 ICT beheer (ROC zuid-oost)',
          year: '09/2015 - 07/2016',
          content: ''
        },
        {
          color: '#ff00ff',
          icon: 'mdi-book-variant',
          title: 'MBO-4 Média Development (Media College)',
          year: ' 09/2016 - 07/2020',
          content: ''
        },
        {
          color: '#183153',
          icon: 'mdi-airballoon',
          title: 'HBO Technisch Informatica (HvA)',
          year: '10/2019 - 07/2020',
          content: ''
        },
        {
          color: '#00a1e1',
          icon: 'mdi-buffer',
          title: 'HBO Open-ICT(AI) (HU)',
          year: '10/2020 - nog bezig',
          content: ''
        },
      ],
        }
    },

    created(){

    },

    methods:{

    }
}
</script>

<style scoped>
    
</style>