import os
import glob
from mutagen.flac import FLAC

# The directory containing the FLAC files
flac_dir = "C:\\Users\\nombredeusuario\\downloads"

# Get a list of all the FLAC files in the flac_dir directory
flac_files = glob.glob(os.path.join(flac_dir, "*.flac"))

# Loop through the FLAC files
for flac_file_path in flac_files:
    # Load the FLAC file
    flac_file = FLAC(flac_file_path)
    
    # Remove the REPLAYGAIN_TRACK_GAIN and REPLAYGAIN_ALBUM_GAIN tags
    flac_file.pop('REPLAYGAIN_TRACK_GAIN')
    flac_file.pop('REPLAYGAIN_ALBUM_GAIN')
    flac_file.pop('REPLAYGAIN_ALBUM_PEAK')
    flac_file.pop('REPLAYGAIN_REFERENCE_LOUDNESS')
    flac_file.pop('REPLAYGAIN_TRACK_PEAK')
    flac_file.pop('WAVEFORMATEXTENSIBLE_CHANNEL_MASK')
    flac_file.pop('KKENCODER')

    # Save the changes to the FLAC file
    flac_file.save()
