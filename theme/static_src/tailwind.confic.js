// theme/static_src/tailwind.config.js

module.exports = {
  content: [
    "../../resume/templates/**/*.html",
    "../../theme/templates/**/*.html",
    "../../**/templates/**/*.html",
    "../../**/*.py",
    "../../**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#1D4ED8',   // You can customize these
        secondary: '#9333EA',
      },
      fontFamily: {
        sans: ['Open Sans', 'sans-serif'],
        roboto: ['Roboto', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
