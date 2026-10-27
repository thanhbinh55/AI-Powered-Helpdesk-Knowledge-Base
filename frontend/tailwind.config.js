/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        helpdesk: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#4384F5', // HelpDesk Signature Blue
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
          sidebar: '#1E293B',
          canvas: '#F5F7F9',
        },
        internal: {
          bg: '#FEF9C3', // Light yellow amber note background
          border: '#FDE047',
          text: '#854D0E',
        },
        ai: {
          accent: '#8B5CF6',
          bg: '#F5F3FF',
          border: '#DDD6FE',
        }
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
