<template>
  <div>
    <span>REGISTRARSE</span>

    <v-form v-model="valid">
      <v-container>
        <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="firstname"
              :rules="nameRules"
              label="Nombre"
              @keypress="isLetter($event)"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="lastname"
              :rules="nameRules"
              label="Apellido"
              @keypress="isLetter($event)"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="mobile"
              :rules="mobileRules"
              label="Número de celular"
              @keypress="isNumber($event)"
              required
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="12" md="4">
            <v-text-field v-model="email" :rules="emailRules" label="Correo electrónico" required></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field
              v-model="password"
              :rules="passwordRules"
              label="Contraseña"
              type="password"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              v-model="confirmpassword"
              :rules="passwordRules"
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
              :rules="docNumRules"
              label="Número de documento"
              @keypress="isNumber($event)"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field v-model="address" :rules="addressRules" label="Dirección" required></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-combobox v-model="gender" label="Género" :items="genderItems"></v-combobox>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </div>
</template>

<script>
export default {
  name: "RegisterComponent",
  data: () => ({
    valid: false,
    firstname: "",
    lastname: "",
    nameRules: [value => !!value || "Este campo no puede estar vacio"],
    mobile: "",
    mobileRules: [
      value => !!value || "Este campo no puede estar vacio",
      value =>
        value.length == 10 || "El número de celular debe contener 10 dígitos",
      value => !/\D+/.test(value) || "Ingresa un telefono valido"
    ],
    email: "",
    emailRules: [
      value => !!value || "Este campo no puede estar vacio",
      value => /.+@.+/.test(value) || "Ingresa un correo valido"
    ],
    password: "",
    confirmpassword: "",
    passwordRules: [value => !!value || "Este campo no puede estar vacio"],
    docType: [
      "Cédula de ciudadanía",
      "Cédula de extranjería",
      "Pasaporte",
      "NIT"
    ],
    docTypeValue: "Cédula de ciudadanía",
    documentnumber: "",
    docNumRules: [value => !!value || "Este campo no puede estar vacio"],
    address: "",
    addressRules: [value => !!value || "Este campo no puede estar vacio"],
    genderItems: ["Femenino", "Masculino", "Prefiero no decir", "Otro"]
  }),
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
    }
  }
};
</script>