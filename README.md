# Toolbox Vue

- [How to Run](#how-to-run)
- [Instructions](#instructions)
  - [Start Toolbox Vue tool](#Start Toolbox Vue tool)
  - [Start three agents](#Start three agents)
  <!-- - [Stopping the Lab](#stopping-the-lab) -->




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

Use vdkms-ca.sh, vdkms-sp.sh, and vdkms-alice.sh to start three agents.




<!-- ### Stopping the Lab

To stop the Aries Toolbox, go to one of the screens and choose the top menu item “File/Quit.” In the first terminal, you will be back at the command line, and you can exit.

To stop the ACA-Py agents, go to the second terminal and:




*   Hit Ctrl-C to terminate the agents.
*   To cleanup the docker sessions run:

        ```
        docker-compose -f docker-compose_alice_bob.yml down

        ```


Exit out of the second terminal session. -->

