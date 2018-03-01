# vue-cli

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

if hot reload doesn't work, try:
```bash
npm rebuild node-sass --force
npm update --dev --save (--save/--save-dev -f)
npm install (--save/--save-dev)
```

For detailed explanation on how things work, consult the [docs for vue-loader](http://vuejs.github.io/vue-loader).


eslint:
.eslintrc.yml -> configuration
.eslintignore -> ignore some directory
run on all files:
./node_modules/eslint/bin/eslint.js --fix --ext .js,.vue .

or, if installed globally:
eslint --fix --ext .js,.vue .
