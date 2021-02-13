/* global __dirname */
/* global module */
/* global require */

const path = require('path')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')

module.exports = {

  entry: {
    main: './assets/src/js/main.js',
  },

  output: {
    path: path.resolve(__dirname, '../assets/dist'),
    filename: '[name].js',

    // See: https://stackoverflow.com/questions/64294706/webpack5-automatic-publicpath-is-not-supported-in-this-browser
    publicPath: ''
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env']
          }
        }
      },
      {
        test: /\.(sa|sc|c)ss$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          {
            loader: 'css-loader'
          },
          {
            loader: 'postcss-loader'
          },
          {
            loader: 'sass-loader',
            options: {
              implementation: require('sass')
            }
          }
        ]
      },
      {
        test: /\.(png|jpe?g|gif|svg)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              outputPath: 'images'
            }
          }
        ]
      }
    ]
  },

  plugins: [

    new MiniCssExtractPlugin({
      filename: 'style.css'
    }),

  ],

  mode: 'development'
}
