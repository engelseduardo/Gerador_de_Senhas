from flask import Flask, render_template, request
import random
import string

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        length = int(request.form["length"])  # Obtém o comprimento da senha
        charset_option = request.form["charset_option"]  # Obtém a opção de tipo de caracteres

        if charset_option == "letters_and_digits":
            # Senha com apenas letras e números
            charset = string.ascii_letters + string.digits
        else:
            # Senha com caracteres Unicode (letras, números e símbolos)
            charset = string.ascii_letters + string.digits + string.punctuation + ''.join(chr(i) for i in range(32, 127))

        password = ''.join(random.choice(charset) for _ in range(length))  # Gera a senha

        return render_template("index.html", password=password)  # Exibe a senha gerada

    return render_template("index.html", password="")  # Caso seja um GET, retorna a página com nenhuma senha

if __name__ == "__main__":
    app.run(debug=True)
