v = [{"cat":"Red","description":"Tandrima_Abhishek Marriage(Tandrima)", "link":"https://youtu.be/UB_zKSXNhC8","image":"img/tm-img-02-tn.jpg" },
    { "cat":"Red","description":"Abhishek Tandrima Marriage (Abhishek)", "link":"https://youtu.be/gSyQjwOsgPMith","image":"img/tm-img-01.jpg" },
    { "cat":"Red","description":"Ushasi Nirveek Marriage Cinematic", "link":"https://youtu.be/4BmjgZYaBZI","image":"img/tm-img-01.jpg" },
    { "cat":"Red","description":"Ushasi Nirveek Marriage Full(Ushasi)", "link":"https://youtu.be/W8AblVh6Z6E","image":"img/tm-img-01.jpg" },
    { "cat":"Red","description":"Jhallika Subham Marriage", "link":"https://youtu.be/cU-1fD9Twh4","image":"img/tm-img-01.jpg" },
    { "cat":"Red","description":"Ipsa Sougata Marriage", "link":"https://youtu.be/Yuwy35stZo0","image":"img/tm-img-01.jpg" },
    { "cat":"Green","description":"Saraswati Puja 2009", "link":"https://youtu.be/hHQ_6U81Y4Y","image":"img/tm-img-01.jpg" },
    { "cat":"Green","description":"Prasanta Kumar De | Renuka De | 50 Years Wedding Anniversary Celebration", "link":"https://youtu.be/hXDlfutLyW8","image":"img/tm-img-01.jpg" },
    { "cat":"Green","description":"Bijaya Sammiloni 2021", "link":"https://youtu.be/Co3i0Jtl_sc","image":"img/tm-img-01.jpg" },
    { "cat":"Green","description":"Dipankar Rimi Marriage(Home videos)", "link":"https://youtu.be/lvWLZuLijK0","image":"img/tm-img-01.jpg" }]

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