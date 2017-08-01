FROM python:3.6

ENV CHAMELEON /usr/src/app
RUN mkdir -pv $CHAMELEON
WORKDIR $CHAMELEON

COPY setup/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY chameleon chameleon
CMD ["gunicorn", "chameleon:app"]

