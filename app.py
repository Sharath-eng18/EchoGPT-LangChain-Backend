import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# --- Configuration ---
# It's highly recommended to use environment variables for sensitive data like API keys.
# Create a .env file in this directory and add:
# HUGGINGFACEHUB_API_TOKEN="your_hugging_face_token"
#
from dotenv import load_dotenv
load_dotenv()
#
# For this example, we'll use the token you provided, but be aware of the security risks.
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
REPO_ID = "moonshotai/Kimi-K2-Instruct"

# --- Model Initialization ---
try:
    llm = HuggingFaceEndpoint(
        repo_id=REPO_ID,
        huggingfacehub_api_token=HUGGINGFACE_TOKEN,
        temperature=0.7,
    )
    model = ChatHuggingFace(llm=llm)
    print("Hugging Face model loaded successfully.")
except Exception as e:
    print(f"Error loading Hugging Face model: {e}")
    # Exit or handle the error appropriately if the model fails to load.
    exit()

# --- Flask App Initialization ---
app = Flask(__name__)
# Enable CORS to allow requests from your React frontend (which runs on a different port)
CORS(app)

# --- API Endpoint for Chat ---
@app.route('/chat', methods=['POST'])
def chat():
    """
    Handles chat requests from the frontend.
    Expects a JSON payload with a 'history' key containing the conversation history.
    """
    try:
        data = request.get_json()
        if not data or 'history' not in data:
            return jsonify({"error": "Invalid request format. 'history' is required."}), 400

        history_from_frontend = data['history']
        
        # Convert the received history into LangChain's message objects
        langchain_messages = []
        for message in history_from_frontend:
            role = message.get('role')
            content = message.get('content')
            if not role or not content:
                continue
            
            if role == 'system':
                langchain_messages.append(SystemMessage(content=content))
            elif role == 'user':
                langchain_messages.append(HumanMessage(content=content))
            elif role == 'ai':
                langchain_messages.append(AIMessage(content=content))

        if not langchain_messages:
            return jsonify({"error": "No valid messages in history."}), 400
            
        # Get the model's response
        response = model.invoke(langchain_messages)
        
        # Return the AI's response content
        return jsonify({'role': 'ai', 'content': response.content})

    except Exception as e:
        print(f"An error occurred during chat processing: {e}")
        return jsonify({"error": "An internal server error occurred."}), 500

# --- Health Check Endpoint ---
@app.route('/')
def index():
    return "Chatbot backend is running!"