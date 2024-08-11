# MongoDB Cloud Connection with Python

This project demonstrates how to connect a Python application to a MongoDB database hosted on MongoDB Cloud (Atlas). The program allows you to perform basic CRUD (Create, Read, Update, Delete) operations on your MongoDB collections.

## Features

- **Database Connection**: Establish a secure connection to a MongoDB Atlas cluster.
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on MongoDB documents.
- **Querying**: Execute various queries to filter and sort data.
- **Indexing**: Learn how to create indexes to improve query performance.

## Getting Started

### Prerequisites

To run this program, you'll need:

- Python 3.6 or later
- A MongoDB Atlas account with an active cluster
- The `pymongo` Python package

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/mongodb-python-connection.git
    cd mongodb-python-connection
    ```

2. **Install the required Python packages:**

    You can install the dependencies using pip:

    ```bash
    pip install pymongo
    ```

3. **Set up your MongoDB Atlas cluster:**

    - Create a free MongoDB Atlas account at [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas).
    - Set up a cluster and create a database user with the necessary permissions.
    - Obtain your MongoDB connection string from the Atlas dashboard.

4. **Configure your connection string:**

    In the `config.py` file, replace the placeholder with your MongoDB connection string:

    ```python
    MONGO_URI = "your-mongodb-connection-string"
    ```

    Ensure that your connection string includes the database name and authentication details.

### Running the Program

To run the main script:

```bash
python main.py
