<template>
  <div id="nav-bar" class="mx-auto overflow-hidden ">
    <v-app-bar color="#0277BD" dark fixed>
      <router-link to="/">
        <img width="90" height="90" alt="Vue logo" :src="require('@/assets/VidrioVargas.png')"/>
      </router-link>
      <v-spacer></v-spacer>
      <v-btn outlined id="menu" v-if="!loggedIn" to="/login">Iniciar Sesión</v-btn>
      <v-btn outlined id="menu" v-if="!loggedIn" to="/register">Registrarse</v-btn>
      <v-menu  v-if="loggedIn" :nudge-right="35" left :nudge-top="-5" transition="slide-y-transition" offset-y center> 
        <template v-slot:activator="{ on, attrs }">
          <v-btn 
            v-ripple="{ class: 'transparent--text' }" 
            icon
            id="userMenu" 
            style="margin-right: 3rem; text-transform: capitalize;"
            v-bind="attrs"
            v-on="on">
            <v-avatar size="46" class="mr-1">
              <img :src="require('@/assets/avatars/avatar_' + retrieveAvatar + '.png')" alt="Avatar"/>
            </v-avatar>
            <span>{{retrieveName}}</span>
            <v-icon right>
              fas fa-angle-down
            </v-icon>
          </v-btn>
        </template>
        <v-list nav-dense>
          <v-list-item-group active-class="deep-purple--text text--accent-4">
            <v-list-item v-for="link in link_user" v-show="link.requireType.includes(retrieveTypeUser)" :key="link.text" @click="moveToRoute(link.route)">
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
import VueJwtDecode from "vue-jwt-decode";
export default {
  name: "NavBar",
  data() {
    return {
      link_user: [
        {icon: 'fas fa-home', text: 'Inicio', route:'Home', requireType: [1,2,3]},
        {icon: 'far fa-calendar-alt', text: 'Agendar Cita', route: 'ClientMain', requireType: [2]},
        {icon: 'fas fa-chart-line', text: 'Dashboard', route:'AdminDashboard', requireType: [1,3]},
        {icon: 'fas fa-user-circle',text:'Perfil', route: 'Profile',requireType: [1,2,3]},
        {icon: 'fas fa-sign-out-alt', text: 'Cerrar Sesión', route:'Logout',requireType: [1,2,3]}
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
    timeToExp(){
      if(this.loggedIn){
        let exp = new Date(VueJwtDecode.decode(this.$store.getters.retrieveUser.token).exp * 1000);
        let actual = new Date()
        let totalTime = exp.getTime() - actual.getTime()
        setTimeout(() => {this.$router.push({ name: 'Logout' });}, totalTime);
      }
    },
  },
  created() {
    this.timeToExp()
  },
  updated(){
    this.timeToExp()
  },
  computed: {
    loggedIn(){
      return this.$store.getters.loggedIn
    },
    retrieveTypeUser(){
      return this.$store.getters.retrieveUser.type_user
    },
    retrieveAvatar(){
      return this.$store.state.user.avatar
    },
    retrieveName(){
      return  this.$store.state.user.name
    },
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