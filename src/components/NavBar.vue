<template>
  <div id="nav-bar" class="mx-auto overflow-hidden">
    <v-app-bar color="#0277BD" dark fixed>
      <router-link to="/">
        <v-toolbar-title>MINVENTORY</v-toolbar-title>
      </router-link>
      <v-app-bar-nav-icon class="right-position-menu" @click="drawer = true"></v-app-bar-nav-icon>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute temporary right>
      <v-list nav dense>
        <v-list-item-group active-class="deep-purple--text text--accent-4">
          <v-list-item @click="moveToRoute('Home')">
            <v-list-item-icon>
              <v-icon>fas fa-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>INICIO</v-list-item-title>
          </v-list-item>

          <v-list-item @click="moveToRoute('Register')">
            <v-list-item-icon>
              <v-icon>fas fa-user-circle</v-icon>
            </v-list-item-icon>
            <v-list-item-title>CUENTA</v-list-item-title>
          </v-list-item>

          <v-list-item @click="moveToRoute('Login')">
            <v-list-item-icon>
              <v-icon>fas fa-sign-in-alt</v-icon>
            </v-list-item-icon>
            <v-list-item-title>INICIAR SESION</v-list-item-title>
          </v-list-item>


        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      drawer: false
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
}
.right-position-menu {
  margin-left: auto;
  margin-right: 0;
}
</style>