import uuid
import random

class MedDatabase:
    def __init__(self):
        # مراكز افتراضية موزعة جغرافياً لحين تعديلها من لوحة التحكم
        self.centers = {
            "C01": {"name": "مركز دمشق المركزي", "lat": 33.5138, "lon": 36.2765, "active": True},
            "C02": {"name": "مركز حلب العملياتي", "lat": 36.2021, "lon": 37.1343, "active": True},
            "C03": {"name": "مركز حمص الطارئ", "lat": 34.7324, "lon": 36.7137, "active": True}
        }
        self.reports = {}

    def add_center(self, name, lat, lon):
        center_id = f"C{random.randint(10,99)}"
        self.centers[center_id] = {"name": name, "lat": lat, "lon": lon, "active": True}
        return center_id

    def delete_center(self, center_id):
        if center_id in self.centers:
            del self.centers[center_id]
            return True
        return False
