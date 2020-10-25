<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import api from "@/api";

export default {
  name: "Home",
  components: {
    HelloWorld
  },
  data: () => ({
    users: []
  }),
  //Prueba para el llamado a la api, no necesario en la versión final
  created() {
    return api
      .getUsers()
      .then(response => response)
      .finally(() => (console.log(this.users)));
  }
};
</script>
