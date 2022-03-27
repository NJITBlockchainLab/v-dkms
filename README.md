# FHWA Agent Demo 


## How to Run 


### Prerequisite 

1. Run `.\ubuntu18_docker_and_py.sh` to install Docker and Python dependencies. 

2. Run `.\ubuntu18_indy_sdk.sh` to install dependencies for our Blockchain Ledger.
 
3. Run `.\ubuntu18_install_nodejs.sh` to install NodeJS.


### Build and Start Ledger 

1. Run `sudo .\libraries\v-network\manage build` to build ledger.

2. Run `sudo .\libraries\v-network\manage start` to start four nodes and web server for our ledger. 

3. In the browser, use http://127.0.0.1:9000 to access ledger exploer. 

4. Run `sudo .\libraries\v-network\manage stop` to stop ledger and web server. 


### Start Agent and Controller 

In the terminal, run script in the [Agent Provision](!cloudagent_provision.md) to start the agent and controller.


<!-- # Toolbox Vue (Under development)

- [How to Run](#how-to-run)
- [Instructions](#instructions)
  - [Start Toolbox Vue tool](#Start Toolbox Vue tool)
  - [Start three agents](#Start three agents)
  - [Stopping the Lab](#stopping-the-lab)




## How to Run

Since the original Aries Toolbox is an [Electron](https://www.electronjs.org/) app, to run this tool you need to install the basic envonriment which inclcudes [nodejs](https://nodejs.org/) and [npm](https://www.npmjs.com/) (node package manager) installed. 


## Instructions

Please open up two terminals running bash, and we’ll start in the first.


### Start Toolbox Vue tool

Use the following command to build and start toolbox, 

`
source LaunchAriesToolbox.sh
`


### Start three agents

Use vdkms-ca.sh, vdkms-sp.sh, and vdkms-alice.sh to start three agents. -->




<!-- ### Stopping the Lab

To stop the Aries Toolbox, go to one of the screens and choose the top menu item “File/Quit.” In the first terminal, you will be back at the command line, and you can exit.

To stop the ACA-Py agents, go to the second terminal and:




*   Hit Ctrl-C to terminate the agents.
*   To cleanup the docker sessions run:

        ```
        docker-compose -f docker-compose_alice_bob.yml down

        ```


Exit out of the second terminal session. -->

