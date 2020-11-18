import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register.vue";
import ClientMain from "../views/ClientMain.vue";
import Profile from "../views/Profile.vue";
import Login from "../views/Login.vue";
import Logout from "../views/Logout.vue";
import About from "../views/About.vue";
import store from "../store";
import AdminDashboard from "../views/AdminDashboard.vue";

Vue.use(VueRouter);

const routes = [{
        path: "/",
        name: "Home",
        component: Home
    },
    {
        path: "/register",
        name: "Register",
        component: Register,
        meta: {
            requiresVisitor: true,
        }
    },
    {
        path: "/client-main",
        name: "ClientMain",
        component: ClientMain,
        meta: {
            requiresAuth: true,
            is_client: true
        }
    },
    {
        path: "/about",
        name: "About",
        component: About
    },
    {
        path: "/login",
        name: "Login",
        component: Login,
        meta: {
            requiresVisitor: true,
        }
    },
    {
        path: "/profile",
        name: "Profile",
        component: Profile,
        meta: {
            requiresAuth: true,
        }
    },
    {
        path: "/logout",
        name: "Logout",
        component: Logout

    },
    {
        path: "/admin-dashboard",
        name: "AdminDashboard",
        component: AdminDashboard,
        meta: {
            requiresAuth: true,
            is_admin: true
        }

    }
];

const router = new VueRouter({
    mode: 'history',
    routes
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(route => route.meta.requiresAuth)) {
        if (!store.getters.loggedIn) {
            next({
                name: 'Login',
            })
        } else if (to.matched.some(route => route.meta.is_client)) {
            if (store.getters.retrieveUser.type_user == 2) {
                next()
            } else {
                next({
                    name: 'Home'
                })
            }
        } else if (to.matched.some(route => route.meta.is_admin)) {
            if (store.getters.retrieveUser.type_user == 1 || store.getters.retrieveUser.type_user == 3) {
                next()
            } else {
                next({
                    name: 'Home'
                })
            }
        } else {
            next()
        }
    } else if (to.matched.some(record => record.meta.requiresVisitor)) {
        if (store.getters.loggedIn) {
            next({
                name: 'Home'
            })
        } else {
            next()
        }
    } else {
        next()
    }
})

export default router;