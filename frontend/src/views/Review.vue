<template>
    <div>
      <h1>{{route}}</h1>  
    </div>
</template>

<script>
export default {
    name: 'ReviewMode',

    data(){
        return{
            route: this.$route.params.mode
        }
    },

    created(){

    },

    methods: {
        
    }
}
</script>

<style scoped>
    
</style>