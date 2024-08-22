# EEG Analysis Package

This repository contains code for loading and processing EEG data.

## Structure

- `data_loader.py`: Functions to load EEG data.
- `event_processor.py`: Functions to parse and process event markers.
- `utils.py`: Utility functions.

## Usage

```python
from eeg_analysis.data_loader import load_eeg_data
from eeg_analysis.event_processor import parse_event_markers, process_events

# Load and process EEG data
raw = load_eeg_data('/path/to/file.vhdr')
events = parse_event_markers(raw)
processed_events = process_events(events)
