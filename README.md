# DNS Record Updater Docker Image

## Overview
This Docker image is designed to automatically check and update a DNS record in Cloudflare based on the current public
IP address of the machine where the container is running. It checks the public IP using `api.ipify.org` and then
compares it with the IP address recorded in Cloudflare for a specific DNS record. If the IP addresses do not match, the
script updates the record in Cloudflare with the current IP. This container is set up to run the update script every 2 hours.

## Prerequisites
Before deploying this Docker container, ensure you have Docker installed on your host machine. If you need to install
Docker, follow the instructions on the [official Docker website](https://docs.docker.com/get-docker/).

## Configuration
The Docker container requires the following environment variables to be set. These variables are necessary to authenticate and interact with the Cloudflare API:

- `CLOUDFLARE_API_TOKEN`: Your API token from Cloudflare. It should have the permissions to read and write DNS records.
- `CLOUDFLARE_ZONE_ID`: The Zone ID of the domain you are managing with this container.
- `CLOUDFLARE_DNS_RECORD_ID`: The DNS Record ID that you want to update.

A sample `.env.example` file is included in the repository. Copy this file to `.env` and update it with your actual values:

```bash
cp .env.example .env
# Edit .env and replace placeholders with your actual data
```
## Running the Container
To run the Docker container, use the following command:
```bash
docker run --env-file .env -d --name dns_record_updater dns_record:latest
```
This command uses the environment variables defined in your `.env` file. The container runs in detached mode with the
name `dns_record_updater`.

## Automating DNS Updates
The script within the container is scheduled to run every 2 hours to check and update the DNS record. This scheduling is
handled internally by the container, so no external cron jobs or task schedulers are needed.

## Logging
To view the logs and see what actions the script has been performing, use the following Docker command:
```bash
docker logs dns_record_updater
```
These logs will include information on when the IP address is checked, any discrepancies found, and the update process
in Cloudflare.

## Stopping the Container
If you need to stop the running container, use:
```bash
docker stop dns_record_updater
```

To remove the container after stopping it, use:
```bash
docker rm dns_record_updater
```

## Contributions and Support
For contributions, please create a pull request with your proposed changes. If you encounter any issues while using
this Docker image or have suggestions for improvements, please open an issue in the repository.