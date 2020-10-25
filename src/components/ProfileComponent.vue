<template>
  <v-container fluid>
    <v-layout column>
      <v-card>
        <v-card-title class="justify-center">{{
          form.firstName + " " + form.lastName
        }}</v-card-title>
        <v-card-text>
          <v-flex class="mb-4">
            <v-avatar size="96" class="mr-4">
              <img
                :src="
                  require('@/assets/avatars/avatar_' + form.avatar + '.png')
                "
                alt="Avatar"
              />
            </v-avatar>
          </v-flex>
          <v-btn v-if="editProfile" @click="openAvatarPicker">Cambiar Avatar</v-btn>
          <v-row class="justify-center">
            <v-col cols="12" md="4">
              <v-text-field
                :disabled="!editProfile"
                v-model="form.firstName"
                label="Nombre"
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field
                :disabled="!editProfile"
                v-model="form.lastName"
                label="Apellido"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="justify-center">
            <v-col cols="12" md="4">
              <v-text-field
                :disabled="!editProfile"
                v-model="form.email"
                label="Correo electrónico"
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field
                :disabled="!editProfile"
                v-model="form.phone"
                label="Número de celular"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="justify-center">
            <v-col cols="12" md="4">
              <v-text-field
                :disabled="!editProfile"
                v-model="form.documentType"
                label="Tipo de documento"
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field
                :disabled="!editProfile"
                v-model="form.documentNumber"
                label="Número de documento"
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row class="justify-center">
            <v-col cols="12" md="4">
              <v-text-field
                :disabled="!editProfile"
                v-model="form.address"
                label="Dirección"
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="4">
              <v-text-field
                :disabled="!editProfile"
                v-model="form.gender"
                label="Género"
              ></v-text-field>
            </v-col>
          </v-row>
        </v-card-text>
        <v-card-actions class="justify-center">
          <v-btn color="primary" :loading="loading" @click="edit_profile">
            {{ btnTitle }}
          </v-btn>
          <v-btn color="primary" :disabled="editProfile">
            Ver mis citas
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
        email: "john@doe.com",
        phone: 3012222222,
        documentType: "Cédula de Ciudadania",
        documentNumber: 123456789,
        address: "some address",
        gender: "Masculino",
        avatar: "MALE_CAUCASIAN_BLACK_BEARD"
      },
      showAvatarPicker: false,
      btnTitle: "Editar Perfil",
      editProfile: false
    };
  },
  methods: {
    openAvatarPicker() {
      this.showAvatarPicker = true;
    },
    selectAvatar(avatar) {
      this.form.avatar = avatar;
    },
    edit_profile() {
      this.editProfile = !this.editProfile;
      if (this.editProfile) {
        this.btnTitle = "Guardar Cambios"
      } else {
        this.btnTitle = "Editar Perfil"
      }
    }
  }
};
</script>