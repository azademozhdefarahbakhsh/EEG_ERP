import numpy as np

def parse_event_markers(raw):
    """
    Parse event markers from the raw EEG data.
    
    Parameters:
        raw (mne.io.Raw): The raw EEG data.
    
    Returns:
        events (ndarray): Array of events.
    """
    events = mne.find_events(raw)
    return events

def process_events(events):
    """
    Process the events to identify specific conditions.
    
    Parameters:
        events (ndarray): Array of events.
    
    Returns:
        processed_events (dict): Dictionary with processed events.
    """
    # Example: Filter events by a certain condition
    processed_events = {}
    for event in events:
        if event[2] == 10:
            processed_events['stimOnset_Cong'] = event
        elif event[2] == 20:
            processed_events['stimOnset_InCong'] = event
    return processed_events
