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
                    docker build -t tvkrishna21/flask-jenkins-argocd-k8s:${BUILD_NUMBER} .
                    ls -ltr
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "5517d3b5-95fe-4a2e-b64a-44eec57dbe03", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "docker push tvkrishna21/flask-jenkins-argocd-k8s:${BUILD_NUMBER}"

                    }
                }
            }
        }

    }
}
