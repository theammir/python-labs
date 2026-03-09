# Загальне завдання
# Написати програму, яка:
# − вводить початкові дані;
# − формує результат з застосуванням концепції ООП;
# − виводить результат роботи.
# Індивідуальні завдання
# 9) Реалізувати клас для створення та редагування записів у календарі.

import datetime
from dataclasses import dataclass
from pprint import pprint


@dataclass
class Note:
    date: datetime.date
    title: str
    content: str


class Calendar:
    def __init__(self) -> None:
        self._notes: list[Note] = []

    @property
    def notes(self) -> list[Note]:
        return self._notes

    def add_note(self, note: Note) -> None:
        self._notes.append(note)

    def get_notes_between(self, from_: datetime.date, to: datetime.date) -> list[Note]:
        result = []
        for note in self._notes:
            if from_ <= note.date <= to:
                result.append(note)
        return result

    def remove_notes_during(self, date: datetime.date) -> list[Note]:
        removed = []
        for i, note in enumerate(self._notes):
            if note.date == date:
                removed.append(note)
                self._notes.pop(i)
        return removed


# if __name__ == "__main__":
#     calendar = Calendar()
#     calendar.add_note(
#         Note(date=datetime.date(2025, 12, 12), title="My first note!", content="Test")
#     )
#     calendar.add_note(
#         Note(
#             date=datetime.date(2025, 12, 15),
#             title="My second note!",
#             content="Still rollin'",
#         )
#     )
#     calendar.add_note(
#         Note(
#             date=datetime.date(2026, 1, 1),
#             title="Happy New Year!",
#             content="Wish you all the best",
#         )
#     )
#
#     in_2025 = calendar.get_notes_between(
#         datetime.date(2025, 1, 1), datetime.date(2025, 12, 31)
#     )
#     print("My notes in 2025:")
#     pprint(in_2025, width=50)
#
#     calendar.remove_notes_during(datetime.date(2025, 12, 15))
#
#     print("\nAll my notes after removal:")
#     pprint(calendar.notes, width=50)

if __name__ == "__main__":
    cal = Calendar()
    date_str = input()
    day, month, year = date_str.split(".", 3)
    note_title = input()
    cal.add_note(Note(datetime.date(int(year), int(month), int(day)), note_title, ""))

    note = cal.notes[0]
    print(note.date.strftime("%d.%m.%Y"), note.title, note.date.day)
