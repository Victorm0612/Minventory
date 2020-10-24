<template>
  <v-container fluid>
    <v-layout column>
      <v-card>
        <v-card-text>
          <v-flex class="mb-4">
            <v-avatar size="96" class="mr-4">
              <img
                :src="require('@/assets/avatars/avatar_' + form.avatar + '.png')"
                alt="Avatar"
              />
            </v-avatar>
            <v-btn @click="openAvatarPicker">Change Avatar</v-btn>
          </v-flex>
          <v-text-field
            v-model="form.firstName"
            label="FirstName"
          ></v-text-field>
          <v-text-field
            v-model="form.lastName"
            label="Last Name"
          ></v-text-field>
          <v-text-field
            v-model="form.contactEmail"
            label="Email Address"
          ></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" :loading="loading">
            Save Changes
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-layout>
    <avatar-picker
      v-model="showAvatarPicker"
      :current-avatar="form.avatar"
      @selected="selectAvatar"
    ></avatar-picker>
  </v-container>
</template>

<script>
import AvatarPicker from "@/components/AvatarPicker.vue";
export default {
  name: "ProfileComponent",
  components: { AvatarPicker },
  data() {
    return {
      loading: false,
      form: {
        firstName: "John",
        lastName: "Doe",
        contactEmail: "john@doe.com",
        avatar: "MALE_CAUCASIAN_BLACK_BEARD"
      },
      showAvatarPicker: false
    };
  },
  methods: {
    openAvatarPicker() {
      this.showAvatarPicker = true;
    },
    selectAvatar(avatar) {
      this.form.avatar = avatar;
    }
  }
};
</script>