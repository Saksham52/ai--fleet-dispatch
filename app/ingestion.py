import random
import uuid
from pydantic import BaseModel, Field

# Defining shape of our data
class CargoTask(BaseModel):
    task_id: str = Field(default_factory= lambda: str(uuid.uuid4()))
    weight_kg: float
    priority: int = Field(ge=1, le=5)
    destination_zone: str

#Building the Conveyer Belt(Mock Data Generator)
def generate_incoming_cargo(num_tasks: int = 5) -> list[CargoTask]:

    zones = ["Zone_A","Zone_B","Zone_C","Zone_D"]
    cargo_batch = []

    for _ in range(num_tasks):
        #Create new piece of cargo with random attributes
        new_cargo = CargoTask(
            weight_kg = round(random.uniform(5.0,100.0), 2),
            priority = random.randint(1,5),
            destination_zone = random.choice(zones)
        )
        cargo_batch.append(new_cargo)
    
    return cargo_batch

if __name__ == "__main__":
    print("---Simulating Incoming Cargo---")
    live_batch = generate_incoming_cargo(3)

    for cargo in live_batch:
        print(cargo.model_dump_json(indent=2))