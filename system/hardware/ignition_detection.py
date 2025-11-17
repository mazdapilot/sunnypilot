from cereal import log


class IgnitionDetection:
  ignition_can_seen = False

  @staticmethod
  def get_ignition_state(panda_states) -> bool:
    valid_states = [ps for ps in panda_states if ps.pandaType != log.PandaState.PandaType.unknown]
    if not valid_states:
      return False

    # Prioritize CAN-based ignition with fallback to line ignition
    if any(ps.ignitionCan for ps in valid_states):
      IgnitionDetection.ignition_can_seen = True
      return True

    return False if IgnitionDetection.ignition_can_seen else any(ps.ignitionLine for ps in valid_states)
