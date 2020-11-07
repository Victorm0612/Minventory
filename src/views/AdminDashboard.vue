<template>
  <div>
    <h1>{{ moduleTitle }}</h1>
    <profile-component v-if="moduleTitle == 'Cuenta'"></profile-component>
    <v-row>
      <v-col cols="12" md="4">
        <registrations-card-component
          v-if="moduleTitle == 'Panel de control'"
        ></registrations-card-component>
      </v-col>
      <v-col cols="12" md="4">
        <requests-card-component
          v-if="moduleTitle == 'Panel de control'"
        ></requests-card-component>
      </v-col>
      <v-col cols="12" md="4">
        <quotation-card-component
          v-if="moduleTitle == 'Panel de control'"
        ></quotation-card-component>
      </v-col>
    </v-row>
  </div>
</template>

<script> 
import ProfileComponent from "@/components/ProfileComponent.vue";
import RegistrationsCardComponent from "@/components/dashboard-components/RegistrationsCardComponent.vue";
import RequestsCardComponent from "@/components/dashboard-components/RequestsCardComponent.vue";
import QuotationCardComponent from "@/components/dashboard-components/QuotationCardComponent.vue";

export default {
  name: "AdminDashboard",
  components: {
    ProfileComponent,
    RegistrationsCardComponent,
    RequestsCardComponent,
    QuotationCardComponent
  },
  computed: {
    moduleTitle() {
      return this.$store.state.moduleTitle;
    }
  }
};
</script>
<style>
h1 {
  padding-bottom: 20px;
}
</style>