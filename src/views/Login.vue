<template>
  <v-container>
    <login-component></login-component>
  </v-container>
</template>

<script>
// @ is an alias to /src
import LoginComponent from "@/components/LoginComponent.vue";

export default {
  name: "Login",
  components: {
    LoginComponent
  },
  data() {
    return {
    };
  },
};
</script>