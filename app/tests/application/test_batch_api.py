from datetime import date
import requests 
import pytest

from application.api.batch.scheme import CreateBatchResponseScheme
from domain.entities.batch import Batch


def test_api_create_batch_request():
    batch_data = { 'reference':  'batch-001', 'sku': 'SMALL-TABLE'}
    url = 'http://127.0.0.1:8000'
    r = requests.post(f'{url}/batch', json=batch_data)
    assert r.status_code == 201
    assert r.json() == batch_data
    
    
def test_api_get_batch_request():
    reference = 'batch-001'
    url = f'http://127.0.0.1:8000/batch/{reference}'
    r = requests.get(f'{url}')
    assert r.status_code == 200
    batch = Batch(**r.json()) 
    assert batch.reference == reference