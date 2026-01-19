const ACTIONS = {
  charge_super: [
    {startFrame: 1, button: "back", duration: 9},
    {startFrame: 10, button: "forward", duration: 1},
    {startFrame: 11, button: "back", duration: 1},
    {startFrame: 12, button: "forward", duration: 1},
    {startFrame: 12, button: "x", duration: 2},
  ],
  hadoken: [
    {startFrame: 0, button: "down", duration: 1},
    {startFrame: 1, button: "down-forward", duration: 1},
    {startFrame: 2, button: "forward", duration: 1},
    {startFrame: 3, button: "x", duration: 1},
  ],
}

export default ACTIONS;
