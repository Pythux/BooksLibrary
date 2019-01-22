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
                name="expend-width"
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
}
</script>

<style>
.expend-width-leave-active, .expend-width-enter-active {
    transition: all .6s ease-in;
}
.expend-width-enter, .expend-width-leave-to
{
    max-width: 0;
}
.expend-width-leave, .expend-width-enter-to
{
    max-width: 200px;
}
</style>
