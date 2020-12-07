<template>
  <v-data-table
    :headers="headers"
    :items="elements"
    :search="search"
    :custom-filter="filterOnlyCapsText"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Inventario</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="fas fa-search"
          label="Buscar..."
          single-line
          hide-details
        ></v-text-field>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              Nuevo Elemento
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
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
                      v-model="editedItem.name"
                      label="Nombre"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
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
                      v-model="editedItem.price"
                      label="Precio"
                      @keypress="isNumber()"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.reseller"
                      label="Vendedor"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.element_stock"
                      label="Stock"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.fkTask_id"
                      label="Tarea asignada"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="close"
              >
                Cancelar
              </v-btn>
              <v-btn
                color="blue darken-1"
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
            <v-card-title class="headline">¿Está seguro que desea Eliminarlo?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Cancelar</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogError" max-width="500px">
          <v-alert
            style="margin-bottom: 0; text-align: start;"
            type="error"
            transition="scale-transition"
          >
            Por favor, revise los datos ingresados e inténtelo nuevamente.
          </v-alert>
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
import Element from "@/classes/element";
  export default {
    data: () => ({
      search: '',
      dialog: false,
      dialogDelete: false,
      dialogError: false,
      headers: [
        {
          text: '#',
          align: 'center',
          sortable: false,
          value: 'id',
        },
        { text: 'Nombre', value: 'name' },
        { text: 'Descripción', value: 'description' },
        { text: 'Precio', value: 'price' },
        { text: 'Vendedor', value: 'reseller' },
        { text: 'Stock', value: 'element_stock' },
        { text: 'Tarea asignada', value: 'fkTask_id'},
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      elements: [],
      editedIndex: -1,
      editedItem: {
        id : '', 
        name : '', 
        description: '', 
        price: '', 
        reseller: '', 
        element_stock: '', 
        fkInventory_id : '', 
        fkTask_id : ''
      },
      defaultItem: {
        id : '', 
        name : '', 
        description: '', 
        price: '', 
        reseller: '', 
        element_stock: '', 
        fkInventory_id : '', 
        fkTask_id : ''
      },
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'Nuevo Elemento' : 'Editar Elemento'
      },
    },

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
    filterOnlyCapsText(value, search) {
      return (
        value != null &&
        search != null &&
        typeof value === "string" &&
        value.toString().toLocaleUpperCase().indexOf(search.toUpperCase()) !==
          -1
      );
    },
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
      initialize () {
        return api
            .getElement()
            .then((response)=> {
                for(let element of response.data){
                    this.elements.push(element)
                }
                for(let element of this.elements){
                    if(element.fkTask_id === null){
                        element.fkTask_id = 'No asignada'
                    }
                }
            })     
      },
      editItem (item) {
          this.editedIndex = this.elements.indexOf(item)
          this.editedItem = Object.assign({}, item)
          this.dialog = true
      },

      deleteItem (item) {
        this.editedIndex = this.elements.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialogDelete = true
      },

      deleteItemConfirm () {
        return api
        .deleteElement(this.editedItem.id)
        .then(()=>{
            this.elements.splice(this.editedIndex, 1)
            this.closeDelete()
        })
        .catch(()=>{
            this.dialogError=true;
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
        let element = new Element(
            this.editedItem.name, 
            this.editedItem.description, 
            this.editedItem.price, 
            this.editedItem.reseller, 
            this.editedItem.element_stock, 
            1, 
            this.editedItem.fkTask_id === 'No asignada' ? null : this.editedItem.fkTask_id
        );
        if (this.editedIndex > -1) {
            return api
            .updateElement(element,this.editedItem.id)
            .then(()=>{
                Object.assign(this.elements[this.editedIndex], this.editedItem)
                this.close()
            })
            .catch(()=>{
                this.dialogError=true;
            })
        } else {
            return api
            .createElement(element)
            .then(()=>{
                this.elements.push(this.editedItem)
                this.close()
            })
            .catch(()=>{
                this.dialogError=true;
            })
        }     
      },
    },
  }
</script>