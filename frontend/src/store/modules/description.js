import axios from "axios";

export default {
  namespaced: true,
  state: {
    descriptionArr: [], // array contains selected works description get from the DB
  },

  getters: {
    setDesc: (state) => (data) => {
      if (state.descriptionArr.length == 0) {
        data.forEach((item) => {
          state.descriptionArr.push(item);
        });
      } else {
        state.descriptionArr = [];
        data.forEach((item) => {
          state.descriptionArr.push(item);
        });
      }
      return state.descriptionArr;
    },
    getDesc: (state) => {
      return state.descriptionArr;
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
    getDescription({ commit, rootState }, payload) {
      commit("getAxiosCall", {
        url: payload.url,
        params: payload.params,
        callback: payload.callback,
        host: rootState.HOST,
      });
    },
  },
};
