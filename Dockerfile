FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y git
RUN pip install Flask
RUN pip install numpy
RUN pip install pandas
RUN pip install scikit-learn
RUN pip install torch
RUN pip install transformers
RUN pip install streamlit
RUN pip install altair

ENV FLASK_APP app.py
ENV FLASK_ENV development

RUN git clone "https://github.com/apophis-web/MLOps-Assignment-2-i191895_i191878"
WORKDIR /MLOps-Assignment-2-i191895_i191878

EXPOSE 5000

CMD ["sh", "-c", "flask run & python3 -m streamlit run infer.py"] 
