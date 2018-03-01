<template>
  <div>
      <modals></modals>
      <router-view name="header-top"></router-view>
      <transition name="slide-fade" mode="out-in" :duration="400">
          <router-view></router-view>
      </transition>
      <router-view name="header-bottom"></router-view>
  </div>
</template>

<script>
    import Modals from './components/Modals.vue'
    export default {
        data() {
            return {
            }
        },
        components: {
            Modals,
        },
        methods: {
        },
    }
</script>
<style>
    /* Les animations d'entrée (« enter ») et de sortie (« leave »)  */
    /* peuvent utiliser différentes fonctions de durée et de temps.  */
    .slide-fade-enter-active {
    transition: all .4s ease;
    }
    .slide-fade-leave-active {
    transition: all .6s cubic-bezier(1.0, 0.5, 0.8, 1.0);
    }
    .slide-fade-enter, .slide-fade-leave-to
    /* .slide-fade-leave-active below version 2.1.8 */ {
    transform: translateX(10px);
    opacity: 0;
    }
</style>
