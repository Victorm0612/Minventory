<template>
  <div id="nav-bar" class="mx-auto overflow-hidden ">
    <v-app-bar color="#0277BD" dark fixed>
      <router-link to="/">
        <img width="90" height="90" alt="Vue logo" src="..\assets\VidrioVargas.png"/>
      </router-link>
      <v-spacer></v-spacer>
      <v-btn outlined id="menu" v-if="!loggedIn" to="Login">Iniciar Sesión</v-btn>
      <v-btn outlined id="menu" v-if="!loggedIn" to="Register">Registrarse</v-btn>
      <v-btn outlined id="menu" v-if="loggedIn" to="Profile">Perfil</v-btn>
      <v-btn outlined id="menu" v-if="loggedIn" to="Logout">Cerrar Sesión</v-btn>
    </v-app-bar>
    
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      drawer: false,
      links: [
        {icon: 'fas fa-home', text: 'Inicio', route:'Home'},
        {icon: 'fas fa-user-circle',text:'Perfil', route: 'Profile'},
        {icon: 'fas fa-sign-in-alt', text: 'Iniciar Sesión', route:'Login'},
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
#title{
  color: #ffffff;
  text-decoration: none;
}
#menu{
  color: #ffff;
  margin-left: auto;
  margin-right: 1rem;
  text-transform: capitalize;
}
</style>