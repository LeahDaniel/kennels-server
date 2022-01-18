class Animal():

    def __init__(self, id,  name,  status, breed, customer_id, location_id):
        self.id = id
        self.name = name
        self.status = status
        self.breed = breed
        self.customer_id = customer_id
        self.location_id = location_id
        self.location = None
        self.customer = None
