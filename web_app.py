from flask import Flask, render_template, request, redirect

app = Flask(__name__,static_url_path='')

@app.route('/')
def hello_world():
    print("HW!")
    return 'Hello, World from Flask!'

@app.route('/formdata', methods=['GET', 'POST'])
def form_data():
    
    if request.method == 'POST':
        print('post...')
        print (request.form) #pega todos os dados do formulário
        print (request.form['nome']) #pega apenas o campo 'nome'
        print (request.form['fruta'])#pega apenas o campo 'fruta'
     
    return redirect('/formdt.html') #Redireciona para a própria página


