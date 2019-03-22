import os

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/racionais-mcs', methods=['POST', 'GET'])
def racionais():

    MUSICA_E_DOS_RACIONAIS = ''

    def verificar_se_musica_e_dos_racionais(musica):

        MUSICAS_DOS_RACIONAIS = [
            'Cores e Valores',
            'Capitulo 4 Versiculo 3',
            'A Vida é Desafio',
        ]

        MUSICAS_DOS_RACIONAIS = [ musica.lower() for musica in MUSICAS_DOS_RACIONAIS]

        if musica.lower() in MUSICAS_DOS_RACIONAIS:
            return True
        else:
            return False

    if request.method == 'POST':

        musica = request.form['nome-musica']

        if verificar_se_musica_e_dos_racionais(musica):
            MUSICA_E_DOS_RACIONAIS = 'É dos Racionais'
        else:
            MUSICA_E_DOS_RACIONAIS = 'Num é não truta'


    return '''
    
        <hr>
        <h2> Somos o que somos. </h2>
        
        <img src="https://raplogia.com.br/wp-content/uploads/2015/11/cores-e-valores-racionais-mcs.jpg">
        
        <br>
        <br>
        <br>
        <form action="/racionais-mcs" method="POST">
            <label for="nome-musica">Nome da Música</label>
            <input type="text" id="nome-musica" name="nome-musica">
            <button>Ver se a música é dos Racionais 'Mcs </button>
        </form>
        
        <p>{}</p>
    
    '''.format(MUSICA_E_DOS_RACIONAIS)
    


@app.route("/")
def index():
    return '''
    
    <style>
    
    img {
        width: 300px;
        height: 300px;
    }
        
    .imagem-grande {
        width: 500px;
        height: 400px;
    }
     
    .imagem-pequena {
        width: 250px;
        height: 200px;
    }   
    
    #letreiro {
        font-size: 25px;
        color: purple;
    }    
    
    </style>
    
    <h1>Flask App/h1>
    <hr>
    <h2> Meu primeiro aplicativo em Flask</h2>
    
    Fringilla suscipit integer laoreet suscipit, sociosqu morbi penatibus condimentum. Mi nec ultricies, tellus aliquam diam dignissim. Convallis sed congue; duis eget a maecenas potenti massa fames eu? Eleifend viverra, quis nibh senectus lacinia. Laoreet nibh convallis platea netus auctor nam nam platea integer viverra per primis. Pharetra urna conubia lectus? Curabitur augue metus velit lectus. Egestas consectetur fermentum vel eros. Potenti hendrerit ac platea mattis vehicula risus; natoque proin euismod dui erat ornare. Facilisi consequat lectus sapien donec natoque per vestibulum enim metus euismod. Inceptos consectetur adipiscing purus nostra lacinia. Tortor amet justo elit?

    <marquee id="letreiro" >LINDOOOO !!! </marquee>
    
    <img src="https://images.pexels.com/photos/1721558/pexels-photo-1721558.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940">
    <img src="https://images.pexels.com/photos/935981/pexels-photo-935981.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940">
    
    <p> by: <strong>Fabio Baldo</strong></p>
    
    '''

if __name__ == '__main__':

    os.environ['FLASK_APP'] = 'app'
    os.environ['FLASK_ENV'] = 'development'

    app.run()