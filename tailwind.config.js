/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.css",
    "./**/templates/**/*.html",
    "./**/static/**/*.css",
    "./frontend/src/**/*.{js,ts,jsx,tsx}",
    "./**/*.py"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
