## Wise Cow Says in Docker 

This project lets you run a fun script (`wisecow.sh`) that displays message in localhost:4499.

**Features:**

* Uses `cowsay` for messages.

**Building the Image:**

1. **Prerequisites:** Docker installed (see https://www.docker.com/).
2. **Build:**

   ```bash
   docker build -t <your_username>/wisecow:latest .

   docker run -p 4499:4499 <your_username>/wisecow:latest

3. For github actions to work, please replace the username and password for your dockerhub account at .github/workflows/build.yaml

4. You can run it as kubernetes service by 

```bash

1. Log into your cluster
2. Run following command

kubectl apply -f manifest.yaml -n my-namespace
