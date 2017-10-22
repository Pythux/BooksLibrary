<template lang="html">
    <button
        :class="'btn btn-' + type"
        @click="$emit('click', $event)"
        ><i :class="'fa fa-' + fontAwesome"></i> <slot></slot></button>
</template>

<script>
    export default {
        props: ['type', 'fontAwesome'],
    }
</script>

<style lang="css" scoped>
    /* how to scope bootstrap:
    https://stackoverflow.com/questions/10568065/limit-the-scope-of-bootstrap-styles
    */
</style>
