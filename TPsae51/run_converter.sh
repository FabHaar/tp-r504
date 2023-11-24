#!/bin/bash

docker run -it \
	--workdir /srv \
	--name sae51-ub \
	--mount type=bind, sources=$(pwd)/shared, target=/srv \
	img_sae51
