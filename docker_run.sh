#!/bin/bash

docker run  -d -p 8002:8002 --network=vod-network --restart always  --volume "$(pwd)":/code --name time-bot time-bot:latest
docker logs -f time-bot