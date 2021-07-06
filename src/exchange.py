import ccxt
import configparser


class Exchange:
    def __init__(self, is_test: bool):
        self.name = "binance"
        self.test = is_test
        self.config_filename = "config.ini"
        self.exchange = self.set_exchange_config()

    def __str__(self):
        return str(self.exchange)

    def set_exchange_config(self):
        config = configparser.ConfigParser()
        section_name = f"test-{self.name}" if self.test else self.name
        if (
            not config.read(self.config_filename)
            or section_name not in config.sections()
        ):
            config[section_name] = {
                "api_key": input("YOUR API KEY: "),
                "secret_key": input("YOUR SECRET KEY: "),
            }
            with open(self.config_filename, "w") as configfile:
                config.write(configfile)
        exchange = self.init_exchange(config, section_name)
        self.check_exchange_credentials(exchange, config, section_name)
        return exchange

    def init_exchange(self, config, section_name):
        exchange_class = getattr(ccxt, self.name)
        exchange = exchange_class(
            {
                "apiKey": config[section_name]["api_key"],
                "secret": config[section_name]["secret_key"],
            }
        )
        exchange.set_sandbox_mode(self.test)
        return exchange

    def check_exchange_credentials(self, exchange, config, section_name):
        try:
            exchange.fetchBalance()
        except:
            print(
                f"Your keys for {section_name} are incorrect.\nTry verify you correctly Copy/Paste them or to generate new keys on the {section_name} website."
            )
            config.remove_section(section_name)
            with open(self.config_filename, "w") as configfile:
                config.write(configfile)
            exit()
