# Base image
FROM ubuntu:18.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    fortune-mod \
    cowsay \ 
    netcat

# Export PATH variables to get cowsay and fortune
ENV PATH="/usr/games:$PATH"

# Set working directory
WORKDIR /app

COPY . .

EXPOSE 4499

# Run the script as the entrypoint
CMD ["./wisecow.sh"]

