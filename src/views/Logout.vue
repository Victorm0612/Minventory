<template>
<v-container>
    <LogoutComponent/>
</v-container>
</template>

<script>
import LogoutComponent from "@/components/LogoutComponent.vue";
export default {
    name: "Login",
    components: {
        LogoutComponent,
        },
        data() {
            return {};
            },
};
</script>

<style lang="sass" scoped></style>
