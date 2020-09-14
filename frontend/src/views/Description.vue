<template lang="">
    <div class='desc-core'>
        <h1>{{param}}</h1>
    </div>
</template>

<script>
// import { mapGetters } from "vuex";
export default {
  name: "Description",

  data() {
    return {
      param: this.$route.params.name
    };
  },

  computed: {},

  created() {},

  methods: {}
};
</script>

<style scoped>
</style>