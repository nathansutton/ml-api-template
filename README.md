## Services

This repository exposes four components that are useful in a data science proof of concept.
- A container running Jupyter notebooks with common machine learning libraries (port:8888)
- A container running Postgres in the event a relational database is useful (port:5432).  Any transformations will persist between containers in a mounted volume (./volumes/postgres)
- A container running FastAPI to serve predictions from a scikit-learn model (port:8080)
- A container running Streamlit allows a user to access the predictions from their scikit-learn model based on user inputs (port:8501)

## Usage
```
docker-compose up 
```

## Structure
```
|-- containers - code
|   |-- python      # interactive jupyter notebooks
|   |-- fastapi     # deploy pickled model as a REST API 
|   |-- streamlit   # access REST API in a user interface 
|-- volumes         # persistent data
|   |-- notebooks   # jupyter notebooks persisted here
|   |-- postgres    # database files persisted here, not in version control
|   |-- static      # static files that are loaded into postgres or jupyter
```

## Database

You can connect to PostgreSQL on localhost:5432 with a user 'local' and no password (POSTGRES_HOST_AUTH_METHOD=trust) with any SQL client you like.

## Sample Endpoint

The model is available as a REST API endpoint on port 8080.  It accepts JSON data that look like 1 row of the dataframe it as trained on. 
```
curl --request POST http://127.0.0.1:8080/predict \
    -H 'Content-Type: application/json' \
    -d '{"age_group": "Under 15 yrs","reported_race_ethnicity": "White, non-Hispanic", "previous_births": "None","tobacco_use_during_pregnancy": "Yes","adequate_prenatal_care": "Inadequate"}'
```

## Known Vulnerabilities
There is literally zero security.  Keep this on localhost.
- There is not password for the postgres database.
- The rest API calls are not encrypted.
- The jupyter notebook runs as root in a container.
- The user interface is exposed without encryption or a password.
