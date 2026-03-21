# 🚚 AI-Powered Fleet Dispatch & Logistics Engine

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Google_Gemini_2.5-F9AB00?logo=google&logoColor=white)

## 📌 Overview
The **AI Fleet Dispatch API** is a containerized, production-ready microservice designed to automate complex logistics and cargo routing. It combines classical reinforcement learning mathematics with modern Generative AI to not only solve routing problems, but seamlessly explain them to human operators.

Instead of relying on basic conditional logic, this engine utilizes a **Markov Decision Process (MDP)** to mathematically optimize cargo distribution across a multi-agent robotic fleet based on dynamic zones, weight capacities, and reward scores. The mathematical output is then autonomously processed by **Google's Gemini 2.5 Flash LLM** to generate real-time, human-readable operational summaries for shift supervisors.

## ✨ Key Features
* **Mathematical Routing (MDP):** Solves multi-agent task allocation problems dynamically without hardcoded pathways.
* **LLM Integration:** Leverages the official `google-genai` Python SDK to translate raw JSON routing data into professional, actionable text reports.
* **Fault-Tolerant AI:** Implements resilient error handling to ensure the core routing math executes flawlessly even if external AI APIs experience downtime.
* **Fully Containerized:** Packaged in a lightweight Docker container for zero-dependency, cross-platform cloud deployment.

## 🛠️ Tech Stack
* **Backend:** Python 3.11, FastAPI, Uvicorn, Pydantic
* **AI & NLP:** Google Gemini 2.5 Flash (`google-genai`)
* **DevOps:** Docker

---

## 🚀 Getting Started

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* A free [Google Gemini API Key](https://aistudio.google.com/app/apikey).

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/ai-fleet-dispatch.git](https://github.com/YOUR_USERNAME/ai-fleet-dispatch.git)
cd ai-fleet-dispatch
