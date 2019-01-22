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

      <v-layout column>
        <v-layout fill-height>
          <v-btn
            flat
            @click="onSearch = true"
          >
            <font-awesome-icon
              icon="search"
              size="2x"
            />
          </v-btn>


          <v-layout fill-height>
            <v-form

              action="/search?"
              method="GET"
            >
              <transition
                @before-enter="beforeEnter"
                @enter="enter"
                @after-enter="afterEnter"
                @enter-cancelled="enterCancelled"
                @leave="leave"
                @after-leave="afterLeave"
                @leave-cancelled="leaveCancelled"
              >
                <v-text-field
                  v-if="onSearch"
                  autocomplete="off"
                  placeholder="Search"
                  name="q"
                />
              </transition>
            </v-form>

            <v-btn
              flat
              @click="onSearch = false"
            >
              <font-awesome-icon
                icon="times"
                size="2x"
              />
            </v-btn>
          </v-layout>
        </v-layout>

        <v-layout
          d-inline-flex
          style="height: 0px;"
        >
          <v-list two-line>
            <template v-for="(item, index) in items">
              <v-list-tile
                :key="item.title"
                @click=""
              >
                <v-list-tile-content>
                  <v-list-tile-title v-html="item.title" />
                  <v-list-tile-sub-title v-html="item.subtitle" />
                </v-list-tile-content>
              </v-list-tile>
            </template>
          </v-list>
        </v-layout>
      </v-layout>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
export default {
    data: () => ({
        onSearch: false,
        items: [
            {title: "yo", subtitle: "data"},
            {title: "yo2", subtitle: "data2"},
        ],
    }),
    methods: {
        beforeEnter (el) {
            el._parent = el.parentNode
            el._initialStyle = {
                transition: el.style.transition,
                visibility: el.style.visibility,
                overflow: el.style.overflow,
                width: el.style.width
            }
        },
        enter (el) {
            const initialStyle = el._initialStyle
            el.style.setProperty('transition', 'none', 'important')
            el.style.visibility = 'hidden'
            const width = `${el.offsetWidth}px`
            el.style.visibility = initialStyle.visibility
            el.style.overflow = 'hidden'
            el.style.width = 0
            void el.offsetWidth // force reflow
            el.style.transition = initialStyle.transition
            el.style.transition = 'all 0.6s'

            requestAnimationFrame(() => {
                el.style.width = width
            })
        },

        afterEnter: resetStyles,
        enterCancelled: resetStyles,

        leave (el) {
            el._initialStyle = {
                overflow: el.style.overflow,
                width: el.style.width
            }

            el.style.overflow = 'hidden'
            el.style.width = `${el.offsetWidth}px`

            requestAnimationFrame(() => el.style.width = 0)
        },
        afterLeave,
        leaveCancelled: afterLeave,
    },
}
function afterLeave (el) {
    resetStyles(el)
}
function resetStyles (el) {
    el.style.overflow = el._initialStyle.overflow
    el.style.width = el._initialStyle.width
    delete el._initialStyle
}
</script>
