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

          <width-transition>
            <v-layout
              v-if="onSearch"
              fill-height
            >
              <v-form
                action="/search?"
                method="GET"
              >
                <v-text-field
                  autocomplete="off"
                  placeholder="Search"
                  name="q"
                  @input="toSearch"
                />
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
          </width-transition>
        </v-layout>

        <v-layout
          v-if="onSearch && items.length > 0"
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
        inputSearch: "",
        items: [
        ],

    }),
    watch: {
        onSearch(onSearch) {
            if (!onSearch) {
                this.items = []
            }
        }
    },
    methods: {
        toSearch(input) {
            if (input == "yo") {
                this.items = [
                    {title: "yo", subtitle: "data"},
                    {title: "yo2", subtitle: "data2"},
                ]
            }
            else {
                this.items = []
            }
        }
    },
}
</script>
