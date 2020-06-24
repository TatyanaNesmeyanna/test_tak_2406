import pytest
import json
import random
from datetime import datetime
from uuid import uuid4
from helpers.stores import Stores


def test_get_all_stores_with_correct_token(token):
    res=Stores.get_all_stores(token)
    assert (res.status_code == 200)
    stores = json.loads(res.content.decode('utf-8'))['data']
    k=random.randint(0, len(stores)-1)
    # checking random item
    assert 'id' in stores[k] and isinstance(stores[k]['id'], int)
    assert 'name' in stores[k] and isinstance(stores[k]['name'], str)
    assert 'address' in stores[k] and isinstance(stores[k]['address'], str)
    assert 'city_id' in stores[k] and isinstance(stores[k]['city_id'], str)
    assert 'city_name' in stores[k] and isinstance(stores[k]['city_name'], str)
    assert  stores[k]['region_id']==0
    assert 'region_name' in stores[k] and isinstance(stores[k]['region_name'], str)
    assert 'store_type_id' in stores[k] and isinstance(stores[k]['store_type_id'], str)
    assert 'store_type_name' in stores[k] and isinstance(stores[k]['store_type_name'], str)
    assert 'segment_id' in stores[k] and isinstance(stores[k]['segment_id'], str)
    assert 'external_id' in stores[k] and isinstance(stores[k]['external_id'], str)
    assert 'external_id2' in stores[k] and isinstance(stores[k]['external_id2'], str)
    assert 'territory1_id' in stores[k] and isinstance(stores[k]['territory1_id'], str)
    assert 'territory' in stores[k] and isinstance(stores[k]['territory'], str)
    assert 'retailer_id' in stores[k] and isinstance(stores[k]['retailer_id'], str)
    assert 'retailer_name' in stores[k] and isinstance(stores[k]['retailer_name'], str)
    assert stores[k]['lon'] == 0
    assert stores[k]['lat'] == 0
    assert 'category' in stores[k] and isinstance(stores[k]['category'], str)
    assert 'type' in stores[k] and isinstance(stores[k]['type'], str)
    assert 'dt_update' in stores[k] and isinstance(stores[k]['dt_update'], datetime.datetime)
    assert stores[k]['active_matrices_count'] == 0

def test_get_all_stores_with_incorrect_token():
    res=Stores.get_all_stores(uuid4())
    assert (res.status_code == 403)
    message = json.loads(res.content.decode('utf-8'))['message']
    assert  message=='Not authorized'

def test_get_all_stores_with_validation_error(token):
    res = Stores.get_sorted_stores(token,'-dates')
    assert (res.status_code == 422)


