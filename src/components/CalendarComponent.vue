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
          @click:day="quotationDialog = true"
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
              <v-btn icon>
                <v-icon>far fa-edit</v-icon>
              </v-btn>
              <v-toolbar-title v-html="selectedEvent.name"></v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon>
                <v-icon>fas fa-heart</v-icon>
              </v-btn>
              <v-btn icon>
                <v-icon>fas fa-ellipsis-v</v-icon>
              </v-btn>
            </v-toolbar>
            <v-card-text>
              <span v-html="selectedEvent"></span>
            </v-card-text>
            <v-card-actions>
              <v-btn text color="secondary" @click="selectedOpen = false">Cancel</v-btn>
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
          ></v-select>
          <v-textarea v-model="taDescription" outlined name="input-7-4" label="Descripción:"></v-textarea>
          <v-menu
            ref="menu"
            v-model="menu2"
            :close-on-content-click="false"
            :nudge-right="40"
            :return-value.sync="time"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="time"
                label="Selecciona una hora"
                prepend-icon="mdi-clock-time-four-outline"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-time-picker
              v-if="menu2"
              v-model="time"
              format="24hr"
              :allowed-hours="allowedHours"
              :allowed-minutes="allowedMinutes"
              min="8:00"
              max="17:00"
              full-width
              @click:minute="$refs.menu.save(time)"
            ></v-time-picker>
          </v-menu>
        </v-card-text>
        <v-card-actions>
          <v-btn
            class="right-position"
            color="primary"
            text
            @click="confirmDialog = true"
          >Confirmar</v-btn>
          <v-btn class="right-position" color="primary" text @click="closeQuotation">Cerrar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="confirmDialog" max-width="400px" min-width="400px">
      <v-card>
        <v-card-title>CONFIRMAR</v-card-title>
        <v-card-text>
          <v-textarea v-model="taDescription" outlined name="input-7-4" label="Descripción:"></v-textarea>
        </v-card-text>
        <v-card-actions>
          <v-btn
            class="right-position"
            color="primary"
            text
            @click="confirmDialog = false"
          >Confirmar</v-btn>
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
    time: null,
    menu2: false,
    events: [],
    colors: [
      "blue",
      "indigo",
      "deep-purple",
      "cyan",
      "green",
      "orange",
      "grey darken-1"
    ]
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
        timed: !allDay
      });

      this.events = events;
    },
    rnd(a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a;
    },
    newEvent({ date }) {
      this.createStart = new Date(`${date}T00:00:00`);
      this.createEvent = {
        name: `Solicitud de cotización`,
        color: this.colors[this.rnd(0, this.colors.length - 1)],
        start: this.createStart,
        end: this.createStart,
        timed: true
      };
      //this.events.push(this.createEvent);
      //console.log(this.createEvent);
    },
    allowedHours: value =>
      value >= 8 &&
      value <= 17 &&
      value != 9 &&
      value != 11 &&
      value != 12 &&
      value != 14 &&
      value != 16,
    allowedMinutes: value => value == 0,
    closeQuotation() {
      this.cbServiceType = "";
      this.taDescription = "";
      this.time = null;
      this.quotationDialog = false;
    }
  }
};
</script>