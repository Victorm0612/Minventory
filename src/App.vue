<template>
  <v-app>
    <div id="app">
      <nav-bar id="navbar"></nav-bar>

      <v-layout row wrap>
        <v-flex d-flex>
          <admin-menu v-if="false || isAdmin"></admin-menu>
          <v-main>
            <router-view />
            <!-- class="container px-5 sm:px-20 py-20 flex justify-center"  -->
          </v-main>
        </v-flex>
      </v-layout>
      <v-footer v-if="!isAdmin" absolute dark padless>
        <v-card class="flex" flat tile>
          <v-card-title class="teal">
            <strong class="subheading"
              >¡Conectate con nosotros!</strong
            >

            <v-spacer></v-spacer>

            <v-btn v-for="icon in icons" :key="icon" class="mx-4" dark icon>
              <v-icon size="24px">
                {{ icon }}
              </v-icon>
            </v-btn>
          </v-card-title>

          <v-card-text class="py-2 white--text text-center">
            {{ new Date().getFullYear() }} — <strong>Vidrios Vargas</strong>
          </v-card-text>
        </v-card>
      </v-footer>
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
    AdminMenu,
  },
  data() {
    return {
      icons: [
        "fab fa-facebook",
        "fab fa-twitter",
        "fab fa-linkedin-in",
        "fab fa-instagram",
      ],
    };
  },
  async mounted() {
    await this.$store.dispatch("checkIfAdmin");
  },
  async updated() {
    await this.$store.dispatch("checkIfAdmin");
  },
  computed: {
    isAdmin() {
      return this.$store.getters.showAdminMenu;
    },
  },
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
  margin-bottom: 3rem;
}
</style>
