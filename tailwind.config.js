/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/base.html',
    './static/src/**/*.js',
    './content_feeds/templates/**/*.html',
    './user_profile/templates/**/*.html',
    './user_submissions/templates/**/*.html'
  ],
  theme: {
    extend: {
      fontFamily: {
        heading: ['Playfair Display', 'serif'],
        body: ['Poppins', 'sans-serif']
      },
      colors: {
        lightest: '#f2f2f2', // Light grey
        light: '#ebd5d5', // Soft pink
        coral: '#ea8a8a', // Coral
        fourth: '#685454', // Deep brown
      },
    },
  },
  plugins: [],
}

