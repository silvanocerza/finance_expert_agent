# Finance Expert Agent

This repo contains the configuration for an agent politician expert in finance and economy usable with [OrchestrIA](https://github.com/orchestria/orchestria).

## Usage

Get data:

```
$ hatch run get_data.py '{{"table": "data_898932971702f1d8205a6b757deea2e1","page": 1,"columns": ["codice stock", "regione", "importo disponibilita liquide"]}}'
```

Get schema:

```
$ hatch run get_schema.py '{{"table": "data_898932971702f1d8205a6b757deea2e1"}}'
```

## License

This repo and all its contents are distributed under the terms of the [AGPL-3.0-or-later](https://spdx.org/licenses/AGPL-3.0-or-later.html) license.
