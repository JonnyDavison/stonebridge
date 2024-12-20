module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
  ],
  theme: {
    extend: {
      spacing: {
        '96': '24rem',
      },
      colors: {
        'custom-color1': '#6c705f',
        'custom-color2': '#eee3d4',
        'custom-color3': '#b8b7a5',
        'custom-color4': '#000000',
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