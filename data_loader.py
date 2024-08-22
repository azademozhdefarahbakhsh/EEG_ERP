import mne

def load_eeg_data(file_path):
    """
    Load EEG data from a .vhdr file using MNE.
    
    Parameters:
        file_path (str): Path to the .vhdr file.
    
    Returns:
        raw (mne.io.Raw): The raw EEG data.
    """
    raw = mne.io.read_raw_brainvision(file_path, preload=True)
    return raw
