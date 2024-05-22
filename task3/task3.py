#task3
import sys, json

def add_values(tests: list, values: list) -> list: # функция добавления значения по ключу "value"
    for i in range(len(tests)):
        for j in range(len(values)):
            if tests[i]["id"] == values[j]["id"]:
                tests[i]["value"] = values[j]["value"]
        if "values" in tests[i]:
            add_values(tests[i]["values"], values)
    return tests

# получение данных из tests.json и values.json
with open(sys.argv[1]) as v:
    values_lst_of_dicts = json.load(v)["values"]

with open(sys.argv[2]) as t:
    tests_lst_of_dicts = json.load(t)["tests"]

#добавление значений по ключу "value"
report_py = {}
report_py["tests"] = add_values(tests_lst_of_dicts, values_lst_of_dicts)

#запись в report.json
with open(sys.argv[3], "w+") as r:
    json.dump(report_py, r, indent=2)
