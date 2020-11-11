<template>
  <v-row class="fill-height">
    <v-col>
      <v-sheet height="64">
        <v-toolbar flat>
          <v-toolbar-title v-if="$refs.calendar">{{
            $refs.calendar.title
          }}</v-toolbar-title>
          <v-btn fab text small color="grey darken-2" @click="prev">
            <v-icon small>fas fa-chevron-left</v-icon>
          </v-btn>
          <v-btn fab text small color="grey darken-2" @click="next">
            <v-icon small>fas fa-chevron-right</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
        </v-toolbar>
      </v-sheet>
      <v-sheet height="600">
        <v-calendar
          ref="calendar"
          v-model="focus"
          color="primary"
          :events="events"
          :event-color="getEventColor"
          :type="type"
          @click:event="showEvent"
          @click:day="newEvent"
        ></v-calendar>
        <v-menu
          v-model="selectedOpen"
          :close-on-content-click="false"
          :activator="selectedElement"
          offset-x
        >
          <v-card color="grey lighten-4" min-width="350px" flat>
            <v-toolbar :color="selectedEvent.color" dark>
              <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon class="right-position" @click="editQuotation">
                <v-icon>far fa-edit</v-icon>
              </v-btn>
            </v-toolbar>
            <v-card-text>
              <span>Detalles de la solicitud</span>
              <br />
              <br />
              <span>Tipo de servicio: {{ selectedEvent.service_type }}</span>
              <br />
              <span>Descripción: {{ selectedEvent.description }}</span>
              <br />
              <span>Fecha: {{ selectedEvent.start }}</span>
              <br />
              <span>Rango de tiempo: {{ selectedEvent.time_range }}</span>
              <br />
            </v-card-text>
            <v-card-actions>
              <v-btn
                class="right-position"
                text
                color="secondary"
                @click="selectedOpen = false"
                >Cerrar</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-sheet>
    </v-col>
    <v-dialog v-model="quotationDialog" max-width="500px">
      <v-card>
        <v-card-title>{{ dialogTitle }}</v-card-title>
        <v-card-text>
          <v-select
            v-model="cbServiceType"
            :items="serviceType"
            label="Tipo de servicio"
            item-value="text"
            :rules="rules"
          ></v-select>
          <v-textarea
            v-model="taDescription"
            outlined
            name="input-7-4"
            label="Descripción:"
            :rules="rules"
          ></v-textarea>
          <v-chip-group
            v-model="selection"
            active-class="deep-purple accent-4 white--text"
            column
          >
            <v-chip>08:00</v-chip>
            <v-chip>10:00</v-chip>
            <v-chip>13:00</v-chip>
            <v-chip>15:00</v-chip>
            <v-chip>17:00</v-chip>
          </v-chip-group>
        </v-card-text>
        <v-card-actions>
          <v-btn
            class="right-position"
            color="primary"
            text
            @click="validateData"
            >Confirmar</v-btn
          >
          <v-btn
            class="right-position"
            color="primary"
            text
            @click="closeQuotation"
            >Cerrar</v-btn
          >
        </v-card-actions>
        <v-alert
          v-model="incompleteData"
          v-if="incompleteData"
          border="left"
          color="red"
          dismissible
          type="error"
          >Por favor llena todos los campos</v-alert
        >
      </v-card>
    </v-dialog>
    <v-dialog v-model="confirmDialog" max-width="400px" min-width="400px">
      <v-card>
        <v-card-title>Confirmación</v-card-title>
        <v-card-text>
          <span>¿Está seguro que desea continuar?</span>
          <br />
          <br />
          <span>Tipo de servicio: {{ cbServiceType }}</span>
          <br />
          <span>Descripción: {{ taDescription }}</span>
          <br />
          <span>Hora: {{ availability[selection] }}</span>
          <br />
        </v-card-text>
        <v-card-actions>
          <v-btn
            class="right-position"
            color="primary"
            text
            @click="confirmQuotation"
            >{{ confirmBtnTitle }}</v-btn
          >
          <v-btn
            class="right-position"
            color="primary"
            text
            @click="confirmDialog = false"
            >Cerrar</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="alertDialog" width="300">
      <v-alert
        style="margin-bottom: 0;"
        type="error"
        transition="scale-transition"
      >
        {{ alertMessage }}
      </v-alert>
    </v-dialog>
  </v-row>
</template>

<script>
import api from "@/api";
import RequestQuotation from "@/classes/requestQuotation";
export default {
  name: "CalendarComponent",
  data: () => ({
    alertDialog: false,
    alertMessage: "",
    focus: "",
    type: "month",
    dialogTitle: "",
    confirmBtnTitle: "",
    selectedEvent: {},
    selectedElement: null,
    selectedOpen: false,
    eventCanceled: false,
    eventId: 0,
    eventDate: "",
    createEvent: null,
    createStart: null,
    quotationDialog: false,
    confirmDialog: false,
    cbServiceType: "",
    serviceType: [
      { text: "Servicio 1" },
      { text: "Servicio 2" },
      { text: "Servicio 3" },
      { text: "Servicio 4" },
      { text: "Servicio 5" },
      { text: "Servicio 6" },
      { text: "Servicio 7" }
    ],
    taDescription: "",
    selection: 0,
    availability: [
      "08:00 - 09:30",
      "10:00 - 11:30",
      "13:00 - 14:30",
      "15:00 - 16:30",
      "17:00 - 18:30"
    ],
    events: [],
    rules: [value => !!value || "Este campo no puede estar vacio"],
    incompleteData: false,
    request_quotation: {},
    quotations_dates: []
  }),
  created() {
    this.getQuotationsByID();
  },
  mounted() {
    this.$refs.calendar.checkChange();
  },
  methods: {
    prev() {
      this.$refs.calendar.prev();
    },
    next() {
      this.$refs.calendar.next();
    },
    getEventColor(event) {
      return event.color;
    },
    showEvent({ nativeEvent, event }) {
      const open = () => {
        this.selectedEvent = event;
        this.selectedElement = nativeEvent.target;
        setTimeout(() => {
          this.selectedOpen = true;
        }, 10);
      };

      if (this.selectedOpen) {
        this.selectedOpen = false;
        setTimeout(open, 10);
      } else {
        open();
      }

      nativeEvent.stopPropagation();
    },
    newEvent({ date }) {
      this.eventCanceled = false;
      this.dialogTitle = "Solicitud de Cotización";
      this.confirmBtnTitle = "Confirmar";
      this.quotationDialog = true;
      this.eventDate = date;
    },
    closeQuotation() {
      this.cbServiceType = "";
      this.taDescription = "";
      this.selection = 0;
      this.eventCanceled = true;
      this.incompleteData = false;
      this.quotationDialog = false;
    },
    confirmQuotation() {
      if (!this.eventCanceled) {
        this.newRequestQuotation();
        this.confirmDialog = false;
      }
    },
    drawEvent() {
      this.createStart = new Date(
        `${this.eventDate}T${this.availability[this.selection].substring(
          0,
          5
        )}:00`
      );
      this.createEvent = {};
      this.createEvent = {
        id: this.eventId,
        name: "Solicitud de cotización",
        color: "cyan",
        scheduled_date: this.eventDate,
        start: this.createStart,
        end: this.createStart,
        service_type: this.cbServiceType,
        description: this.taDescription,
        time_range: this.availability[this.selection],
        timed: true
      };
      this.events.push(this.createEvent);
      this.closeQuotation();
    },
    newRequestQuotation() {
      let request_quotation = new RequestQuotation(
        this.eventDate,
        this.availability[this.selection],
        false,
        this.cbServiceType,
        this.taDescription,
        this.$store.getters.retrieveId
      );
      if (this.confirmBtnTitle == "Confirmar") {
        return api.createRequestQuotation(request_quotation).then(resp => {
          if (resp.status == 400) {
            this.alertDialog = true;
            this.alertMessage = resp.data.scheduled_date_and_time_range[0];
            this.confirmDialog = false;
          } else {
            this.eventId = resp.data.id;
            this.drawEvent();
          }
        });
      } else if (this.confirmBtnTitle == "Guardar") {
        return api
          .updateQuotationByID(
            this.selectedEvent.id,
            request_quotation,
            this.selectedEvent.scheduled_date
          )
          .then(resp => {
            if (resp.status == 400) {
              this.alertDialog = true;
              this.alertMessage = resp.data;
              this.confirmDialog = false;
            } else {
              this.events = [];
              this.getQuotationsByID();
              this.closeQuotation();
            }
          });
      }
    },
    validateData() {
      if (this.cbServiceType != "" && this.taDescription != "") {
        this.confirmDialog = true;
      } else {
        this.incompleteData = true;
      }
    },
    editQuotation() {
      let now = new Date();
      let nowPlus2 = now.setDate(now.getDate() + 2);
      let validDate = new Date(nowPlus2);

      if (this.selectedEvent.start >= validDate) {
        this.eventCanceled = false;
        this.selectedOpen = false;
        this.dialogTitle = "Editar Solicitud de Cotización";
        this.confirmBtnTitle = "Guardar";
        this.cbServiceType = this.selectedEvent.service_type;
        this.taDescription = this.selectedEvent.description;
        this.selection = this.availability.indexOf(
          this.selectedEvent.time_range
        );
        this.quotationDialog = true;
      } else {
        this.alertDialog = true;
        this.alertMessage =
          "Error al editar la cita. Solo se puede editar las citas con dos(2) o más días de anticipación";
      }
    },
    getQuotationsByID() {
      return api
        .getQuotationsByID()
        .then(res => {
          if (res.status != 200) {
            this.alertDialog = true;
            this.alertMessage = "Error al obtener citas: " + res.data.detail;
          } else {
            this.quotations_dates = res.data;
          }
        })
        .finally(() => {
          this.quotations_dates.forEach(element => {
            this.createStart = new Date(
              `${element.scheduled_date}T${element.time_range.substring(
                0,
                5
              )}:00`
            );
            this.createEvent = {};
            this.createEvent = {
              id: element.id,
              name: "Solicitud de cotización",
              color: "cyan",
              scheduled_date: element.scheduled_date,
              start: this.createStart,
              end: this.createStart,
              service_type: element.service_type,
              description: element.description,
              time_range: element.time_range,
              timed: true
            };
            this.events.push(this.createEvent);
          });
        })
        .catch(e => {
          console.log(e);
        });
    }
  }
};
</script>