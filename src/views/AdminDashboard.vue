<template>
  <div>
    <h1>{{ moduleTitle }}</h1>
    <profile-component v-if="moduleTitle == 'Cuenta'"></profile-component>
    <task-component v-if="moduleTitle == 'Tareas'"></task-component>
    <employees-component v-if="moduleTitle == 'Empleados'"></employees-component>
    <expenses-component v-if="moduleTitle == 'Gastos'"></expenses-component>
    <billing-component v-if="moduleTitle == 'Facturación'"></billing-component>
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
    <v-row class="custom4cols">
      <v-col cols="12" md="4">
        <revenue-card-component
          v-if="moduleTitle == 'Panel de control'"
        ></revenue-card-component>
      </v-col>
      <v-col cols="12" md="4">
        <cancel-card-component
          v-if="moduleTitle == 'Panel de control'"
        ></cancel-card-component>
      </v-col>
      <v-col cols="12" md="4">
        <twitter-card-component
          v-if="moduleTitle == 'Panel de control'"
        ></twitter-card-component>
      </v-col>
      <v-col cols="12" md="4">
        <instagram-card-component
          v-if="moduleTitle == 'Panel de control'"
        ></instagram-card-component>
      </v-col>
    </v-row>
  </div>
</template>

<script> 
import ProfileComponent from "@/components/ProfileComponent.vue";
import RegistrationsCardComponent from "@/components/dashboard-components/RegistrationsCardComponent.vue";
import RequestsCardComponent from "@/components/dashboard-components/RequestsCardComponent.vue";
import QuotationCardComponent from "@/components/dashboard-components/QuotationCardComponent.vue";
import RevenueCardComponent from "@/components/dashboard-components/RevenueCardComponent.vue";
import CancelCardComponent from "@/components/dashboard-components/CancelCardComponent.vue";
import TwitterCardComponent from "@/components/dashboard-components/TwitterCardComponent.vue";
import InstagramCardComponent from "@/components/dashboard-components/InstagramCardComponent.vue";
import TaskComponent from '@/components/TaskComponent.vue';
import EmployeesComponent from '@/components/EmployeesComponent.vue';
import ExpensesComponent from '@/components/ExpensesComponent.vue';
import BillingComponent from '@/components/BillingComponent.vue';

export default {
  name: "AdminDashboard",
  components: {
    ProfileComponent,
    RegistrationsCardComponent,
    RequestsCardComponent,
    QuotationCardComponent,
    RevenueCardComponent,
    CancelCardComponent,
    TwitterCardComponent,
    InstagramCardComponent,
    TaskComponent,
    EmployeesComponent,
    ExpensesComponent,
    BillingComponent
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

.custom4cols {
  width: 76.5% !important;
  max-width: 76.5% !important;
  flex-basis: 76.5% !important;
  flex-wrap: unset !important;
}
</style>