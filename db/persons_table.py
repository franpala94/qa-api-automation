import boto3
from botocore.exceptions import ClientError
import logging

# Configuración básica del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PersonsTable:

    def __init__(self, region_name="us-east-1"):
        """
        Inicializa el recurso de DynamoDB.
        Se asume que las credenciales y configuración de AWS están resueltas por entorno o perfil.
        """
        self.dynamodb = boto3.resource("dynamodb", region_name=region_name)
        self.table_name = "Persons"
        self.table = self.dynamodb.Table(self.table_name)
        logger.info("Conectado a la BD")

    def get_person(self, person_id: int):
        """
        Simula la consulta:
        SELECT DISTINCT * FROM Test.Worldsys WHERE personId = <person_id>
        usando get_item en DynamoDB.
        """
        try:
            response = self.table.get_item(Key={"personId": person_id})
            item = response.get("Item")
            if item:
                logger.info("Item encontrado")
                return item
            else:
                logger.warning("No se encontro el item")
                return None
        except ClientError as e:
            logger.error(f"Error al acceder a DynamoDB: {e.response['Error']['Message']}")
            return None