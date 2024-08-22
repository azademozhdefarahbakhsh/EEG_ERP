from eeg_analysis.data_loader import load_eeg_data
from eeg_analysis.event_processor import parse_event_markers, process_events
from eeg_analysis.utils import list_vhdr_files

directory = "/path/to/eeg/files"
files = list_vhdr_files(directory)

for file_path in files:
    raw = load_eeg_data(file_path)
    events = parse_event_markers(raw)
    processed_events = process_events(events)
    print(processed_events)
