<template>
  <v-dialog
    :fullscreen="$vuetify.breakpoint.xs"
    width="500"
    transition="dialog-bottom-transition"
    v-model="show"
  >
    <v-card class="block-x-overflow">
      <v-toolbar dark color="primary">
        <v-toolbar-title>Select an Avatar</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn class="right-position" color="primary" @click="show = false">
          Cerrar
        </v-btn>
      </v-toolbar>
      <v-layout row wrap v-if="avatars">
        <v-flex v-for="avatar in avatars" :key="avatar.id" xs4 sm3 d-flex>
          <v-card tile flat class="d-flex">
            <v-card-text class="d-flex">
              <v-avatar
                size="96"
                @click="selectAvatar(avatar)"
                class="avatar-picker-avatar"
                :class="{ current: avatar.id === currentAvatar }"
              >
                <img :src="require('@/assets/avatars/' + avatar.path)" />
              </v-avatar>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "AvatarPicker",
  props: {
    currentAvatar: {
      type: String,
      required: true
    },
    value: Boolean
  },
  async mounted() {
    await this.$store.dispatch("fetchAvatars");
  },
  computed: {
    avatars() {
      return this.$store.state.avatars;
    },
    show: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      }
    }
  },
  methods: {
    selectAvatar(avatar) {
      this.$emit("selected", avatar.id);
      this.show = false;
    }
  }
};
</script>
<style scoped>
.block-x-overflow{
  overflow-x: hidden;
}
</style>>
