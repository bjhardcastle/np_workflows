try:
    #! the wse allows import errors to pass silently!
    #* put all imports in this try block so that we can see the error before exiting
    
    import datetime
    import time
    import pdb
    from typing import Type

    from np_workflows.workflows.shared.npxc import experiment
    from np_workflows.workflows.shared import npxc
    from np_workflows.workflows.shared.initialize import (
        select_mouse_and_operator_enter, 
        select_mouse_and_operator_input,
        select_experiment_enter, 
        select_experiment_input,
        )
    from np_workflows.workflows.shared.photodoc import (
        capture_photodoc_input,
        review_photodoc_enter,
    )
    from np_workflows.workflows.shared.pretest import (
        run_pretest_input,
    )
    
except Exception as exc:
    print(repr(exc))
    import pdb; pdb.set_trace()
    exit()

# name each photodoc state `capture_photodoc_<state>`, `review_photodoc_<state>`
photodoc_states_to_labels = {
    0: 'pretest',
    }
for state, label in photodoc_states_to_labels.items():
    exec(
        f"""def capture_photodoc_{state}_enter(state_globals):
            npxc.set(state_globals, photodoc_label='{label}')
        """
    )
    exec(
        f"""def capture_photodoc_{state}_input(state_globals):
            capture_photodoc_input(state_globals)
        """
    )
    exec(
        f"""def review_photodoc_{state}_enter(state_globals):
            review_photodoc_enter(state_globals)
        """
    )
    
if False:
    def msg_enter(state_globals) -> None: 
        state_globals["external"]["transition_result"] = False # T/F just sets text at bottom green/red - switches to T in next state
        state_globals["external"]["status_message"] = 'status_message at bottom'
        state_globals["external"]["msg_text"] = 'msg_text in main widget'
        state_globals['external']['alert'] = True # T adds warning icon 
