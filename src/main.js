import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import axios from 'axios'
import VueAxios from 'vue-axios';
import VueJwtDecode from 'vue-jwt-decode';

Vue.use(VueAxios, axios)
Vue.use(VueJwtDecode)

axios.defaults.baseURL = 'http://localhost:8000/api/';
Vue.config.productionTip = false;


new Vue({
    router,
    store,
    vuetify,
    render: h => h(App)
}).$mount("#app");