from faker import Faker
from faker.providers import DynamicProvider

class CellTypes:
    def __init__(self):
        self.faker = Faker()
        self.cell_types = {
            1: "Red Blood",
            2: "Plasma",
            3: "Platelets"
        }
        
       
        cell_type_provider = DynamicProvider(
            provider_name="cell_type",
            elements=list(self.cell_types.keys())
        )
        self.faker.add_provider(cell_type_provider)

    def generate_cell_type(self):
        cell_type_key = int(self.faker.cell_type())
        return cell_type_key