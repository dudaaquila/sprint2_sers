from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/comando/<string:acao>')
def comando(acao):
    if acao == "modo_solar":
        return jsonify({"status": "Modo solar ativado!"})
    elif acao == "consumo":
        return jsonify({"consumo": "2.1 kW"})
    else:
        return jsonify({"erro": "Comando não reconhecido"}), 400

# Roda o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
