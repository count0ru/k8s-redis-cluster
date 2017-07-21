FROM redis:3.2.8

COPY redis-master.conf /redis-master/redis.conf
COPY redis-slave.conf /redis-slave/redis.conf
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]

ENTRYPOINT [ "bash", "-c" ]
