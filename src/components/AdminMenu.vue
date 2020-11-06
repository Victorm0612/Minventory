<template>
  <v-card height="400" width="256">
    <v-navigation-drawer class="drawer" color="#0277BD" dark permanent fixed clipped >
      <v-list>
        <v-list-item v-for="item in items" :key="item.title" :to="item.route">
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <template v-slot:append>
        <div class="pa-2">
          <v-btn block>
            Logout
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
export default {
  name: "AdminMenu",
  data() {
    return {
      items: [
        { title: "Dashboard", icon: "fas fa-columns", route: "/"},
        { title: "Account", icon: "fas fa-user-circle", route: "/profile"},
        { title: "Admin", icon: "fas fa-gavel", route: "/" }
      ]
    };
  }
};
</script>
 <style>
.drawer {
  top: 3.2rem !important;
}
</style>