<template>
  <div id="nav-bar" class="mx-auto overflow-hidden">
    <v-app-bar color="#0277BD" dark fixed>
      <router-link to="/">
        <v-toolbar-title>MINVENTORY</v-toolbar-title>
      </router-link>
      <v-app-bar-nav-icon class="right-position" @click="drawer = true"></v-app-bar-nav-icon>
    </v-app-bar>
    <v-navigation-drawer v-model="drawer" absolute temporary right>
      <v-list nav-dense>
        <v-lis-item-group active-class="deep-purple--text text--accent-4">
          <v-list-item v-for="link in links" :key="link.text" @click="moveToRoute(link.route)">
            <v-list-item-icon><v-icon>{{link.icon}}</v-icon></v-list-item-icon>
            <v-list-title class="text-capitalize">{{link.text}}</v-list-title>
          </v-list-item>
        </v-lis-item-group>
      </v-list>
    </v-navigation-drawer>
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
        {icon: 'fas fa-sign-in-alt', text: 'Iniciar Sesión', route:'Login'}
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
  }
};
</script>

<style>
#nav-bar a {
  color: #ffffff;
  text-decoration: none;
  margin-bottom: 10px;
}
.right-position {
  margin-left: auto;
  margin-right: 0;
}
</style>