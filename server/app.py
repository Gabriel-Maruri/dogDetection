from flask import Flask, request

app = Flask(__name__)

@app.route('/perro', methods=['POST'])
def perro_detectado():
    print("PERRO DETECTADO")
    return '', 204

if __name__ == '__main__':
    import os
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=PORT)
    
