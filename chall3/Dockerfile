FROM ubuntu:22.04
RUN apt-get update -y && apt-get install -y \
    lib32z1 xinetd \
 && rm -rf /var/lib/apt/lists/*
RUN apt-get update -y && apt-get install -y python3 python3-pip
RUN pip3 install pycryptodome
RUN useradd error
RUN mkdir /crypto
RUN echo "You've been blocked by our xinetd - try again, and report if this repeats." > /etc/banner_fail
COPY ./ctf.xinetd /etc/xinetd.d/crypto
COPY ./start.sh /start.sh
COPY ./setup.sh /setup.sh
COPY ./show.py /crypto/show.py
# COPY ./bin/exploit.py /crypto/exploit.py
# RUN chown -R root:error /crypto && chmod -R 750 /crypto
RUN chmod +x /setup.sh
RUN chown root:error /start.sh && chmod 750 /start.sh

CMD ["/setup.sh"]

EXPOSE 9999


