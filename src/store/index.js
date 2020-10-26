import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    avatars: {}
  },
  mutations: {
    setAvatars (state, avatars) {
      state.avatars = avatars
    }
  },
  actions: {
    fetchAvatars ({ commit, state }) {
      if (Object.keys(state.avatars).length) {
        return state.avatars
      }

      let avatars = {}
      let files = require.context('../assets/avatars', false, /\.png$/)
      files.keys().map((key) => {
        let id = key.split('/').pop().split('.')[0].substring(7).toUpperCase()
        avatars[id] = {
          path: key.split('/').pop(),
          id: id
        }
      })

      commit('setAvatars', avatars)
    }
  },
  modules: {}
});
