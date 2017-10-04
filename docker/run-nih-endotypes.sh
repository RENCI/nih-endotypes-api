#!/usr/bin/env bash

PATH_TO_DOCKERFILE=../server/
LOCAL_PORT=5000
PATH_TO_ENV_FILE=nih-endotypes.env
PATH_TO_SSL_CERTS=

cd $PATH_TO_DOCKERFILE
docker build -t nih-endotypes .
cd -

docker stop nih-endotypes
sleep 2s
docker rm -fv nih-endotypes
sleep 2s
if [[ ! -z ${PATH_TO_SSL_CERTS} ]]; then
    docker run -d --name nih-endotypes \
        --env-file=${PATH_TO_ENV_FILE} \
        -p ${LOCAL_PORT}:5000 \
        -v ${PATH_TO_SSL_CERTS}:/certs \
        nih-endotypes
    echo "NIH Endotypes API running over https"
else
    docker run -d --name nih-endotypes \
        --env-file=${PATH_TO_ENV_FILE} \
        -p ${LOCAL_PORT}:5000 \
        nih-endotypes
    echo "NIH Endotypes API running over http"
fi

exit 0;
