docker stop $(docker ps -a -q)
docker rmi -f chat-app
docker rmi -f $(docker images -aq)
docker rm -f $(docker ps -a -q)
