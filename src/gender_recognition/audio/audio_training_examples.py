import librosa


def get_window_indecies(audio_series, window_size):
    oko =  [window_size*i for i in range(len(audio_series) // window_size)]
    return [window_size*i for i in range(len(audio_series) // window_size)]


def calculate_noise_or_voice_per_interval(window_intervals, sound_intervalas):
    window_sound_pertengage = {}

    for i in range(1, len(window_intervals)):
        window_start = window_intervals[i - 1]
        window_end = window_intervals[i]

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


class AudioSampleGenerator:

    #
    #   Parameters:
    #   - overlap_threshold - since window does not match with detected silence intervals we calculate percentage of sound in window; above threshold we mark as person speaking
    #   - window_size - size of single sample length (time in seconds can be can be calculated as window_size / sampling_rate
    #   - sampling_rate - for audio read from file
    #   - top_db_silence_threshold - move that value in decibel sound is considered as voice no silence
    #
    def __init__(self,overlap_threshold = 0.2, window_size = 2048, sampling_rate =44100, top_db_silence_threshold = 30) -> None:
        super().__init__()
        self.overlap_threshold = overlap_threshold
        self.window_size = window_size
        self.sampling_rate = sampling_rate
        self.top_db_silence_threshold = top_db_silence_threshold


    def generate_audio_window_is_person_pairs_for_audio(self, audio_path):
        audio_series, sampling_rate = librosa.core.load(audio_path, sr=self.sampling_rate)
        # http://jamesmontgomery.us/blog/Voice_Recognition_Model.html
        splitted_series = librosa.effects.split(audio_series, top_db=self.top_db_silence_threshold)
        window_indecies = get_window_indecies(audio_series, self.window_size)
        window_overlap_percentage = calculate_noise_or_voice_per_interval(window_indecies, splitted_series)
        window_is_person_map = {window: (window_overlap_percentage[window] > self.overlap_threshold) for window in
                                window_overlap_percentage.keys()}

        

        return self.generate_window_samples_is_person_map(audio_series, window_is_person_map), sampling_rate

    def generate_window_samples_is_person_map(self, audio_samples, window_is_person_map):
        return [ (audio_samples[window[0]:window[1]], window_is_person_map[window] )for window in window_is_person_map]


if __name__ =='__main__':
    window_is_person_pairs, sampling_rate = AudioSampleGenerator().generate_audio_window_is_person_pairs_for_audio('k_1_1.wav')
    print(len(window_is_person_pairs))


