import os
import sys
import pyperclip
import rich
import rich.tree
from colorclass import Color
from terminaltables import SingleTable

from database import *

os.system("clear")
help_tree = rich.tree.Tree("[green]Доступные команды", style="bold")
help_tree.add("show_history - показать историю буфера обмена")
help_tree.add("copy № - скопировать запись истории")
help_tree.add("clear - очистить вывод")
help_tree.add("clear_history - очистить историю")
help_tree.add("help - помощь")
help_tree.add("exit - выйти")
rich.print(help_tree)
while True:
    try:
        rich.print("[bold green]>>> ", end="")
        command = input(Color("{green}")).lower()
        if command.startswith("show_history"):
            history = get_records()
            try:
                if " " in command:
                    N = int(command.split(" ")[-1])
                else:
                    N = len(history)
            except:
                N = len(history)
            print(Color("{/green}{cyan}"), end="")
            table = [[Color("№"), Color("Дата"), Color("Значение")]]
            for i in range(N):
                record = history[-i-1]
                if len(record['data']) > 35:
                    data = ""
                    for x in range(35):
                        data += record['data'][x]
                    data += "..."
                else:
                    data = record['data']
                table.append([record['id'], record['date'], data])

            table_instance = SingleTable(table, Color('Clipboard History'))
            table_instance.inner_heading_row_border = False
            table_instance.inner_row_border = True
            table_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center'}
            print(table_instance.table + Color("{/cyan}"))
        elif command == "clear_history":
            clear_history()
            rich.print("[bold green]История буфера обмена очищена ☑️")
        elif command.startswith("copy"):
            if " " in command:
                try:
                    record_id = command.split(" ")[-1]
                    data = get_record(record_id)['data']
                    pyperclip.copy(data)
                    rich.print("[bold green]Значение скопировано ☑️")
                except:
                    rich.print("[bold red]Использовать: copy №")
            else:
                rich.print("[bold red]Использовать: copy №")
        elif command == "exit":
            os.system("clear")
            sys.exit()
        elif command == "clear":
            os.system("clear")
        elif command == "help":
            help_tree = rich.tree.Tree("[green]Доступные команды", style="bold")
            help_tree.add("show_history (кол-во записей) - показать историю буфера обмена")
            help_tree.add("copy № - скопировать запись истории")
            help_tree.add("clear - очистить вывод")
            help_tree.add("clear_history - очистить историю")
            help_tree.add("help - помощь")
            help_tree.add("exit - выйти")
            rich.print(help_tree)
        else:
            rich.print("[bold red]‼️ Команда нераспознана!")
    except Exception as e:
        os.system("clear")
        rich.print(f"[bold red]‼️ Произошла ошибка в работе ({e})")
        sys.exit()
    except:
        os.system("clear")
        rich.print(f"[bold red]‼️ Вы вышли из менеджера!")
        sys.exit()
