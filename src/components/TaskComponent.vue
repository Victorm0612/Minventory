<template>
    <v-expansion-panels class="pl-5">
        <v-expansion-panel v-for="item in Task" :key="item.id">
            <v-expansion-panel-header style="font-weight: bold;">
                <v-row class="d-flex" align="center" justify="start">
                    <v-col cols="12" sm="8" md="6">
                        {{item.id}}
                    </v-col>
                </v-row>
            </v-expansion-panel-header>
                <v-expansion-panel-content style="text-align: start;">
                    <hr class="mb-3" style="border: 1px solid black;">
                    <v-row>
                        <v-col id="title">
                            Fecha de aprovación:
                        </v-col>
                        <v-col>
                            {{item.approved_date}}
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col id="title">
                            Fecha a realizar:
                        </v-col>
                        <v-col>
                            {{item.realization_date}}
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col id="title">
                            Trabajador asignado:
                        </v-col>
                        <v-col>
                            {{item.fkAssignment_worker}}
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col id="title">
                            Elementos para tarea:
                        </v-col>
                        <v-col>
                            {{item.fkElement_id}}
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col id="title">
                            Estado actual de la tarea:
                        </v-col>
                        <v-col>
                            {{item.fkTask_status}}
                        </v-col>
                    </v-row>
                </v-expansion-panel-content>
        </v-expansion-panel>
    </v-expansion-panels>
</template>

<script>
import api from "@/api";
    export default {
        name: "TaskComponent",
        data(){
            return {
                Task:[],
            }
        },
        created(){
            return api
            .getTasks(this.isAdmin)
            .then(response=>{
                this.Task = response.data
            })
            .catch((error)=>{
                console.log(error)
            })
        },
        computed: {
            isAdmin(){
                if(this.$store.getters.retrieveUser.type_user == 3){
                    return 'task/employee-task/'+this.$store.getters.retrieveUser.id_user
                }
                else{
                    return 'task/'
                }
            }
        },
        methods: {
        },
    }

</script>

<style scoped>
#title{
    font-weight: bold;
}
</style>