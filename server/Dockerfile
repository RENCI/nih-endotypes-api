FROM r-model:latest

# Set default environment variables
# [connexion/api-server]
ENV CONNEXION_SERVER=''
ENV CONNEXION_DEBUG=True
ENV API_SERVER_HOST=localhost
ENV API_SERVER_PORT=5000
ENV API_SERVER_KEYFILE=''
ENV API_SERVER_CERTFILE=''
# [sys-path]
ENV SYS_PATH_CONTROLLERS=/nih-endotypes/controllers
ENV SWAGGER_HOST=localhost:5000

COPY . /nih-endotypes
WORKDIR /nih-endotypes

RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

ENTRYPOINT ["/nih-endotypes/docker-entrypoint.sh"]
EXPOSE 5000
CMD ["app.py"]
