from datetime import datetime


class Operation:
    def __init__(self, pk: int, date: str, state: str, operation_amount: dict, description: str, from_: str, to_: str):
        self.pk = pk
        self.date = self.date_converter(date)
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = self.convert_data(from_) if from_ else ""
        self.to_ = self.convert_data(to_) if from_ else ""

    def convert_data(self, card_or_account: str) -> str:
        if card_or_account.startswith("Счет"):
            info = card_or_account.split()[1]
            return f"****{info[:4]}"
        else:
            info = card_or_account.split()[1]
            return f"{info[:4]} {info[5:7]}** **** {info[-4:]}"
            # return info[:5]

    def date_converter(self, date: str) -> datetime:
        return datetime.fromisoformat(date)
