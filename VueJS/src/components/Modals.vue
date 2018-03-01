<template lang="html">
    <simplert :useRadius="true"
            :useIcon="true"
            ref="simplert">
    </simplert>
</template>

<script>
    import Simplert from 'vue2-simplert'
    export default {
        data() {
            return {
                modal_alert: {
                    title: 'Hi there',
                    message: 'the <b>content!<b>',
                    type: 'info',
                }
            }
        },
        components: {
            Simplert,
        },
        mounted() {
            this.$refs.simplert.openSimplert(this.modal_alert)
        }
    }
</script>

<style lang="css">
</style>
