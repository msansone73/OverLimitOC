FROM python:2.7
RUN pip install pyocclient
RUN pip install unittest-data-provider
RUN pip install pycurl
#RUN mkdir overlimitoc
RUN mkdir saida
COPY . /
#RUN ls | more 
#RUN ls /usr/local/lib/python2.7/site-packages/owncloud
COPY  ./owncloud/ /usr/local/lib/python2.7/site-packages/owncloud
#RUN ls /usr/local/lib/python2.7/site-packages/owncloud 
CMD ["python", "smashbox2.py"]
#cMD ["python", "validaoc.py"] 
