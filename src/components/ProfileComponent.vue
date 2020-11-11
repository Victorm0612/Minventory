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
                    @click="saveChange"
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
import api from "@/api";
import User from "@/classes/user";
export default {
  name: "ProfileComponent",
  components: { AvatarPicker },
  data() {
    return {
      show: false,
      loading: false,
      valid: true,
      form: {
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        confirmPassword: "",
        mobile: 0,
        documentType: "",
        documentNumber: 0,
        address: "",
        gender: "",
        avatar: "DEFAULT"
      },
      formBeforeEdit: {},
      showAvatarPicker: false,
      editProfile: false,
      rules: {
        required: value => !!value || "Este campo no puede estar vacio",
        emailRules: value => /.+@.+/.test(value) || "Ingresa un correo valido",
        passwordRules: value =>
          /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#%&*])(?=.{8,})/.test(
            value
          ) ||
          "*Mínimo 8 caracteres. *Mínimo una letra minúscula. *Mínimo una letra mayúscula. *Mínimo un número. *Mínimo un caracter especial[!@#%&*]."
      }
    };
  },
  created() {
    this.formBeforeEdit = Object.assign({}, this.form);
  },
  mounted(){
    this.initialData()
  },
  computed: {
    passwordConfirmationRule() {
      return (
        this.form.password === this.form.confirmPassword ||
        "Las contraseñas deben coincidir"
      );
    },
    mobileRules() {
      return () =>
        this.form.mobile.toString().length == 10 ||
        "El número de celular debe contener 10 dígitos";
    }
  },
  methods: {
    initialData: function(){
    return api
      .getUsers(this.$store.getters.retrieveId)
      .then(res=>{
        this.form.avatar=res.data.avatar
        this.form.firstName= res.data.name
        this.form.lastName= res.data.last_name
        this.form.email= res.data.email
        this.form.password= res.data.password
        this.form.confirmPassword= res.data.password
        this.form.mobile= res.data.phone
        this.form.documentType= res.data.document_type
        this.form.documentNumber= res.data.document_number
        this.form.address= res.data.address
        this.form.gender= res.data.gender
      })
    },
    cancelChanges: function() {
      this.initialData()
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
    },
    saveChange(evt){
      evt.preventDefault();
      let user = new User(
        this.form.avatar,
        this.form.firstName,
        this.form.lastName,
        this.form.documentType,
        this.form.documentNumber,
        this.form.mobile,
        this.form.email,
        this.form.password,
        this.form.address,
        this.form.gender,
        2
      );
      return api
        .updateUser(user)
        .then(() => {
          this.$store.commit('assignDataUser',{
            avatar: this.form.avatar,
            name: this.form.firstName,
          })
          this.editProfile = false
          })
        .catch((error) => {
          console.log(error);
              });
    }
    
  }
};
</script>