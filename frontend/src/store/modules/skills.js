import axios from "axios";

export default {
  namespaced: true,
  state: {
    skillsArr: [], // array contains all skills get from the DB
    progLangs: [], // array contains all programming languages get from the DB
  },

  getters: {
    setSkills: (state) => (data) => {
      if (state.skillsArr.length == 0) {
        data.forEach((item) => {
          state.skillsArr.push(item);
        });
      } else {
        state.skillsArr = [];
        data.forEach((item) => {
          state.skillsArr.push(item);
        });
      }
      return state.skillsArr;
    },
    getSkills: (state) => {
      return state.skillsArr;
    },

    setProgLangs: (state) => (data) => {
      if (state.progLangs.length == 0) {
        data.forEach((item) => {
          state.progLangs.push(item);
        });
      } else {
        state.progLangs = [];
        data.forEach((item) => {
          state.progLangs.push(item);
        });
      }
      return state.progLangs;
    },
    getProgLangs: (state) => {
      return state.progLangs;
    },
  },

  mutations: {
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

    postAxiosCall(state, payload) {
      /*
                 http post request
                 params:
                     payload: [object]: [data sended with the request]
             */
      axios
        .post(`${payload.host}/api/${payload.url}/`, {
          body: payload.params,
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
    allSkills({ commit, rootState }, payload) {
      commit("getAxiosCall", {
        url: payload.url,
        params: payload.params,
        callback: payload.callback,
        host: rootState.HOST,
      });
    },
  },
};
