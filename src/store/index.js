import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        avatars: {},
        token: localStorage.getItem('access_token') || null,
        id_user: localStorage.getItem('id_user') || null,
        showAdminMenu: false,
        moduleTitle: "Panel de control"
    },
    getters: {
        loggedIn(state) {
            return state.token !== null
        },
        retrieveId(state) {
            return state.id_user
        },
        retrieveToken(state) {
            return state.token
        },
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
        userLogin(state, token) {
            state.token = token
        },
        destroyToken(state) {
            state.token = null
            state.id_user = null
        },
        setShowAdminMenu(state, value) {
            state.showAdminMenu = value
        },
        setModuleTitle(state, title) {
            state.moduleTitle = title
        },
        retrieveId(state, id) {
            state.id_user = id
        }
    },
    actions: {
        destroyToken(context) {
            if (context.getters.loggedIn) {
                return new Promise((resolve, reject) => {
                    axios.post('logout/', { id: context.getters.retrieveId }, {
                            headers: {
                                "Authorization": 'Token ' + context.getters.retrieveToken,
                            }
                        })
                        .then(res => {
                            localStorage.removeItem('access_token')
                            localStorage.removeItem('id_user')
                            context.commit('destroyToken')
                            resolve(res)

                        })
                        .catch(err => {
                            reject(err)
                        })
                })
            }
        },
        userLogin(context, credentials) {
            return new Promise((resolve, reject) => {
                axios.post('login/', {
                        email: credentials.email,
                        password: credentials.password,
                    })
                    .then(res => {
                        const token = res.data.access_token;
                        const id_user = res.data.user.id;
                        localStorage.setItem('access_token', token)
                        localStorage.setItem('id_user', id_user)
                        context.commit('retrieveId', id_user)
                        context.commit('userLogin', token)
                        resolve(res)

                    })
                    .catch(err => {
                        reject(err)
                    })
            })
        },
        fetchAvatars({
            commit,
            state
        }) {
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
        checkIfAdmin({
            commit
        }) {
            return (window.location.href.indexOf("admin-dashboard") > -1) ? commit('setShowAdminMenu', true) :
                commit('setShowAdminMenu', false);
        }
    },
    modules: {}
});