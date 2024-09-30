from dataclasses import dataclass
import sqlite3
from domain.entities.batch import Batch
from infrastructure.exceptions.repository import BatchNotFoundInDataBase
from infrastructure.repository.base import BaseRepository
from infrastructure.repository.converter import convert_batch_data

@dataclass
class SQLiteBatchRepository(BaseRepository):
    
    db_path: str
    
    def __post_init__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.execute('''
                                CREATE TABLE IF NOT EXISTS batches (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    reference TEXT,
                                    sku TEXT,
                                    _purchased_quantity INTEGER NOT NULL,
                                    eta TEXT
                                );
                               ''')
        
        self.connection.execute(
                                '''
                                CREATE TABLE IF NOT EXISTS order_lines (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        sku TEXT,
                                        qty INTEGER,
                                        orderid TEXT
                                    )
                                ''')                         
    
    def add_batch(self, batch: Batch):
        with self.connection:
            self.connection.execute(
                '''
                INSERT INTO batches (reference, sku, _purchased_quantity, eta) VALUES (?, ?, ?, ?)
                ''',
                (batch.reference, batch.sku, batch._purchased_quantity, batch.eta)
            )
    
    def get_batch(self, reference: str) -> Batch:
        cursor = self.connection.execute(
                '''
                SELECT reference, sku, _purchased_quantity, eta FROM batches WHERE reference = ?
                ''',
                (reference, )
            )
        if batch_data := cursor.fetchone():
            return convert_batch_data(batch_data)
        
        raise BatchNotFoundInDataBase()

    def __del__(self):
        self.connection.close()
