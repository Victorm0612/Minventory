<template v-slot:activator="{ on, attrs }">
  <v-container class="fill-height" fluid>
    <v-row class="d-flex" align="center" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card class="elevation-12 __b-20 pa-4">
          <v-card-text>
            <v-container fluid>
              <v-row>
                <v-col cols="12" class="text-center">
                  <h3 class="headline">Registrate</h3>
                  <h4 class="subtitle-1 mb-3">En nuestra plataforma web</h4>
                </v-col>
              </v-row>
              <v-row align="center">
                <v-col cols="12" class="align-center">
                  <v-form v-model="valid">
                    <v-row>
                      <v-col cols="6">
                        <v-text-field
                          v-model="firstname"
                          :rules="[rules.required]"
                          label="Nombre"
                          @keypress="isLetter($event)"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="6">
                        <v-text-field
                          v-model="lastname"
                          :rules="[rules.required]"
                          label="Apellido"
                          @keypress="isLetter($event)"
                          required
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col cols="12">
                        <v-text-field
                          v-model="mobile"
                          :rules="[rules.required, rules.mobileRules]"
                          label="Número de celular"
                          @keypress="isNumber($event)"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field
                          v-model="email"
                          :rules="[rules.required, rules.emailRules]"
                          label="Correo electrónico"
                          required
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col cols="6">
                        <v-text-field
                          v-model="password"
                          :rules="[
                            rules.required,
                            rules.passwordRules,
                            passwordConfirmationRule
                          ]"
                          label="Contraseña"
                          :append-icon="
                            show ? 'fas fa-eye' : 'fas fa-eye-slash'
                          "
                          :type="show ? 'text' : 'password'"
                          @click:append="show = !show"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="6">
                        <v-text-field
                          v-model="confirmpassword"
                          :rules="[
                            rules.required,
                            rules.passwordRules,
                            passwordConfirmationRule
                          ]"
                          label="Confirmar contraseña"
                          :append-icon="
                            show ? 'fas fa-eye' : 'fas fa-eye-slash'
                          "
                          :type="show ? 'text' : 'password'"
                          @click:append="show = !show"
                          required
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col cols="6">
                        <v-select
                          label="Tipo de documento"
                          v-model="docTypeValue"
                          :items="docType"
                        >
                        </v-select>
                      </v-col>
                      <v-col cols="6">
                        <v-text-field
                          v-model="documentnumber"
                          :rules="[rules.required]"
                          label="Número de documento"
                          @keypress="isNumber($event)"
                          required
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row>
                      <v-col cols="12">
                        <v-text-field
                          v-model="address"
                          :rules="[rules.required]"
                          label="Dirección"
                          required
                        >
                        </v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-select
                          v-model="gender"
                          label="Género"
                          :items="genderItems"
                          :rules="[rules.required]"
                        ></v-select>
                      </v-col>
                      <v-col cols="12">
                        <v-btn
                          :disabled="!valid"
                          depressed
                          class="text-none px-5"
                          color="primary"
                          elevation="10"
                          v-bind="attrs"
                          v-on="on"
                          @click="saveUser"
                          >Registrarte
                        </v-btn>
                        <br />
                        <br />
                        <span>¿Ya tienes una cuenta?</span>
                        <br />
                        <router-link to="/login">
                          <span>Haz click aquí para Iniciar Sesión</span>
                        </router-link>
                      </v-col>
                    </v-row>
                  </v-form>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-card>
        <v-dialog v-model="dialog" width="300">
          <v-alert
            style="margin-bottom: 0;"
            type="error"
            transition="scale-transition"
          >
            Por favor, revise los datos ingresados e inténtelo nuevamente.
          </v-alert>
        </v-dialog>
        <v-overlay :value="load">
          <v-progress-circular
            :width="5"
            indeterminate
            color="white"
            size="64"
          ></v-progress-circular>
        </v-overlay>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from "@/api";
import User from "@/classes/user";
export default {
  name: "RegisterComponent",
  data: () => ({
    valid: false,
    show: false,
    dialog: false,
    load: false,
    firstname: "",
    lastname: "",
    mobile: "",
    email: "",
    password: "",
    confirmpassword: "",
    docType: [
      "Cédula de ciudadanía",
      "Cédula de extranjería",
      "Pasaporte",
      "NIT"
    ],
    docTypeValue: "Cédula de ciudadanía",
    documentnumber: "",
    address: "",
    gender: "",
    genderItems: ["Femenino", "Masculino", "Prefiero no decirlo", "Otro"],
    rules: {
      required: value => !!value || "Este campo no puede estar vacio",
      mobileRules: value =>
        value.length == 10 || "El número de celular debe contener 10 dígitos",
      emailRules: value => /.+@.+/.test(value) || "Ingresa un correo valido",
      passwordRules: value =>
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#%&])(?=.{8,})/.test(
          value
        ) ||
        "*Mínimo 8 caracteres. *Mínimo una letra minúscula. *Mínimo una letra mayúscula. *Mínimo un número. *Mínimo un caracter especial[!@#%&]."
    }
  }),
  watch: {
    overlay(val) {
      val &&
        setTimeout(() => {
          this.load = false;
        }, 3000);
    }
  },
  computed: {
    passwordConfirmationRule() {
      return (
        this.password === this.confirmpassword ||
        "Las contraseñas deben coincidir"
      );
    }
  },
  methods: {
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
    saveUser(evt) {
      evt.preventDefault();
      let user = new User(
        this.firstname,
        this.lastname,
        this.documentnumber,
        this.mobile,
        this.email,
        this.password,
        this.address,
        this.gender.toLowerCase().replace(/ /g, "_"),
        "client"
      );
      return api
        .createUser(user)
        .then(res => {
          console.log("post response: " + res.data);
          this.load = !this.load;
          setTimeout(() => {
            this.$router.push({ name: "Login" });
          }, 1500);
        })
        .catch(() => {
          this.dialog = true;
        });
    }
  }
};
</script>