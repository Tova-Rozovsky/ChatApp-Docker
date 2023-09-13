docker build -t chat-app . -f large.Dockerfile
#docker run -d -p 5000:5000 chat-app
docker run --name chat_container -d -p 5000:5000 --memory=1g --memory-reservation=512m --cpus=1 --cpuset-cpus=2 chat-app 
