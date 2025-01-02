module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
  ],
  theme: {
    screens: {
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
    extend: {
      spacing: {
        '96': '24rem',
      },
      colors: {
        'custom-color1': '#6C733D',
        'custom-color2': '#F2F2F2',
        'custom-color3': '#202426',
        'custom-color4': '#8C8C88',
        'custom-color5': '#9DA65D',

      },
      fontFamily: {
        'body': ['Syne', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/aspect-ratio'),
  ],
}