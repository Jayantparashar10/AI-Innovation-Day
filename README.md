# ai-innovation-day
Documentation to build your own AI chatbot through Github Copilot, Github Models and Streamlit in AI Innovation Day '25 held at K.R. Mangalam University

# Medical Chatbot

This project is a simple medical chatbot built using the o3-mini model and deployed on Streamlit. The chatbot is designed to provide health advice and respond to user queries related to medical topics.

## Project Structure

- `src/app.py`: Main entry point of the Streamlit application.
- `src/model/chatbot.py`: Implementation of the medical chatbot using the o3-mini model.
- `src/utils/`: Contains utility functions for processing input and formatting responses.
- `src/config/config.py`: Configuration settings for the application.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `.env`: Contains environment variables used in the application.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/Rishav23av/AI-Innovation-Day
   cd medical-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables in the `.env` file.

4. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

## Usage

Once the application is running, you can interact with the chatbot through the web interface. Simply type your medical queries, and the chatbot will provide responses based on the o3-mini model.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
