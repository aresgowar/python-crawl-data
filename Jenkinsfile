pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/aresgowar/python-crawl-data.git'
            }
        }
        // stage('Docker') {
        //     steps {
        //         withDockerRegistry(credentialsId: 'docker-hub', url: ' https://index.docker.io/v1/') {
        //         }
        //     }
        // }
    }
}
