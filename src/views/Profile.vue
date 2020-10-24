<template>
  <v-container>
      <profile-component></profile-component>
  </v-container>
</template>

<script>
import ProfileComponent from "@/components/ProfileComponent.vue";

export default {
    name: "Profile",
    components: {
    ProfileComponent
  }
}
</script>