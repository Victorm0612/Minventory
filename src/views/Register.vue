<template>
  <v-container>
    <register-component></register-component>
  </v-container>
</template>

<script>
// @ is an alias to /src
import RegisterComponent from "@/components/RegisterComponent.vue";

export default {
  name: "Register",
  components: {
    RegisterComponent
  }
};
</script>