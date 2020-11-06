import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    avatars: {},
    showAdminMenu: false
  },
  getters: {
    showAdminMenu (state){
      return state.showAdminMenu
    }
  },
  mutations: {
    setAvatars (state, avatars) {
      state.avatars = avatars
    },
    setShowAdminMenu (state, value){
      state.showAdminMenu = value
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
    },
    checkIfAdmin( {commit} ) {
      if (window.location.href.indexOf("admin-dashboard") > -1) {
        commit('setShowAdminMenu', true)
      } else {
        commit('setShowAdminMenu', false)
      }
    }
  },
  modules: {}
});
