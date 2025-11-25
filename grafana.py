import json
import sys
import copy

fh = open(sys.argv[1])
panel = json.load(fh)

# TODO: position


def buildRow(name):
    return (
        {
            "collapsed": False,
            "gridPos": {"h": 1, "w": 24, "x": 0, "y": 0},
            "id": 3,
            "panels": [],
            "title": name,
            "type": "row",
        },
    )


def buildPanel(metric, template):
    panel = copy.deepcopy(template)
    panel["title"] = metric

    expr = panel["targets"][0]["expr"]
    expr.replace("runtime_cpu_load_1", metric)
    panel["targets"][0]["expr"] = expr
    return panel
