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
    },
  },
  plugins: [],
}

