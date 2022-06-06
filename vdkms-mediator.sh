#!/bin/bash
docker-compose -f libraries/acapy-conf/demo2/docker-compose.factory-usecase.yml up -f libraries/aries-acapy-plugin-toolbox/demo_dot/docker-compose.mediator.yml up --build