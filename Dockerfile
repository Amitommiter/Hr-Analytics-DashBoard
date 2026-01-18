FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir streamlit pandas numpy matplotlib seaborn plotly scikit-learn

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
