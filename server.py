from flask import Flask, request, jsonify

app = Flask(__name__)

# Route de test pour vérifier que le serveur fonctionne
@app.route("/", methods=["GET"])
def home():
    return "Serveur en ligne !"

# Route pour recevoir des données JSON
@app.route("/get_data", methods=["POST"])
def get_data():
    # Récupère les données envoyées en JSON
    data = request.get_json()
    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400
    
    # Affiche les données reçues dans le terminal
    print("Données reçues :", data)
    
    # Retourne une réponse avec les données reçues
    return jsonify({"message": "Données bien reçues", "data": data}), 200

if __name__ == "__main__":
    # Écoute sur le port 8080 pour Render
    app.run(host="0.0.0.0", port=8080)
