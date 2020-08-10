FROM python:alpine3.12
MAINTAINER greenmind.sec@gmail.com
RUN pip3 install youtube-search-python
WORKDIR /opt
ADD . .
RUN chmod +x /opt/greenScan.py
ENTRYPOINT ["python","/opt/greenScan.py"]
CMD ["--help"]
