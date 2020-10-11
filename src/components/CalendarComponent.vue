<template>
  <v-row class="fill-height">
    <v-col>
      <v-sheet height="64">
        <v-toolbar flat>
          <v-toolbar-title v-if="$refs.calendar">{{ $refs.calendar.title }}</v-toolbar-title>
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
          @change="updateRange"
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
              <v-btn icon class="right-position">
                <v-icon>far fa-edit</v-icon>
              </v-btn>
            </v-toolbar>
            <v-card-text>
              <span>Detalles de la solicitud</span>
              <br />
              <br />
              <span>Tipo de servicio: {{selectedEvent.service_type}}</span>
              <br />
              <span>Descripción: {{selectedEvent.description}}</span>
              <br />
              <span>Fecha: {{selectedEvent.start}}</span>
              <br />
            </v-card-text>
            <v-card-actions>
              <v-btn
                class="right-position"
                text
                color="secondary"
                @click="selectedOpen = false"
              >Cerrar</v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-sheet>
    </v-col>
    <v-dialog v-model="quotationDialog" max-width="500px">
      <v-card>
        <v-card-title>Solicitud de cotización</v-card-title>
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
          <v-chip-group v-model="selection" active-class="deep-purple accent-4 white--text" column>
            <v-chip>8:00</v-chip>
            <v-chip>10:00</v-chip>
            <v-chip>13:00</v-chip>
            <v-chip>15:00</v-chip>
            <v-chip>17:00</v-chip>
          </v-chip-group>
        </v-card-text>
        <v-card-actions>
          <v-btn class="right-position" color="primary" text @click="validateData">Confirmar</v-btn>
          <v-btn class="right-position" color="primary" text @click="closeQuotation">Cerrar</v-btn>
        </v-card-actions>
        <v-alert v-model="incompleteData" v-if="incompleteData" border="left" color="red" dismissible type="error">Por favor llena todos los campos</v-alert>
      </v-card>
    </v-dialog>
    <v-dialog v-model="confirmDialog" max-width="400px" min-width="400px">
      <v-card>
        <v-card-title>Confirmación</v-card-title>
        <v-card-text>
          <span>¿Está seguro que desea continuar?</span>
          <br />
          <br />
          <span>Tipo de servicio: {{cbServiceType}}</span>
          <br />
          <span>Descripción: {{taDescription}}</span>
          <br />
          <span>Hora: {{availability[selection]}}</span>
          <br />
        </v-card-text>
        <v-card-actions>
          <v-btn class="right-position" color="primary" text @click="confirmQuotation">Confirmar</v-btn>
          <v-btn class="right-position" color="primary" text @click="confirmDialog = false">Cerrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  name: "CalendarComponent",
  data: () => ({
    focus: "",
    type: "month",
    selectedEvent: {},
    selectedElement: null,
    selectedOpen: false,
    eventCanceled: false,
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
    availability: ["08:00", "10:00", "13:00", "15:00", "17:00"],
    events: [],
    colors: [
      "blue",
      "indigo",
      "deep-purple",
      "cyan",
      "green",
      "orange",
      "grey darken-1"
    ],
    rules: [value => !!value || "Este campo no puede estar vacio"],
    incompleteData: false
  }),
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
        console.log(nativeEvent);
        console.log(event);
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
    updateRange() {
      const events = [];
      const allDay = this.rnd(0, 3) === 0;
      events.push({
        name: "Prueba",
        start: new Date("2020-10-05T18:00:00"),
        end: new Date("2020-10-05T18:59:59"),
        color: this.colors[this.rnd(0, this.colors.length - 1)],
        service_type: "Servicio 1",
        description: "Una descripción",
        timed: !allDay
      });

      this.events = events;
    },
    rnd(a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a;
    },
    newEvent({ date }) {
      this.eventCanceled = false;
      this.quotationDialog = true;
      this.eventDate = date;
    },
    closeQuotation() {
      this.cbServiceType = "";
      this.taDescription = "";
      this.selection = 0;
      this.eventCanceled = true;
      this.incompleteData, this.quotationDialog = false;
    },
    confirmQuotation() {
      this.confirmDialog = false;

      if (!this.eventCanceled) {
        this.createStart = new Date(
          `${this.eventDate}T${this.availability[this.selection]}:00`
        );
        this.createEvent = {
          name: "Solicitud de cotización",
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          start: this.createStart,
          end: this.createStart,
          service_type: this.cbServiceType,
          description: this.taDescription,
          timed: true
        };

        this.events.push(this.createEvent);
      }
      this.closeQuotation();
    },
    validateData() {
      if (this.cbServiceType != "" && this.taDescription != "") {
        this.confirmDialog = true;
      } else {
        this.incompleteData = true;
      }
    }
  }
};
</script>