FROM selenium/standalone-chrome
USER root
RUN sudo apt-get update && sudo apt-get install dialog -y --no-install-recommends apt-utils

ADD hatebase_vocab_asian.csv /tmp
ADD hatebase_vocab_chinese.csv /tmp
ADD hatespeech.py /tmp
ADD BE5E7B3BAE09762ADC693A15C64B839F.txt /tmp
Add requirements.txt /

RUN sudo apt-get update -y
RUN sudo apt-get install -y vim
RUN sudo apt-get install -y python3
RUN sudo apt-get install -y python3-pip



RUN pip3 install pystrich
RUN pip3 install -r /requirements.txt



ENTRYPOINT ["python3"]
CMD ["/tmp/hatespeech.py"]