# QA Automation Challenge – API Testing

Este proyecto fue desarrollado como parte de un challenge técnico para automatizar pruebas sobre una API REST utilizando `pytest`, el patrón **POM (Page Object Model)** adaptado a APIs, y una simulación de conexión con **DynamoDB**.

---

## 🚀 Estructura del Proyecto

```
qa_api_project/
│
├── api/
│   └── import_api.py            # Lógica de interacción con la API REST
│
├── db/
│   └── person_table.py          # Cliente para consultar la tabla 'Persons' en DynamoDB
│
├── tests/
│   └── test_import_api.py       # Test suite con casos happy/sad path
│
├── utils/
│   └── data_generator.py        # Generador de personId aleatorios válidos
│
├── .env                         # Archivo con tokens de autenticación
├── requirements.txt             # Dependencias del proyecto
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.8+
- pip
- Acceso a AWS configurado (perfil, variables o roles) (Simulado)
- Permisos para leer la tabla DynamoDB `Persons` (Simulado)
- No olvidarse del archivo `.env` (Explicado mas adelante)

---

## 📦 Instalación

1. Clonar el proyecto y entrar al directorio:

```bash
git clone <repo-url>
cd qa_api_project
```

2. Crear un entorno virtual (Pycharm lo hace automaticamente):

```bash
python -m venv venv
source venv/bin/activate  # en Windows: venv\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuración

Crear un archivo `.env` en la raíz con el siguiente contenido:

```
API_TOKEN=your_valid_token
EXPIRED_TOKEN=your_expired_token
```


---

## ✅ Ejecutar los tests

```bash
pytest -v
```

Cada test cubre:

- ✔️ Happy path con `personId` válidos (parametrizado)
- ❌ Sad path con datos inválidos
- 🔒 Casos sin token y token expirado
- 🧾 Validación del resultado contra la tabla **DynamoDB `Persons`**

---

## 🧪 Simulación de consulta a DynamoDB

El archivo `person_table.py` usa `boto3` como si fuera un entorno real en AWS:

```python
response = self.table.get_item(Key={"personId": person_id})
```

---

## ✨ Extras implementados

- Uso de `@pytest.mark.parametrize`
- Logs con `logging`
- Validación cruzada contra base de datos
- Manejo de tokens desde `.env`
- Código modular con buena separación de responsabilidades

---

## 📩 Contacto

> Desarrollado por **Franco Palavecino** – QA Engineer  
> [LinkedIn](https://www.linkedin.com/in/franco-palavecino/) | [Email](mailto:francogpalavecino@gmail.com)
