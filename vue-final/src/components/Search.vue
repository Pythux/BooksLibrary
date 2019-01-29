<template lang="html">
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
        <template v-for="item in items">
          <v-list-tile
            :key="item.id"
            @click=""
          >
            <v-list-tile-content>
              <v-list-tile-title :style="item.style.title">
                {{ item.title }}
              </v-list-tile-title>
              <v-list-tile-sub-title
                v-if="'subtitle' in item"
                :style="item.style.subtitle"
              >
                {{ item.subtitle }}
              </v-list-tile-sub-title>
            </v-list-tile-content>
          </v-list-tile>
        </template>
      </v-list>
    </v-layout>
  </v-layout>
</template>

<script>
export default {
    data: () => ({
        onSearch: false,
        inputSearch: "",
        items: [],
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
            if (input == '') {
                this.items = []
                return
            }
            const promises = [];
            [
                ['books', books_parser, 'title'],
                ['authors', authors_parser, 'first_name', 'last_name'],
                ['subjects', subjects_parser, 'subject']
            ].forEach(category => {
                const subject = category.shift()
                const parser = category.shift()

                promises.push(this.$http.get('/' + subject, {
                    params: {
                        q: {
                            filters: [
                                {
                                    or: category.map(filterOn => ({
                                        name: filterOn,
                                        op: "like",
                                        val: `%${input}%`,
                                    }))
                                }
                            ]
                        }
                    }
                })
                    .then(response => {
                        return response.data.objects.map(parser)
                    }))
            })
            const http_search = async () => {
                this.items = (await Promise.all(promises)).flat(1)
            }
            http_search()
        }
    },
}
const books_parser = ({id, title, description}) => ({
    id: 'books' + '/' + id,
    title,
    subtitle: description,
    style: {
        title: {
            color: 'orange',
        },
        subtitle: {
            color: 'pink',
        },
    }
})
const authors_parser = ({id, first_name, last_name}) => ({
    id: 'authors' + '/' + id,
    title: first_name + ' ' + last_name,
    style: {
        title: {
            color: 'green',
        },
    }
})
const subjects_parser = ({id, subject}) => ({
    id: 'subjects' + '/' + id,
    title: subject,
    style: {
        title: {
            color: 'blue',
        },
    }
})
</script>
