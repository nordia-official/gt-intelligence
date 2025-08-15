from flask import Flask, jsonify, render_template_string
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Template HTML para GT Intelligence
DASHBOARD_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GT Intelligence - NORDIA</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-gray-100">
    <div class="container mx-auto p-8">
        <header class="text-center mb-12">
            <h1 class="text-6xl font-bold bg-gradient-to-r from-blue-400 to-purple-600 bg-clip-text text-transparent">
                GT Intelligence
            </h1>
            <p class="text-xl text-gray-400 mt-4">NORDIA - Electoral Analytics Platform</p>
            <p class="text-lg text-green-400 mt-2">🚀 Live on Railway ✨ Demo Ready</p>
        </header>
        
        <main class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div class="bg-gray-800 rounded-lg p-6">
                <h2 class="text-2xl font-bold mb-4">🏛️ Sistema Electoral</h2>
                <div class="space-y-4">
                    <div class="bg-blue-900/50 rounded p-4">
                        <p class="text-sm text-gray-400">Municipios Cargados</p>
                        <p class="text-3xl font-bold">6</p>
                    </div>
                    <div class="bg-green-900/50 rounded p-4">
                        <p class="text-sm text-gray-400">Sistema</p>
                        <p class="text-xl font-bold text-green-400">✅ ONLINE</p>
                    </div>
                </div>
            </div>
            
            <div class="bg-gray-800 rounded-lg p-6">
                <h2 class="text-2xl font-bold mb-4">📊 Demo Features</h2>
                <div class="space-y-2">
                    <div class="bg-purple-900/50 rounded p-3">API de Municipios</div>
                    <div class="bg-purple-900/50 rounded p-3">Análisis Electoral</div>
                    <div class="bg-purple-900/50 rounded p-3">Dashboard Interactivo</div>
                </div>
            </div>
        </main>
        
        <footer class="text-center mt-12 text-gray-500">
            <p>Powered by NORDIA | Railway Platform | Demo Version</p>
        </footer>
    </div>
</body>
</html>
'''

@app.route('/')
def dashboard():
    return render_template_string(DASHBOARD_TEMPLATE)

@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'GT Intelligence',
        'company': 'NORDIA',
        'version': '1.0.0',
        'platform': 'Railway',
        'message': '🚀 Demo funcionando perfectamente!'
    })

@app.route('/api/municipios')
def get_municipios():
    return jsonify({
        'municipalities': [
            {'id': 1, 'nombre': 'Capital'},
            {'id': 2, 'nombre': 'Goya'},
            {'id': 3, 'nombre': 'Mercedes'},
            {'id': 4, 'nombre': 'Santo Tomé'},
            {'id': 5, 'nombre': 'Paso de los Libres'},
            {'id': 6, 'nombre': 'Monte Caseros'}
        ],
        'total': 6,
        'timestamp': '2025-08-15',
        'powered_by': 'NORDIA',
        'platform': 'Railway'
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
