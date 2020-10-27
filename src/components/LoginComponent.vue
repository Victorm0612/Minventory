<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="12">
          <h1>Iniciar Sesión</h1>
          <v-text-field
            label="Usuario o correo electrónico"
            :rules="[rules.required, rules.email]"
            v-model="email"
            hide-details="auto">
          </v-text-field>
          <v-text-field
            label="Contraseña"
            :rules="[rules.required, rules.password]"
            :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
            v-model="password"
            :type="show ? 'text' : 'password'"
            @click:append="show = !show">
          </v-text-field>
          <v-btn text color="primary" @click="getUser">Iniciar Sesión</v-btn>
          <h4>¿No estás registrado?</h4>
          <router-link text color="primary" to="register">Registrarse</router-link>
        </v-col>
        <v-col cols="12">
          <v-btn text color="primary">Ingresar como Empleado</v-btn>
          <v-btn text color="primary">Ingresar como Administrador</v-btn>
          <v-alert class="mt-3" 
              :value="show_credentials"
              :type="alert ? 'success' : 'error'"
              >{{message}}
          </v-alert>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "LoginComponent",
  data() {
    return {
      users:[],
      message: "",
      step: 1,
      email: "",
      password: "",
      show: false,
      show_credentials: false,
      alert: false,
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
  },
  created(){
      axios.get('user/')
      .then(res=>{
        this.users=res.data
        console.log(this.users)})
  },
  methods: {
    getUser(evt){
      evt.preventDefault();
      for(let user of this.users){
        if(user.email == this.email && user.password == this.password){
          this.message="Loading..."
          this.alert= true
          setTimeout(() => { this.$router.push({ name: "ClientMain" }); }, 1500);
          break;
        }
        else{
          this.message="El correo o la contraseña ingresada no son correctas."
          this.alert= false
        }
      }
      this.show_credentials = true;
    }
  },
};
</script>
