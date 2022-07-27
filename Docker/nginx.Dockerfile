FROM nginx
RUN rm /etc/nginx/nginx.conf
COPY Docker/nginx.conf /etc/nginx/
COPY Docker/keys/cert_chain.crt /etc/nginx
COPY Docker/keys/server.key /etc/nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY Docker/socket.conf /etc/nginx/conf.d/
