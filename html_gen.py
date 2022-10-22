v = [
    { "cat":"Green","description":"Bijaya Sammiloni 2020", "link":"https://youtu.be/Et5bGzjZKhA","image":"img/dp20.JPG" },
    { "cat":"Green","description":"Bijaya Sammiloni 2019", "link":"https://youtu.be/V5AucnMtkvk","image":"img/dp19.JPG" },
    { "cat":"Green","description":"Bijaya Sammiloni 2018", "link":"https://youtu.be/ZiY6jc9FxIc","image":"img/dp18.png" },
    { "cat":"Red","description":"Dipankar Rimi Marriage (Katwa)", "link":"https://youtu.be/JsDWkX09miE","image":"img/DR.JPG" }]

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