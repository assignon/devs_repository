import Vue from "vue";
import Vuex from "vuex";

import work from "./modules/work";
import description from "./modules/description";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    HOST: "http://127.0.0.1:8000",
    AUTHENTICATED: undefined,
    usertoken: undefined,
  },

  getters: {
    set: (state) => (data, arr) => {
      /*
        update the items of an array
        params:
          data: [array]: [array of data]
          arr: [array]: []
    */
      console.log(state);
      if (arr.length == 0) {
        data.forEach((item) => {
          arr.push(item);
        });
      } else {
        arr = [];
        data.forEach((item) => {
          arr.push(item);
        });
      }
      return arr;
    },

    get: (state) => (elem) => {
      /*
        get given element
        params:
          elem: [array, string, number, boolean]: [element to get]
        return: rray, string, number, boolean
    */
      console.log(state);
      return elem;
    },

    filterArr: (state) => (arr, callback) => {
      /*
        filter array en return machted elem on condition
        params:
          arr: [array]: [array we want to get the lenth]
          callback: [function]: []
        return: callback function
      */
      console.log(state);
      let count = arr.filter((value) => {
        return callback(value);
      }).length;
      return count;
    },

    // getCount: (state) => (arr) => {
    //   /*
    //     get array lenth
    //     params:
    //       arr: [array]: [array we want to get the lenth]
    //       callback: [function]: []
    //     return: callback function
    //   */
    // }
  },

  mutations: {
    splitToArray(state, str) {
      /*
      split a string words in to array
      params:
        str: [str]: [string to split]
      returns: return array
      */
      let arr = str.split(",");
      console.log(arr);
      // return "hallo tehre";
    },
  },

  actions: {
    splitToArray({ commit }, str) {
      commit("splitToArray", str);
    },
  },

  modules: {
    work: work,
    description: description,
  },
});
