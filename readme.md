# Text Chatbot with LangChain, Groq API & Streamlit

This project builds a chatbot that can answer natural language questions without needing a document upload. It uses LangChain for prompt management, the Groq API to power the LLaMA3 model, and Streamlit for a user-friendly interface.

## Features

- **Text Input:** Ask open-ended or specific questions.
- **LLM Response:** Uses the Groq API with LLaMA3 for generating intelligent answers.
- **Prompt Handling:** Clean prompt pipeline using LangChain.
- **Streamlit UI:** Simple web interface to interact with the chatbot.

## How It Works

1. **Ask a Question:**
   - Type any question you like.
   - LangChain sends it directly to the LLM via the Groq API.

2. **User Interaction:**
   - The user types a question into the Streamlit interface.
   - LangChain formats the prompt.
   - The question is sent to LLaMA3 through Groq.
   - The LLM generates a response, which is displayed in the UI.

3. **Environment & Configuration:**
   - Sensitive information like the **Groq API Key** is stored in a `.env` file.
   - The `.env` file is added to `.gitignore` to ensure it is **not pushed** to GitHub.
   - An example file (`.env.example`) is provided to illustrate which environment variables are needed.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/text-chatbot.git
    cd text-chatbot
    ```

2. **Create & Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables:**

    - Copy `.env.example` to `.env`:

      ```bash
      cp .env.example .env
      ```

    - Open `.env` and replace `your-groq-api-key-here` with your actual Groq API key.

## Running the Application

1. **Start the Streamlit App:**

    ```bash
    streamlit run app.py
    ```

2. **Using the Chatbot:**
   - Type a question into the input box and press Enter.
   - The chatbot will return an AI-generated answer using the Groq-powered LLaMA3 model.

## File Structure

text-chatbot/
├── app.py                  
├── README.md                
├── .gitignore               
├── .env.example             
├── requirements.txt         
├── config.toml              
├── .streamlit/            
│   └── config.toml          
└── docs/                    
    ├── detailed_doc.md      
    └── detailed_doc.docx

## Security & Best Practices

- **Environment Variables:**  
  Your `.env` file is listed in `.gitignore` so it is not tracked by Git. This keeps your sensitive Groq API key secure.
  
- **Avoid Hardcoding Secrets:**  
  Never include secrets directly in your code. Always use environment variables for sensitive data.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain) for providing a flexible framework for building language model apps.
- [Groq API](https://groq.com/) for LLM acceleration.
- The Streamlit community for an easy and interactive way to build web apps.
