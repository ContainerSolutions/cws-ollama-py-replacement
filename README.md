# cws-ollama-py-replacement

## Docker build and run

```bash
podman build -t embedding-service .
podman run -p 8000:8000 embedding-service
```

## Testing conditions

`-n 1000`: 1000 total requests

`-c 50`: 50 concurrent workers

```bash
hey -n 1000 -c 50 -m POST -H "Content-Type: application/json" -d '{"text":"John Smith"}' http://localhost:8000/embed
```

## Model benchmarks

1. `all-MiniLM-L6-v2`

```
Summary:
  Total:	18.9186 secs
  Slowest:	3.8480 secs
  Fastest:	0.0144 secs
  Average:	0.8902 secs
  Requests/sec:	52.8581

  Total data:	8050000 bytes
  Size/request:	8050 bytes
```

2. `nli-mpnet-base-v2`

