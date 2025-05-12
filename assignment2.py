
class Device:
    def __init__(self, device_id, model):
        self.device_id = device_id
        self.model = model

    def device_info(self):
        return f"Device ID: {self.device_id}, Model: {self.model}"


class Flyer:
    def fly(self):
        return "Drone is flying..."


class Drone(Device, Flyer):
    def __init__(self, device_id, model, camera_quality):
        Device.__init__(self, device_id, model)
        self.camera_quality = camera_quality

    def capture_image(self):
        return f"Image captured with {self.camera_quality} camera"


brone = Drone("MQ-9 Reaper", "Alpha-Pro", "8K")


print(brone.device_info())       
print(brone.fly())               
print(brone.capture_image())     