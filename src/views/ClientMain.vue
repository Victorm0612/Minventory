<template>
  <v-container>
    <calendar-component></calendar-component>
  </v-container>
</template>

<script>
import CalendarComponent from "@/components/CalendarComponent.vue";

export default {
  name: "ClienMain",
  components: { CalendarComponent }
};
</script>