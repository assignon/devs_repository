import Vue from "vue";
import Vuex from "vuex";

import work from "./modules/work";
import description from "./modules/description";
import skills from "./modules/skills";

import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    HOST: "http://127.0.0.1:8000",
    AUTHENTICATED: undefined,
    usertoken: undefined,
    progLangArr: [],
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

    setProgLang: (state) => (data) => {
      /*
        push current programming language data
        params:
          data: [array]: [array of data]
    */
      console.log(state);
      if (state.progLangArr.length == 0) {
        data.forEach((item) => {
          state.progLangArr.push(item);
        });
      } else {
        state.progLangArr = [];
        data.forEach((item) => {
          state.progLangArr.push(item);
        });
      }
      return state.progLangArr;
    },
    getProgLang: (state) => {
      return state.progLangArr;
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

    getAxiosCall(state, payload) {
      /*
                      http get request
                      params:
                          payload: [object]: [data sended with the request]
                  */
      axios
        .get(`${payload.host}/api/${payload.url}/`, {
          params: payload.params,
          // headers: {
          //     "X-CSRFToken": payload.csrftoken,
          //     Authorization: `token ${payload.auth}`,
          // },
        })
        .then((response) => {
          let res = response.data;
          payload.callback(res);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  actions: {
    splitToArray({ commit }, str) {
      commit("splitToArray", str);
    },

    progLangName({ commit, rootState }, payload) {
      /**
       *get programming languages name
       */
      commit("getAxiosCall", {
        url: "proglang/get_pl",
        params: { plId: payload.progLangId },
        callback: payload.callback,
        host: rootState.HOST,
      });
    },
  },

  modules: {
    work: work,
    description: description,
    skills: skills,
  },
});
