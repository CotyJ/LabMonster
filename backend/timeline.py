
def timeline_generator(action_list):
  if not action_list:
    return []
  max_frames = action_list[-1]["startFrame"] + action_list[-1]["duration"] + 1

  print("\nMax Frames:", max_frames, "\n")
  timeline = [{} for _ in range(max_frames)]

  for action in action_list:
    startFrame = action["startFrame"]
    endFrame = startFrame + action["duration"]
    timeline[startFrame][action["button"]] =  True
    timeline[endFrame][action["button"]] = False

    # Leaving these because they're useful for debugging
    # print(startFrame, timeline[startFrame])
    # print(endFrame, timeline[endFrame])

  return timeline
