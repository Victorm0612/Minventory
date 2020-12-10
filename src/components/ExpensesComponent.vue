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
        <v-toolbar-title>Gastos</v-toolbar-title>
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
            <v-btn color="black" dark class="text-none mb-2" v-bind="attrs" v-on="on">
              Nuevo Gasto
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
              <v-btn class="text-none" color="dark" text @click="close">
                Cancelar
              </v-btn>
              <v-btn
                :disabled="!valid"
                class="text-none"
                color="dark"
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
              >¿Está seguro que desea eliminar el gasto?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn class="text-none" color="dark" text @click="closeDelete"
                >Cancelar</v-btn
              >
              <v-btn class="text-none" color="dark" text @click="deleteItemConfirm"
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
import Bill from "@/classes/bill";

String.prototype.capitalize = function () {
  return this.charAt(0).toUpperCase() + this.slice(1);
};
export default {
  name: "ExpensesComponent",
  data: () => ({
    alertDialog: false,
    alertMessage: "",
    valid: false,
    dialog: false,
    dialogDelete: false,
    search: '',
    headers: [
      {
        text: "ID",
        align: "start",
        value: "id",
      },
      { text: "Fecha", value: "bill_date" },
      { text: "Tipo", value: "bill_type", sortable: false },
      { text: "Total", value: "total_price" },
      { text: "Descripción", value: "description", sortable: false },
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
    },
    defaultBill: {
      id: "",
      bill_date: "",
      bill_type: "",
      total_price: "",
      description: "",
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
      return api.getBillByType("egreso").then((response) => {
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
          if (response.status == 200) {
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