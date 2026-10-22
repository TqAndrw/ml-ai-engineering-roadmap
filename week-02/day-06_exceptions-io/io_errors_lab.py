import json


class ConfigError(Exception):
    pass


def load_config(path):
    try:
        with open(path, "r") as f:
            config = json.load(f)

    except FileNotFoundError as e:
        raise ConfigError(f"Config file not found: {path}") from e

    except json.JSONDecodeError as e:
        raise ConfigError(f"Invalid JSON in config: {path}") from e

    if "name" not in config:
        raise ConfigError("Missing required field: name")

    if "port" not in config:
        raise ConfigError("Missing required field: port")

    if not isinstance(config["port"], int):
        raise ConfigError("Field 'port' must be an integer")

    return config


def main():
    try:
        config = load_config("config.json")
    except ConfigError as e:
        print("Configuration error:", e)
    else:
        print("Config loaded successfully")
        print(config)
    finally:
        print("Finished config loading attempt")


if __name__ == "__main__":
    main()
