# CA End Instance Nodejs Portion of Controller
Web controller for a Hyperledger Aries CA End Web Agent

## Table of Contents

- [Running Locally](#running-locally)
    - [Prerequisites](#prerequisites)
    - [Starting the Application](#starting-the-application)
- [Notes](#notes)

### Prerequisites

### Running Locally

#### Prerequisites

This Controller requires `Node.js 10.x` or higher. Node.js can be downloaded [here](https://nodejs.org/en/download/). Alternatively you can use a Node.js version manager like [`nvm`](https://github.com/nvm-sh/nvm) or [`nvm-windows`](https://github.com/coreybutler/nvm-windows).

#### Starting the Application

From the ca-end-hbs root directory, simply install application node modules then call `npm start`

For example on Linux:

```
$ npm install
$ npm start
```

You can now open your browser tab to `localhost:3000` to see the application.

### Notes

_Note: Ca-End Controller has already been configured to connect to it's agent on localhost:8021. If the controller is not connected to it's agent you will see a red status indicator on the top right-hand side of the navbar. If the agent is succesffully connected, you will see a green status indicator._
