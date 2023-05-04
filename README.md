# ProyectoFinal_Docker
# Deploying the Service Using the Dockerfile

This README file will guide you through the steps required to deploy the service using the Dockerfile.

## Prerequisites

* Docker
* Git

## Steps

1. Clone the repository

```git clone https://github.com/[your-username]/[repository-name].git```

2. Change directory to the repository:

```cd [repository-name]```

3. Build the Docker image:

```docker build -t [image-name] .```

4. Run the Docker image:

```docker run -p [port]:[port] [image-name]```

For example, to run the Docker image on port 8080, you would use the following command:

```docker run -p 8080:8080 [image-name]```

5. Access the service:

Once the Docker image is running, you can access the service at the following URL:

```http://localhost:[port]```

For example, if you are running the Docker image on port 8080, you would access the service at the following URL:

```http://localhost:8080```

## Troubleshooting

If you are having trouble deploying the service, please check the following:

* Make sure that you have Docker and Git installed.
* Make sure that you have built the Docker image correctly.
* Make sure that you are running the Docker image on the correct port.

If you are still having trouble, please feel free to open an issue on the repository.


