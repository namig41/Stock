from domain.entities.batch import Batch


def convert_batch_data_to_entity(batch_data: dict) -> Batch:
    return Batch(
        reference=batch_data[0],
        sku=batch_data[1],
        eta=batch_data[2],
        _purchased_quantity=batch_data[3],
    )
