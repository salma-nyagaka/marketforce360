### marketforce360

#### Description
Simple functions to save and retrieve data from CSV file and Sqlite database

#### Development set up
-   Check that python 3.10.0 is installed:

    ```
    python --version
    >> Python 3.10.0
    ```

-   Clone the repo and cd into it:

    ```
    git clone https://github.com/salma-nyagaka/marketforce360.git
    ```

-   Create a virtual environment and activate it:

    ```
    virtualenv venv
    source venv/bin/activate
    ```

-   Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

-   Run the tests:

    ```
    pytest
    ```


- Create the database

    ```
    python3 questions/database.py
    ```

-   Run the following commands to view the functionalities.
    ```
    python3 questions/csv_question.py
    ```

    ```
    python3 questions/db_question.py
    ```
