from container import app
import logging

logger = logging.getLogger(__name__)

logger.info('Servidor HomeCircuit no ar')


app.run(debug=True)
