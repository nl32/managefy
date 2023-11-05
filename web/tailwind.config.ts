import { type Config } from "tailwindcss";
import { fontFamily } from "tailwindcss/defaultTheme";

export default {
  content: ["./src/**/*.tsx"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["var(--font-sans)", ...fontFamily.sans],
      },
      colors: {
        "neutral-primary": "#FDF0D5",
        "accent-primary": "#C6D8D3",
        "accent-secondary": "#F0544F",
        "neutral-secondary": "#331832",
        highlight: "#D81E5B",
      },
    },
  },
  plugins: [],
} satisfies Config;
