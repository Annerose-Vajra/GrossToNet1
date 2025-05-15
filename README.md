# Gross-To-Net Income Calculator (Vietnam)

This project is a comprehensive tool to calculate Vietnamese **Net Income** from **Gross Income**, including Personal Income Tax (PIT), social insurance, health insurance, and unemployment insurance, following the latest Vietnamese regulations effective from 2025.

---

## Features

- **Single Calculation:** Calculate net salary with detailed breakdown of taxes and insurance.
- **Batch Processing:** Upload Excel files for bulk calculations and download reports.
- **REST API:** FastAPI backend exposing calculation endpoints.
- **Interactive Frontend:** Streamlit UI for easy user input and result visualization.
- **Saved Calculations:** CRUD operations to manage calculation records.
- **Containerized:** Docker support for easy deployment.
- **Deployable:** Ready to deploy on Render.com or similar platforms.

---

## Technology Stack

- Python 3.11+
- FastAPI for backend API
- Streamlit for frontend UI
- Docker for containerization
- PostgreSQL (optional) for persistent storage
- Render.com for cloud deployment

---

## Getting Started

### Prerequisites

- Python 3.11+
- Git
- Docker (optional, for containerized setup)
- Virtual environment tool (venv, conda, etc.)

### Installation

### 1. Clone the repository:
```bash
git clone https://github.com/Annerose-Vajra/GrossToNet1.git
cd GrossToNet1
```
### 2. Create and activate a virtual environment:

On Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```
On Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```
### 3. Install required Python packages:

```bash
pip install -r requirements.txt
```
### 4. Run the backend server locally:

```bash
uvicorn api.main:app --reload
```
### 5. Run the frontend app locally:
```bash
streamlit run frontend/app.py
```
## Usage
  -Access the frontend UI at http://localhost:8501.
  
  - Input Gross Income, number of dependents, and region.
  
  - View detailed tax and insurance breakdowns.
  
  - Export results as Excel or CSV.
  
  - Use backend REST API for programmatic access.

## CI/CD Pipeline
The project uses GitHub Actions to automate testing and deployment:

 Continuous Integration (CI):

  - Automatically runs on code push.

  - Checks out code.

  - Sets up Python environment.

  - Installs dependencies.

  - Runs linting and tests.

  - Builds Docker images (optional).

Continuous Deployment (CD):

  - Deploys the application to Render.com after successful CI.

  - Runs health checks and notifies on success or failure.

## Deploying on Render.com
### 1. Create a Render account if you don’t have one at https://render.com.

### 2. Connect your GitHub repository:

 - Go to Render Dashboard → New Web Service.

 - Select GitHub and authorize.

 - Choose the GrossToNet1 repository.

### 3. Configure the Web Service:

 - Name: e.g., grossnet-api for backend, grossnet-frontend for frontend.
  
 - Region: select nearest to your users (e.g., Oregon).
  
 - Branch: main.
  
 - Environment: Python.

### 4. Set Build Commands:

Backend:

```bash
pip install -r requirements.txt
```
Frontend:

```bash
pip install -r requirements.txt
```
### 5. Set Start Commands:

Backend:

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```
Frontend:

```bash
streamlit run frontend/app.py --server.port $PORT --server.address 0.0.0.0
```
### 6. Add Environment Variables:

 - For example: DATABASE_URL for your database connection string.

 - BACKEND_API_URL for frontend to communicate with backend.

### 7. Deploy and monitor:

 - Click Create Web Service.
  
 - Monitor build logs and application status.
  
 - Access your app via Render-provided URLs.

## Contributing
Contributions are welcome!
Please submit pull requests or open issues.
Ensure code follows style guidelines and tests are added for new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

@CCN-HUST
Computation & Communication Networking


