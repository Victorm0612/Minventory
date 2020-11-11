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
        moduleTitle: "Panel de control",
        user: JSON.parse(localStorage.getItem('user')) || null,
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
        },
        retrieveUser(state) {
            return state.user
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
            state.user = {}
        },
        setShowAdminMenu(state, value) {
            state.showAdminMenu = value
        },
        setModuleTitle(state, title) {
            state.moduleTitle = title
        },
        retrieveId(state, id) {
            state.id_user = id
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
                    axios.post('logout/', { id: context.getters.retrieveId }, {
                            headers: {
                                "Authorization": 'Token ' + context.getters.retrieveToken,
                            }
                        })
                        .then(res => {
                            localStorage.removeItem('access_token')
                            localStorage.removeItem('id_user')
                            localStorage.removeItem('user')
                            context.commit('destroyToken')
                            resolve(res)

                        })
                        .catch((error) => {
                            if (error.response.status === 403 && error.response.data.detail === 'access_token expired') {
                                localStorage.removeItem('access_token')
                                localStorage.removeItem('id_user')
                                localStorage.removeItem('user')
                            } else {
                                reject(error)
                            }
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
                        const user = {
                            avatar: res.data.user.avatar,
                            name: res.data.user.name
                        }
                        localStorage.setItem('access_token', token)
                        localStorage.setItem('id_user', id_user)
                        context.commit('retrieveId', id_user)
                        context.commit('userLogin', token)
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