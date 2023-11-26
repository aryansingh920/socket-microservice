const net = require('net');

// Specify the host and port of the microservice
const host = '127.0.0.1';
const port = 12345;

// Create a TCP socket
const client = new net.Socket();

// Connect to the microservice
client.connect(port, host, () => {
    console.log(`Connected to microservice at ${host}:${port}`);

    // Send a message to the microservice
    const message = 'Hello, microservice!';
    client.write(message);
});

// Handle data received from the microservice
client.on('data', (data) => {
    console.log(`Received from microservice: ${data}`);

    // Close the connection after receiving a response
    client.end();
});

// Handle the connection closed event
client.on('close', () => {
    console.log('Connection to microservice closed');
});
