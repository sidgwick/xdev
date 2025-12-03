import json
import sys
import copy

fh = open(sys.argv[1])
panel = json.load(fh)

# TODO: position


height = 7
width_list = [0, 6, 12, 18]

# x = w
# y = A * h


def buildRow(name):
    return {
        "collapsed": False,
        "gridPos": {"h": 1, "w": 24, "x": 0, "y": 0},
        "id": 3,
        "panels": [],
        "title": name,
        "type": "row",
    }


def buildPanel(metric, template, index):
    panel = copy.deepcopy(template)
    panel["title"] = metric

    expr = panel["targets"][0]["expr"]
    expr.replace("runtime_cpu_load_1", metric)
    panel["targets"][0]["expr"] = expr

    gridPos = panel["gridPos"]
    gridPos["x"] = width_list[index % 4]
    gridPos["y"] = height * int(index / 4)
    panel["gridPos"] = gridPos

    return panel


metrics = [
    "runtime_cpu_load_1",
    "runtime_cpu_load_15",
    "runtime_cpu_load_5",
    "runtime_cpu_total",
    "runtime_cpu_usage_percent",
    "runtime_gc_num",
    "runtime_gc_pause_total",
    "runtime_goroutine_num",
    "runtime_mem_alloc",
    "runtime_mem_heap_alloc",
    "runtime_mem_heap_object_num",
    "runtime_mem_system_alloc",
    "runtime_mem_total",
    "runtime_mem_usage_percent",
]

result = []

result.append(buildRow("Runtime"))

for idx, m in enumerate(metrics):
    panel = buildPanel(m, panel, idx)
    result.append(panel)

print(json.dumps(result))
