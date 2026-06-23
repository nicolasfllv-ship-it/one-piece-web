from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <html>
    <head>
        <title>One Piece</title>

        <style>
        body {
    background: linear-gradient(135deg, #283694, #35408F, #1a1f4f);
    background-size: 400% 400%;
    animation: fondo 10s ease infinite;
    margin: 0;
    font-family: Arial;
    color: white;
    text-align: center;
}
       .card {
    background: rgba(0,0,0,0.6);
    border-radius: 20px;
    padding: 15px;
    width: 180px;
    transition: 0.3s;
    box-shadow: 0 8px 20px rgba(0,0,0,0.4);
}
.card img {
    width: 100%;
    height: 220px;
    object-fit: cover;
    border-radius: 15px;
}
}

.card img:hover {
    transform: scale(1.1);
}
.card:hover {
    transform: scale(1.08);
    box-shadow: 0 12px 25px rgba(0,0,0,0.6);
}
            body {
                background-color: #434D69;
                color: white;
                text-align: center;
                font-family: Arial;
            }

            .contenedor {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 20px;
                margin-top: 30px;
            }

            .card {
                background: #1e1e1e;
                border-radius: 20px;
                padding: 15px;
                width: 200px;
            }
        
             .card h3 {
               font-size: 20px;    
            }

            .card img {
                width: 100%;
                border-radius: 15px;
            }    
            .card a {
    display: inline-block;
    background: #ff6b35;
    color: white;
    padding: 8px 15px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
}
            }

            .card a {
                display: block;
                margin-top: 10px;
                color: gold;
                text-decoration: none;
            }
        </style>
    </head>

    <body>

        <h1>🏴‍☠️ ELIGE UN MUGIWARA 🏴‍☠️</h1>

        <div class="contenedor">

            <div class="card">
                <img src="/static/luffy.jpg">
                <h3>Luffy</h3>
                <a href="/luffy">Ver</a>
            </div>

            <div class="card">
                <img src="/static/zoro.jpg">
                <h3>Zoro</h3>
                <a href="/zoro">Ver</a>
            </div>

            <div class="card">
                <img src="/static/nami.jpg">
                <h3>Nami</h3>
                <a href="/nami">Ver</a>
            </div>

            <div class="card">
                <img src="/static/sanji.jpg">
                <h3>Sanji</h3>
                <a href="/sanji">Ver</a>
            </div>

            <div class="card">
                <img src="/static/chopper.jpg">
                <h3>Chopper</h3>
                <a href="/chopper">Ver</a>
            </div>

            <div class="card">
               <img src="/static/brook.jpg">
               <h3> Brook </h3>
               <a href="/brook"> Ver </a>
            </div>
            <div class="card">
               <img src="/static/nico robin.jpg">
               <h3>Nico Robin</h3>
               <a href="/nico-robin">ver</a>
            </div>
            <div class="card">
               <img src="/static/usopp.jpg">
               <h3>Usopp</h3>
               <a href="/usopp">ver</a>
            </div>
            <div class="card">
               <img src="/static/franky.jpg">
               <h3>Franky</h3>
               <a href="/franky">ver</a>
            </div>
            <div class="card">
               <img src="/static/jinbe.jpg">
               <h3>Jinbe</h3>
               <a href="/jinbe">ver</a>
            </div>
        </div>

    </body>
    </html>
    """

@app.route("/zoro")
def zoro():
    return """
    <html>
    <head>
        <title>zoro</title>

        <style>
            body {
                background: linear-gradient(135deg, #00a86b, #00331f); !important;
                margin: 0;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            .box {
                background: rgba(0,0,0,0.6);
                width: 60%;
                margin: auto;
                margin-top: 40px;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(255,255,255,0.2);
            }

            img {
                width: 250px;
                border-radius: 20px;
                transition: 0.3s;
            }

            img:hover {
                transform: scale(1.05);
            }

            a button {
                margin-top: 15px;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                background: gold;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>⚔️ Roronoa Zoro</h1>

            <img src="/static/zoro pagina.jpg">

            <p>
               Roronoa Zoro (ロロノア・ ゾロ Roronoa Zoro?),[16] conocido como El Cazador de Piratas (海賊狩り Kaizoku Gari?),[17] es el primer pirata que se unió a Monkey D. Luffy, y el principal combatiente de los Piratas de Sombrero de Paja, uno de sus dos espadachines y uno de los oficiales principales de la Gran Flota de Sombrero de Paja, así como un antiguo cazarrecompensas.[18][4]
            </p>

            <a href="/">
                <button>🏠 Volver</button>
            </a>
        </div>

    </body>
    </html>
    """
@app.route("/nami")
def nami():
    return """
    <html>
    <head>
        <title>Nami</title>

        <style>
            body {
            background: linear-gradient(135deg, #ff9f1c, #cc7000); !important;
                margin: 0;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            .box {
                background: rgba(0,0,0,0.6);
                width: 60%;
                margin: auto;
                margin-top: 40px;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(255,255,255,0.2);
            }

            img {
                width: 250px;
                border-radius: 20px;
                transition: 0.3s;
            }

            img:hover {
                transform: scale(1.05);
            }

            a button {
                margin-top: 15px;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                background: gold;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>🧭 Nami</h1>

            <img src="/static/nami pagina.jpg">

            <p>
                ami (ナミ Nami?), apodada Gata Ladrona (泥棒猫 Dorobō Neko?),[12] es una pirata y la navegante de los Piratas de Sombrero de Paja , así como una de los oficiales principales de la Gran Flota de Sombrero de Paja. Es el tercer miembro de la tripulación y la segunda en unirse, haciéndolo oficialmente durante el arco de Arlong Park.[13]
            </p>

            <a href="/">
                <button>🏠 Volver</button>
            </a>
        </div>

    </body>
    </html>
    """
@app.route("/luffy")
def luffy():
    return """
    <html>
    <head>
        <title>Luffy</title>

        <style>
            body {
                background: linear-gradient(135deg, #ff3c3c, #7a0000); !important;
                margin: 0;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            .box {
                background: rgba(0,0,0,0.6);
                width: 60%;
                margin: auto;
                margin-top: 40px;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(255,255,255,0.2);
            }

            img {
                width: 250px;
                border-radius: 20px;
                transition: 0.3s;
            }

            img:hover {
                transform: scale(1.05);
            }

            a button {
                margin-top: 15px;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                background: gold;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>🍖 Monkey D. Luffy</h1>

            <img src="/static/luffy pagina.jpg">

            <p>
               Monkey D. Luffy (モンキー・Ｄ・ルフィ Monkī Dī Rufi?), más conocido como Luffy «Sombrero de Paja» (麦わらのルフィ Mugiwara no Rufi?), es el protagonista principal de la serie de manga y anime One Piece. Es el capitán y fundador de los Piratas de Sombrero de Paja así como un de los Cuatro Emperadores que gobiernan los mares del Nuevo Mundo.[19] Comió una fruta del diablo llamada fruta Gomu Gomu, que le convirtió en un hombre de goma. Además de esto, posee varias habilidades que le hacen ser un pirata más que especial; un gran ejemplo de ello es la capacidad de usar el haoshoku haki ―que sólo lo posee una persona dentro de un millón― y poseer también los otros dos tipos de haki.
            </p>

            <a href="/">
                <button>🏠 Volver</button>
            </a>
        </div>

    </body>
    </html>
    """
@app.route("/sanji")
def sanji():
    return """
    <html>
    <head>
        <title>Sanji</title>

        <style>
            body {
                background: linear-gradient(135deg, #283694, #111a5c); !important;
                margin: 0;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            .box {
                background: rgba(0,0,0,0.6);
                width: 60%;
                margin: auto;
                margin-top: 40px;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(255,255,255,0.2);
            }

            img {
                width: 250px;
                border-radius: 20px;
                transition: 0.3s;
            }

            img:hover {
                transform: scale(1.05);
            }

            a button {
                margin-top: 15px;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                background: gold;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>👨‍🍳 Sanji</h1>

            <img src="/static/sanji pagina.jpg">

            <p>
               Sanji (サンジ Sanji?), conocido como Pierna Negra (黒脚 Kuro Ashi?) y nacido como Vinsmoke Sanji (ヴィンスモーク・サンジ Vinsumōku Sanji?),[3] es el cocinero de los Piratas de Sombrero de Paja, así como uno de los oficiales principales de la Gran Flota de Sombrero de Paja. Es el quinto miembro de la tripulación, y el cuarto en unirse. Él nació en el North Blue, siendo el primer tripulante en no ser originario del East Blue.
            </p>

            <a href="/">
                <button>🏠 Volver</button>
            </a>
        </div>

    </body>
    </html>
    """
@app.route("/chopper")
def chopper():
    return """
    <html>
    <head>
        <title>Chopper</title>

        <style>
            body {
                background: linear-gradient(135deg, #4cc9f0, #1d4ed8); !important;
                margin: 0;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            .box {
                background: rgba(0,0,0,0.6);
                width: 60%;
                margin: auto;
                margin-top: 40px;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(255,255,255,0.2);
            }

            img {
                width: 250px;
                border-radius: 20px;
                transition: 0.3s;
            }

            img:hover {
                transform: scale(1.05);
            }

            a button {
                margin-top: 15px;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                background: gold;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>🦌 Chopper</h1>

            <img src="/static/chopper pagina.jpg">

            <p>
               ony Tony Chopper (トニートニー・チョッパー Tonī Tonī Chopā?) es el médico de los Piratas de Sombrero de Paja, así como uno de los oficiales principales de la Gran Flota de Sombrero de Paja. Es un reno que comió la fruta Hito Hito de la isla de Drum. Él es el sexto miembro de la tripulación y el quinto en unirse a ella.
            </p>

            <a href="/">
                <button>🏠 Volver</button>
            </a>
        </div>

    </body>
    </html>
    """
@app.route("/brook")
def brook():
    return """
    <html>
    <head>
        <title>Brook</title>
        <style>
            body {
               background: linear-gradient(135deg, #FAFAFA, #000000); !important;
                margin: 0;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            .box {
                background: rgba(0,0,0,0.6);
                width: 60%;
                margin: auto;
                margin-top: 40px;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(255,255,255,0.2);
            }

            img {
                width: 250px;
                border-radius: 20px;
                transition: 0.3s;
            }

            img:hover {
                transform: scale(1.05);
            }

            a button {
                margin-top: 15px;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                background: gold;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>💀 Brook</h1>

            <img src="/static/brook pagina.jpg">

            <p>
               Brook (ブルック Burukku?), conocido como Soul King (ソウルキング Souru Kingu?), es el músico de los Piratas de Sombrero de Paja, uno de sus dos espadachines y uno de los oficiales principales de la Gran Flota de Sombrero de Paja. Es el noveno miembro de la tripulación y el octavo en unirse, haciéndolo al final del arco de Thriller Bark.
            </p>

            <a href="/">
                <button>🏠 Volver</button>
            </a>
        </div>

    </body>
    </html>
    """
@app.route("/nico-robin")
def nico_robin():
    return """
    <html>
    <head>
        <title>Nico Robin</title>
        <style>
            body {
              background: linear-gradient(135deg, #7b2cbf, #3c096c); !important;
                margin: 0;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            .box {
                background: rgba(0,0,0,0.6);
                width: 60%;
                margin: auto;
                margin-top: 40px;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(255,255,255,0.2);
            }

            img {
                width: 250px;
                border-radius: 20px;
                transition: 0.3s;
            }

            img:hover {
                transform: scale(1.05);
            }

            a button {
                margin-top: 15px;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                background: gold;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>📖 Nico Robin</h1>

            <img src="/static/nico robin pagina.jpg">

            <p>
                Nico Robin (ニコ・ロビン Niko Robin?), también conocida por sus epítetos: Niña Demonio (悪魔の子 Akuma no Ko?) y La Luz de la Revolución (革命の灯 Kakumei no Tomoshibi?) es la arqueóloga de los Piratas de Sombrero de Paja, así como una de los oficiales principales de la Gran Flota de Sombrero de Paja. Es el séptimo miembro de la tripulación y el sexto en unirse, haciéndolo al final del arco de Arabasta.
            </p>

            <a href="/">
                <button>🏠 Volver</button>
            </a>
        </div>

    </body>
    </html>
    """
@app.route("/usopp")
def usopp():
    return """
    <html>
    <head>
        <title>Usopp</title>
        <style>
            body {
               background: linear-gradient(135deg, #b08968, #6f4e37); !important;
                margin: 0;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            .box {
                background: rgba(0,0,0,0.6);
                width: 60%;
                margin: auto;
                margin-top: 40px;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(255,255,255,0.2);
            }

            img {
                width: 250px;
                border-radius: 20px;
                transition: 0.3s;
            }

            img:hover {
                transform: scale(1.05);
            }

            a button {
                margin-top: 15px;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                background: gold;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>🔫​ Usopp</h1>

            <img src="/static/usopp pagina.jpg">

            <p>
                Usopp (ウソップ Usoppu?) es el francotirador de los Piratas de Sombrero de Paja y uno de los oficiales principales de la Gran Flota de Sombrero de Paja. Es el cuarto miembro de la tripulación y el tercero en unirse oficialmente. A pesar de abandonar la banda en el arco de Water 7, se volvió a unir en el arco del regreso a Water 7.
            </p>

            <a href="/">
                <button>🏠 Volver</button>
            </a>
        </div>

    </body>
    </html>
    """
@app.route("/franky")
def franky():
    return """
    <html>
    <head>
        <title>Franky</title>
        <style>
            body {
               background: linear-gradient(135deg, #00b4d8, #0077b6); !important;
                margin: 0;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            .box {
                background: rgba(0,0,0,0.6);
                width: 60%;
                margin: auto;
                margin-top: 40px;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(255,255,255,0.2);
            }

            img {
                width: 250px;
                border-radius: 20px;
                transition: 0.3s;
            }

            img:hover {
                transform: scale(1.05);
            }

            a button {
                margin-top: 15px;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                background: gold;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>​🤖​ Franky</h1>

            <img src="/static/franky pagina.jpg">

            <p>
                (フランキー Furankī?), apodado el Hombre de Hierro (鉄人 tetsujin?), es el carpintero naval de los Piratas de Sombrero de Paja y uno de los oficiales principales de la Gran Flota de Sombrero de Paja. Es el octavo miembro de la tripulación y el séptimo en unirse, haciéndolo al final del arco del regreso a Water 7.
            </p>

            <a href="/">
                <button>🏠 Volver</button>
            </a>
        </div>

    </body>
    </html>
    """
@app.route("/jinbe")
def jinbe():
    return """
    <html>
    <head>
        <title>Jinbe</title>
        <style>
            body {
               background: linear-gradient(135deg, #1d4ed8, #0f172a); !important;
                margin: 0;
                color: white;
                font-family: Arial;
                text-align: center;
            }

            .box {
                background: rgba(0,0,0,0.6);
                width: 60%;
                margin: auto;
                margin-top: 40px;
                padding: 20px;
                border-radius: 20px;
                box-shadow: 0 0 20px rgba(255,255,255,0.2);
            }

            img {
                width: 250px;
                border-radius: 20px;
                transition: 0.3s;
            }

            img:hover {
                transform: scale(1.05);
            }

            a button {
                margin-top: 15px;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                background: gold;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>​🏊​ Jinbe</h1>

            <img src="/static/jinbe pagina.jpg">

            <p>
                侠のジンベエ Kaikyō no Jinbē?) es el timonel de los Piratas de Sombrero de Paja y uno de los oficiales principales de la Gran Flota de Sombrero de Paja, siendo el décimo miembro de la banda y el noveno en unirse haciéndolo durante los eventos del Arco de Whole Cake Island.[3] Es un gyojin tiburón ballena,[2] que sirvió como antiguo capitán de los Piratas del Sol[11] y como miembro de los Siete Señores de la Guerra del Mar.[9]
            </p>

            <a href="/">
                <button>🏠 Volver</button>
            </a>
        </div>

    </body>
    </html>
    """
app.run(host="0.0.0.0", port=5000, debug=True)