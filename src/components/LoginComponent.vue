<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12">
          <h1>Iniciar Sesión</h1>
          <v-text-field
            label="Usuario o correo electrónico"
            :rules="[rules.required, rules.email]"
            hide-details="auto">
          </v-text-field>
          <v-text-field
            label="Contraseña"
            :rules="[rules.required, rules.password]"
            :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
            :type="show ? 'text' : 'password'"
            @click:append="show = !show">
          </v-text-field>
          <v-btn text color="primary">Iniciar Sesión</v-btn>
          <h4>¿No estás registrado?</h4>
          <router-link text color="primary" to="register">Registrarse</router-link>
        </v-col>
        <v-col cols="12">
          <v-btn text color="primary">Ingresar como Empleado</v-btn>
          <v-btn text color="primary">Ingresar como Administrador</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "LoginComponent",
  data() {
    return {
      step: 1,
      email: "",
      show: false,
      rules: {
        required: value => !!value || "Complete el campo.",
        password: value => {
          const pattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#%&])(?=.{8,})/;
          return pattern.test(value) || "Mínimo 8 caracteres";
        },
        email: value => {
          const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
          return pattern.test(value) || "e-mail inválido.";
        }
      }
    };
  }
};
</script>
