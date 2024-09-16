ChatApp-Docker

Important Note:The core application code was sourced from an external project and was not written as part of this repository.
Modifications were made to adapt it to a Docker environment.

Overview
This repository contains a Dockerized chat application built using Node.js. 
It provides a simple, real-time chat experience with message broadcasting and user joining/leaving notifications.

Prerequisites
Docker
Node.js and npm (or yarn)

Installation
Clone the repository:
Bash
git clone https://github.com/Tova-Rozovsky/ChatApp-Docker.git

Navigate to the project directory:
Bash
cd ChatApp-Docker
Build the Docker image:
Bash
docker build -t chatapp .

Running the Container
Bash
docker run -p 3000:3000 chatapp

This will start the chat application on port 3000 of your local machine.

Accessing the Application
Open a web browser and navigate to http://localhost:3000.

Features
Real-time messaging: Messages are instantly broadcast to all connected users.
User joining/leaving notifications: The chat displays messages when users join or leave the room.
Simple user interface: A basic interface for sending and receiving messages.
Customization
You can customize the application by modifying the app.js file. This includes changing the port, adding more features, or modifying the user interface.

Additional Notes
Security: For production environments, consider implementing additional security measures such as authentication and authorization.
Scalability: The Dockerized setup makes it easy to scale the application by running multiple containers.
Persistence: If you need to persist chat history, you can integrate a database like MongoDB or Redis.
Enjoy chatting!
