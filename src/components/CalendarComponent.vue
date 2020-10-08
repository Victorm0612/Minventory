<template>
  <v-row class="fill-height">
    <v-col>
      <v-sheet height="64">
        <v-toolbar flat>
          <v-toolbar-title v-if="$refs.calendar">{{ $refs.calendar.title }}</v-toolbar-title>
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

        <v-menu
          v-model="selectedOpen2"
          :close-on-content-click="false"
          position-x="50"
        >
          <v-card elevation="2" color="grey lighten-4" min-width="350px" flat>
            <v-toolbar :color="selectedEvent2.color" dark>
              <v-btn icon>
                <v-icon>far fa-edit</v-icon>
              </v-btn>
              <v-toolbar-title v-html="selectedEvent2.name"></v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
            <v-card-text>
              <span v-html="selectedEvent2"></span>
            </v-card-text>
            <v-card-actions>
              <v-btn text color="secondary" @click="selectedOpen2 = false">Cancel</v-btn>
            </v-card-actions>
          </v-card>
        </v-menu>
      </v-sheet>
    </v-col>
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
    selectedEvent2: {},
    selectedOpen2: false,
    createEvent: null,
    createStart: null,
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
    names: [
      "Meeting",
      "Holiday",
      "PTO",
      "Travel",
      "Event",
      "Birthday",
      "Conference",
      "Party"
    ]
  }),
  mounted() {
    this.$refs.calendar.checkChange();
  },
  methods: {
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

      //const min = new Date(`${start.date}T00:00:00`);
      //const max = new Date(`${end.date}T23:59:59`);
      //const days = (max.getTime() - min.getTime()) / 86400000;
      //const eventCount = this.rnd(days, days + 20);

      /**for (let i = 0; i < eventCount; i++) {
        const allDay = this.rnd(0, 3) === 0;
        const firstTimestamp = this.rnd(min.getTime(), max.getTime());
        const first = new Date(firstTimestamp - (firstTimestamp % 900000));
        const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000;
        const second = new Date(first.getTime() + secondTimestamp);

        events.push({
          name: this.names[this.rnd(0, this.names.length - 1)],
          start: first,
          end: second,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          timed: !allDay
        });
      }**/

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
      const open = () => {
        this.selectedEvent2 = this.createEvent;
        setTimeout(() => {
          this.selectedOpen2 = true;
        }, 10);
      };

      if (this.selectedOpen2) {
        this.selectedOpen2 = false;
        setTimeout(open, 10);
      } else {
        open();
        this.events.push(this.createEvent);
      }
    }
  }
};
</script>