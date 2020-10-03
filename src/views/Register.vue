<template>
  <v-container>
    <span>REGISTRARSE</span>
    <register-component></register-component>
    <router-link to="/client-main">
      <button-component :title="title"></button-component>
    </router-link>
  </v-container>
</template>

<script>
// @ is an alias to /src
import RegisterComponent from "@/components/RegisterComponent.vue";
import ButtonComponent from "@/components/ButtonComponent.vue";

export default {
  name: "Register",
  components: {
    RegisterComponent,
    ButtonComponent
  },
  data() {
    return {
      title: "Registrarse"
    };
  }
};
</script>