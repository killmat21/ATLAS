import ccxt
import configparser

class Exchange:
    def __init__(self, exchange_name: str, is_test: bool):
        self.name = exchange_name
        self.config_filename = "config.ini"
        self.exchange = self.set_exchange_config()
        self.exchange.set_sandbox_mode(is_test)

    def __str__(self):
        return str(self.exchange)

    def set_exchange_config(self):
        config = configparser.ConfigParser()
        if not config.read(self.config_filename) or self.name not in config.sections():
            config[self.name] = {
                "api_key": input("YOUR API KEY: "),
                "secret_key": input("YOUR SECRET KEY: "),
            }
            with open(self.config_filename, 'w') as configfile:
                config.write(configfile)
        exchange = self.init_exchange(config)
        self.check_exchange_credentials(exchange, config)
        return exchange

    def init_exchange(self, config):
        exchange_class = getattr(ccxt, self.name)
        exchange = exchange_class({
            "apiKey": config[self.name]["api_key"],
            "secret": config[self.name]["secret_key"]
        })
        return exchange

    def check_exchange_credentials(self, exchange, config):
        name = self.name
        try:
            exchange.fetchBalance()
        except:
            print(f"Your keys for {name} are incorrect.\nTry verify you correctly Copy/Paste them or to generate new keys on the {name} website.")
            config.remove_section(name)
            with open(self.config_filename, "w") as configfile:
                config.write(configfile)
            exit()

