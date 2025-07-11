import mido
import pandas as pd

def read_midi_to_df(midi_path): 
    midi = mido.MidiFile(midi_path)
    df = pd.DataFrame(midi.tracks)
    return df
