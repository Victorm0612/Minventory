<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="Task"
      :items-per-page="5"
      :search="search"
      :custom-filter="filterOnlyCapsText"
      :show-select="isAdmin('getTypeUser')"
      :expanded.sync="expanded"
      show-expand
      class="elevation-1"
    >
      <template v-slot:top>
        <v-text-field
          v-model="search"
          append-icon="fas fa-search"
          label="Buscar tarea"
          class="mx-4"
          single-line
        >
        </v-text-field>
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
      <template v-slot:expanded-item="{ headers, item }">
        <td :colspan="headers.length">
          Los detalles de la tarea {{ item.id }}
        </td>
      </template>
    </v-data-table>
    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">{{ formTitle }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="6" md="4">
                <v-text-field v-model="editedItem.id" label="ID"></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="editedItem.approved_date"
                  label="Fecha de aprovación"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="editedItem.realization_date"
                  label="Fecha a realizar"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="editedItem.fkAssignment_worker"
                  label="ID Trabajador"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="editedItem.fkElement_id"
                  label="Elementos asignados"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="6" md="4">
                <v-text-field
                  v-model="editedItem.fkTask_status"
                  label="Estado de la tarea"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            text
            color="primary"
            class="text-none px-2 __btn-login-text"
            @click="save"
          >
            Guardar
          </v-btn>
          <v-btn
            text
            color="primary"
            class="text-none px-2 __btn-login-text"
            @click="close"
          >
            Cancelar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title class="headline"
          >Are you sure you want to delete this item?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteItemConfirm"
            >OK</v-btn
          >
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import api from "@/api";
export default {
  name: "TaskComponent",
  data() {
    return {
      search: "",
      dialog: false,
      dialogDelete: false,
      placeClick: false,
      check: false,
      expanded: [],
      editedIndex: -1,
      editedItem: {
        id: 0,
        approved_date: 0,
        realization_date: 0,
        fkAssignment_worker: 0,
        fkElement_id: 0,
        fkTask_status: 0,
      },
      Task: [
        {
          id: 4,
          approved_date: "2020",
          realization_date: "2020",
          fkAssignment_worker: "Arianny",
          fkElement_id: "Taladro",
          fkTask_status: "APROBADO",
        },
        {
          id: 5,
          approved_date: "2020",
          realization_date: "2020",
          fkAssignment_worker: "Victor",
          fkElement_id: "Taladro",
          fkTask_status: "APROBADO",
        },
      ],
      headers: [
        { text: "#", align: "start", sortable: false, value: "id" },
        { text: "Fecha de aprovación", value: "approved_date" },
        { text: "Fecha a realizar", value: "realization_date" },
        { text: "Trabajador asignado", value: "fkAssignment_worker" },
        { text: "Elementos x Tarea", value: "fkElement_id" },
        { text: "Estado actual", value: "fkTask_status" },
        { text: "Acciones", value: "actions", sortable: false },
        { text: "", value: "data-table-expand" },
      ],
    };
  },
  created() {
    return api
      .getTasks(this.isAdmin("request"))
      .then((response) => {
        this.Task = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Nueva Tarea" : "Editar Tarea";
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
  methods: {
    filterOnlyCapsText(value, search) {
      return (
        value != null &&
        search != null &&
        typeof value === "string" &&
        value.toString().toLocaleUpperCase().indexOf(search.toUpperCase()) !==
          -1
      );
    },
    editItem(item) {
      this.editedIndex = this.Task.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.Task.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      this.Task.splice(this.editedIndex, 1);
      this.closeDelete();
    },

    close() {
      this.dialog = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.Task[this.editedIndex], this.editedItem);
      } else {
        this.Task.push(this.editedItem);
      }
      this.close();
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

<style scoped>
#title {
  font-weight: bold;
}
#btnsEdit::before {
  background-color: transparent !important;
}
</style>