<template lang="html">
    <button-bootstrap
        :type="type"
        :fontAwesome="i"
        @click="$emit('click', $event)"
    ><slot>Submit</slot></button-bootstrap>
</template>

<script>
    import ButtonBootstrap from './ButtonBootstrap.vue'
    export default {
        props: {
            type: {
                type: String,
                default: 'secondary'
            },
            i: {
                type: String,
                default: 'circle-o'
            }
        },
        components: {
            ButtonBootstrap
        }
    }
</script>
