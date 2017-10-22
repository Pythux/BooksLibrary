<template lang="html">
  <ui-button
        type="primary"
        :color="color"
        size="large"
        @click="$emit('click', $event)"
  >
    <slot name="icon"><i :class="'fa fa-' + i"></i></slot>
    <slot></slot>
  </ui-button>
</template>

<script>
    import UiButton from '../Keen-UI/src/UiButton.vue'
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
            UiButton
        },
        computed: {
            color() {
                var arr = ['primary', 'orange', 'red']
                return arr[['primary', 'warning', 'danger'].indexOf(this.type)]
            }
        }
    }
</script>
