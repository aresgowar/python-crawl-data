pipeline {
    agent {
        docker { image 'aresgowar/aresdockercrawl:1.0' }
    }
    stages {
        stage('Test') {
            steps {
                sh """
                    python --version
                """
            }
        }
    }
}
