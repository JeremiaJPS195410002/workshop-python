import json
x = [1, 'simple', 'list']
json.dumps(x)
#'[1, "simple", "list"]' (Output)

json.dump(x, f)
x = json.load(f)