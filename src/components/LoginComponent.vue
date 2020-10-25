<template>
  <v-container class="fill-height" fluid>
    <v-row class="d-flex" align="center" justify="center">
      <v-col cols="12" sm="5" md="4">
        <v-card class="elevation-12 __b-20">
          <v-card-text>
            <v-container fluid>
              <v-row>
                <v-col cols="12" class="text-center">
                  <h3 class="headline">
                    Iniciar Sesión
                  </h3>
                  <h4 class="subtitle-1 mb-3">
                    ¡Bienvenido {{message_user}}!
                  </h4>
                </v-col>
              </v-row>
              <v-row align="center">
                <v-col cols="12" class="aling-center">
                  <v-form>
                    <v-text-field
                    label="correo electrónico"
                    type="email"
                    outlined dense
                    :rules="[rules.required, rules.email]"
                    v-model="email">
                    </v-text-field>
                    <v-text-field
                    label="Contraseña"
                    outlined dense
                    :rules="[rules.required, rules.password]"
                    :append-icon="show ? 'fas fa-eye' : 'fas fa-eye-slash'"
                    v-model="password"
                    :type="show ? 'text' : 'password'"
                    @click:append="show = !show">
                    </v-text-field>
                    <div class="d-flex">
                      <v-btn text color="primary" class="text-none px-2 __btn-login-text" @click="moveToRegister">
                        Crear cuenta
                      </v-btn>
                      <v-spacer/>
                      <v-btn color="primary" class="text-none px-2" @click="getUser">
                        Iniciar Sesión
                      </v-btn>
                    </div>
                  </v-form>
                </v-col>
              </v-row>
              <v-row align="center">
                <v-col>
                  <v-radio-group>
                    <v-radio
                    v-for="item in typeUser"
                    :key="item"
                    @click="message_user=item"
                    :label="`Ingresar como ${item}`"
                    :value="item"
                    ></v-radio>
                    </v-radio-group>
                </v-col>
              </v-row>
            </v-container>
          </v-card-text>
        </v-card>
        <v-alert class="mt-3" 
        :value="show_credentials"
        :type="alert ? 'success' : 'error'">
        {{message_login}}
        </v-alert>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
  name: "LoginComponent",
  data() {
    return {
      typeUser:['Administrador','Empleado','Cliente'],
      users:[],
      message_login: "",
      message_user: "",
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
          this.message_login="Loading..."
          this.alert= true
          setTimeout(() => { this.$router.push({ name: "ClientMain" }); }, 1500);
          break;
        }
        else{
          this.message_login="El correo o la contraseña ingresada no son correctas."
          this.alert= false
        }
      }
      this.show_credentials = true;
    },
    moveToRegister: function() {
      this.$router.push({ name: "Register" });
    }
  },
};
</script>