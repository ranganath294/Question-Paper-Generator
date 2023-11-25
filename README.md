# Question Paper Generator

This is a Django project that allows you to generate question papers based on certain parameters and also create new questions.

## Prerequisites

- Python 3.12
- pip (Python package installer)

## Setting Up the Project

1. **Clone the repository**

    ```
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment**

    Please create a virtual environment for Python based on your operating system.

3. **Activate the virtual environment**

    Please activate the virtual environment you created based on your operating system.

4. **Install the required packages**

    ```
    pip install -r requirements.txt
    ```

    This will install the required packages as listed in the `requirements.txt` file. Please note that the versions of the packages are compatible with Python 3.12. If you're using a different version of Python, you might need to use different versions of the packages. Please check the appropriate documentation of each package for more details.

5. **Run the server**

    ```
    python manage.py runserver
    ```

    This will start the Django development server. You can access the application at `http://127.0.0.1:8000/`.

## API Documentation

The application has two main routes:

1. `generate_question_paper`: This route generates a question paper based on the parameters provided in the request. The parameters include `total_marks`, `subject`, `easy_percentage`, `medium_percentage`, `hard_percentage`, `num_of_easy_ques`, `num_of_medium_ques`, and `num_of_hard_ques`. The URL to use this route is `http://127.0.0.1:8000/generate_question_paper`.

2. `create_question`: This route creates a new question in the database. The parameters for the request include `question`, `subject`, `topic`, `difficulty`, and `marks`. The URL to use this route is `http://127.0.0.1:8000/create_question`.

### generate_question_paper

This is a `GET` method that generates a question paper based on the parameters provided in the request. The parameters include:

- `total_marks`: The total marks for the question paper. Default is 100.
- `subject`: The subject for which the question paper is to be generated. This is a required field.
- `easy_percentage`, `medium_percentage`, `hard_percentage`: The percentage of easy, medium, and hard questions respectively. The sum of these percentages should be 100.
- `num_of_easy_ques`, `num_of_medium_ques`, `num_of_hard_ques`: The number of easy, medium, and hard questions respectively.

### create_question

This is a `POST` method that creates a new question in the database. The parameters for the request include:

- `question`: The text of the question.
- `subject`: The subject of the question.
- `topic`: The topic of the question.
- `difficulty`: The difficulty level of the question.
- `marks`: The marks for the question.

## Contributing

If you want to contribute to this project, please feel free to fork the repository, make your changes, and create a pull request. If you have any questions or need further assistance, feel free to create an issue.

