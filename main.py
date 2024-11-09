import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Informática"
    page.bgcolor = "#17a589"
    page.window_width = 650
    page.window_height = 800
    
    image_width_Portada = 800
    image_height_Portada = 400
    
    img_height = 100
    img_width = 100
    border_radius = 25  # Ajusta el valor para el radio del borde

    # Audios Padres de la informática
    intro = ft.Audio(src="Intro.mp3", volume=1, balance=0)
    page.overlay.append(intro)
    
    Pascal = ft.Audio(src="Pascal.mp3", volume=1, balance=0)
    page.overlay.append(Pascal)
    
    Leibniz = ft.Audio(src="Leibniz.mp3", volume=1, balance=0)
    page.overlay.append(Leibniz)
    
    Babbage = ft.Audio(src="Babbage.mp3", volume=1, balance=0)
    page.overlay.append(Babbage)
    
    Lovelace = ft.Audio(src="Lovelace.mp3", volume=1, balance=0) 
    page.overlay.append(Lovelace)
    
    Hollerith = ft.Audio(src="Hollerith.mp3", volume=1, balance=0)
    page.overlay.append(Hollerith)
    
    Turing = ft.Audio(src="Turing.mp3", volume=1, balance=0)
    page.overlay.append(Turing)
    
    Neumann = ft.Audio(src="Neumann.mp3", volume=1, balance=0)
    page.overlay.append(Neumann)
    
    Shannon = ft.Audio(src="shannon.mp3", volume=1, balance=0)
    page.overlay.append(Shannon)
    
    Hopper = ft.Audio(src="Hopper.mp3", volume=1, balance=0)
    page.overlay.append(Hopper)
    
    McCarthy = ft.Audio(src="McCarthy.mp3", volume=1, balance=0)
    page.overlay.append(McCarthy)
    
    Berners = ft.Audio(src="Berners.mp3", volume=1, balance=0)
    page.overlay.append(Berners)
    
    Ritchie = ft.Audio(src="Ritchie.mp3", volume=1, balance=0)
    page.overlay.append(Ritchie)
    
    Thompson = ft.Audio(src="Thompson.mp3", volume=1, balance=0)
    page.overlay.append(Thompson)
    
    Gosling = ft.Audio(src="Gosling.mp3", volume=1, balance=0)
    page.overlay.append(Gosling)
    
    Jobs = ft.Audio(src="Jobs.mp3", volume=1, balance=0)
    page.overlay.append(Jobs)
    
    Wozniak= ft.Audio(src="Wozniak.mp3", volume=1, balance=0)
    page.overlay.append(Wozniak)
    
    Gates = ft.Audio(src="Gates.mp3", volume=1, balance=0)
    page.overlay.append(Gates)
    
    Zuckerberg = ft.Audio(src="Zuckerberg.mp3", volume=1, balance=0)
    page.overlay.append(Zuckerberg)
    
    Pages = ft.Audio(src="Pages.mp3", volume=1, balance=0)
    page.overlay.append(Pages)
    
    Brin = ft.Audio(src="Brin.mp3", volume=1, balance=0)
    page.overlay.append(Brin)

    #audios de lenguajes
    fortran = ft.Audio(src="fortran.mp3", volume=1, balance=0)
    page.overlay.append(fortran)
    
    cobol = ft.Audio(src="cobol.mp3",volume=1,balance=0)
    page.overlay.append(cobol)
    
    pascal = ft.Audio(src="pascal_lenguaje.mp3", volume=1,balance=0)
    page.overlay.append(pascal)
    
    c = ft.Audio(src="c.mp3",volume=1, balance=0)
    page.overlay.append(c)
    
    html = ft.Audio(src="html.mp3",volume=1,balance=0)
    page.overlay.append(html)
    
    python = ft.Audio(src="python.mp3",volume=1,balance=0)
    page.overlay.append(python)
    
    sql = ft.Audio(src="sql.mp3",volume=1,balance=0)
    page.overlay.append(sql)
    
    php = ft.Audio(src="php.mp3",volume=1,balance=0)
    page.overlay.append(php)
    
    java = ft.Audio(src="java.mp3",volume=1,balance=0)
    page.overlay.append(java)
    
    js = ft.Audio(src="ttsmaker-file-2024-11-4-19-0-25.mp3",volume=1,balance=0)
    page.overlay.append(js)
    
    perl = ft.Audio(src="perl.mp3",volume=1,balance=0)
    page.overlay.append(perl)
    
    swift = ft.Audio(src="swift.mp3",volume=1,balance=0)
    page.overlay.append(swift)
    
    facebook = ft.Audio(src="facebook.mp3",volume=1,balance=0)
    page.overlay.append(facebook)
    
    insta = ft.Audio(src="instagram (2).mp3",volume=1,balance=0)
    page.overlay.append(insta)
    
    twitter = ft.Audio(src="twitter.mp3",volume=1,balance=0)
    page.overlay.append(twitter)
    
    tinder = ft.Audio(src="tinder.mp3",volume=1,balance=0)
    page.overlay.append(tinder)
    
    whatsapp = ft.Audio(src="WhatsApp.mp3",volume=1,balance=0)
    page.overlay.append(whatsapp)
    
    tiktok = ft.Audio(src="WhatsApp.mp3",volume=1,balance=0)
    page.overlay.append(tiktok)
    
    telegram = ft.Audio(src="telegram.mp3",volume=1,balance=0)
    page.overlay.append(telegram)
    
    pinte = ft.Audio(src="Pinterest.mp3",volume=1,balance=0)
    page.overlay.append(pinte)
    
    grindr = ft.Audio(src="Grindr.mp3",volume=1,balance=0)
    page.overlay.append(grindr)
    
    link = ft.Audio(src="linkedin.mp3",volume=1,balance=0)
    page.overlay.append(link)
    
    videollamadas = ft.Audio(src="videollamada.mp3",volume=1, balance=0)
    page.overlay.append(videollamadas)
    
    homeoffice = ft.Audio(src="homeoffice.mp3",volume=1,balance=0)
    page.overlay.append(homeoffice)
    
    educacion = ft.Audio(src="educacion.mp3",volume=1,balance=0)
    page.overlay.append(educacion)
    
    streaming = ft.Audio(src="streaming.mp3",volume=1,balance=0)
    page.overlay.append(streaming)
    
    delivery =ft.Audio(src="delivery.mp3",volume=1,balance=0)
    page.overlay.append(delivery)
    
    redes=ft.Audio(src="delivery.mp3",volume=1,balance=0)
    page.overlay.append(redes)
    
    ia = ft.Audio(src="IA.mp3",volume=1,balance=0)
    page.overlay.append(ia)
    
    g = ft.Audio(src="5G.mp3",volume=1,balance=0)
    page.overlay.append(g)
    
    cuantica = ft.Audio(src="cuantica.mp3",volume=1,balance=0)
    page.overlay.append(cuantica)
    
    blockchain= ft.Audio(src="blockchain.mp3",volume=1,balance=0)
    page.overlay.append(blockchain)
    
    realidad1= ft.Audio(src="realidad_aumentada.mp3",volume=1,balance=0)
    page.overlay.append(realidad1)
    
    realidad2= ft.Audio(src="realidad_virtual.mp3",volume=1,balance=0)
    page.overlay.append(realidad2)
    
    biotecnologias= ft.Audio(src="biotecnologias.mp3",volume=1,balance=0)
    page.overlay.append(biotecnologias)
    
    impresion3d= ft.Audio(src="impresion3d.mp3",volume=1,balance=0)
    page.overlay.append(impresion3d)
    
    internetcosas= ft.Audio(src="internetcosas.mp3",volume=1,balance=0)
    page.overlay.append(internetcosas)
    
    def StopAll():
        intro.pause()
        Pascal.pause()
        Leibniz.pause()
        Babbage.pause()
        Lovelace.pause()
        Hollerith.pause()
        Turing.pause()
        Neumann.pause()
        Shannon.pause()
        Hopper.pause()
        McCarthy.pause()
        Berners.pause()
        Ritchie.pause()
        Thompson.pause()
        Gosling.pause()
        Jobs.pause()
        Wozniak.pause()
        Gates.pause()
        Zuckerberg.pause()
        Pages.pause()
        Brin.pause()
        fortran.pause()
        cobol.pause()
        pascal.pause()
        c.pause()
        html.pause()
        python.pause()
        sql.pause()
        php.pause()
        java.pause()
        js.pause()
        perl.pause()
        swift.pause()
        facebook.pause()
        insta.pause()
        twitter.pause()
        tinder.pause()
        whatsapp.pause()
        tiktok.pause()
        telegram.pause()
        pinte.pause()
        grindr.pause()
        link.pause()
        videollamadas.pause()
        homeoffice.pause()
        educacion.pause()
        streaming.pause()
        delivery.pause()
        redes.pause()
        ia.pause()
        g.pause()
        cuantica.pause()
        blockchain.pause()
        realidad1.pause()
        realidad2.pause()
        biotecnologias.pause()
        impresion3d.pause()
        internetcosas.pause()
        
    def play_intro(e):
        StopAll()
        intro.play()
        
    def play_pascal(e):
        StopAll()
        Pascal.play()
        
    def play_leibniz(e):
        StopAll()
        Leibniz.play()
        
    def play_babbage(e):
        StopAll()
        Babbage.play()
        
    def play_lovelace(e):    
        StopAll()
        Lovelace.play()
        
    def play_hollerith(e):
        StopAll()
        Hollerith.play()
        
    def play_turing(e):
        StopAll()
        Turing.play()
    
    def play_neumann(e):
        StopAll()
        Neumann.play()
        
    def play_shannon(e):
        StopAll()
        Shannon.play()
    
    def play_hopper(e):
        StopAll()
        Hopper.play()
    
    def play_mccarthy(e):
        StopAll()
        McCarthy.play()
    
    def play_berners(e):
        StopAll()
        Berners.play()
    
    def play_ritchie(e):
        StopAll()
        Ritchie.play()
        
    def play_thompson(e):
        StopAll()
        Thompson.play()
        
    def play_gosling(e):
        StopAll()
        Gosling.play()
        
    def play_jobs(e):
        StopAll()
        Jobs.play()
        
    def play_wozniak(e):
        StopAll()
        Wozniak.play()
        
    def play_gates(e):
        StopAll()
        Gates.play()
    
    def play_zuckerberg(e):
        StopAll()
        Zuckerberg.play()
    
    def play_pages(e):
        StopAll()
        Pages.play()
    
    def play_brin(e):
        StopAll()
        Brin.play()
    
    def play_fortran(e):
        StopAll()
        fortran.play()
    
    def play_cobol(e):
        StopAll()
        cobol.play()
        
    def play_pascal2(e):
        StopAll()
        pascal.play()
    
    def play_c(e):
        StopAll()
        c.play()
    
    def play_html(e):
        StopAll()
        html.play()
    
    def play_python(e):
        StopAll()
        python.play()
    
    def play_sql(e):
        StopAll()
        sql.play()
    
    def play_php(e):
        StopAll()
        php.play()
    
    def play_java(e):
        StopAll()
        java.play()
    
    def play_js(e):
        StopAll()
        js.play()
    
    def play_perl(e):
        StopAll()
        perl.play()
    
    def play_swift(e):
        StopAll()
        swift.play()
    
    def play_facebook(e):
        StopAll()
        facebook.play()
    
    def play_insta(e):
        StopAll()
        insta.play()
    
    def play_twitter(e):
        StopAll()
        twitter.play()
    
    def play_tinder(e):
        StopAll()
        tinder.play()
    
    def play_whatsapp(e):
        StopAll()
        whatsapp.play()
    
    def play_tiktok(e):
        StopAll()
        tiktok.play()
    
    def play_telegram(e):
        StopAll()
        telegram.play()
    
    def  play_pinterest(e):
        StopAll()
        pinte.play()
    
    def  play_grindr(e):
        StopAll()
        grindr.play()
    
    def  play_link(e):
        StopAll()
        link.play()
    
    def play_videollamadas(e):
        StopAll()
        videollamadas.play()
    
    def play_homeoffice(e):
        StopAll()
        homeoffice.play()
    
    def play_educacion(e):
        StopAll()
        educacion.play()
    
    def play_streaming(e):
        StopAll()
        streaming.play()
    
    def play_delivery(e):
        StopAll()
        delivery.play()
    
    def play_redes(e):
        StopAll()
        redes.play()
    
    def play_ia(e):
        StopAll()
        ia.play()
    
    def play_5g(e):
        StopAll()
        g.play()
    
    def play_cuantica(e):
        StopAll()
        cuantica.play()
    
    def play_bloackchain(e):
        StopAll()
        blockchain.play()
    
    def play_realidad1(e):
        StopAll()
        realidad1.play()
    
    def play_realidad2(e):
        StopAll()
        realidad2.play()
    
    def play_biotecnologias(e):
        StopAll()
        biotecnologias.play()
        
    def play_impresion3d(e):
        StopAll()
        impresion3d.play()
    
    def play_internetcosas(e):
        StopAll()
        internetcosas.play()
    
    
    btn1 = ElevatedButton(content=ft.Image(src="Pascal.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Blaise Pascal"), on_click=play_pascal)
    btn2 = ElevatedButton(content=ft.Image(src="Leibniz.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Gottfried Wilhelm Leibniz"), on_click=play_leibniz)
    btn3 = ElevatedButton(content=ft.Image(src="babbage.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Charles Babbage"), on_click=play_babbage)
    btn4 = ElevatedButton(content=ft.Image(src="Lovelace.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ada Lovelace"), on_click=play_lovelace)
    btn5 = ElevatedButton(content=ft.Image(src="Hollerith.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Herman Hollerith"), on_click=play_hollerith)
    btn6 = ElevatedButton(content=ft.Image(src="Turing.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Alan Turing"), on_click=play_turing)
    btn7 = ElevatedButton(content=ft.Image(src="Neumann.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John von Neumann"), on_click=play_neumann)
    btn8 = ElevatedButton(content=ft.Image(src="shannon.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Claude Shannon"), on_click=play_shannon)
    btn9 = ElevatedButton(content=ft.Image(src="Hopper.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Grace Hopper"), on_click=play_hopper)
    btn10 = ElevatedButton(content=ft.Image(src="McCarthy.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="John McCarthy"), on_click=play_mccarthy)
    btn11 = ElevatedButton(content=ft.Image(src="Berners.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Tim Berners-Lee"), on_click=play_berners)
    btn12 = ElevatedButton(content=ft.Image(src="Ritchie.png", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Dennis Ritchie"), on_click=play_ritchie)
    btn13 = ElevatedButton(content=ft.Image(src="Thompson.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Ken Thompson"), on_click=play_thompson)
    btn14 = ElevatedButton(content=ft.Image(src="Gosling.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="James Gosling"), on_click=play_gosling)
    btn15 = ElevatedButton(content=ft.Image(src="Jobs.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Jobs"), on_click=play_jobs)
    btn16 = ElevatedButton(content=ft.Image(src="Wozniak.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Steve Wozniak"), on_click=play_wozniak)
    btn17 = ElevatedButton(content=ft.Image(src="Gates.jpeg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Bill Gates"), on_click=play_gates)
    btn18 = ElevatedButton(content=ft.Image(src="Zuckerberg.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Mark Zuckerberg"), on_click=play_zuckerberg)
    btn19 = ElevatedButton(content=ft.Image(src="Pages.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Larry Page"), on_click=play_pages)
    btn20 = ElevatedButton(content=ft.Image(src="Brin.webp", width=img_width, height=img_height, border_radius=border_radius, semantics_label="Sergey Brin"), on_click=play_brin)
    btn21 = ElevatedButton(content=ft.Image(src="fortran.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="Fortran"), on_click=play_fortran)
    btn22 = ElevatedButton(content=ft.Image(src="cobol.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="cobol"), on_click=play_cobol)
    btn23 = ElevatedButton(content=ft.Image(src="pascal.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="pascal"), on_click=play_pascal2)
    btn24 = ElevatedButton(content=ft.Image(src="c.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="C"),on_click=play_c)
    btn25 = ElevatedButton(content=ft.Image(src="html.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="html"),on_click=play_html)
    btn26 = ElevatedButton(content=ft.Image(src="python.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="python"),on_click=play_python)
    btn27 = ElevatedButton(content=ft.Image(src="sql.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="sql"),on_click=play_sql)
    btn28 = ElevatedButton(content=ft.Image(src="php.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="php"),on_click=play_php)
    btn29 = ElevatedButton(content=ft.Image(src="java.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="java"),on_click=play_java)
    btn30 = ElevatedButton(content=ft.Image(src="javascrip.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="javascrip"),on_click=play_js)
    btn31 = ElevatedButton(content=ft.Image(src="perl.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="perl"),on_click=play_perl)
    btn32 = ElevatedButton(content=ft.Image(src="swift.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="swift"),on_click=play_swift)
    btn33 =  ElevatedButton(content=ft.Image(src="facebook.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="facebook"),on_click=play_facebook)
    btn34 =  ElevatedButton(content=ft.Image(src="insta.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="insta"),on_click=play_insta)
    btn35 =  ElevatedButton(content=ft.Image(src="twitter.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="twitter"),on_click=play_twitter)
    btn36 =  ElevatedButton(content=ft.Image(src="tinder.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="tinder"),on_click=play_tinder)
    btn37 =  ElevatedButton(content=ft.Image(src="what.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="whatsapp"),on_click=play_whatsapp)
    btn38 =  ElevatedButton(content=ft.Image(src="tiktok.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="tik tok"),on_click=play_tiktok)
    btn39 =  ElevatedButton(content=ft.Image(src="telegram.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="telegram"),on_click=play_telegram)
    btn40 = ElevatedButton(content=ft.Image(src="pinte.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="pinte"),on_click=play_pinterest)
    btn41 = ElevatedButton(content=ft.Image(src="grindr.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="grindr"),on_click=play_grindr)
    btn42 = ElevatedButton(content=ft.Image(src="link.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="linked"),on_click=play_link)
    btn43 = ElevatedButton(content=ft.Image(src="videollamada.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="videollamadas"),on_click=play_videollamadas)
    btn44 = ElevatedButton(content=ft.Image(src="homeoffice.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="home office"),on_click=play_homeoffice)
    btn45 = ElevatedButton(content=ft.Image(src="educacion.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="educacion"),on_click=play_educacion)
    btn46 = ElevatedButton(content=ft.Image(src="streaming.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="streaming"),on_click=play_streaming)
    btn47 = ElevatedButton(content=ft.Image(src="delivery.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="delivery"),on_click=play_delivery)
    btn48 = ElevatedButton(content=ft.Image(src="redes.png",width=img_width,height=img_height,border_radius=border_radius,semantics_label="redes sociales"),on_click=play_redes)
    btn49 = ElevatedButton(content=ft.Image(src="ia.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="ia"),on_click=play_ia)
    btn50 = ElevatedButton(content=ft.Image(src="5g.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="5g"),on_click=play_5g)
    btn51 = ElevatedButton(content=ft.Image(src="cuantica.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="cuantica"),on_click=play_cuantica)
    btn52 = ElevatedButton(content=ft.Image(src="blockchain.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="blockchain"),on_click=play_bloackchain)
    btn53 = ElevatedButton(content=ft.Image(src="realidad_aumentada.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="realidad aumentada"),on_click=play_realidad1)
    btn54 = ElevatedButton(content=ft.Image(src="realidad_virtual.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="realidad virtual"),on_click=play_realidad2)
    btn55 = ElevatedButton(content=ft.Image(src="biotecnologia.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="biotecnologias"),on_click=play_biotecnologias)
    btn56 = ElevatedButton(content=ft.Image(src="impresion3d.jpeg",width=img_width,height=img_height, border_radius=border_radius, semantics_label="impresion 3d"),on_click=play_impresion3d)
    btn57 = ElevatedButton(content=ft.Image(src="internetcosas.png",width=img_width,height=img_height, border_radius=border_radius, semantics_label="internet de las cosas"),on_click=play_internetcosas)
    # Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la Informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.ElevatedButton(
                                                'Los padres de la informática',
                                                on_click=lambda _: [StopAll(), page.go('/padres')]),
                                            ft.ElevatedButton(
                                                "la evolucion de los lenguajes de programacion",
                                                on_click=lambda _: [StopAll(), page.go('/lenguajes'),]),
                                        ]
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.ElevatedButton(
                                                'Las Redes Sociales',
                                                on_click=lambda _: [StopAll(), page.go('/redes')]),
                                            ft.ElevatedButton(
                                                'la informatica durante la pandemia de covid-19',
                                            on_click=lambda _: [StopAll(), page.go('/pandemia')]),
                                        ]
                                        ),
                                    ft.ElevatedButton(
                                        'las nuevas tecnologias',
                                        on_click=lambda _: [StopAll(), page.go('/nuevas')]),
                                    ft.Image(
                                        src="Portada.png",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Escucha el intro",
                                        on_click=play_intro
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Vista de los padres de la informática
        elif page.route == '/padres':
            page.views.append(
                View(
                    "/padres",
                    controls=[
                        AppBar(
                            title=ft.Text("Los padres de la informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "la evolucion de los lenguajes de informatica"',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3,btn4
                                        ]
                                    ),
                                    ft.Row(
                                      alignment="center",
                                      controls=[
                                        btn5, btn6, btn7,btn8
                                      ]  
                                    ),
                                    ft.Row(
                                       alignment="center",
                                        controls=[
                                          btn9, btn10, btn11,btn12
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn13,btn14,btn15,btn16
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn17,btn18,btn19,btn20
                                        ] 
                                    ),
                                     ElevatedButton(
                                        'La evolución de los lenguajes de programación',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de la evolución de los lenguajes de programación
        elif page.route == '/lenguajes':
            page.views.append(
                View(
                    "/lenguajes",
                    controls=[
                        AppBar(
                            title=ft.Text("La evolución de los lenguajes de programación"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "las redes sociales"',
                                        on_click=lambda _: page.go('/redes')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn21,btn22,btn23,btn24]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn25,btn26,btn27,btn28]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn29,btn30,btn31,btn32]
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de las redes sociales
        elif page.route == '/redes':
            page.views.append(
                View(
                    "/redes",
                    controls=[
                        AppBar(
                            title=ft.Text("Las redes sociales"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "la informatica durante la pandemia"',
                                        on_click=lambda _: page.go('/pandemia')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn33,btn34,btn35]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn36,btn37,btn38]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn39,btn40,btn41]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[btn42,]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        #viata de la informatica durante la pandemia
        elif page.route == '/pandemia':
            page.views.append(
                View(
                    "/pandemia",
                    controls=[
                        AppBar(
                            title=ft.Text("la informatica durante la pandemia de covid-19"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Ir a "las nuevas tecnologias"',
                                        on_click=lambda _: page.go('/nuevas')
                                    ),
                                    ft.Row(alignment="center",
                                        controls=[btn43,btn44,btn45]),
                                    ft.Row(alignment="center",
                                        controls=[btn46,btn47,btn48]),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        #vista de la las nuevas tecnologias
        elif page.route == '/nuevas':
            page.views.append(
                View(
                    "/nuevas",
                    controls=[
                        AppBar(
                            title=ft.Text("las nuevas tecnologias"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(alignment="center",
                                        controls=[btn49,btn50,btn51]),
                                    ft.Row(alignment="center",
                                        controls=[btn52,btn53,btn54]),
                                    ft.Row(alignment="center",
                                        controls=[btn55,btn56,btn57]
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
#ft.app(target=main,view=ft.WEB_BROWSER, assets_dir="assets")
