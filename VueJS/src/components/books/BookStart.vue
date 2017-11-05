<template lang="html">
  <div>
      <router-link
            tag="button"
            :to="{ name: 'bookDetail', params: { id: 'myBook' } }"
            class="btn"
      >Create a Book</router-link>
  </div>
</template>

<script>
    import UiButton from '../../lib/std/UiButton.vue'
    export default {
        components: {
            UiButton
        },
    }
</script>
