pipeline {
    agent {
        docker {
            image "aresgowar/aresdockercrawl:1.0"
        }
    }

    stages {
        stage('Build') {
            steps {
                sh """
                    python --version
                    python crawl.py
                """
            }
        }
    }
}
