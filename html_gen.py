v = [
    { "cat":"Green","description":"Ipsa Sougata Marriage (Slideshow)", "link":"https://youtu.be/KUkxvJ61hyA","image":"img/placeholder.png" },
    { "cat":"Green","description":"Ipsa Ushasi 25 Yrs Birthday Celebration", "link":"https://youtu.be/KRNiRlYu2hk","image":"img/placeholder.png" }]

for item in v:
    clr = item['cat']
    link = item['link']
    desc = item['description']
    image=item['image']


    a = f'''                                <div class="grid-item">
                                            <figure class="effect-bubba">
                                                <img src="{image}" alt="Image" class="img-fluid tm-img">
                                                <figcaption>
                                                    <p class="tm-figure-description">{desc}</p>
                                                </figcaption>           
                                            </figure>
                                            <a style="color:{clr}; font-weight: bold;" target="_blank" href="{link}">{desc}</a>
                                        </div> \n\n'''
    print(a)
for item in v:
    clr = item['cat']
    link = item['link']
    desc = item['description']
    image=item['image']


    a = f'''                                <a style="color:{clr}; font-weight: bold;" target="_blank" href="{link}">{desc}</a></br>'''
    print(a)