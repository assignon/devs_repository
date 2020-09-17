import axios from "axios";

export default {
  namespaced: true,
  state: {
    worksArr: [], // array contains all works get from the DB
    searchArr: [], // array content founded works on search
  },

  getters: {
    setWorks: (state) => (data) => {
      if (state.worksArr.length == 0) {
        data.forEach((item) => {
          state.worksArr.push(item);
        });
      } else {
        state.worksArr = [];
        data.forEach((item) => {
          state.worksArr.push(item);
        });
      }
      return state.worksArr;
    },
    getWorks: (state) => {
      return state.worksArr;
    },
    setSearchesWorks: (state) => (data) => {
      if (state.searchArr.length == 0) {
        data.forEach((item) => {
          state.searchArr.push(item);
        });
      } else {
        state.searchArr = [];
        data.forEach((item) => {
          state.searchArr.push(item);
        });
      }
      return state.searchArr;
    },
    getSearchedWorks: (state) => {
      return state.searchArr
    }
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
    allWorks({ commit, rootState }, payload) {
      commit("getAxiosCall", {
        url: payload.url,
        params: payload.params,
        callback: payload.callback,
        host: rootState.HOST,
      });
    },
  },
};
