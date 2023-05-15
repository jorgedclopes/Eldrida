#!/bin/bash

docker container stop delaney || true
docker container rm delaney || true

VERSION=$1

docker build . --file Dockerfile --tag carequinha/eldrida:"$VERSION"
docker run -d \
--name eldrida \
-e DISCORD_KEY=MTEwNzA0ODM5NjMzNTg5MDQ0Mw.GiTn7S.c3WWPx5sZJsJ0OWMh3efwvyDcXv6s44dBaqbt8 \
-e OPENAI_API_KEY=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 \
--restart always \
carequinha/eldrida:"$VERSION"