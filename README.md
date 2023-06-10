# deanonymize

This Python script 'deanonymizes' sensitive info in documents. The script uses aliases for sensitive names. When ran, the deanonymization script replaces the alias with the sensitive name. The names and aliases are read from a CSV file.

## Requirements

- Python 3.8 or later
- Docker

## Setup

1. Clone this repository to your local machine.
2. Ensure that Docker is installed and running on your machine.

## Building the Docker Image

From the project directory, run:

```
docker build -t deanonymize .
```

This command builds a Docker image named `deanonymize` using the Dockerfile in the current directory (`.`).

## Running the Docker Container

After building the Docker image, you can run the Docker container with this command:

```
docker run -it -v /path/to/your/documents_and_csv/:/app/ -u $(id -u):$(id -g) deanonymize python ./deanonymize.py /app/your_documents_directory /app/your_csv_file
```

In the `docker run` command:

- `-v /path/to/your/documents_and_csv/:/app/` mounts your directory to `/app/` in the Docker container.
- `-u $(id -u):$(id -g)` runs the command in the Docker container as the current user, which helps to avoid permission issues.
- `deanonymize` is the name of the Docker image to run.
- `python ./deanonymize.py /app/your_documents_directory /app/your_csv_file` is the command to run in the Docker container. Replace `your_documents_directory` with the path to your documents directory inside the Docker container and `your_csv_file` with the name of your CSV file inside the Docker container.

Remember to replace `/path/to/your/documents_and_csv/`, `your_documents_directory`, and `your_csv_file` with your actual paths and filenames.

## Notes

Please ensure that the `deanonymize.py` script and the CSV file are both located in the `/path/to/your/documents_and_csv/` directory on your host machine.

This script assumes that 'names_and_aliases.csv' is the CSV file with the names and aliases and that `your_documents_directory` is the directory with the documents. If your CSV file is not in the same directory as your documents, you will need to modify the `-v` option to mount the CSV file in the correct location in the container.
