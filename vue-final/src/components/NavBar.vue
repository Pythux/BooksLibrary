<template>
  <v-toolbar app>
    <v-toolbar-title class="headline">
      <font-awesome-icon icon="book" />
      Library
    </v-toolbar-title>
    <v-spacer />
    <v-toolbar-items>
      <v-btn flat>
        Login
      </v-btn>
      <navSearch />
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
import Search from './Search.vue'
export default {
    components: {
        navSearch: Search,
    }
}
</script>
