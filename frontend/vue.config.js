module.exports = {
  devServer: {
    proxy: {
      "^/": {
        target: "https://yanick007.pythonanywhere.com/",
        // target: "http://127.0.0.1:8000/",
        ws: false,
      },
    },
  },
  // outputDir must be added to Django's TEMPLATE_DIRS
  outputDir: "./dist/",
  // assetsDir must match Django's STATIC_URL
  assetsDir: "static",
};
