docker stop $(docker ps -a -q)
#docker rmi -f chat-app
docker rmi -f $(docker images -aq)
docker rm -f $(docker ps -a -q)
docker build -t chat-app . 
 #-f thin.Dockerfile
docker run --name chat_container -d -p 5000:5000 --memory=1g --memory-reservation=512m --cpus=1 --cpuset-cpus=2 chat-app 
#docker container run --rm -it -d --name chat_container --memory=1g --memory-reservation=512m nginx:alpine
