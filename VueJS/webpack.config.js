
const path = require('path')
const webpack = require('webpack')

module.exports = {
    entry: './src/main.js',
    output: {
        path: path.resolve(__dirname, './dist'), // server side
        publicPath: '/',
        filename: 'bundle.js',
    },
    module: {
        rules: [
            // {
            //   test: /\.css$/,
            //   use: [
            //     'vue-style-loader',
            //     'css-loader'
            //   ],
            // },
            {
                test: /\.(css|scss|sass|less)$/i,
                use: [{
                    loader: 'style-loader',
                }, {
                    loader: 'css-loader',
                }, {
                    loader: 'sass-loader',
                }],

            },
            {
                test: /\.vue$/,
                use: [{
                    loader: 'vue-loader',
                }],
            },
            {
                test: /\.js$/,
                use: [{
                    loader: 'babel-loader',
                }],
                exclude: /node_modules/,
            },
            {
                test: /\.(png|jpg|gif|svg)$/,
                use: [{
                    loader: 'file-loader',
                    query: {
                        name: '[name].[ext]?[hash]',
                    },
                }],
            },
            {
                test: /\.(png|woff|woff2|eot|ttf|svg)$/,
                use: [{
                    loader: 'url-loader',

                    options: {
                        limit: 100000,
                    },
                }],
            },
        ],
    },
    resolveLoader: {
        alias: {
            'scss-loader': 'sass-loader',
        },
    },
    resolve: {
        alias: {
            vue$: 'vue/dist/vue.esm.js',
        },
        extensions: ['*', '.js', '.vue', '.json'],
    },
    performance: {
        hints: false,
    },
    devtool: '#eval-source-map',
    devServer: {
        historyApiFallback: true, // fallback 404 to index.html
    },
}

if (process.env.NODE_ENV === 'production') {
    module.exports.devtool = '#source-map'
    // http://vue-loader.vuejs.org/en/workflow/production.html
    module.exports.plugins = (module.exports.plugins || []).concat([
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: '"production"',
            },
        }),
        new webpack.optimize.UglifyJsPlugin({
            sourceMap: true,
            compress: {
                warnings: false,
            },
        }),
        new webpack.LoaderOptionsPlugin({
            minimize: true,
        }),
        new webpack.NamedModulesPlugin(),
    ])
}
