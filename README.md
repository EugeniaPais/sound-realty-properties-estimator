# Sound Realty Properties Estimator

## Description
Sound Realty Properties Estimator is a tool designed to help real estate professionals estimate property prices using machine learning models. 

## Cloning the Repository
To clone this repository, ensure you have [Git](https://git-scm.com/) installed on your system. Then, run the following command in your terminal:

```sh
git clone https://github.com/EugeniaPais/sound-realty-properties-estimator.git
```

## Running the Application with Docker

### Prerequisites
- Ensure you have [Docker](https://docs.docker.com/get-docker/) installed on your system.

### Build the Docker Image
To build the Docker image, run the following command in the root directory of the project:
```sh
docker build -t sound-realty-mle .
```

### Run the Application
To run the application, use the following command:
```sh
docker run -p 8000:8000 -v ./app:/app/app sound-realty-mle
```
This will start the application and map port `8000` on your local machine.

## Run Tests
To run the tests, use the following command:
```sh
docker run --rm sound-realty-mle poetry run pytest --maxfail=1 --disable-warnings -q
```
This will execute the test suite inside the Docker container.

## Performance Analysis

For a detailed performance analysis of the model, you can check the Jupyter Notebook located at:

```
/app/base_code/performance_analysis.ipynb
```
