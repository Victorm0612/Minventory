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
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
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
                        v-model="editedUser.email"
                        label="Correo Electrónico"
                        :rules="[rules.required, rules.emailRules]"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedUser.phone"
                        label="Número de Celular"
                        :rules="[rules.required, rules.mobileRules]"
                        @keypress="isNumber($event)"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-select
                          label="Tipo de documento"
                          v-model="editedUser.doc_type"
                          :items="docType"
                          :rules="[rules.required]"
                        >
                        </v-select>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedUser.doc_number"
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
              <v-btn color="blue darken-1" text @click="close">
                Cancelar
              </v-btn>
              <v-btn :disabled="!valid" color="blue darken-1" text @click="save"> Guardar </v-btn>
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
              <v-btn color="blue darken-1" text @click="closeDelete"
                >Cancelar</v-btn
              >
              <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                >Eliminar</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)"> fas fa-edit </v-icon>
      <v-icon small @click="deleteItem(item)"> fas fa-trash-alt </v-icon>
    </template>
  </v-data-table>
</template>

<script>
export default {
  name: "EmployeesComponent",
  data: () => ({
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
      { text: "Tipo de documento", value: "doc_type", sortable: false },
      { text: "Número de documento", value: "doc_number", sortable: false },
      { text: "Dirección", value: "address", sortable: false },
      { text: "Género", value: "gender", sortable: false },
      { text: "Actions", value: "actions", sortable: false },
    ],
    users: [],
    editedIndex: -1,
    editedUser: {
      id: "",
      name: "",
      email: "",
      phone: "",
      doc_type: "",
      doc_number: "",
      address: "",
      gender: "",
    },
    defaultUser: {
      id: "",
      name: "",
      email: "",
      phone: "",
      doc_type: "",
      doc_number: "",
      address: "",
      gender: "",
    },
    docType: [
      "Cédula de ciudadanía",
      "Cédula de extranjería",
      "Pasaporte",
      "NIT"
    ],
    genderItems: ["Femenino", "Masculino", "Prefiero no decirlo", "Otro"],
    rules: {
      required: (value) => !!value || "Este campo no puede estar vacio",
      emailRules: (value) =>
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
          value
        ) || "Ingresa un correo valido",
      mobileRules: (value) =>
        value.length == 10 || "El número de celular debe contener 10 dígitos",
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Nuevo Empleado" : "Editar Empleado";
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
      this.users = [
        {
          id: 1,
          name: "Ari",
          email: "ari@ari.com",
          phone: 21234343,
          doc_type: "Cédula de ciudadanía",
          doc_number: 354354,
          address: "some address",
          gender: "Femenino",
        },
        {
          id: 2,
          name: "Jessica",
          email: "jessica@ejemplo.com",
          phone: 434656456,
          doc_type: "Cédula de ciudadanía",
          doc_number: 3542343243354,
          address: "this address",
          gender: "Masculino",
        },
      ];
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
      this.users.splice(this.editedIndex, 1);
      this.closeDelete();
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
      if (this.editedIndex > -1) {
        Object.assign(this.users[this.editedIndex], this.editedUser);
      } else {
        this.users.push(this.editedUser);
      }
      this.close();
    },
  },
};
</script>