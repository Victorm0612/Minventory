<template>
  <div>
    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="firstname"
              :rules="[rules.required]"
              label="Nombre"
              @keypress="isLetter($event)"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="lastname"
              :rules="[rules.required]"
              label="Apellido"
              @keypress="isLetter($event)"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="mobile"
              :rules="[rules.required, rules.mobileRules]"
              label="Número de celular"
              @keypress="isNumber($event)"
              required
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="email"
              :rules="[rules.required, rules.emailRules]"
              label="Correo electrónico"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="password"
              :rules="[rules.required, rules.passwordRules]"
              label="Contraseña"
              type="password"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="confirmpassword"
              :rules="[rules.required, rules.passwordRules, passwordConfirmationRule]"
              label="Confirmar contraseña"
              type="password"
              required
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="4">
            <v-combobox label="Tipo de documento" v-model="docTypeValue" :items="docType"></v-combobox>
            <v-text-field
              v-model="documentnumber"
              :rules="[rules.required]"
              label="Número de documento"
              @keypress="isNumber($event)"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field v-model="address" :rules="[rules.required]" label="Dirección" required></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-combobox
              v-model="gender"
              label="Género"
              :items="genderItems"
              :rules="[rules.required]"
            ></v-combobox>
          </v-col>
        </v-row>
        <v-btn
          :disabled="!valid"
          depressed
          color="primary"
          elevation="10"
          @click="saveUser"
        >Registrarse</v-btn>
        <br />
        <br />
        <span>¿Ya tienes una cuenta?</span>
        <br />
        <router-link to="/login">
          <span>Haz click aquí para Iniciar Sesión</span>
        </router-link>
      </v-container>
    </v-form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "RegisterComponent",
  data: () => ({
    valid: false,
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
    genderItems: ["Femenino", "Masculino", "Prefiero no decir", "Otro"],
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
  computed: {
    passwordConfirmationRule() {
      return () =>
        this.password === this.confirmpassword ||
        "Las contraseñas deben coincidir";
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
    saveUser(evt){
      evt.preventDefault();
      axios.post('user/',{
            name: this.firstname,
            last_name: this.lastname,
            document_number: this.documentnumber,
            phone: this.mobile,
            email: this.email,
            password: this.password,
            address: this.address,
            gender: this.gender,
            type: "client"
      })
      .then(res=>{
        console.log(res.data);
        setTimeout(() => { this.$router.push({ name: "Login" }); }, 1500);
      })
    }
  },     
};
</script>