// Configuración base de la API
const API_BASE_URL = 'http://localhost:5000/api';

// Clase para manejar las llamadas a la API
class ApiService {
    constructor() {
        this.baseURL = API_BASE_URL;
    }

    // Método auxiliar para hacer peticiones HTTP
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers,
            },
            ...options,
        };

        try {
            const response = await fetch(url, config);
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || data.message || `HTTP error! status: ${response.status}`);
            }
            
            return data;
        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    // Método para hacer login
    async login(correo, contraseña) {
        return this.request('/login', {
            method: 'POST',
            body: JSON.stringify({ correo, contraseña }),
        });
    }

    // Método para probar la conexión con el backend
    async testConnection() {
        return this.request('/test-db');
    }

    // Aquí puedes agregar más métodos para otras operaciones de tu aplicación
    // Ejemplo:
    // async getMaquinas() {
    //     return this.request('/maquinas');
    // }
    
    // async createMaquina(maquinaData) {
    //     return this.request('/maquinas', {
    //         method: 'POST',
    //         body: JSON.stringify(maquinaData),
    //     });
    // }
}

// Exportar una instancia del servicio
const apiService = new ApiService();
export default apiService;
