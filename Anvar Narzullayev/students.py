from rich.console import Console
from rich.table import Table

console = Console()
table = Table(show_header=True, header_style="bold blue", show_lines=True)  # show_lines=True

# Jadval ustunlarini qo'shish
table.add_column("Nomlari")
table.add_column("Narxi")
table.add_column("Miqdori")

# Satrlarga shart qo'yish
items = [
    ("Olma", "10 000 so'm", "5 kg"),
    ("Banan", "20 000 so'm", "3 kg"),
    ("Uzum", "15 000 so'm", "4 kg")
]

# Har bir satrni qo'shish
for item in items:
    table.add_row(item[0], item[1], item[2])

# Jadvalni chiqarish
console.print(table)
