import librosa


def get_window_indecies(audio_series, window_size):
    return [window_size*i for i in range(len(audio_series) // window_size)]


def calculate_noise_or_voice_per_interval(window_intervals, sound_intervalas):
    window_sound_pertengage = {}

    for i in range(1, len(window_indecies)):
        window_start = window_intervals[i - 1]
        window_end = window_indecies[i]

        # Select all matching windows
        # TODO -> move along

        matching_intervals = []

        for j in range(len(sound_intervalas)):
            interval_start = sound_intervalas[j, 0]
            interval_end = sound_intervalas[j, 1]

            # Check if interval matches window
            if (window_start >= interval_start and window_start <= interval_end) or (
                    window_end >= interval_start and window_end <= interval_end):
                matching_intervals.append(sound_intervalas[j])

        window_overlap = 0
        for interval in matching_intervals:
            left_start_point = interval[0]
            if left_start_point < window_start:
                left_start_point = window_start

            right_start_point = interval[1]
            if right_start_point < window_end:
                right_start_point = window_end

            window_overlap = (right_start_point - left_start_point) / (interval[1] - interval[0])

        window_sound_pertengage[(window_start, window_end)] = window_overlap

    return window_sound_pertengage



#
#   Parameters:
#   - overlap_threshold - since window does not match with detected silence intervals we calculate percentage of sound in window; above threshold we mark as person speaking
#   - window_size - size of single sample length (time in seconds can be can be calculated as window_size / sampling_rate
#   - sampling_rate - for audio read from file
#   - top_db_silence_threshold - move that value in decibel sound is considered as voice no silence
#
def generate_window_is_person_map_for_audio(audio_path, overlap_threshold = 0.2, window_size = 2048, sampling_rate =44100, top_db_silence_threshold = 30):
    audio_series, sampling_rate = librosa.core.load(audio_path, sr=sampling_rate)
    # http://jamesmontgomery.us/blog/Voice_Recognition_Model.html
    splitted_series = librosa.effects.split(audio_series, top_db=top_db_silence_threshold)
    window_indecies = get_window_indecies(audio_series, window_size)
    window_overlap_percentage = calculate_noise_or_voice_per_interval(window_indecies, splitted_series)
    window_is_person_map = {window: (window_overlap_percentage[window] > overlap_threshold) for window in
                            window_overlap_percentage.keys()}

    return window_is_person_map

if __name__ =='__main__':
    generate_window_is_person_map_for_audio('k_1_1.wav')


