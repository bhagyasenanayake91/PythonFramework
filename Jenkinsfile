pipeline {
   // agent { 
   //    docker { 
   //       image 'mcr.microsoft.com/playwright/python:v1.47.0-noble' 
   //       } 
   // }
   agent { dockerfile true }
   stages {
      stage('install') {
         environment {
            HOME="."
         }
         // steps {
         //    // sh 'pip install -r requirements.txt'
         //    sh '''
         //       pip install playwright
         //       playwright install --with-deps
         //    '''
         // }
      }
      stage('test') {
         steps {
            sh 'echo TEST'
         }
      }
   }
}