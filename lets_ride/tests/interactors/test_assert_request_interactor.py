import datetime
from unittest.mock import create_autospec
from lets_ride.interactors.storages.storage_interface \
    import StorageInterface
from lets_ride.interactors.asset_request_interactor \
    import AssertRequestInteractor

def test_asset_request_wrapper():
    # Arrange
    user_id =  1
    source = "kurnool"
    destination = "Hyderabad"
    travel_date_time = "2020-04-12 05:30 PM"
    datetime_obj = datetime.datetime(2020, 4, 12, 17, 30)
    flexible_timings = False
    flexible_from_date_time = ""
    flexible_to_date_time = ""
    asset_type = "LAPTOP"
    asset_quantity = 3
    asset_type_others = ""
    asset_sensitivity = "LOW"
    deliver_to = "User1"
    phone_number = "2142353246"
    storage = create_autospec(StorageInterface)
    interactor = AssertRequestInteractor(storage=storage)

    # Assert
    interactor.asset_request_wrapper(
        user_id=user_id,
        source=source,
        destination=destination,
        travel_date_time=travel_date_time,
        flexible_timings=flexible_timings,
        flexible_travel_from_date_time=flexible_from_date_time,
        flexible_travel_to_date_time=flexible_to_date_time,
        asset_type=asset_type,
        asset_quantity=asset_quantity,
        asset_type_others=asset_type_others,
        asset_sensitivity=asset_sensitivity,
        deliver_to=deliver_to,
        phone_number=phone_number
    )

    # Act
    storage.create_asset_request.assert_called_once_with(
        user_id=user_id,
        source=source,
        destination=destination,
        travel_date_time=datetime_obj,
        flexible_timings=flexible_timings,
        asset_type=asset_type,
        asset_quantity=asset_quantity,
        asset_type_others=asset_type_others,
        asset_sensitivity=asset_sensitivity,
        deliver_to=deliver_to,
        phone_number=phone_number
    )

def test_asset_request_wrapper_with_flexible_timings():
    # Arrange
    user_id =  1
    source = "kurnool"
    destination = "Hyderabad"
    travel_date_time = "2020-04-12 05:30 PM"
    from_datetime_obj = datetime.datetime(2020, 4, 12, 17, 30)
    to_datetime_obj = datetime.datetime(2020, 4, 12, 19, 30)
    flexible_timings = True
    flexible_from_date_time = "2020-04-12 05:30 PM"
    flexible_to_date_time = "2020-04-12 07:30 PM"
    asset_type = "LAPTOP"
    asset_quantity = 3
    asset_type_others = ""
    asset_sensitivity = "LOW"
    deliver_to = "User1"
    phone_number = "2142353246"
    storage = create_autospec(StorageInterface)
    interactor = AssertRequestInteractor(storage=storage)

    # Assert
    interactor.asset_request_wrapper(
        user_id=user_id,
        source=source,
        destination=destination,
        travel_date_time=travel_date_time,
        flexible_timings=flexible_timings,
        flexible_travel_from_date_time=flexible_from_date_time,
        flexible_travel_to_date_time=flexible_to_date_time,
        asset_type=asset_type,
        asset_quantity=asset_quantity,
        asset_type_others=asset_type_others,
        asset_sensitivity=asset_sensitivity,
        deliver_to=deliver_to,
        phone_number=phone_number
    )

    # Act
    storage.create_asset_request_with_flexible_timings.assert_called_once_with(
        user_id=user_id,
        source=source,
        destination=destination,
        flexible_timings=flexible_timings,
        flexible_travel_from_date_time=from_datetime_obj,
        flexible_travel_to_date_time=to_datetime_obj,
        asset_type=asset_type,
        asset_quantity=asset_quantity,
        asset_type_others=asset_type_others,
        asset_sensitivity=asset_sensitivity,
        deliver_to=deliver_to,
        phone_number=phone_number
    )
