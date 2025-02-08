TalentScout AI Interview Assistant
==================================

Please find the demo video here: https://drive.google.com/file/d/1K1dlMu02XMQXt2TH9PAkiraX1OY3Jqcy/view?usp=sharing

Project Overview:
-----------------

TalentScout is an AI-powered hiring assistant chatbot. It helps conduct technical interviews by asking tailored questions based on the candidate's tech stack. After the user provides basic details, such as name, contact, role, and experience, the chatbot generates questions specific to the tech stack provided, asking one question at a time.

Installation Instructions:
--------------------------

1.  Clone the repository:

    bash

    CopyEdit

    `git clone https://github.com/binduhegde/pgagi_assignment.git'

2.  Install dependencies:

    bash

    CopyEdit

    `pip install -r requirements.txt`

3.  Set up environment variables:

    -   Create a `.env` file and add your Google API key:

        ini

        CopyEdit

        `google_api_key=<your-google-api-key>`

4.  Run the application:

    bash

    CopyEdit

    `streamlit run main.py`

    Open `http://localhost:8501` in your browser to start.

Usage Guide:
------------

1.  Enter your name, contact number, location, position, and years of experience.
2.  The chatbot will then ask about your tech stack and generate questions based on it.
3.  Answer the questions or type "exit" to end the chat.

Technical Details:
------------------

-   **Libraries used**: `streamlit`, `google.generativeai`, `python-dotenv`.
-   **Model**: Gemini API ("gemini-pro" model).
-   **Architecture**: Frontend built with Streamlit, backend powered by Gemini API.

Prompt Design:
--------------

The chatbot's prompt ensures it:

-   Greets the candidate.
-   Collects tech stack details.
-   Generates 3-5 questions based on the tech stack.
-   Asks only one question at a time.

Challenges & Solutions:
-----------------------

1.  **Chatbot Flow**: Managed using Streamlit's session state to store user details and chat history.
2.  **Dynamic Question Generation**: Crafted clear prompts for each tech stack to ensure relevant questions.
3.  **API Integration**: Used `python-dotenv` for secure API key management and error handling.
4.  **Prompt Endineering**: Got to the final prompt by trial and error
5.  **API Key Protection**: Done through creating a .env file and including that in the .gitignore file

Additional Improvement Suggestions:
-----------------------------------

1. **Video Recording**: With the help of cv2, we can easily record the video of the candidate being interviewed.
2. **Cheating Detection**: With the help of head movement tracking and cv2, we can save the frame where the candidate seems to be cheating
3. **Voice Recording**: with the help of streamlit_mic_recorder, we can record the user's answers instead of the user typing the answers. This would help the candidate save time, also we can later use it for analysis purposes (confidence level detection, voice modulation, etc)
4. **Data Storage**: We can store the candidate information in noSQL databases like MongoDB, chromaDB, etc