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
        
        stage('echo'){
            steps {
                script{
                    sh '''
                    echo 'Build Docker Image'
                    echo $IMAGE_TAG
                    PREV_TAG=$((IMAGE_TAG - 1))
                    echo $PREV_TAG
                    docker build -t tvkrishna21/flask-jenkins-argocd-k8s:${BUILD_NUMBER} .
                    ls -ltr
                    docker images
                    '''
                }
            }
        }

        stage('Push the artifacts'){
           steps{
                script{
                    withCredentials([string(credentialsId: ‘dockerhub’, variable: ‘dockerhubpwd’)]) {
                        sh 'docker login -u tvkrishna21 -p ${dockerhubpwd}’
                        sh 'docker push tvkrishna21/flask-jenkins-argocd-k8s:${BUILD_NUMBER}'
                    }
                }
            }
        }
    }
}
