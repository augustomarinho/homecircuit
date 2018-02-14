from container import app
import logging

logger = logging.getLogger(__name__)

logger.info('Servidor HomeCircuit iniciando')
app.run(debug=True)
