from fastapi import FastAPI
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI DevOps Assistant is running!"}


@app.get("/docker")
def docker(prompt: str):

    full_prompt = f"""
    You are a senior DevOps engineer.

    Generate ONLY a Dockerfile.

    Request:
    {prompt}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )

    return {
        "dockerfile": response.choices[0].message.content
    }
@app.get("/k8s")
def k8s(prompt: str):

    full_prompt = f"""
    You are a Kubernetes expert.

    Generate ONLY Kubernetes YAML.

    Give me in a structed way.

    Request:
    {prompt}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )

    return {
        "yaml": response.choices[0].message.content
    }
@app.get("/terraform")
def terraform(prompt: str):

    full_prompt = f"""
    You are a Terraform expert.

    Generate ONLY Terraform code.

    Request:
    {prompt}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": full_prompt
            }
        ]
    )

    return {
        "terraform": response.choices[0].message.content
    }