from src.utils.midi_utils import read_midi_to_df
import os
DATA_DIR = "./data/input"
def extract_audio_features(audio_path):
        """Extract features from audio file"""
        pass

def extract_midi_features(midi_path):
        """Extract features from MIDI file"""
        # TODO: Implement MIDI feature extraction
        pass
    
def compute_cost_matrix(midi_features, audio_features):
        """Compute cost matrix between two feature sets"""
        # TODO: Implement cost matrix computation
        pass

def compute_dtw_warping_path(cost_matrix):
        """Compute DTW warping path from cost matrix"""
        # TODO: Implement DTW warping path computation
        pass

def align_midi_with_warping_path(midi_df, warping_path):
        """Align MIDI file using warping path"""
        # TODO: Align MIDI using warping path
        pass

def clean_aligned_midi(aligned_midi_df):
        """Clean aligned MIDI file"""
        # TODO: Clean aligned MIDI file
        pass

def clean_midi(midi_df):
        """Clean MIDI file"""
        # TODO: Implement MIDI cleaning
        pass

def evaluate_alignment_accuracy(reference_df, aligned_df):
        """Evaluate alignment accuracy"""
        # TODO: Evaluate alignment accuracy
        pass

def main():
    midi_path = os.path.join(DATA_DIR, "complicated.mid")  
    audio_path = os.path.join(DATA_DIR, "complicated.m4a")

    midi_features = extract_midi_features(midi_path)
    # audio_features = extract_audio_features(audio_path)
    # cost_matrix = compute_cost_matrix(midi_features, audio_features)
    # warping_path = compute_dtw_warping_path(cost_matrix)
    # midi_df = read_midi_to_df(midi_path) 
    # aligned_midi_df = align_midi_with_warping_path(midi_df, warping_path)
    # cleaned_aligned_midi_df = clean_aligned_midi(aligned_midi_df)
    # cleaned_midi_df = clean_midi(midi_df)
    # accuracy = evaluate_alignment_accuracy(midi_df, cleaned_aligned_midi_df)

if __name__ == "__main__":
    main()