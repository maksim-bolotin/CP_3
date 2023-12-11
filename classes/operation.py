from datetime import datetime


class Operation:
    def __init__(self, id_: int, date: str, state: str, operation_amount: dict, description: str, from_: str, to_: str):
        self.id_ = id_
        self.date = self.date_converter(date) if date else ""
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        self.from_ = self.convert_data(from_) if from_ else ""
        self.to_ = self.convert_data(to_) if to_ else ""

    def convert_data(self, card_or_account: str) -> str:
        """
        Формирование защищённого вывода информации о счетах и картах.
        """
        if card_or_account.startswith("Счет"):
            info = card_or_account.split()[1]
            return f"Счёт ****{info[-4:]}"
        elif card_or_account.startswith("Visa"):
            cart_info = " ".join(card_or_account.split()[:2])
            info = card_or_account.split()[2]
            return f"{cart_info} {info[:4]} {info[4:6]}** **** {info[-4:]}"
        elif card_or_account.startswith("Maestro") or card_or_account.startswith("MasterCard"):
            cart_info = card_or_account.split()[0]
            info = card_or_account.split()[1]
            return f"{cart_info} {info[:4]} {info[4:6]}** **** {info[-4:]}"

    def date_converter(self, date: str) -> datetime:
        """
        Конвертация строки с информацией о дате операции в понятный для python формат.
        """
        return datetime.fromisoformat(date)

    def __str__(self) -> str:
        """
        Реализация формата вывода для каждой операции.
        """
        return f"""{datetime.strftime(self.date, '%d.%m.%Y')} {self.description}
{self.from_} -> {self.to_}
{self.operation_amount['amount']} {self.operation_amount['currency']['name']}\n"""
