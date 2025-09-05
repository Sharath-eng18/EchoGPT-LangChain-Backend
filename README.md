# EchoGPT Backend

The backend for EchoGPT is a robust and scalable API responsible for processing user requests and communicating with the large language model. It's designed to be lightweight and efficient, ensuring low latency for a smooth conversational experience.

### 🛠️ Technologies Used

* **Python & Flask:** The backend is built using Flask, a micro web framework for Python, which provides the necessary tools for handling API routes and serving responses.

* **Hugging Face API:** This API is used to interact with various open-source language models, providing the core AI capabilities for generating conversational text.

* **Render:** The backend is deployed on Render, a cloud platform that simplifies the hosting of web services and APIs.

### 🚀 Getting Started

Follow these steps to get the backend of EchoGPT up and running on your local machine.

#### Prerequisites

Before you begin, ensure you have the following installed:

* Python (v3.8 or higher)

* pip (Python package installer)

#### Installation

1.  **Clone the repository:**

    \`\`\`
    git clone [https://github.com/your-username/echogpt-backend.git](https://github.com/your-username/echogpt-backend.git)
    cd echogpt-backend
    
    \`\`\`

2.  **Create and activate a virtual environment:**

    \`\`\`
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\\Scripts\\activate     # On Windows
    
    \`\`\`

3.  **Install dependencies:**

    \`\`\`
    pip install -r requirements.txt
    
    \`\`\`

#### Environment Variables

Create a \`.env\` file in the root directory of the project and add your Hugging Face API key.

\`\`\`
HUGGING_FACE_API_KEY=your_hugging_face_api_key

\`\`\`

### 🏃 Running the Application

Once everything is set up, you can start the Flask development server:

\`\`\`
flask run

\`\`\`

The application will now be running on \`http://127.0.0.1:5000\`.

### 📄 License

Distributed under the MIT License. See \`LICENSE\` for more information.
