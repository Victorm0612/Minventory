<template>
  <v-data-table
    :headers="headers"
    :items="bills"
    :search="search"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Facturas</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="fas fa-search"
          label="Buscar..."
          single-line
          hide-details
        ></v-text-field>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">
              Nueva Factura
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
                        v-model="editedBill.total_price"
                        label="Total"
                        :rules="[rules.required]"
                        @keypress="isNumber($event)"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedBill.description"
                        label="Descripción"
                        :rules="[rules.required]"
                      ></v-text-field>
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
              <v-btn
                :disabled="!valid"
                color="blue darken-1"
                text
                @click="save"
              >
                {{ btnTitle }}
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="viewMoreDialog" max-width="800px">
          <v-card class="block-x-overflow">
            <v-card-title class="headline">Detalles de la factura</v-card-title>
            <v-row justify="center">
              <v-expansion-panels inset>
                <v-expansion-panel>
                  <v-expansion-panel-header>
                    Información general de la factura
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <strong>ID de factura:</strong> {{ editedBill.id }} <br>
                    <strong>Fecha de la factura:</strong> {{ editedBill.bill_date }} <br>
                    <strong>Tipo de factura:</strong> {{ editedBill.bill_type }} <br>
                    <strong>Descripción:</strong> {{ editedBill.description }} <br>
                    <strong>Precio total:</strong> {{ editedBill.total_price }} <br>
                  </v-expansion-panel-content>
                </v-expansion-panel>
                <v-expansion-panel>
                  <v-expansion-panel-header>
                    Información del cliente
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <strong>ID de usuario:</strong> {{ editedBill.user_id }} <br>
                    <strong>Nombre:</strong> {{ editedBill.name }} <br>
                    <strong>Tipo de documento:</strong> {{ editedBill.document_type }} <br>
                    <strong>Número de documento:</strong> {{ editedBill.document_number }} <br>
                    <strong>Correo electrónico:</strong> {{ editedBill.email }} <br>
                    <strong>Número de celular:</strong> {{ editedBill.phone }} <br>
                  </v-expansion-panel-content>
                </v-expansion-panel>
                <v-expansion-panel>
                  <v-expansion-panel-header>
                    Información de tarea y trabajador
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    <strong>ID de tarea:</strong> {{ editedBill.task_id }} <br>
                    <strong>ID del trabajador asignado:</strong> {{ editedBill.assignment_worker_id }} <br>
                    <strong>Fecha de aprobación:</strong> {{ editedBill.approved_date }} <br>
                    <strong>Fecha de realización:</strong> {{ editedBill.realization_date }} <br>
                    <strong>Estado de la tarea:</strong> {{ editedBill.task_status_id }}
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </v-row>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="520px">
          <v-card>
            <v-card-title class="headline"
              >¿Está seguro que desea eliminar la factura?</v-card-title
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
    <template v-slot:[`item.view_more`]="{ item }">
      <v-btn x-small @click="viewMore(item)">Ver más</v-btn>
    </template>
  </v-data-table>
</template>

<script>
import api from "@/api";
import Bill from "@/classes/bill";

String.prototype.capitalize = function () {
  return this.charAt(0).toUpperCase() + this.slice(1);
};
export default {
  name: "BillingComponent",
  data: () => ({
    alertDialog: false,
    alertMessage: "",
    viewMoreDialog: false,
    valid: false,
    dialog: false,
    dialogDelete: false,
    search: "",
    headers: [
      {
        text: "ID",
        align: "start",
        value: "id",
      },
      { text: "Fecha", value: "bill_date" },
      { text: "Tipo", value: "bill_type", sortable: false },
      { text: "Descripción", value: "description", sortable: false },
      { text: "Total", value: "total_price" },
      { text: "Detalles", value: "view_more", sortable: false },
      { text: "Actions", value: "actions", sortable: false },
    ],
    bills: [],
    editedIndex: -1,
    editedBill: {
      id: "",
      bill_date: "",
      bill_type: "",
      total_price: "",
      description: "",
      approved_date: "",
      realization_date: "",
      assignment_worker_id: "",
      user_id: "",
      document_number: "",
      document_type: "",
      email: "",
      name: "",
      last_name: "",
      phone: "",
      task_id: "",
      task_status_id: "",
    },
    defaultBill: {
      id: "",
      bill_date: "",
      bill_type: "",
      total_price: "",
      description: "",
      approved_date: "",
      realization_date: "",
      assignment_worker_id: "",
      user_id: "",
      document_number: "",
      document_type: "",
      email: "",
      name: "",
      last_name: "",
      phone: "",
      task_id: "",
      task_status_id: "",
    },
    billType: ["Egreso"],
    rules: {
      required: (value) => !!value || "Este campo no puede estar vacio",
    },
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Nuevo Gasto" : "Editar Gasto";
    },
    btnTitle() {
      return this.editedIndex === -1 ? "Crear" : "Guardar";
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
    initialize() {
      return api.getBillByType("ingreso").then((response) => {
        if (response.status == 500) {
          this.alertDialog = true;
          this.alertMessage = response.data.message;
        } else {
          this.bills = response.data;
          this.bills.forEach((element) => {
            element.bill_type = element.bill_type.capitalize();
          });
        }
      });
    },
    editItem(item) {
      this.editedIndex = this.bills.indexOf(item);
      this.editedBill = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.bills.indexOf(item);
      this.editedBill = Object.assign({}, item);
      this.dialogDelete = true;
    },

    viewMore(item) {
      this.editedIndex = this.bills.indexOf(item);
      this.editedBill = Object.assign({}, item);
      this.viewMoreDialog = true;
    },

    deleteItemConfirm() {
      return api.deleteBillByID(this.editedBill.id).then((response) => {
        if (response.status == 400 || response.data.status == 500) {
          this.alertDialog = true;
          this.alertMessage = response.data.message;
        } else {
          this.bills.splice(this.editedIndex, 1);
          this.closeDelete();
        }
      });
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedBill = Object.assign({}, this.defaultBill);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedBill = Object.assign({}, this.defaultBill);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.btnTitle == "Crear") {
        let bill = new Bill(
          "egreso",
          this.editedBill.total_price,
          this.editedBill.description,
          null
        );
        return api.createExpense(bill).then((response) => {
          if (response.status == 201) {
            this.bills = [];
            this.initialize();
            this.close();
          } else {
            this.alertDialog = true;
            this.alertMessage = response.data;
          }
        });
      } else if (this.btnTitle == "Guardar") {
        let bill = new Bill(
          "egreso",
          this.editedBill.total_price,
          this.editedBill.description,
          null
        );
        return api.updateBillByID(this.editedBill.id, bill).then((response) => {
          if (response.status == 400) {
            this.alertDialog = true;
            this.alertMessage = response.data;
          } else {
            Object.assign(this.bills[this.editedIndex], this.editedBill);
            this.close();
          }
        });
      }
    },
  },
};
</script>