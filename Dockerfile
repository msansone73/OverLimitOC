FROM python:2.7
MKDIR owncloud
COPY * owncloud/*
CMD ["python", "owncloud/overlimitoc.py"]