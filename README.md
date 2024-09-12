# Retrieval-Augmented Generation Experiment

An initial exploration of retrieval-augmented generation for a research software repository.

## Quickstart

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    ```

2. **Add the API URL to Your .env File**:
    - Add the following lines to your `.env` file in the root directory:
      ```
      API_URL="Your API URL here"
      QUERY="Your query here"
      ```

3. **Navigate to the Project Directory**:
    ```bash
    cd <project-directory>
    ```

4. **Install the Necessary Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

    *Using Python 3.12.4 is recommended.*


5. **Create the directories:**
- Create a /models, /vectorisations and /data directory in the root directory.

6. **Create the Dataset & Vectorizations**:
    - Before running the notebook for the RAG experiment, you need to create the dataset and generate text vectorizations for the retrieval part of the RAG.

    - To do this, simply execute the `1_vectorisation.ipynb` notebook. The data will be saved to your machine and will be available the next time you open the project.


7. **Install Ollama**

- Install Ollama and download the model you want to use. For this notebook.
- To install `llama3`, the model we're using in this notebook, run the following command `ollama run llama3`
- Ollama has to run in the background for the chat-bots to work.
