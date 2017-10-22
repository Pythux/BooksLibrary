import Header from './components/Header.vue'
import Home from './components/Home.vue'

import BookStart from './components/books/BookStart.vue'
import BookDetail from './components/books/BookDetail.vue'
import BookEdit from './components/books/BookEdit.vue'
import About from './components/About.vue'

// lazy loading
const Books = resolve => {
    require.ensure(['./components/books/Books.vue'], () => {
        resolve(require('./components/books/Books.vue'))
    }, ) // add 'books' to load all components in the same bundle 'books'
}

// route.params to props:
// https://github.com/vuejs/vue-router/blob/dev/examples/route-props/app.js
// props: true }, // Pass route.params to props
// props: { name: 'world' }}, // static values
// props: dynamicPropsFn }, // custom logic for mapping between route and props

export const routes = [
    { path: '', name: 'home',
        components: {
            default: Home,
            'header-top': Header
        }
    },
    { path: '/books',
        components: {
            default: Books,
            'header-top': Header
            // 'header-bottom': Header
        },
        children: [
            { path: '', component: BookStart }, // if path: '/', it's / of main URL
            { path: ':id', component: BookDetail, name: 'bookDetail' },
            { path: ':id/edit', component: BookEdit, name: 'bookEdit' },
        ]
    },
    { path: '/about/:name',
        components: {
            default: About,
            'header-top': Header
        },
        props: true,  name: 'about'
    },
    { path: '/redirect', redirect: { name: 'about', params: { name: 'Stranger' } } },
    { path: '*', redirect: '/' },
]
