actions = [
    {"startFrame": 0,  "button": "back",    "holdFor": 30},
    {"startFrame": 32, "button": "forward", "holdFor": 1},
    {"startFrame": 32, "button": "y",        "holdFor": 1},
    {"startFrame": 33, "button": "back",    "holdFor": 1},
    {"startFrame": 34, "button": "forward", "holdFor": 1},
    {"startFrame": 34, "button": "x",       "holdFor": 1},
  ]

def timeline_generator(action_list):
  # count up to last item start frame and iterate upwards and make new list
  max_frames = action_list[-1]["startFrame"] + action_list[-1]["holdFor"]
  timeline = [{} for _ in range(max_frames)]

  for i in range(max_frames):
    for action in action_list:
      if action["startFrame"] == i:
        timeline[i]["button"] = action
        print(action["button"])
      else:
        print(i)
    timeline[i]

  print(timeline)
  # return timeline


timeline_generator(actions)


# goal data shape

data = [
  {"back": True}, # x30
  {"back": False, "forward": True}, # 31
  {"back": True, "forward": False, "y": True},  # 32
  {"back": False, "forward": True, "y": False},  # 33
  {"back": False, "forward": True, "x": True},  # 34
  # probably a helper function to unpress all buttons pressed
  {"back": False, "forward": False, "x": False},  # 35
]
