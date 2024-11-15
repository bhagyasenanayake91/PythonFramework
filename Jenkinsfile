pipeline {
   agent { 
      docker { 
         image 'mcr.microsoft.com/playwright/python:v1.48.0-focal' 
         } 
   }
   // agent { dockerfile true }
   stages {
      stage('install') {
         steps {
            // sh 'pip install -r requirements.txt'
            sh '''
               pip install playwright
               playwright install --with-deps
            '''
         }
      }
      stage('test') {
         steps {
            sh 'pytest'
         }
      }
   }
}