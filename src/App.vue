<template>
  <v-app>
    <div id="app" :style="'background-image:'+imageBackground.gradient+',url('+require('@/assets/'+imageBackground.msg)+'); height:'+imageBackground.height+';'">
      <nav-bar id="navbar"></nav-bar>
      <v-layout v-if="!isAdmin" row wrap>
        <v-flex d-flex>
          <admin-menu v-if="false || isAdmin"></admin-menu>
          <v-main>
            <router-view />
          </v-main>
        </v-flex>
      </v-layout>
      <v-container v-if="isAdmin" class="fill-height" style="background-color:white;" fluid>
        <v-row align="center" justify="center">
            <v-col>
              <v-layout row wrap>
                <v-flex d-flex>
                  <admin-menu v-if="false || isAdmin"></admin-menu>
                  <v-main>
                    <router-view class="container px-5 sm:px-20 py-20 flex justify-center" />
                  </v-main>
                </v-flex>
              </v-layout>
            </v-col>
        </v-row>
      </v-container>
      <div style="height:100px"></div>
      <v-footer v-if="!isAdmin" absolute dark padless>
        <v-card class="flex" flat tile>
          <v-card-title class="teal">
            <strong class="subheading">¡Conectate con nosotros!</strong>
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
    moduleTitle() {
      return this.$store.state.moduleTitle;
    },
    imageBackground(){
      let image={msg: '',height:'',gradient: ''};
      if(this.moduleTitle === 'Login'){
        image.msg='login.jpg';
        image.height='100vh';
        image.gradient='linear-gradient(to left, rgba(13,8,84,.2), rgba(48,142,126,.24), rgba(73,164,246,.7))';
      }
      else if(this.moduleTitle === 'Register'){
        image.msg='Register.jpg';
        image.height='';
        image.gradient='linear-gradient(to left, rgba(13,9,69,.5), rgba(22,19,19,.6), rgba(26,119,204,.3))';
      }
      else if(this.moduleTitle === 'Home'){
        image.msg='worker.jpg';
        image.height='';
        image.gradient='';
      }
      else{
        image.msg='worker.jpg';
        image.height='';
        image.gradient='linear-gradient(to top right, rgba(2,0,36,.1), rgba(9,9,121,.2), rgba(0,212,255,.5))';
      }
      return image;
    }
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
  background-size: cover;
  
}
#navbar {
  margin-bottom: 3rem;
}
</style>
