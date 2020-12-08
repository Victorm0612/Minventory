<template>
  <div>
    <v-img
      class="fill-height"
      height="700"
      gradient="to top right, rgba(2,0,36,.1), rgba(9,9,121,.2), rgba(0,212,255,.5)"
      src="../assets/imageOne.jpg"
    >
      <v-container class="fill-height" fluid>
        <v-row id="title" align="center" justify="center">
          <v-col class="text-center" cols="12">
            <h1 class="display-2 font-weight-thin mb-4">Vidrios Vargas</h1>
            <h4 class="subheading">¡Cotiza con nosotros ahora!</h4>
          </v-col>
          <v-col align="center" justify="center">
            <v-btn
            id="down"
            v-ripple="{ class: 'transparent--text' }"  
            class="mx-2"
            fab
            dark
            large
            icon>
              <v-icon>fas fa-chevron-down</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-img>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#title {
  text-shadow: 2px 2px 5px black;
  color: white;
}
#down::before {
  background-color: transparent !important;
}
</style>
