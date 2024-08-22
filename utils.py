import os

def list_vhdr_files(directory):
    """
    List all .vhdr files in a directory.
    
    Parameters:
        directory (str): Path to the directory.
    
    Returns:
        list of str: List of .vhdr file paths.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.vhdr')]
