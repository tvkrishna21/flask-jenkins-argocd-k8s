pipeline {
    
    agent any 
    
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
    }
    
    stages {
        
        stage('Checkout'){
           steps {
                git credentialsId: '0819c8c8-4583-4950-bfa5-a23ae01ff226', 
                url: 'https://github.com/tvkrishna21/flask-jenkins-argocd-k8s',
                branch: 'main'
           }
        }
        
        stage('build'){
            steps {
                script{
                    sh '''
                    echo 'Build Docker Image'
                    echo $IMAGE_TAG
                    docker build -t tvkrishna21/flask-jenkins-argocd-k8s:${BUILD_NUMBER} .
                    docker images
                    '''
                }
            }
        }

        stage('Push the artifacts'){
           steps{
                script{
                    withDockerRegistry([ credentialsId: "dockerhub", url: "" ]) {
                        sh 'docker push tvkrishna21/flask-jenkins-argocd-k8s:${BUILD_NUMBER}'
                    }
                }
            }
        }
    }
}
