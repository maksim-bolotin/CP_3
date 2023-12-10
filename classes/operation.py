class Operation:
    def __init__(self, pk: int, date: str, state: str, operation_amount: dict, description: str, from_: str, to_: str):
        self.pk = pk
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = from_
        self.to_ = to_
