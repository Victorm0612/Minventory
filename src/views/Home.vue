<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import api from '@/api'

export default {
  name: "Home",
  components: {
    HelloWorld
  },
  data: () => ({
    users: []
  }),
  created() {
    return api
        .getUsers()
        .then(response => (this.users = response))
        .finally(() => (
          this.users ? {} : console.log(this.users)
        ))
  }
};
</script>
