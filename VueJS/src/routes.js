import Header from './components/Header.vue'
import Home from './components/Home.vue'

import BookDetail from './components/books/BookDetail.vue'
import About from './components/About.vue'

// lazy loading
/* eslint-disable global-require */
const Books = resolve => {
    require.ensure(['./components/books/Books.vue'], () => {
        resolve(require('./components/books/Books.vue'))
    }) // add 'books' to load all components in the same bundle 'books'
}

// route.params to props:
// https://github.com/vuejs/vue-router/blob/dev/examples/route-props/app.js
// props: true }, // Pass route.params to props
// props: { name: 'world' }}, // static values
// props: dynamicPropsFn }, // custom logic for mapping between route and props

export default [
    {
        path: '',
        name: 'home',
        components: {
            default: Home,
            'header-top': Header,
        },
    },
    {
        path: '/books',
        components: {
            default: Books,
            'header-top': Header,
            // 'header-bottom': Header
        },
        children: [
            { path: ':id', component: BookDetail, name: 'bookDetail' },
        ],
    },
    {
        path: '/about/:name',
        components: {
            default: About,
            'header-top': Header,
        },
        name: 'about',
        props: true,
    },
    { path: '/redirect', redirect: { name: 'about', params: { name: 'Stranger' } } },
    { path: '*', redirect: '/' },
]
