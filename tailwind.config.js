/** @type {import('tailwindcss').Config} */
module.exports = {
content: ["./themes/**/*.html", "./themes/**/*.js", "./content/**/*.md"],
theme: {
    extend: {},
},
corePlugins: {
    aspectRatio: false,
},
plugins: [
    require('@tailwindcss/aspect-ratio'),
    require("@catppuccin/tailwindcss")({
        // prefix to use, e.g. `text-pink` becomes `text-ctp-pink`.
        // default is `false`, which means no prefix
        prefix: "ctp",
        // which flavour of colours to use by default, in the `:root`
        defaultFlavour: "latte",
    }),
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
],
};
