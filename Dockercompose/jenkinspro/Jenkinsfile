pipeline {
    agent any

    environment {
        // Define environment variables
        DOCKER_IMAGE = 'django-hello-world:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checks out the source code
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                // Builds a Docker image from Dockerfile
                script {
                    docker.build(env.DOCKER_IMAGE)
}
            }
        }

        stage('Run Docker Container') {
            steps {
                // Stops previously running container
                script {
                    sh 'docker stop django-app || true'
                    sh 'docker rm django-app || true'
                }
                // Runs the newly built Docker image
                script {
                    sh "docker run -d --name django-app -p 8000:8000 ${env.DOCKER_IMAGE}"
                }
            }
