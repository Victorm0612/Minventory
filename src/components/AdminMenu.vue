<template>
  <v-card height="400" width="256">
    <v-navigation-drawer
      class="drawer"
      color="#0277BD"
      dark
      permanent
      fixed
      clipped
    >
      <v-list>
        <v-list-item v-for="item in items" :key="item.title" link @click="changeComponent(item.title)">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
export default {
  name: "AdminMenu",
  data() {
    return {
      items: [
        { title: "Dashboard", icon: "fas fa-columns"},
        { title: "Cuenta", icon: "fas fa-user-circle"},
        { title: "Empleados", icon: "fas fa-users"},
        { title: "Gastos", icon: "fas fa-hand-holding-usd"},
        { title: "Facturación", icon: "fas fa-money-check-alt"},
        { title: "Inventario", icon: "fas fa-boxes"}
      ]
    };
  },
  methods: {
    changeComponent(listTitle) {
      this.$store.commit('setModuleTitle', listTitle);
    }
  }
};
</script>
 <style>
.drawer {
  top: 3.2rem !important;
}
.v-navigation-drawer__content {
  padding-top: 20px;
}
</style>