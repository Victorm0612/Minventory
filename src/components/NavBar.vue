<template>
  <div id="nav-bar" class="mx-auto overflow-hidden">
    <v-app-bar color="#0277BD" dark fixed>
      <v-app-bar-nav-icon v-show="!isHome" @click="drawer = true"></v-app-bar-nav-icon>
      <router-link to="/">
        <v-toolbar-title>MINVENTORY</v-toolbar-title>
      </router-link>
      <router-link to="/register" class="custom-btn-login">
        <v-btn elevation="1" outlined small>
          <v-icon small>fas fa-user</v-icon>Iniciar sesión
        </v-btn>
      </router-link>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" absolute temporary>
      <v-list nav dense>
        <v-list-item-group active-class="deep-purple--text text--accent-4">
          <v-list-item @click="goToHome">
            <v-list-item-icon>
              <v-icon>fas fa-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-icon>
              <v-icon>fas fa-user-circle</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Account</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  props: { isHome: { type: Boolean, default: true } },
  data() {
    return {
      drawer: false
    };
  },
  methods: {
    goToHome: function() {
      if (this.$router.currentRoute.name !== "Home") {
        this.$router.push({ name: "Home" });
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
.custom-btn-login {
  margin-left: auto;
  margin-right: 0;
}
.fa-user {
  padding-right: 5px;
}
</style>