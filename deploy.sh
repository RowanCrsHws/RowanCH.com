pelcan -v -D
tailwindcss -i input.css -o output/output.css
rsync -avHAX ./output/ rowanch.com:/home/rowan/domains/www.rowanch.com/public_html/
