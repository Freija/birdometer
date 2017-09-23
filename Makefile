TAG=freija/birdometer
.PHONY: build run

build:
	docker build -t "$(TAG)" .

run: clean
	docker run --name birdometer -v /home/eaubsho/birdometer/data:/data --device /dev/vchiq:/dev/vchiq --device /dev/mem:/dev/mem --device /dev/gpiomem:/dev/gpiomem -it "$(TAG)" /bin/bash -il

clean:
	docker stop birdometer; true
	docker rm birdometer; true
