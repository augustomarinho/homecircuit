from flask import Flask
import logging.config
import os
import yaml

app = Flask(__name__, static_folder='../static', template_folder='../templates')

from routes import routes


def setup_logging(
    default_path='/home/augustomarinho/dev/workspace_python/homecircuit/logconfig.yml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

setup_logging()
