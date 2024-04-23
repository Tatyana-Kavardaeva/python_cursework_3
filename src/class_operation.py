from datetime import datetime


class Operation:
    def __init__(self, date, description, where_from, to, operationamount):
        self.date = date
        self.description = description
        self.where_from = where_from
        self.to = to
        self.operationamount = operationamount

    def __repr__(self):
        return f"Operation(date = '{self.date}'" \
               f"description = '{self.description}'" \
               f"self = '{self.where_from}'" \
               f"to = '{self.to}'" \
               f"operationamount = '{self.operationamount}'"

    def mask_card_number(self):
        """Принимает номер карты и возвращает замаскированную версию в формате
        XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры,
        разделенных пробелом) Пример: 7000 79** **** """
        if self.where_from:
            card_number = self.where_from.split(' ')
            i = len(card_number) - 1
            name_card = " ".join(card_number[:i])
            return f"{name_card} {card_number[-1][:4]} {card_number[-1][4:6]}** **** {card_number[-1][-4:]}"
        else:
            return ''

    def mask_account_number(self):
        """Принимает номер счета и возвращает замаскированную версию в формате  **XXXX
        (видны только последние 4 цифры номера счета) Пример: **9638"""
        account_number = self.to.split(' ')
        return f"{account_number[0]} **{account_number[1][-4:]}"

    def formatted_date(self):
        """Приводит дату операции к формату ДД.ММ.ГГГГ"""
        date = datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S.%f")
        formatted_date = date.strftime("%d.%m.%Y")
        return formatted_date

    def formatted_amount(self):
        """Возвращает сумму и валюту операции: 82771.72 руб."""
        currency = self.operationamount.get("currency")
        return f'{self.operationamount.get("amount")} {currency.get("name")}'

    def __str__(self):
        """Выводит указанное количество операций из отсортированного списка по шаблону:
           14.10.2018 Перевод организации
           Visa Platinum 7000 79** **** 6361 -> Счет **9638
           82771.72 руб."""
        formatted_date = self.formatted_date()
        masked_card_number = self.mask_card_number()
        masked_account_number = self.mask_account_number()
        return f"{formatted_date} {self.description}\n{masked_card_number} -> {masked_account_number}\n" \
               f"{self.formatted_amount()}\n"
