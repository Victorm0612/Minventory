<template>
  <v-data-table
    :headers="headers"
    :items="quotations"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Solicitudes</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <v-card>
            <v-card-title>
              <span class="headline">Editar solicitud de cotización</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.id"
                      label="ID"
                      :disabled="true"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.request_date"
                      label="Fecha de solicitud"
                      :disabled="true"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.scheduled_date"
                      label="Fecha agendada"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      :items="availability"
                      v-model="editedItem.time_range"
                      label="Horario"
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      v-model="editedItem.approved"
                      label="Aprobado"
                      :items="approvedList"
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-select
                      :items="serviceType"
                      v-model="editedItem.service_type"
                      label="Servicio"
                    ></v-select>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="12"
                  >
                    <v-text-field
                      v-model="editedItem.description"
                      label="Descripción"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.fkUser_id"
                      label="ID Usuario"
                      :disabled="true"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                class="text-none" color="black"
                text
                @click="close"
              >
                Cancelar
              </v-btn>
              <v-btn
                class="text-none" color="black"
                text
                @click="save"
              >
                Guardar
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">¿Está seguro que desea eliminarlo?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn class="text-none" color="black" text @click="closeDelete">Cancelar</v-btn>
              <v-btn class="text-none" color="black" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        fas fa-edit
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        fas fa-trash-alt
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
import api from '@/api';
import RequestQuotation from '@/classes/requestQuotation';
  export default {
    data: () => ({
      dialog: false,
      dialogDelete: false,
      headers: [
        {
          text: 'ID',
          align: 'center',
          sortable: false,
          value: 'id',
        },
        { text: 'Fecha de solicitud', value: 'request_date' },
        { text: 'Fecha agendada', value: 'scheduled_date' },
        { text: 'Horario', value: 'time_range' },
        { text: 'Aprobado', value: 'approved' },
        { text: 'Tipo de servicio', value: 'service_type' },
        { text: 'Descripción', value: 'description' },
        { text: 'Id de usuario', value: 'fkUser_id' },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
        serviceType: [
        {text:"Acero inoxidable"},
        {text:"Acrílicos"},
        {text:"Angeos"},
        {text:"Barandas"},
        {text:"Divisiones de baño"},
        {text:"Enmarcaciones"},
        {text:"Espejos"},
        {text:"Estructuras metálicas"},
        {text:"Fachadas en vidrio templado"},
        {text:"Pasamanos"},
        {text:"Policarbonato"},
        {text:"Puertas electrónicas"},
        {text:"Puertas"},
        {text:"Venta de accesorios y repuestos"},
        {text:"Ventanas"},
        {text:"Vidrios"},
        ],
        availability: [
        "08:00 - 09:30",
        "10:00 - 11:30",
        "13:00 - 14:30",
        "15:00 - 16:30",
        "17:00 - 18:30",
        ],
        approvedList:["Sí","No"],
      quotations: [],
      editedIndex: -1,
      editedItem: {
        id: 1,
        request_date: 0,
        scheduled_date: 0,
        time_range: 0,
        approved: false,
        service_type: '',
        description: '',
        fkUser_id: 0
      },
      defaultItem: {
        id: 1,
        request_date: 0,
        scheduled_date: 0,
        time_range: 0,
        approved: false,
        service_type: '',
        description: '',
        fkUser_id: 0
      },
    }),
    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
    },

    created () {
      this.initialize()
    },

    methods: {
      initialize () {
          return api
          .getQuotations()
          .then(response=>{
              this.quotations=response.data
              for(let quotation of this.quotations){
                  quotation.approved === true ? quotation.approved="Sí" : quotation.approved="No"
              }
          })
          .catch(error=>{
              console.log(error)
          })
      },

      editItem (item) {
        this.editedIndex = this.quotations.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.quotations.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        return api
        .deleteQuotationByID(this.editedItem.id)
        .then(()=>{
            this.quotations.splice(this.editedIndex, 1)
            this.closeDelete()
        })
        .catch(error=>{
            console.log(error)
        })
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      closeDelete () {
        this.dialogDelete = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
          let request =  new RequestQuotation(
                this.editedItem.scheduled_date,
                this.editedItem.time_range,
                this.editedItem.approved === "Sí" ? true : false,
                this.editedItem.service_type,
                this.editedItem.description,
                this.editedItem.fkUser_id,
          )
          return api
          .updateQuotationByID(this.editedItem.id,request, this.editedItem.scheduled_date)
          .then(()=>{
            Object.assign(this.quotations[this.editedIndex], this.editedItem)
            this.close()
          })
          .catch(error=>{
              console.log(error)
          })
      },
    },
  }
</script>