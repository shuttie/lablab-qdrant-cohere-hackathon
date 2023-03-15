# lablab.ai Qdrant/Cohere hackathon

A demo of a semantic recommender by `metacrank` team.

## Running locally

The whole app is packaged in a single docker compose manifest:
```
docker compose -f compose.yml up
```

The manifest does the following steps:
* Starts the Qdrant server
* Starts the Metarank in the standalone mode
* ALS model is trained based on MovieLens dataset
* Embeddings for MiniLM-L6-v2 are computed and dumped to the Qdrant
* Cohere embeddings for the same dataset are also dumped to the Qdrant
* A simple flask web app is started

After that go to the `http://localhost:8080` and play with the app.

### License

Apache 2.0