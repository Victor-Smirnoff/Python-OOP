class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = [arg for arg in args]

    def get_config(self):
        mem_str = "; ".join([f"{x.name} - {x.volume}" for x in self.mem_slots])

        return [f"Материнская плата: {self.name}",
                f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
                f"Слотов памяти: {self.total_mem_slots}",
                f"Память: {mem_str}"]


mb = MotherBoard("Intel", CPU("Intel", 2100), Memory("King", 4000), Memory("King", 8000))
