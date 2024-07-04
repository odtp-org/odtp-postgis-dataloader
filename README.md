# POSTGIS to CSV

Description of the component

| Tool Info | Links |
| --- | --- |
| Original Tool | []() |
| Current Tool Version  | [commit-hash](link-to-commit-hash) |


## ODTP command 

```
odtp new odtp-component-entry \
--name odtp-postgis-dataloader \
--component-version 0.1.1 \
--repository https://github.com/odtp-org/odtp-postgis-dataloader
``` 

## Data sheet

### Parameters

| Parameter | Description | Default Value |
| --- | --- | --- |
| HOST | PostgreSQL HOST | None |
| PORT | PostgreSQL PORT | None |
| DATABASE | PostgreSQL database to be queried | C |
| QUERY | Query. Please wrap it between `"`: `"QUERY"`  | None |
| OUTPUT_FILENAME | Output file name | `output.csv` |
| GEOM_COL | Column where to find the geometry | `geometry` |

### Secrets

| Secrets | Description | Default Value |
| --- | --- | --- |
| LOGIN_USER | User in the PostgreSQL database | None |
| PASSWORD | Password in the PostgreSQL database | None |


### Input Files

No input files are required. 

### Output Files

| File/Folder | Description |
| --- | --- | 
| CSV File | CSV file containing the results from the QUERY |

## Tutorial

### How to run this component as docker

Build the dockerfile with:

```bash
docker build -t odtp-postgis-dataloader .
```

Copy `.env.dist` in `.env` and fill the variables. Run the following command. Mount the correct volumes for input/output folders. 

```bash
docker run -it --rm \
-v {PATH_TO_YOUR_INPUT_VOLUME}:/odtp/odtp-input \
-v {PATH_TO_YOUR_OUTPUT_VOLUME}:/odtp/odtp-output \
--env-file .env odtp-component
```

### Development

This command will create a test folder with the volumes to be mounted. If you are using Powershell, replace `$(pwd)` by `${PWD}`.

```bash
mkdir test
mkdir test/odtp-input
mkdir test/odtp-output
mkdir test/odtp-logs

docker run -it --rm \
-v $(pwd)/test/odtp-input:/odtp/odtp-input \
-v $(pwd)/test/odtp-output:/odtp/odtp-output \
-v $(pwd)/test/odtp-logs:/odtp/odtp-logs \
-v $(pwd)/app:/odtp/odtp-app --env-file .env --entrypoint bash odtp-postgis-dataloader
```

Then in order to run the component, you can execute:

```bash
bash /odtp/odtp-component-client/startup.sh
```

Finally, when you are done, please remove the test folder.

```bash
rm -r test
```


## CHANGELOG

- v0.1.0
    - Ubuntu fixed at 22.04
    - Python fixed at 3.10


## Developed by

CSFM & SDSC
