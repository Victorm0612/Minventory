import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    avatars: {},
    showAdminMenu: false,
    moduleTitle: "Dashboard"
  },
  getters: {
    showAdminMenu(state) {
      return state.showAdminMenu
    },
    moduleTitle(state) {
      return state.moduleTitle
    }
  },
  mutations: {
    setAvatars(state, avatars) {
      state.avatars = avatars
    },
    setShowAdminMenu(state, value) {
      state.showAdminMenu = value
    },
    setModuleTitle(state, title) {
      state.moduleTitle = title
    }
  },
  actions: {
    fetchAvatars({ commit, state }) {
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
    checkIfAdmin({commit}) {
      return (window.location.href.indexOf("admin-dashboard") > -1) ? commit('setShowAdminMenu', true) :
        commit('setShowAdminMenu', false);
    }
  },
  modules: {}
});