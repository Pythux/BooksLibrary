<template lang="html">
  <div class="col-md-offset-1 col-xs-offset-1">
      <h1>Header...
          <ui-button
            type="primary"
            i="camera"
            @click="navigateToHome"
          >
          Home
          </ui-button>

      </h1>
      <ul class="nav nav-pills">
          <router-link to="/books" tag="li" active-class="active" exact>
              <a>Books</a>
          </router-link>
          <router-link
            to="/about/you?a=2" tag="li"
            active-class="active" exact
          ><a>about</a></router-link>
      </ul>
  </div>
</template>

<script>
    import UiButton from '../lib/std/UiButton.vue'
    export default {
        components: {
            UiButton
        },
        methods: {
            navigateToHome() {
                // this.$router.push('/')
                // this.$router.push({path: '/'})
                this.$router.push({ name: 'home' })
            }
        }
    }
</script>

<style lang="css">
</style>
