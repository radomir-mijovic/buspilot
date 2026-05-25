from driver.models import DriverDocument
from vehicle.models import VehicleDocument


def count_all_in_danger_documents(request):
    if not request.user.is_authenticated:
        return {}

    vehicles_docs = (
        VehicleDocument.expiring.close_to_expire()
        .filter(
            company=request.user.company,
        )
        .count()
    )
    drivers_docs = (
        DriverDocument.expiring.close_to_expire()
        .filter(
            company=request.user.company,
        )
        .count()
    )
    return {"total_in_danger_documents": vehicles_docs + drivers_docs}


def list_in_danger_driver_documents(request):
    if not request.user.is_authenticated:
        return {}

    in_danger_documents = DriverDocument.expiring.close_to_expire().filter(
        company=request.user.company,
    )
    return {"in_danger_driver_documents": in_danger_documents}


def list_in_danger_vehicle_documents(request):
    if not request.user.is_authenticated:
        return {}

    in_danger_documents = VehicleDocument.expiring.close_to_expire().filter(
        company=request.user.company,
    )
    return {"in_danger_vehicle_documents": in_danger_documents}


def list_all_driver_expired_documents(request):
    if not request.user.is_authenticated:
        return {}

    expired_documents = DriverDocument.expiring.expired().filter(
        company=request.user.company,
    )
    return {"expired_driver_documents": expired_documents}

def list_all_vehicle_expired_documents(request):
    if not request.user.is_authenticated:
        return {}

    expired_documents = VehicleDocument.expiring.expired().filter(
        company=request.user.company,
    )
    return {"expired_vehicle_documents": expired_documents}
