module.exports = {
  css: {
    loaderOptions: {
      scss: {
        prependData: '@import "./src/assets/sass/global.scss";'
      }
    }
  },
  devServer: {
    proxy: {
      '/api*': {
        // Forward frontend dev server request for /api to flask dev server
        target: 'http://localhost:5000/'
      }
    }
  }
}
