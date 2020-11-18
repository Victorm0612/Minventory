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
        <v-list-item v-show="item.requireType.includes(retrieveTypeUser)" v-for="item in items" :key="item.title" link @click="changeComponent(item.title)">
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
        { title: "Panel de control", icon: "fas fa-columns", requireType: [1,3]},
        { title: "Cuenta", icon: "fas fa-user-circle", requireType: [1,3]},
        { title: "Empleados", icon: "fas fa-users", requireType: [1]},
        { title: "Tareas", icon:'fas fa-tasks', requireType: [1,3]},
        { title: "Gastos", icon: "fas fa-hand-holding-usd", requireType: [1,3]},
        { title: "Facturación", icon: "fas fa-money-check-alt", requireType: [1,3]},
        { title: "Inventario", icon: "fas fa-boxes", requireType: [1,3]}
      ]
    };
  },
  methods: {
    changeComponent(listTitle) {
      this.$store.commit('setModuleTitle', listTitle);
    }
  },
  created(){
    console.log(this.retrieveTypeUser)
  },
  computed: {
    retrieveTypeUser(){
      return this.$store.getters.retrieveUser.type_user
    },
  },
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