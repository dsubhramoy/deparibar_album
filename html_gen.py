v = [
    { "cat":"Green","description":"Bijaya Sammiloni 2022 | Part I", "link":"https://youtu.be/WhakBSGX9Uw","image":"img/dp221.JPG" },
    { "cat":"Green","description":"Bijaya Sammiloni 2022 | Part II", "link":"https://youtu.be/rhTp1580tnI","image":"img/dp222.JPG" },
    { "cat":"Green","description":"Sougata Ipsa Marriage (Sindhri)", "link":"https://youtu.be/tddOFpF4924","image":"img/IS.JPG" }]

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