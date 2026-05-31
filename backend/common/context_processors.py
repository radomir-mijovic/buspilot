from driver.models import DriverDocument
from vehicle.models import VehicleDocument


def list_in_danger_driver_documents(request):
    if not request.user.is_authenticated:
        return {}

    in_danger_documents = (
        DriverDocument.expiring.close_to_expire()
        .filter(
            company=request.user.company,
        )
        .select_related("driver")
    )
    return {"in_danger_driver_documents": in_danger_documents}


def list_in_danger_vehicle_documents(request):
    if not request.user.is_authenticated:
        return {}

    in_danger_documents = (
        VehicleDocument.expiring.close_to_expire()
        .filter(
            company=request.user.company,
        )
        .select_related("vehicle")
    )
    return {"in_danger_vehicle_documents": in_danger_documents}


def list_all_driver_expired_documents(request):
    if not request.user.is_authenticated:
        return {}

    expired_documents = (
        DriverDocument.expiring.expired()
        .filter(
            company=request.user.company,
        )
        .select_related("driver")
    )
    return {"expired_driver_documents": expired_documents}


def list_all_vehicle_expired_documents(request):
    if not request.user.is_authenticated:
        return {}

    expired_documents = (
        VehicleDocument.expiring.expired()
        .filter(
            company=request.user.company,
        )
        .select_related("vehicle")
    )
    return {"expired_vehicle_documents": expired_documents}
