<template>
  <v-row align="center" justify="space-around">
    <v-btn depressed color="primary" elevation="10">{{title}}</v-btn>
  </v-row>
</template>

<script>
export default {
  name: "ButtonComponent",
  props: { title: { type: String, default: "" } },
};
</script>