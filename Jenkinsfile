pipeline{
        agent any
        stages{ 
		    stage('---Build_Image---'){
                        steps{
                            sh "sudo docker build -t flask-app ."
                        }
                }
                stage('---clean---'){
                        steps{
                              sh label: '', script: '''if [ ! "$(sudo docker ps -q -f name=flask-app)" ]; then
    					if [ "$(sudo docker ps -aq -f status=exited -f name=flask-app)" ]; then
       				 		# cleanup
        					sudo docker rm -f flask-app
    					fi
    					# run your container
				sudo docker run -d --name flask-app -p 8888:8888 flask-app
				fi'''
                        }
                }
		stage('--run--'){
			steps{
				sudo docker run -d --name flask-app -p 5000:5000 flask-app
			}
		}
        }
}
