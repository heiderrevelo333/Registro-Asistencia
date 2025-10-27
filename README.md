#  🧾 Attendance Tracker API (FastAPI)

REST API built with **FastAPI** to manage attendance records.  
Includes full **CRUD operations**, basic validation, and in-memory data handling.

---

## 📁 Project Structure

Registro-Asistencia/ 
│ 
├── src/ 
│ 
├── pycache/ 
│ └── main.py 
│ ├── .venv/ # Virtual environment (do not push to Git) 
├── requirements.txt # Project dependencies 
└── README.md # Documentation

Código

---

## ⚙️ Installation & Execution

### 1️⃣ Clone the repository

```bash
git clone https://github.com/heiderrevelo333/Registro-Asistencia.git
cd Registro-Asistencia
2️⃣ Create and activate virtual environment
bash
python -m venv .venv
# On Windows PowerShell
.venv\Scripts\Activate.ps1
# On Linux/Mac
source .venv/bin/activate
3️⃣ Install dependencies
bash
pip install -r requirements.txt
4️⃣ Run the server
bash
uvicorn src.main:app --reload
🔹 The API will be available at: 👉 http://127.0.0.1:8000

🚀 Available Endpoints
Method	Route	Description
GET	/asistencias	List all attendance records
GET	/asistencias/{id}	Get attendance by ID
POST	/asistencias	Create a new record
PUT	/asistencias/{id}	Update an existing record
DELETE	/asistencias/{id}	Delete attendance by ID
🧠 Sample JSON Object
json
{
  "nombre": "Carlos Ruiz",
  "estado": "asiste"
}
🧩 Technologies Used
Python 3.13+

FastAPI

Uvicorn

Pydantic

📄 requirements.txt
Example content:

Código
fastapi
uvicorn
🧑‍💻 Author
Esteban Revelo
Yojhann Vasquez
Jeffry Lopez 
📍 SENA - Software Analysis and Software Development 📅 2025