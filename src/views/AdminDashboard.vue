<template>
  <div>
    <h1>{{ moduleTitle }}</h1>
    <profile-component v-if="moduleTitle == 'Cuenta' "></profile-component>
  </div>
</template>

<script>
import ProfileComponent from "@/components/ProfileComponent.vue";

export default {
  name: "AdminDashboard",
  components: {
    ProfileComponent
  },
  computed: {
    moduleTitle() {
      return this.$store.state.moduleTitle;
    }
  }
};
</script>