# birdometer-rpi
Code for the birdometer. This is the code that runs on the Raspberry Pi. It captures images whenever the IR sensor is triggered.

The code is run inside a Docker container. To run:
 1. Make sure Docker is installed
 2. As root or sudo: ```make clean && make build && make run```

