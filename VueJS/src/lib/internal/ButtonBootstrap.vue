<template lang="html">
    <button
        :class="'btn btn-' + type"
        @click="$emit('click', $event)"
    ><i
        :class="'fa fa-' + fontAwesome"
        aria-hidden="true"
    /> <slot/></button>
</template>

<script>
export default {
    props: {
        type: {
            type: String,
            required: true,
        },
        fontAwesome: {
            type: String,
            required: true,
        },
    },
}
</script>

<style lang="css" scoped>
    /* how to scope bootstrap:
    https://stackoverflow.com/questions/10568065/limit-the-scope-of-bootstrap-styles
    */
</style>
