import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        avatars: {},
        token: localStorage.getItem('access_token') || null
    },
    getters: {
        loggedIn(state) {
            return state.token !== null
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
        }
    },
    actions: {
        destroyToken(context) {
            if (context.getters.loggedIn) {
                localStorage.removeItem('access_token')
                context.commit('destroyToken')
            }
        },
        userLogin(context, credentials) {
            return new Promise((resolve, reject) => {
                axios.post('login/', {
                        email: credentials.email,
                        password: credentials.password,
                    })
                    .then(res => {
                        console.log(res)
                        const token = res.data.access_token;
                        localStorage.setItem('access_token', token)
                        context.commit('userLogin', token)
                        resolve(res)

                    })
                    .catch(err => {
                        console.log(err)
                        reject(err)
                    })
            })
        },
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
        }
    },
    modules: {}
});