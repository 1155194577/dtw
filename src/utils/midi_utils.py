import mido
import pandas as pd

def read_midi_to_df(midi_path): 
    midi = mido.MidiFile(midi_path)
    df = pd.DataFrame(midi.tracks)
    return df

def write_df_to_midi(df, midi_path): 
    midi = mido.MidiFile()
    midi.tracks.append(df)
    midi.save(midi_path)