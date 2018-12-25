FROM python:3.7.1

WORKDIR /opt/slapec/melodyminer

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "melodyminer"]
