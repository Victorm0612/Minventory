<template>
  <div>
    <v-img
      class="fill-height mb-5"
      height="800"
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
              icon
              @click="gotoSelectedVendor()"
            >
              <v-icon>fas fa-chevron-down</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-img>
    <div
      id="timeline"
      style="
        height: 250px;
        display: flex;
        justify-content: center;
        align-items: center;
      "
    >
      <div>
        <h1 class="display-1 font-weight-thin" style="font-style: italic">
          Nuestra Historia
        </h1>
        <hr />
      </div>
    </div>
    <v-row class="pt-5 d-flex" align="center" justify="center">
      <v-col cols="12" md="10">
        <v-timeline class="mt-5">
          <v-timeline-item
            v-for="(year, i) in years"
            :key="i"
            :color="year.color"
            small
          >
            <template v-slot:opposite>
              <span
                :class="`headline font-weight-bold ${year.color}--text`"
                v-text="year.year"
              ></span>
            </template>
            <div class="py-4">
              <h2
                :class="`headline font-weight-light mb-4 ${year.color}--text`"
              >
                Lorem ipsum
              </h2>
              <div>
                Lorem ipsum dolor sit amet, no nam oblique veritus. Commune
                scaevola imperdiet nec ut, sed euismod convenire principes at.
                Est et nobis iisque percipit, an vim zril disputando
                voluptatibus, vix an salutandi sententiae.
              </div>
            </div>
          </v-timeline-item>
        </v-timeline>
      </v-col>
    </v-row>
    <div
      id="timeline"
      style="
        height: 250px;
        display: flex;
        justify-content: center;
        align-items: center;
      "
    >
      <div>
        <h1 class="display-1 font-weight-thin" style="font-style: italic">
          Nosotros
        </h1>
        <hr />
      </div>
    </div>
    <v-row class="ml-5 pb-5 pt-5 d-flex" align="center" justify="center">
      <v-col cols="12" md="4">
        <v-img class="rounded-lg" src="../assets/worker.jpg"></v-img>
      </v-col>
      <v-col cols="12" md="6">
        <h1 class="display-1 font-weight-thin" style="font-style: italic">
          ¿Quiénes somos?
        </h1>
        <p style="text-align: justify">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Est iusto
          mollitia beatae! Minus qui cupiditate temporibus voluptatum
          consequuntur natus voluptatem rem ipsam est explicabo laudantium
          possimus consequatur quidem ut magni molestias eum perspiciatis iusto
          similique dignissimos, culpa enim! Labore eos eligendi corrupti,
          alias, quia repellendus reprehenderit quo est quibusdam totam
          asperiores ab? Expedita repellendus dolores dicta magnam aliquam illo
          incidunt perspiciatis quidem et, ea provident aperiam nihil distinctio
          placeat aspernatur mollitia sunt earum assumenda deserunt suscipit
          ipsam explicabo laudantium. Ipsa provident in a vitae unde? Soluta eum
          cum repudiandae sit. Earum provident fugiat at nemo in rem, cumque
          reiciendis magnam?
        </p>
      </v-col>
    </v-row>
    <div
      id="timeline"
      style="
        height: 250px;
        display: flex;
        justify-content: center;
        align-items: center;
      "
    >
      <div>
        <h1 class="display-1 font-weight-thin" style="font-style: italic">
          Nuestro Trabajo
        </h1>
        <hr />
      </div>
    </div>
    <v-container>
      <v-row class="ml-5 pb-5 pt-5 d-flex" align="center" justify="center">
        <v-col v-for="n in 6" :key="n" class="d-flex child-flex" cols="4">
          <v-img
            :src="require('@/assets/gallery/' + n + '.jpg')"
            :lazy-src="require('@/assets/gallery/' + n + '.jpg')"
            aspect-ratio="1"
            class="grey lighten-2"
          >
            <template v-slot:placeholder>
              <v-row class="fill-height ma-0" align="center" justify="center">
                <v-progress-circular
                  indeterminate
                  color="grey lighten-5"
                ></v-progress-circular>
              </v-row>
            </template>
          </v-img>
        </v-col>
      </v-row>
    </v-container>
    <div
      id="timeline"
      style="
        height: 100px;
        display: flex;
        justify-content: center;
        align-items: center;
      "
    >
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  data() {
    return {
      years: [
        {
          color: "cyan",
          year: "1960",
        },
        {
          color: "green",
          year: "1970",
        },
        {
          color: "pink",
          year: "1980",
        },
        {
          color: "amber",
          year: "1990",
        },
        {
          color: "orange",
          year: "2000",
        },
      ],
    };
  },
  methods: {
    gotoSelectedVendor() {
      this.$vuetify.goTo("#timeline");
    },
    onScroll(e) {
      this.offsetTop = e.target.scrollTop;
    },
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
