# AI-Powered Fleet Dispatch & Logistics Engine

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Google_Gemini_2.5-F9AB00?logo=google&logoColor=white)

## Overview
The **AI Fleet Dispatch API** is a containerized, production-ready microservice designed to automate complex logistics and cargo routing. It combines classical reinforcement learning mathematics with modern Generative AI to not only solve routing problems but seamlessly explain them to human operators.

Instead of relying on basic conditional logic, this engine utilizes a **Markov Decision Process (MDP)** to mathematically optimize cargo distribution across a multi-agent robotic fleet based on dynamic zones, weight capacities, and reward scores. The mathematical output is then autonomously processed by **Google's Gemini 2.5 Flash LLM** to generate real-time, human-readable operational summaries for shift supervisors.

## Key Features
* **Mathematical Routing (MDP):** Solves multi-agent task allocation problems dynamically without hardcoded pathways.
* **LLM Integration:** Leverages the modern `google-genai` Python SDK to translate raw JSON routing data into professional, actionable text reports.
* **Fault-Tolerant Architecture:** Implements resilient error handling to ensure the core routing math executes flawlessly even if external AI APIs experience downtime.
* **Fully Containerized:** Packaged in a lightweight Docker container for zero-dependency, cross-platform cloud deployment.

## Tech Stack
* **Backend:** Python 3.11, FastAPI, Uvicorn, Pydantic
* **AI & LLM:** Google Gemini 2.5 Flash
* **DevOps:** Docker

## 📂 Project Structure
> ai-fleet-dispatch/
> ├── app/
> │   ├── main.py          # FastAPI application and endpoint definitions
> │   └── reporter.py      # Google Gemini AI integration and prompt engineering
> ├── .env                 # Secret environment variables (Ignored by Git)
> ├── .gitignore           # Git ignore rules
> ├── Dockerfile           # Docker container blueprint
> ├── requirements.txt     # Python dependencies
> └── README.md            # Project documentation

## Getting Started

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* A free [Google Gemini API Key](https://aistudio.google.com/app/apikey).

### 1. Clone the Repository
```bash
git clone [https://github.com/Saksham52/ai-fleet-dispatch.git](https://github.com/Saksham52/ai-fleet-dispatch.git)
cd ai-fleet-dispatch
```

### 2. Configure Environment Variables
Create a file named `.env` in the root directory and add your Gemini API key (do not use quotation marks):
```text
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Build and Run with Docker
Build the Docker image:
```bash
docker build -t fleet-dispatch-api .
```

Run the container, passing in your secure environment file:
```bash
docker run -p 8000:8000 --env-file .env fleet-dispatch-api
```

## API Usage

Once the container is running, access the interactive Swagger UI documentation at:
 **[http://localhost:8000/docs](http://localhost:8000/docs)**

### `POST /dispatch`
Executes the MDP routing algorithm and triggers the AI report generation.

**Sample Response:**
```json
{
  "status": "success",
  "total_cargo": 5,
  "manager_report": "Good morning. Robots Alpha, Beta, and Gamma are active and have been successfully assigned all current tasks across various zones. There are no unassigned tasks requiring immediate human intervention.",
  "dispatch_plan": {
    "assignments": {
      "Robot_Alpha": [
        { "task_id": "a242dcf0-1df9", "zone": "Zone_B", "reward_score": 25 }
      ],
      "Robot_Beta": [
        { "task_id": "8c1494dc-6399", "zone": "Zone_C", "reward_score": 55 }
      ],
      "Robot_Gamma": [
        { "task_id": "21285038-edcf", "zone": "Zone_D", "reward_score": 35 }
      ]
    },
    "unassigned_tasks": []
  }
}
```

## Architectural Decisions
* **Why FastAPI?** Chosen for its asynchronous capabilities, exceptional speed, and automatic OpenAPI validation, which is critical for standardizing data before it reaches the MDP solver.
* **Why Gemini 2.5 Flash?** Optimized for high-frequency, low-latency text summarization tasks, making it highly cost-effective for operational APIs compared to heavier reasoning models.
* **Why Docker?** Eliminates "it works on my machine" issues by packaging the exact Python runtime and dependencies, ensuring it is ready for immediate deployment to AWS, GCP, or Azure.

## Author
**Saksham**
* **GitHub:** [@Saksham52](https://github.com/Saksham52)

---
*Note: This project was built to demonstrate full-stack AI integration and mathematical routing for production environments.*
