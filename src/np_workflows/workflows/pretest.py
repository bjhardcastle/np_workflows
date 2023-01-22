try:
    # the wse allows import errors to pass silently, which we don't want: put all
    # imports in this try block so that we can see the error and exit
    import datetime
    import time
    import pdb
    from typing import Type

    from np_workflows.experiments.baseclasses import Experiment
    import np_workflows.experiments.classes as classes
    from np_workflows.workflows.shared import npxc
    
    from np_workflows.workflows.shared.initialize import (
        select_mouse_and_operator_enter, 
        select_mouse_and_operator_input,
        select_experiment_enter, 
        select_experiment_input,
        experiment,
        )

except ImportError as exc:
    print(repr(exc))
    import pdb; pdb.set_trace()
    quit()
    

def msg_enter(state_globals) -> None: 
    state_globals["external"]["transition_result"] = False # T/F just sets text at bottom green/red - switches to T in next state
    state_globals["external"]["status_message"] = 'status_message at bottom'
    state_globals["external"]["msg_text"] = 'msg_text in main widget'
    state_globals['external']['alert'] = True # T adds warning icon 
    # state_globals["external"]["next_state"] = 'warn' # sets next state by name
# def msg_input(state_globals) -> None: ... 
# def msg_exit(state_globals) -> None: ...
# def warn_enter(state_globals) -> None: ...
# def warn_input(state_globals) -> None: ...
# def workflow_complete_enter(state_globals) -> None: ...
# def workflow_complete_input(state_globals) -> None: ...
# def workflow_complete_exit(state_globals) -> None: ...