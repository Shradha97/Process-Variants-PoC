config_data = {
    "path": {"data": "../data/", "cache": "../cache/", "db": "prod-mnr"},
}

data_file_name = config_data["path"]["db"]
cache = config_data["path"]["cache"] + data_file_name + "/"
data = config_data["path"]["data"] + data_file_name + "/"
