from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os
from groq import Groq
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI and set up CORS
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



api_key = "Your api key here"
with open("prompt.txt", "r") as file:
    prompt = file.read()


class ChatRequest(BaseModel):
    user_input: str


def generate(user_prompt: str, system_prompt: str = prompt) -> str:
    if not user_prompt:
        raise HTTPException(status_code=400, detail="User prompt cannot be empty")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    if not api_key:
        raise HTTPException(status_code=500, detail="API key for Groq is not set")


    response = Groq(api_key=api_key).chat.completions.create(
        model='llama3-70b-8192',
        messages=messages,
        max_tokens=4096
    )

    return response.choices[0].message.content


@app.get("/{query}")
def respond_to_query(query: str):
    try:
        response = generate(query, system_prompt=prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/my/doc/chat")
def lgu_admission_chat(chat_request: ChatRequest):
    try:
        response = generate(chat_request.user_input, system_prompt=prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
def read_root():
    return {"message": "Welcome to the Dr. CareBot API. Use the /{query} endpoint to interact with the AI. Replace {query} with your query."}
