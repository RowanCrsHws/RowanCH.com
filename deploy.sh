pelican -v -D -s publishconf.py
tailwindcss -i input.css -o output/static/output.css
rsync -avHAX ./output/ rowanch.com:/home/rowan/domains/www.rowanch.com/public_html/
