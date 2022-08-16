# T5-BASE MODEL as an API

A service to expose HuggingFace's T5-Base model as an API

## Application Requirements

- [docker](https://www.docker.com/) 20.10+
- Minimum RAM size needed to run is 8GB, Recommended is 16GB+
- To use less resource as well and for convenience sake the application relies uses the CPU-support version of the transformers library `transformers[torch]`.
As the result, a GPU is not necessary for building and running the application.

## Getting Started

```bash
# Clone repository to your local and navigate into the folder
git clone https://github.com/horlali/api.translator-t5-base
cd api.translator-t5-base/

# Build and start the application with docker-compose
docker-compose up --build
```

## Application Docs

See [Application README](./src/README.md)

## T5-Base Model

See links to model features, documentation, and training proceduces [here](https://huggingface.co/t5-base)
