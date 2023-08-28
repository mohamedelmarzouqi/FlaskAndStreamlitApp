FROM python:3.10.6

WORKDIR /streamlit_app

COPY . /streamlit_app

RUN pip install -r requirements.txt

EXPOSE 8501

ENV STREAMLIT_APP=streamlit_app.py

CMD ["streamlit", "run", "streamlit_app.py"]