#!/usr/bin/env bash

PATH_TO_DOCKERFILE=../server/
LOCAL_PORT=5000
DOCKER_NETWORK=bridge
PATH_TO_SSL_CERTS=''

cd $PATH_TO_DOCKERFILE
docker build -t nih-endotypes .
cd -

docker stop nih-endotypes
sleep 2s
docker rm -fv nih-endotypes
sleep 2s
if [[ ! -z ${PATH_TO_SSL_CERTS} ]]; then
    docker run -d --name nih-endotypes \
        -p ${LOCAL_PORT}:5000 \
        --network=${DOCKER_NETWORK} \
        -v ${PATH_TO_SSL_CERTS}:/certs \
        nih-endotypes
    echo "NIH Endotypes API running at https://localhost:"${LOCAL_PORT}"/v1/ui/#/default"
else
    docker run -d --name nih-endotypes \
        -p ${LOCAL_PORT}:5000 \
        --network=${DOCKER_NETWORK} \
        nih-endotypes
    echo "NIH Endotypes API running at http://localhost:"${LOCAL_PORT}"/v1/ui/#/default"
fi

exit 0;
