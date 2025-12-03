import json
import sys
import copy

name_map = {
    "grpc": "GRPC",
    "http": "HTTP",
    "mysql": "MySQL",
    "redis": "Redis",
    "runtime": "Runtime",
}

height = 7
width_list = [0, 12]


def parseMetrics(config):
    result = {}

    for line in config.readlines():
        line = line.strip("\n")
        if len(line) == 0:
            continue

        typ, name = line.split(" ")
        category = name_map[name.split("_")[0]]

        pannels = result.get(category, [])
        pannels.append({
            "name": name,
            "type": typ,
        })

        result[category] = pannels

    return result


class Grafana:
    def __init__(self, template):
        self.pannels = 0
        self.rows = 0
        self.template = template

    def get_template(self):
        panel = copy.deepcopy(self.template)
        return panel

    def adjust_pannel_num(self):
        nums = len(width_list)
        if self.pannels % nums != 0:
            self.pannels += nums - self.pannels % nums

    def get_pos(self, isRow=False):
        nums = len(width_list)
        if isRow:
            y = height * int(self.pannels / nums) + (self.rows - 1)
            return {"h": 1, "w": 24, "x": 0, "y": y}

        x = width_list[(self.pannels - 1) % nums]
        y = height * int((self.pannels - 1) / nums) + self.rows
        return {"h": height, "w": 12, "x": x, "y": y}

    def buildRow(self, name):
        self.rows += 1

        return {
            "collapsed": False,
            "gridPos": self.get_pos(isRow=True),
            "id": 3,
            "panels": [],
            "title": name,
            "type": "row",
        }

    def buildPanel(self, config):
        self.pannels += 1

        metric = config.get("name")
        typ = config.get("type")

        panel = self.get_template()
        panel["title"] = metric

        expr = """runtime_cpu_load_1{native_env=~"$native_env", app=~"$app", pod_name=~"$pod_name"}"""
        if typ == "Timer":
            expr = """rate(runtime_cpu_load_1_sum{native_env=~"$native_env", app=~"$app", pod_name=~"$pod_name"}[1m]) / rate(runtime_cpu_load_1_count{native_env=~"$native_env", app=~"$app", pod_name=~"$pod_name"}[1m])"""

        expr = expr.replace("runtime_cpu_load_1", metric)
        panel["targets"][0]["expr"] = expr

        panel["gridPos"] = self.get_pos(isRow=False)

        return panel

    def build_row(self, rowName, metrics):
        result = []
        result.append(self.buildRow(rowName))

        for m in metrics:
            panel = self.buildPanel(m)
            result.append(panel)

        return result

    def build(self, config):
        result = []

        # ("GRPC", "HTTP", "Redis", "MySQL", "Runtime")
        for rowName, metrics in config.items():
            if rowName != "GRPC":
                continue
            self.adjust_pannel_num()
            row = self.build_row(rowName, metrics)
            result.extend(row)

        return result

    def merge_dashboard(self, dashboards):
        result = []
        for dash in dashboards:
            self.adjust_pannel_num()

            pannels = dash.get("panels", [])
            if len(pannels) <= 0:
                continue

            self.rows += 1
            row = pannels[0]
            row["gridPos"] = self.get_pos(isRow=True)
            result.append(row)

            for pan in pannels[1:]:
                self.pannels += 1
                pan["gridPos"] = self.get_pos(isRow=False)
                result.append(pan)

        return result


def merge_pannels(file):
    dashboards = []
    fh = open(file)
    for line in fh.readlines():
        line = line.strip("\n")
        if len(line) <= 0:
            continue

        dash = json.loads(line)
        dashboards.append(dash)

    return dashboards


template = json.load(open("grafana/template/panel.json"))

config = parseMetrics(open("grafana/template/metric.txt"))
# dashboards = merge_pannels(sys.argv[2])

g = Grafana(template)
result = g.build(config)

# result = g.merge_dashboard(dashboards)

print(json.dumps(result))
