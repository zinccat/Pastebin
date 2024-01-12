const { defineConfig } = require('@vue/cli-service')
require('dotenv').config({ path: '../.env' })
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    allowedHosts: 'all'
  },
})