<template>
  <div id="nav-bar" class="mx-auto overflow-hidden ">
    <v-app-bar color="#0277BD" dark fixed>
      <router-link to="/">
        <img width="90" height="90" alt="Vue logo" src="..\assets\VidrioVargas.png"/>
      </router-link>
      <v-spacer></v-spacer>
      <v-btn outlined id="menu" v-if="!loggedIn" to="Login">Iniciar Sesión</v-btn>
      <v-btn outlined id="menu" v-if="!loggedIn" to="Register">Registrarse</v-btn>
      <v-menu  v-if="loggedIn" :nudge-top="-5" transition="slide-y-transition" offset-y center> 
        <template v-slot:activator="{ on, attrs }">
          <v-btn 
            v-ripple="{ class: 'transparent--text' }" 
            icon
            id="userMenu" 
            style="margin-right: 3rem; text-transform: capitalize;"
            v-bind="attrs"
            v-on="on">
            <v-avatar size="46" class="mr-1">
              <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John">
            </v-avatar>
            <span>{{name}}</span>
            <v-icon right>
              fas fa-angle-down
            </v-icon>
          </v-btn>
        </template>
        <v-list nav-dense>
          <v-list-item-group active-class="deep-purple--text text--accent-4">
            <v-list-item v-for="link in links" :key="link.text" @click="moveToRoute(link.route)">
              <v-list-item-icon><v-icon>{{link.icon}}</v-icon></v-list-item-icon>
              <v-list-item-title class="text-capitalize">{{link.text}}</v-list-item-title>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</template>

<script>
import api from "@/api";
export default {
  name: "NavBar",
  data() {
    return {
      name: "",
      links: [
        {icon: 'fas fa-home', text: 'Inicio', route:'Home'},
        {icon: 'fas fa-user-circle',text:'Perfil', route: 'Profile'},
        {icon: 'fas fa-sign-out-alt', text: 'Cerrar Sesión', route:'Logout'}
      ]
    };
  },
  methods: {
    moveToRoute: function(route) {
      if (this.$router.currentRoute.name !== route) {
        this.$router.push({ name: route });
      } else {
        this.drawer = false;
      }
    },
  },
    updated(){
      if(this.$store.getters.loggedIn){
        return api
        .getUsers(this.$store.getters.retrieveId)
        .then(res=>{
          this.name=res.data.name
        })
      }
    },
  computed: {
    loggedIn(){
      return this.$store.getters.loggedIn
    }
  },
};
</script>

<style>
#menu{
  color: #ffff;
  margin-left: auto;
  margin-right: 1rem;
  text-transform: capitalize;
}
#userMenu::before {
  background-color: transparent !important;
}
</style>