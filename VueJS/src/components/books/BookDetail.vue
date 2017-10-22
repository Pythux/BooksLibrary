<template lang="html">
  <div class="container">
      <p>Detail of Book: {{ $route.params.id }}</p>
      <router-link
            tag="button"
            :to="{ name: 'bookEdit', params: { id: $route.params.id } }"
            class="btn"
      >Edit User</router-link>
  </div>
</template>

<script>
    import UiButton from '../../lib/std/UiButton.vue'
    export default {
        components: {
            UiButton
        }
    }
</script>
