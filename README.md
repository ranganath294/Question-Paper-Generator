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

5. **Run the server**

    ```bash
    python manage.py runserver
    ```

    This will start the Django development server. You can access the application at `http://127.0.0.1:8000/`.

## API Documentation

The application has two main routes:

1. **`generate_question_paper`**

    - **Method:** GET
    - **Description:** Generates a question paper based on the parameters provided in the request.
    - **Parameters:**
        - `total_marks` (optional, default is 100): The total marks for the question paper.
        - `subject` (required): The subject for which the question paper is to be generated.
        - `easy_percentage`, `medium_percentage`, `hard_percentage`: The percentage of easy, medium, and hard questions respectively. The sum of these percentages should be 100.
        - `num_of_easy_ques`, `num_of_medium_ques`, `num_of_hard_ques`: The number of easy, medium, and hard questions respectively.

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
    - **Description:** Creates a new question in the database.
    - **Parameters:**
        - `question`: The text of the question.
        - `subject`: The subject of the question.
        - `topic`: The topic of the question.
        - `difficulty`: The difficulty level of the question.
        - `marks`: The marks for the question.

    - **Example Request:**
        ```json
        {
            "question": "question",
            "subject": "Physics",
            "topic": "topic_1",
            "difficulty": "easy",
            "marks": 10
        }
        ```

## Contributing

If you want to contribute to this project, please feel free to fork the repository, make your changes, and create a pull request. If you have any questions or need further assistance, feel free to create an issue.

## Extending the Project

This project can be extended in various ways, such as:

- Adding authentication to secure the API endpoints.
- Implementing more advanced algorithms for question paper generation.
- Creating a user interface for easier interaction.
- Adding support for different question types (multiple-choice, short answer, etc.).
- Implementing a tagging system for questions to enhance organization.

Feel free to explore these possibilities and contribute to the project's growth!
