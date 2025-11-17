from cereal import log


ignition_can_seen = False

def get_ignition_state(panda_states) -> bool:
  global ignition_can_seen

  valid_states = [ps for ps in panda_states if ps.pandaType != log.PandaState.PandaType.unknown]
  if not valid_states:
    return False

  # Prefer CAN ignition once seen, fall back to line ignition if all attached pandas lack it.
  if any(ps.ignitionCan for ps in valid_states):
    ignition_can_seen = True
    return True

  return False if ignition_can_seen else any(ps.ignitionLine for ps in valid_states)
