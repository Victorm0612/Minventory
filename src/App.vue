<template>
  <v-app>
    <div id="app">
      <nav-bar id="navbar"></nav-bar>
      <v-layout row wrap>
        <v-flex d-flex>
          <admin-menu></admin-menu>
          <router-view
            class="container px-5 sm:px-20 py-20 flex justify-center"
          />
        </v-flex>
      </v-layout>
    </div>
  </v-app>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
import AdminMenu from "@/components/AdminMenu.vue";

export default {
  name: "App",
  components: {
    NavBar,
    AdminMenu
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#navbar {
  margin-bottom: 5rem;
}
</style>
