<template>
  <v-data-table
    :headers="headers"
    :items="users"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Empleados</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="black" dark class="text-none mb-2" v-bind="attrs" v-on="on">
              Nuevo Empleado
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-form v-model="valid">
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedUser.name"
                        label="Nombre"
                        :rules="[rules.required]"
                        @keypress="isLetter($event)"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedUser.last_name"
                        label="Apellido"
                        :rules="[rules.required]"
                        @keypress="isLetter($event)"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedUser.email"
                        label="Correo Electrónico"
                        :rules="[rules.required, rules.emailRules]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedUser.phone"
                        label="Número de Celular"
                        :rules="[rules.required, mobileRules]"
                        @keypress="isNumber($event)"
                        required
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-select
                        label="Tipo de documento"
                        v-model="editedUser.document_type"
                        :items="docType"
                        :rules="[rules.required]"
                      >
                      </v-select>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedUser.document_number"
                        label="Número de documento"
                        :rules="[rules.required]"
                        @keypress="isNumber($event)"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedUser.address"
                        label="Dirección"
                        :rules="[rules.required]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-select
                        v-model="editedUser.gender"
                        label="Género"
                        :items="genderItems"
                        :rules="[rules.required]"
                      ></v-select>
                    </v-col>
                  </v-row>
                </v-form>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn class="text-none" color="black" text @click="close">
                Cancelar
              </v-btn>
              <v-btn
                class="text-none"
                :disabled="!valid"
                color="black"
                text
                @click="save"
              >
                {{ btnTitle }}
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="520px">
          <v-card>
            <v-card-title class="headline"
              >¿Está seguro que desea eliminar el usuario?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="black" class="text-none" text @click="closeDelete"
                >Cancelar</v-btn
              >
              <v-btn color="black" class="text-none" text @click="deleteItemConfirm"
                >Eliminar</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
      <v-dialog v-model="alertDialog" width="300">
        <v-alert
          style="margin-bottom: 0"
          type="error"
          transition="scale-transition"
        >
          {{ alertMessage }}
        </v-alert>
      </v-dialog>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)"> fas fa-edit </v-icon>
      <v-icon small @click="deleteItem(item)"> fas fa-trash-alt </v-icon>
    </template>
  </v-data-table>
</template>

<script>
import api from "@/api";
import User from "@/classes/user";

String.prototype.capitalize = function () {
  return this.charAt(0).toUpperCase() + this.slice(1);
};
export default {
  name: "EmployeesComponent",
  data: () => ({
    alertDialog: false,
    alertMessage: "",
    valid: false,
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "ID",
        align: "start",
        value: "id",
      },
      { text: "Nombre", value: "name", sortable: false },
      { text: "Correo Electrónico", value: "email", sortable: false },
      { text: "Número de celular", value: "phone", sortable: false },
      { text: "Tipo de documento", value: "document_type", sortable: false },
      {
        text: "Número de documento",
        value: "document_number",
        sortable: false,
      },
      { text: "Dirección", value: "address", sortable: false },
      { text: "Género", value: "gender", sortable: false },
      { text: "Acciones", value: "actions", sortable: false },
    ],
    users: [],
    editedIndex: -1,
    editedUser: {
      id: "",
      avatar: "",
      name: "",
      last_name: "",
      email: "",
      password: "",
      phone: "",
      document_type: "",
      document_number: "",
      address: "",
      gender: "",
      type: "",
    },
    defaultUser: {
      id: "",
      avatar: "",
      name: "",
      last_name: "",
      email: "",
      password: "",
      phone: "",
      document_type: "",
      document_number: "",
      address: "",
      gender: "",
      type: "",
    },
    docType: [
      "Cedula de ciudadania",
      "Cedula de extranjeria",
      "Pasaporte",
      "NIT",
    ],
    genderItems: ["Femenino", "Masculino", "Prefiero no decirlo", "Otro"],
    rules: {
      required: (value) => !!value || "Este campo no puede estar vacio",
      emailRules: (value) =>
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          value
        ) || "Ingresa un correo valido",
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Nuevo Empleado" : "Editar Empleado";
    },
    btnTitle() {
      return this.editedIndex === -1 ? "Crear" : "Guardar";
    },
    mobileRules() {
      return () =>
        this.editedUser.phone.toString().length == 10 ||
        "El número de celular debe contener 10 dígitos";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  created() {
    this.initialize();
  },

  methods: {
    isNumber: function (evt) {
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
    isLetter: function (evt) {
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
    initialize() {
      return api.getUsersByType(3).then((response) => {
        if (response.status == 500) {
          this.alertDialog = true;
          this.alertMessage = response.data.message;
        } else {
          this.users = response.data;
          this.users.forEach((element) => {
            element.document_type = element.document_type
              .replace(/_/g, " ")
              .capitalize();
            element.gender = element.gender.replace(/_/g, " ").capitalize();
          });
        }
      });
    },
    editItem(item) {
      this.editedIndex = this.users.indexOf(item);
      this.editedUser = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.users.indexOf(item);
      this.editedUser = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      return api.deleteUser(this.editedUser.id).then((response) => {
        if (response.status == 400 || response.data.status == 500) {
          this.alertDialog = true;
          this.alertMessage = response.data.message;
        } else {
          this.users.splice(this.editedIndex, 1);
          this.closeDelete();
        }
      });
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedUser = Object.assign({}, this.defaultUser);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedUser = Object.assign({}, this.defaultUser);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.btnTitle == "Crear") {
        let user = new User(
          null,
          this.editedUser.name,
          this.editedUser.last_name,
          this.editedUser.document_type.toLowerCase().replace(/ /g, "_"),
          this.editedUser.document_number,
          this.editedUser.phone,
          this.editedUser.email,
          "employee!123",
          this.editedUser.address,
          this.editedUser.gender.toLowerCase().replace(/ /g, "_"),
          3
        );
        return api.createUser(user).then((response) => {
          if (response.status == 201) {
            this.users = [];
            this.initialize();
            this.close();
          } else {
            this.alertDialog = true;
            this.alertMessage = response.data;
          }
        });
      } else if (this.btnTitle == "Guardar") {
        let user = new User(
          this.editedUser.avatar,
          this.editedUser.name,
          this.editedUser.last_name,
          this.editedUser.document_type.toLowerCase().replace(/ /g, "_"),
          this.editedUser.document_number,
          this.editedUser.phone,
          this.editedUser.email,
          this.editedUser.password,
          this.editedUser.address,
          this.editedUser.gender.toLowerCase().replace(/ /g, "_"),
          this.editedUser.type
        );
        return api.updateUser(this.editedUser.id, user).then((response) => {
          if (response.status == 400) {
            this.alertDialog = true;
            this.alertMessage = response.data;
          } else {
            Object.assign(this.users[this.editedIndex], this.editedUser);
            this.close();
          }
        });
      }
    },
  },
};
</script>

<style>
.v-data-table {
  max-width: 1080px !important;
}
</style>