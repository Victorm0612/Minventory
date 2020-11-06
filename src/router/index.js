import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Register from "../views/Register.vue";
import ClientMain from "../views/ClientMain.vue";
import Profile from "../views/Profile.vue";
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
        component: Register
    },
    {
        path: "/client-main",
        name: "ClientMain",
        component: ClientMain
    },
    {
        path: "/about",
        name: "About",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ "../views/About.vue")
    },
    {
        path: "/login",
        name: "Login",
        component: () =>
            import ("../views/Login.vue")
    },
    {
        path: "/profile",
        name: "Profile",
        component: Profile
    },
    {
        path: "/admin-dashboard",
        name: "AdminDashboard",
        component: AdminDashboard
    }
];

const router = new VueRouter({
    mode: 'history',
    routes
});

export default router;