v = [
    { "cat":"Green","description":"Prasanta Kumar De | Renuka De | 50 Years Wedding Anniversary Celebration | Part II", "link":"https://youtu.be/yefauNhzn5Y","image":"img/50.png" },
    { "cat":"Green","description":"Basanta Utsab 2022", "link":"https://youtu.be/Co3i0Jtl_sc","image":"img/bu2022.jpg" }]

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