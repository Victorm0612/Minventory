<template>
  <div>
    <v-form v-model="valid">
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
              <v-btn v-if="editProfile" @click="openAvatarPicker"
                >Cambiar Avatar</v-btn
              >
              <v-row class="justify-center">
                <v-col cols="12" md="4">
                  <v-text-field
                    :disabled="!editProfile"
                    :rules="[rules.required]"
                    v-model="form.firstName"
                    label="Nombre"
                    @keypress="isLetter($event)"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-text-field
                    :disabled="!editProfile"
                    v-model="form.lastName"
                    :rules="[rules.required]"
                    label="Apellido"
                    @keypress="isLetter($event)"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row class="justify-center">
                <v-col cols="12" md="4">
                  <v-text-field
                    :disabled="!editProfile"
                    v-model="form.email"
                    :rules="[rules.required, rules.emailRules]"
                    label="Correo electrónico"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-text-field
                    :disabled="!editProfile"
                    v-model="form.mobile"
                    :rules="[rules.required, mobileRules]"
                    label="Número de celular"
                    @keypress="isNumber($event)"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row class="justify-center">
                <v-col cols="12" md="4">
                  <v-text-field
                    :disabled="true"
                    v-model="form.documentType"
                    :rules="[rules.required]"
                    label="Tipo de documento"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-text-field
                    :disabled="true"
                    v-model="form.documentNumber"
                    :rules="[rules.required]"
                    label="Número de documento"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row class="justify-center">
                <v-col cols="12" md="4">
                  <v-text-field
                    :disabled="!editProfile"
                    v-model="form.address"
                    :rules="[rules.required]"
                    label="Dirección"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-text-field
                    :disabled="true"
                    v-model="form.gender"
                    :rules="[rules.required]"
                    label="Género"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row v-if="editProfile" class="justify-center">
                <v-col cols="12" md="4">
                  <v-text-field
                    :disabled="!editProfile"
                    v-model="form.password"
                    :rules="[
                      rules.required,
                      rules.passwordRules,
                      passwordConfirmationRule
                    ]"
                    :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
                    :type="show ? 'text' : 'password'"
                    @click:append="show = !show"
                    label="Contraseña"
                  ></v-text-field>
                </v-col>
                <v-col cols="12" md="4">
                  <v-text-field
                    :disabled="!editProfile"
                    v-model="form.confirmPassword"
                    :rules="[
                      rules.required,
                      rules.passwordRules,
                      passwordConfirmationRule
                    ]"
                    :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
                    :type="show ? 'text' : 'password'"
                    @click:append="show = !show"
                    label="Confirmar contraseña"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-card-text>
            <v-card-actions class="justify-center">
              <v-container v-if="!editProfile">
                <v-row class="justify-center">
                  <v-col cols="12" md="4">
                    <v-btn
                      color="primary"
                      :loading="loading"
                      @click="editProfile = true"
                    >
                      Editar Perfil
                    </v-btn>
                  </v-col>
                  <v-col cols="12" md="4">
                    <v-btn color="primary">
                      Ver mis citas
                    </v-btn>
                  </v-col>
                </v-row>
              </v-container>
              <v-row class="justify-center">
                <v-col cols="12" md="4">
                  <v-btn
                    v-if="editProfile"
                    color="primary"
                    @click="editProfile = false"
                    :disabled="!valid"
                  >
                    Guardar Cambios
                  </v-btn>
                </v-col>
                <v-col cols="12" md="4" @click="cancelChanges">
                  <v-btn v-if="editProfile" color="primary">
                    Cancelar
                  </v-btn>
                </v-col>
              </v-row>
            </v-card-actions>
          </v-card>
        </v-layout>
        <avatar-picker
          v-model="showAvatarPicker"
          :current-avatar="form.avatar"
          @selected="selectAvatar"
        ></avatar-picker>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import AvatarPicker from "@/components/AvatarPicker.vue";
export default {
  name: "ProfileComponent",
  components: { AvatarPicker },
  data() {
    return {
      show: false,
      loading: false,
      valid: true,
      form: {
        firstName: "John",
        lastName: "Doe",
        email: "john@doe.com",
        password: "aaaA23456#",
        confirmPassword: "aaaA23456#",
        mobile: 3014705281,
        documentType: "Cédula de Ciudadania",
        documentNumber: 123456789,
        address: "some address",
        gender: "Masculino",
        avatar: "MALE_CAUCASIAN_BLACK_BEARD"
      },
      formBeforeEdit: {},
      showAvatarPicker: false,
      editProfile: false,
      rules: {
        required: value => !!value || "Este campo no puede estar vacio",
        emailRules: value => /.+@.+/.test(value) || "Ingresa un correo valido",
        passwordRules: value =>
          /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#%&])(?=.{8,})/.test(
            value
          ) ||
          "*Mínimo 8 caracteres. *Mínimo una letra minúscula. *Mínimo una letra mayúscula. *Mínimo un número. *Mínimo un caracter especial[!@#%&]."
      }
    };
  },
  created() {
    this.formBeforeEdit = Object.assign({}, this.form);
  },
  computed: {
    passwordConfirmationRule() {
      return () =>
        this.form.password === this.form.confirmPassword ||
        "Las contraseñas deben coincidir";
    },
    mobileRules() {
      return () =>
        this.form.mobile.toString().length == 10 ||
        "El número de celular debe contener 10 dígitos";
    }
  },
  methods: {
    cancelChanges: function() {
      Object.assign(this.form, this.formBeforeEdit);
      this.editProfile = false;
    },
    isNumber: function(evt) {
      evt = evt ? evt : window.event;
      var charCode = evt.which ? evt.which : evt.keyCode;
      if (
        charCode > 31 &&
        (charCode < 48 || charCode > 57) &&
        charCode !== 46
      ) {
        evt.preventDefault();
      } else {
        return true;
      }
    },
    isLetter: function(evt) {
      evt = evt ? evt : window.event;
      var charCode = evt.which ? evt.which : evt.keyCode;
      if (
        (charCode < 97 || charCode > 122) &&
        (charCode < 65 || charCode > 90)
      ) {
        evt.preventDefault();
      } else {
        return true;
      }
    },
    openAvatarPicker() {
      this.showAvatarPicker = true;
    },
    selectAvatar(avatar) {
      this.form.avatar = avatar;
    }
  }
};
</script>