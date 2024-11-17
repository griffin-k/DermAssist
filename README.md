# Dr. CareBot API

## Introduction
Welcome to the Dr. CareBot API! This project provides an AI-powered medical chatbot that can assist with health-related queries. Built with FastAPI, it integrates with an AI model to provide real-time responses to users. The bot is designed to deliver concise and accurate answers to health and medical questions, helping users find essential information quickly.

---

## Requirements

Before running this project, make sure you have the following installed:

- **Python 3.7 or higher**
- **API Key**: For integration with the AI model, you will need an API key (Groq API key).
- **Required Python Libraries**:
  - `fastapi`
  - `uvicorn`
  - `pydantic`
  - `python-dotenv`
  - `groq`
  - `googlesearch` (optional, if you want web search integration)
  - `https://console.groq.com/` for api key login here

---

## Installation Guide

### 1. Clone the repository
To get started, clone the repository to your local machine:
```bash
git clone https://github.com/griffin-k/dr-carebot-api.git
```

### Usage Guide
Run the API locally To run the API locally, use uvicorn to start the server:

bash
```bash
uvicorn bot:app --reload
```
The API will be available at http://127.0.0.1:8000/.

Interact with the API You can interact with the Dr. CareBot API by either sending GET requests or POST requests to the available endpoints (detailed below).

### API Endpoints
1. Home Page
Endpoint: GET /
Description: Provides a welcome message with basic instructions for using the API.
Response:
```json

{
  "message": "Welcome to the Dr. CareBot API. Use the /{query} endpoint to interact with the AI. Replace {query} with your query."
}
```
2. Ask Questions (GET Request)
Endpoint: GET /{query}
Description: Send a query to Dr. CareBot and receive a response based on the AI's understanding.
Example:
URL: http://127.0.0.1:8000/flu precautions
Response Example:
```json

{
  "response": "To prevent the flu, wash your hands regularly, avoid close contact with sick people, and get vaccinated."
}
```
3. Chat with Dr. CareBot (POST Request)
Endpoint: POST /my/doc/chat
Description: Allows users to send a message to Dr. CareBot and receive a response in a conversation-like format.
Request Body:
Format: JSON
Example:
```json

{
  "user_input": "What are the symptoms of flu?"
}
```
Response Example:

```json
{
  "response": "Common flu symptoms include fever, chills, cough, sore throat, muscle aches, and fatigue."
}
```

