A demo for DOT 
=================================================

## Running the Demos

Requirements:
- Docker
- Docker Compose

#### Single Agent

Run the following from the this directory:

```sh
$ docker-compose up --build
```

E.g. If you are running CA agent, then use command: 


```sh
$ docker-compose -f ./docker-compose.ca.yml up --build 
```



#### Alice + CA

Run the following from the `demo` directory:

```sh
$ docker-compose \
    -f ./docker-compose.ca.yml \
    -f ./docker-compose.alice.yml \
	up --build
```

#### Alice + CA + Service Provider

Run the following from the `demo` directory:

```sh
$ docker-compose \
    -f ./docker-compose.ca.yml \
    -f ./docker-compose.alice.yml \
    -f ./docker-compose.sp.yml \
	up --build
```


#### Standalone Mediator

Run the following from the `demo` directory:

```sh
$ docker-compose \
    -f ./docker-compose.mediator.yml \
	up --build
```
