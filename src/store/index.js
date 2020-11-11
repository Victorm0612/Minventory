import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        avatars: {},
        showAdminMenu: false,
        moduleTitle: "Panel de control",
        user: JSON.parse(localStorage.getItem('user')) || {
            id_user: null,
            token: null,
            avatar: null,
            name: null,
            type_user: null
        },
    },
    getters: {
        loggedIn(state) {
            return state.user.token !== null
        },
        showAdminMenu(state) {
            return state.showAdminMenu
        },
        moduleTitle(state) {
            return state.moduleTitle
        },
        retrieveUser(state) {
            return state.user
        }
    },
    mutations: {
        setAvatars(state, avatars) {
            state.avatars = avatars
        },
        destroyToken(state) {
            state.user = {
                id_user: null,
                token: null,
                avatar: null,
                name: null,
                type_user: null
            }
        },
        setShowAdminMenu(state, value) {
            state.showAdminMenu = value
        },
        setModuleTitle(state, title) {
            state.moduleTitle = title
        },
        assignDataUser(state, user) {
            localStorage.setItem('user', JSON.stringify(user))
            state.user = user
        }
    },
    actions: {
        destroyToken(context) {
            if (context.getters.loggedIn) {
                return new Promise((resolve, reject) => {
                    axios.post('logout/', { id: context.getters.retrieveUser.id_user }, {
                            headers: {
                                "Authorization": 'Token ' + context.getters.retrieveUser.token,
                            }
                        })
                        .then(res => {
                            localStorage.removeItem('user')
                            context.commit('destroyToken')
                            resolve(res)

                        })
                        .catch((error) => {
                            reject(error)
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
                        const user = {
                            id_user: res.data.user.id,
                            token: res.data.access_token,
                            avatar: res.data.user.avatar,
                            name: res.data.user.name,
                            type_user: res.data.user.type
                        }
                        context.commit('assignDataUser', user)
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