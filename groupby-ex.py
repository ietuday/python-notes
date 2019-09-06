# things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "harley"),
#           ("vehicle", "speed boat"), ("vehicle", "school bus")]

# dict = {}


# def f(x): return x[0]


# for key, group in groupby(sorted(things, key=f), f):
#     dict[key] = list(group)
# dict


things = [["animal", "bear"], ["animal", "duck"], ["vehicle", "harley"], ["plant", "cactus"],
          ["vehicle", "speed boat"], ["vehicle", "school bus"]]
dic = {}


def f(x): return x[0]


for key, group in groupby(sorted(things, key=f), f):
    dic[key] = list(group)
dic
