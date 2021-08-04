# HTTP host to CSV

- [HTTP host to CSV](#http-host-to-csv)
  - [What it does](#what-it-does)
  - [How to use](#how-to-use)
    - [Setup](#setup)
    - [Executing](#executing)

## What it does

Given a list of servers, this script connects using SSH on each server, retrieving HTTP server's hosts and their ports, outputting CSV files with that relation (a CSV file for each server), and then joining all those files in an xlsx spreadsheet.

This is a CSV file output example:
```csv
Porta, Hosts
8080,prod.server.com
8081,test.server.com
```

## How to use

### Setup

- Copy `config.yaml.example` to `config.yaml`
- Edit according to your needs
- If `key_path` is not provided, the script will use your local SSH key.
- Install the dependencies with:
    ```bash
    pip3 install -r requirements.txt
    ```


### Executing

You can run the script with the following command

```bash
python3 http-host-to-csv.py
```
