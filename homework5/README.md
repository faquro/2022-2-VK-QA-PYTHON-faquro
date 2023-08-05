## Домашнее задание №5

---

Cкрипты на **bash** и **python** для анализа готового **access.log**

### Bash-скрипт

Скрипт может принимать на вход 2 аргумента:
- Файл с логами (**Обязательный аргумент**)
- Название выходного файла с результатами (Необязательный аргумент, по умолчанию название "**result.txt**")


Пример запуска из терминала:

```
bash script.sh access.log result_07.11.22.txt
```

### Python-скрипт

Скрипт может принимать на вход 2 аргумента:
- Файл с логами (**Обязательный аргумент**)
- Название выходного **JSON** файла с результатами (**Необязательный аргумент**)

**Вывод результатов осуществляется в терминал.**

Пример запуска из терминала:

```
python3 pyscript.py -f access.log
```

Если нужно сохранить результаты в файл, для этого можно воспользоваться перенаправлением вывода в терминале:

```
python3 pyscript.py -f access.log > result.txt
```

Для сохранения результатов в JSON файл, необходимо указать аргумент -j (--json) и название файла.

```
python3 pyscript.py -f access.log -j result.json
```