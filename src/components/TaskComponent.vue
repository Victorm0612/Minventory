<template>
  <v-data-table
    :headers="headers"
    :items="tasks"
    :search="search"
    :single-expand="singleExpand"
    :expanded.sync="expanded"
    show-expand
    sort-by="id"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Tareas</v-toolbar-title>
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
            <v-btn
              v-if="!isWorker"
              color="black"
              dark
              class="mb-2 text-none"
              v-bind="attrs"
              v-on="on"
            >
              Nueva Tarea
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
                        v-model="editedTask.id"
                        label="ID"
                        :disabled="true"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedTask.approved_date"
                        label="Fecha de aprovación"
                        :disabled="true"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedTask.realization_date"
                        label="Fecha a realizar"
                        :rules="[rules.required]"
                        :disabled="editedIndex != -1"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedTask.fkAssignment_worker"
                        label="ID Trabajador"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field
                        v-model="editedTask.fkRequestquotation"
                        label="ID Cotización"
                        :disabled="editedIndex != -1"
                      ></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-select
                        v-model="editedTask.fkTask_status"
                        label="Estado de la tarea"
                        :items="listStatus"
                      ></v-select>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-select
                        v-model="editedTask.type_task"
                        label="Tipo de tarea"
                        :items="taskType"
                        :rules="[rules.required]"
                        :disabled="editedIndex != -1"
                      ></v-select>
                    </v-col>
                  </v-row>
                </v-form>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="black" class="text-none" text @click="close">
                Cancelar
              </v-btn>
              <v-btn
                :disabled="!valid"
                color="black" class="text-none"
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
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
        :disabled="!isAdmin('getTypeUser')"
      >
        fas fa-edit
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
        :disabled="!isAdmin('getTypeUser')"
      >
        fas fa-trash-alt
      </v-icon>
    </template>
    <template v-slot:expanded-item="{ item, headers }">
      <td valign="middle" align="center" :colspan="headers.length">
        <table cellspacing="10">
          <thead>
            <tr>
              <th>ID</th>
              <th>Fecha de solicitud</th>
              <th>Fecha de agenda</th>
              <th>Horario</th>
              <th>Servicio</th>
              <th>Id del cliente</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td valign="middle" align="center">
                {{ item.requestQuotation.id }}
              </td>
              <td valign="middle" align="center">
                {{ item.requestQuotation.request_date }}
              </td>
              <td valign="middle" align="center">
                {{ item.requestQuotation.scheduled_date }}
              </td>
              <td valign="middle" align="center">
                {{ item.requestQuotation.time_range }}
              </td>
              <td valign="middle" align="center">
                {{ item.requestQuotation.service_type }}
              </td>
              <td valign="middle" align="center">
                {{ item.requestQuotation.fkUser_id }}
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </template>
  </v-data-table>
</template>

<script>
import api from "@/api";
import Task from "@/classes/task";

String.prototype.capitalize = function () {
  return this.charAt(0).toUpperCase() + this.slice(1);
};
export default {
  name: "TaskComponent",
  data: () => ({
    alertDialog: false,
    alertMessage: "",
    valid: false,
    dialog: false,
    dialogDelete: false,
    expanded: [],
    singleExpand: false,
    search: "",
    listStatus: [
      "CREADA",
      "ASIGNADA",
      "EN REVISIÓN - TÉCNICO",
      "EN REVISIÓN - CLIENTE",
      "ACEPTADA",
      "FINALIZADA",
      "CANCELADA",
    ],
    headers: [
      { text: "ID", align: "start", sortable: false, value: "id" },
      { text: "Fecha de aprovación", value: "approved_date" },
      { text: "Fecha a realizar", value: "realization_date" },
      { text: "Trabajador asignado", value: "fkAssignment_worker" },
      { text: "Tipo de tarea", value: "type_task" },
      { text: "ID Cotización", value: "fkRequestquotation" },
      { text: "Estado", value: "fkTask_status" },
      { text: "Acciones", value: "actions", sortable: false },
      { text: "", value: "data-table-expand" },
    ],
    tasks: [],
    editedIndex: -1,
    editedTask: {
      id: "",
      approved_date: "",
      realization_date: "",
      fkAssignment_worker: "",
      fkRequestquotation: "",
      requestQuotation: {
        id: '',
        request_date: '',
        scheduled_date: '',
        time_range: '',
        service_type: '',
        fkUser_id: '',
      },
      fkTask_status: "",
      type_task: "",
    },
    defaultTask: {
      id: "",
      approved_date: "",
      realization_date: "",
      fkAssignment_worker: "",
      fkRequestquotation: "",
      requestQuotation: {
        id: '',
        request_date: '',
        scheduled_date: '',
        time_range: '',
        service_type: '',
        fkUser_id: '',
      },
      fkTask_status: "",
      type_task: "",
    },
    taskType: ["Solicitud de cotización", "Trabajo en ejecución"],
    rules: {
      required: (value) => !!value || "Este campo no puede estar vacio",
    },
  }),

  computed: {
    isWorker() {
      return this.$store.getters.retrieveUser.type_user === 3 ? true : false;
    },
    formTitle() {
      return this.editedIndex === -1 ? "Nueva Tarea" : "Editar Tarea";
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
      return api
        .getTasks(this.isAdmin("request"))
        .then((response) => {
          for (let task of response.data){
            this.tasks.push({
              id: task.id,
              approved_date: task.approved_date,
              realization_date: task.realization_date,
              Assignment_worker: task.fkAssignment_worker,
              fkRequestquotation: task.fkRequestquotation,
              fkTask_status: task.fkTask_status,
              type_task: task.type_task,
              requestQuotation: {
                id: '',
                request_date: '',
                scheduled_date: '',
                time_range: '',
                service_type: '',
                fkUser_id: '',
              },
            })
          }
          for (let task of this.tasks) {
            task.fkTask_status = this.listStatus[task.fkTask_status];
            task.type_task === "request_quotation"
              ? (task.type_task = "Solicitud de cotización")
              : (task.type_task = "Trabajo en ejecución");
            this.assignRequest(task);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    assignRequest(task) {
      return api
        .getQuotationsByIDs(task.fkRequestquotation)
        .then((response) => {
          task.requestQuotation = response.data;
        })
        .catch((error) => {
          this.alertDialog = true;
          this.alertMessage = error;
        });
    },
    editItem(item) {
      this.editedIndex = this.tasks.indexOf(item);
      this.editedTask = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.tasks.indexOf(item);
      this.editedTask = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      return api.deleteTask(this.editedTask.id).then((response) => {
        if (response.status == 400 || response.data.status == 500) {
          this.alertDialog = true;
          this.alertMessage = response.data.message;
        } else {
          this.tasks.splice(this.editedIndex, 1);
          this.closeDelete();
        }
      });
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedTask = Object.assign({}, this.defaultTask);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedTask = Object.assign({}, this.defaultTask);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.btnTitle == "Crear") {
        let task = new Task(
          null,
          this.editedTask.realization_date,
          this.editedTask.fkAssignment_worker,
          this.editedTask.fkRequestquotation,
          this.listStatus.indexOf(this.editedTask.fkTask_status) + 1,
          this.editedTask.type_task === "Solicitud de cotización"
            ? "request_quotation"
            : "job_execution"
        );
        return api.createTask(task).then((response) => {
          if (response.status == 201) {
            this.tasks = [];
            this.initialize();
            this.close();
          } else {
            this.alertDialog = true;
            this.alertMessage = response.data;
          }
        });
      } else if (this.btnTitle == "Guardar") {
        let task = new Task(
          null,
          this.editedTask.realization_date,
          this.editedTask.fkAssignment_worker,
          this.editedTask.fkRequestquotation,
          this.listStatus.indexOf(this.editedTask.fkTask_status) + 1,
          this.editedTask.type_task === "Solicitud de cotización"
            ? "request_quotation"
            : "job_execution"
        );
        return api.updateTask(task, this.editedTask.id).then((response) => {
          if (response.status == 400) {
            this.alertDialog = true;
            this.alertMessage = response.data;
          } else {
            Object.assign(this.tasks[this.editedIndex], this.editedTask);
            this.close();
          }
        });
      }
    },
    isAdmin(forWhat) {
      if (forWhat === "request") {
        if (this.$store.getters.retrieveUser.type_user == 3) {
          return (
            "task/employee-task/" + this.$store.getters.retrieveUser.id_user
          );
        } else {
          return "task/";
        }
      } else if (forWhat === "getTypeUser") {
        if (this.$store.getters.retrieveUser.type_user == 3) {
          return false;
        } else {
          return true;
        }
      } else {
        return false;
      }
    },
  },
};
</script>
