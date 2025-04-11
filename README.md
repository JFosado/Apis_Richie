# 🏥 HOSPITAL S.A. de C.V. - API de Recursos Materiales

## 📖 Descripción

Esta API está enfocada exclusivamente en la **gestión de recursos materiales** dentro del hospital. Su propósito principal es administrar las entidades relacionadas con la estructura física, usuarios internos, y los recursos médicos de uso común.

Las tablas y entidades que se gestionan son:

- 👤 **Personas**  
- 👨‍💻 **Usuarios**  
- 🏢 **Espacios físicos del hospital**  
- 🏥 **Áreas médicas**  
- 🧴 **Consumibles** (material médico)  
- 🛠️ **Servicios médicos consumibles** (asociación entre servicios y consumibles)  
- 🧾 **Servicios médicos espacios** (asociación entre servicios y espacios físicos)

> ❌ **Importante:** Esta API **no** incluye funciones para gestión de pacientes, doctores, citas médicas o expedientes clínicos.

---

## 📁 Estructura del Proyecto

```
BackendHospital/
├── app/
│   ├── main.py
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   └── services/
├── requirements.txt
├── README.md
└── .env
```

---

## 🚀 Instalación y Ejecución

### **1️⃣ Clonar el repositorio**

```sh
git clone <URL_DEL_REPOSITORIO>
cd BackendHospital
```

### **2️⃣ Crear y activar el entorno virtual**

#### Linux & Mac:

```sh
python3 -m venv venv
source venv/bin/activate
```

#### Windows:

```sh
python -m venv venv
venv\Scripts\activate
```

### **3️⃣ Instalar dependencias**

```sh
pip install -r requirements.txt
```

### **4️⃣ Configurar variables de entorno**

Crea un archivo `.env` en la raíz del proyecto con la conexión a base de datos:

```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/hospitaldb
```

### **5️⃣ Ejecutar la API**

```sh
uvicorn app.main:app --reload
```

📌 **La API estará disponible en:** [`http://localhost:8000/docs`](http://localhost:8000/docs)
