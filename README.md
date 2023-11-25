# Question Paper Generator

This is a Django project that allows you to generate question papers based on certain parameters and also create new questions.

## Prerequisites

- Python 3.12
- pip (Python package installer)

## Setting Up the Project

1. **Clone the repository**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment**

    Please create a virtual environment for Python based on your operating system.

3. **Activate the virtual environment**

    Please activate the virtual environment you created based on your operating system.

4. **Install the required packages**

    ```bash
    pip install -r requirements.txt
    ```

    This will install the required packages as listed in the `requirements.txt` file. Please note that the versions of the packages are compatible with Python 3.12. If you're using a different version of Python, you might need to use different versions of the packages. Please check the appropriate documentation of each package for more details.

5. **Run migrations**

    Apply migrations to set up the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the server**

    ```bash
    python manage.py runserver
    ```

    This will start the Django development server. You can access the application at `http://127.0.0.1:8000/` (Base URL).

## Using Postman
You can use Postman to interact with these APIs. Simply enter the URL for the route you want to use, select the appropriate method (GET for generate_question_paper and POST for create_question), and enter the parameters in the Body section in JSON format.

## API Documentation

The application has two main routes:

1. **`generate_question_paper`**

    - **Method:** GET
    - **End Point:** `http://127.0.0.1:8000/generate_question_paper` or `your_base_url/generate_question_paper`
    - **Description:** Generates a question paper based on the parameters provided in the request.
    - **Parameters:**
        - `total_marks` (optional, default is 100): The total marks for the question paper.
        - `subject` (required, string): The subject for which the question paper is to be generated.
        - `easy_percentage`(required, integer), `medium_percentage` (required, integer), `hard_percentage` (required, integer): The percentage of easy, medium, and hard questions respectively. The sum of these percentages should be 100.
        - `num_of_easy_ques` (optional, integer), `num_of_medium_ques` (optional, integer), `num_of_hard_ques` (optional, integer): The number of easy, medium, and hard questions respectively.
    - Make sure you replace base URL with your base URL

    - **Example Request:**
        ```json
        {
            "total_marks": 100,
            "subject": "Physics",
            "easy_percentage": 50,
            "medium_percentage": 30,
            "hard_percentage": 20,
            "num_of_easy_ques": 11,
            "num_of_medium_ques": 5,
            "num_of_hard_ques": 5
        }
        ```

2. **`create_question`**

    - **Method:** POST
    - **End Point:** `http://127.0.0.1:8000/create_question` or `your_base_url/create_question`
    - **Description:** Creates a new question in the database.
    - **Parameters:**
        - `question` (string): The text of the question.
        - `subject` (string): The subject of the question.
        - `topic` (string): The topic of the question.
        - `difficulty` (string): The difficulty level of the question.
        - `marks` (integer): The marks for the question.
    - Make sure you replace base URL with your base URL

    - **Example Request:**
        ```json
        {
            "question": "What is the capital of France?",
            "subject": "Geography",
            "topic": "World Capitals",
            "difficulty": "easy",
            "marks": 10
        }
        ```

## Testing

To test the functionality of the question paper generator, create a sample database using the `create_question` endpoint and then use the `generate_question_paper` endpoint to generate question papers with different parameters. Ensure that the generated question papers meet the specified criteria.


## Extending the Project

This project can be extended in various ways, such as:

- Implementing a tagging system for questions to enhance organization.
- Adding support for different question types (multiple-choice, short answer, etc.).
- Implementing topic-wise percentages, providing flexibility in generating question papers that adhere to distribution requirements across different subjects and topics.
- Creating a user interface for easier interaction.
- Adding authentication to secure the API endpoints.
- Implementing more advanced algorithms for question paper generation.