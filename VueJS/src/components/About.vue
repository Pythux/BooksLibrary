<template lang="html">
  <div>
      <p>Lorem ipsum dolor sit amet,
           at nulla pariatur. Excepteur sint occaecat cupi
           datat non proident, sunt in culpa qui officia deserun
           t mollit anim id est laborum.
       </p>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit,
           sed do eiusmod tempor incididunt ut labore et dolore m
           agna aliqua. Ut enim ad minim veniam, quis nostrud exerc
           tation ullamco laboris nisi ut aliquip ex ea commodo conse
           quat. Duis aute irure dolor in reprehenderit in voluptate
            velit esse cillum dolore eu fugiat nulla pariatur. Exce
            pteur sint occaecat cupidatat non proident, sunt in
          officia deserunt mollit anim id est laborum.
      </p>
      <!-- <p>Hi: {{ name }}</p> -->
      <hr>
      <p>params: {{ $route.params }}</p>
      <hr>
      <p>query: {{ $route.query }}</p>
      <div class="col-md-offset-5 col-xs-offset-5">
          <ui-button type="warning" i="check" @click="increment">Inc</ui-button>
          <ui-button type="danger" i="close" @click="decrement">Dec</ui-button>
          <!-- <button class="btn btn-primary" @click="decrement">Dec</button> -->
          <p>Counter is: {{ counter }}, double is: {{ double }}</p>
      </div>
      <hr>
      <div class="col-md-offset-2 col-xs-offset-2">
          <ui-button i='plus' @click="add">Ajouter</ui-button>
          <ui-button i ='minus' @click="remove">Enlever</ui-button>
          <transition-group name="list" tag="p">
            <span v-for="item in items" :key="item" class="list-item">
              {{ item }}
            </span>
          </transition-group>
      </div>
  </div>
</template>

<script>
    import UiButton from '../lib/std/UiButton.vue'
    export default {
        props: ['name'],
        components: {
            UiButton
        },
        data() {
            return {
                items: [1,2,3,4,5,6,7,8,9],
                nextNum: 10
            }
        },
        methods: {
            increment() {
                // this.$emit('updated', 1)
                this.$store.state.counter++
            },
            decrement() {
                // this.$emit('updated', -1)
                this.$store.state.counter--
            },
            randomIndex: function () {
                return Math.floor(Math.random() * this.items.length)
            },
            add: function () {
                this.items.splice(this.randomIndex(), 0, this.nextNum++)
            },
            remove: function () {
                this.items.splice(this.randomIndex(), 1)
            },
        },
        computed: {
            counter() {
                return this.$store.state.counter
            },
            double() {
                return this.$store.getters.doubleCounter
            }
        }
    }
</script>

<style>
    .list-item {
        display: inline-block;
        margin-right: 10px;
    }
    .list-enter-active, .list-leave-active {
        transition: all 1s;
    }
    .list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
        opacity: 0;
        transform: translateY(30px);
    }
</style>
