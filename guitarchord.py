import tkinter as tk

# define dictionarys of strings w/ frets and their notes
low_e_string = {
    0:'E',1:'F',2:'F#',3:'G',4:'G#',5:'A',
    6:'A#',7:'B',8:'C',9:"C#",10:'D',11:'D#',
    12:'E',13:'F',14:'F#',15:'G'
}

low_d_string = {
    0:'D',1:'D#',2:'E',3:'F',4:'F#',5:'G',
    6:'G#',7:'A',8:'A#',9:'B',10:'C',11:'C#',
    12:'D',13:'D#',14:'E',15:'F'
}

a_string = {
    0: 'A', 1: 'A#', 2: 'B', 3: 'C', 4: 'C#', 5: 'D',
    6: 'D#', 7: 'E', 8: 'F', 9: 'F#', 10: 'G', 11: 'G#',
    12: 'A', 13: 'A#', 14: 'B', 15: 'C'
}
d_string = {
    0: 'D', 1: 'D#', 2: 'E', 3: 'F', 4: 'F#', 5: 'G',
    6: 'G#', 7: 'A', 8: 'A#', 9: 'B', 10: 'C', 11: 'C#',
    12: 'D', 13: 'D#', 14: 'E', 15: 'F'
}
g_string = {
    0: 'G', 1: 'G#', 2: 'A', 3: 'A#', 4: 'B', 5: 'C',
    6: 'C#', 7: 'D', 8: 'D#', 9: 'E', 10: 'F', 11: 'F#',
    12: 'G', 13: 'G#', 14: 'A', 15: 'A#'
}
b_string = {
    0: 'B', 1: 'C', 2: 'C#', 3: 'D', 4: 'D#', 5: 'E',
    6: 'F', 7: 'F#', 8: 'G', 9: 'G#', 10: 'A', 11: 'A#',
    12: 'B', 13: 'C', 14: 'C#', 15: 'D'
}
high_e_string = {
    0: 'E', 1: 'F', 2: 'F#', 3: 'G', 4: 'G#', 5: 'A',
    6: 'A#', 7: 'B', 8: 'C', 9: 'C#', 10: 'D', 11: 'D#',
    12: 'E', 13: 'F', 14: 'F#', 15: 'G'
}

fret_maps = {                   # Standard Tuning
    'E_high':   high_e_string,
    'B':        b_string,
    'G':        g_string,
    'D':        d_string,
    'A':        a_string,
    'E_low':    low_e_string
}

fret_maps_drop_d = {
    'E_high':   high_e_string,
    'B':        b_string,
    'G':        g_string,
    'D':        d_string,
    'A':        a_string,
    'D_low':    low_d_string
}

flat_conversion = {                
        'C':'C', 'C#':'D♭', 'D':'D', 
        'D#':'E♭', 'E':'E', 'F':'F',
        'F#':'G♭', 'G':'G', 'G#':'A♭',
        'A':'A', 'A#':'B♭', 'B':'B',
        }

def convert_notes_to_flat(notes): #this function replaces notes with their flat enharmonic equivalents
    return [flat_conversion.get(note, note) for note in notes]

def convert_chord_name_to_flats(chord_name):
    if chord_name in ("No notes", "No Match"):
        return chord_name
    if len(chord_name) >= 2 and chord_name[1] == '#':
        root_sharp = chord_name[:2]
        suffix = chord_name[2:]
    else:
        root_sharp = chord_name[0]
        suffix = chord_name[1:]
    flat_root = flat_conversion.get(root_sharp, root_sharp)
    return flat_root + suffix



# This function will initalize the dictionary containing chords
# and their definitions. 
def initialize_chord_dictionary():
    semitones = ['A','A#','B', 'C','C#','D','D#','E','F','F#','G','G#']
    chord_formulas = {
        '': [0,4,7], # major triad
        'm': [0,3,7], # minor triad
        'dim': [0,3,6], # diminished triad
        'aug': [0,4,8], # augmented triad
        'Maj7': [[0,4,7,11], [0,7,11], [0,4,11]], # major 7th variations
        'min7': [[0,3,7,10], [0,7,10], [0,3,10]], # minor 7th variations
        'dom7':[[0,4,7,10], [0,4,10]], # dominant 7 variations
        'min7b5': [[0,3,6,10], [0,6,10]], # half diminished 7 variations (no dropping the fifth)
        'dim7': [0,3,6,9], # fully diminished 7
        'aug7': [[0,4,8,11], [0,8,11]], # augmented 7 variations
        'Maj7+9': [[0,4,7,11,2], [0,4,11,2], [0,7,11,2]], # major 7 add 9 variations
        'min7+9': [[0,3,7,10,2], [0,3,10,2], [0,7,10,2]], # minor 7 add 9 variations
        'dom7+9':[[0,4,7,10,2], [0,4,10,2]], # dominant 7 add 9 variations
        'Maj9': [0,4,7,2], # major 9
        'min9': [0,3,7,2], # minor 9
        'sus2': [0,2,7], # suspended 2
        'sus4': [0,5,7], # suspended 4
        'Maj6': [[0,4,7,9], [0,7,9], [0,4,9]], # major 6 variations
        'min6': [[0,3,7,8], [0,7,8], [0,3,8]], # minor 6 variations 
        'Majmin6':[[0,4,7,8], [0,4,8]], # major triad with minor 6 variations
        'minMaj6':[[0,3,7,9], [0,3,9]], # minor triad with major 6 variations
        'Maj7b9':[[0,4,7,11,1], [0,4,11,1], [0,7,11,1]], # major 7 flat 9 variations
        'Maj7#9':[[0,4,7,11,3], [0,4,11,3], [0,7,11,3]], # major 7 sharp 9 variations
        'dom7b9':[[0,4,7,10,1], [0,4,10,1], [0,7,10,1]], # dominant 7 flat 9 variations
        'dom7#9':[[0,4,7,10,3], [0,4,10,3], [0,7,10,3]], # dominant 7 sharp 9 variations
        'maj11':[[0,4,7,11,2,5], [0,4,11,2,5], [0,7,11,2,5], # major 7 add 9 add 11 variations
                 [0,4,11,5], [0,7,11,5], [0,4,7,2,5], [0,4,2,5]],
        'maj7#11': [[0,4,7,11,2,6], [0,4,7,11,6], [0,4,7,2,6], # maj 7 sharp 11 variations
                    [0,4,11,2,6], [0,4,11,6], [0,4,7,6], [0,4,6],
                    [0,7,11,2,6], [0,7,10,6], [0,7,6], [0,7,2,6]],
        'maj7b9add11': [[0,4,7,11,1,5], [0,4,11,1,5],[0,7,11,1,5]], # major 7 flat nine add 11 variations
        'maj7b9#11': [[0,4,7,11,1,6], [0,4,11,1,6], [0,7,11,1,6]], # major 7 flat 9 sharp 11 variations
        'min11': [[0,3,7,10,2,5], [0,3,7,10,5], [0,3,7,2,5], # minor 7 add 11 variations
                  [0,3,10,2,5], [0,3,10,5], [0,3,7,5], [0,3,5],
                  [0,7,10,2,5], [0,7,10,5]],
        'min7b9add11': [[0,3,7,10,1,5], [0,3,10,1,5], [0,7,10,1,5]], # minor 7 flat 9 add 11 variations
        'min7#11':[[0,3,7,10,2,6], [0,3,10,2,6], [0,3,10,6], # minor 7 add sharp 11 variations
                   [0,3,7,10,6], [0,3,10,6]],
        'min7b9#11': [[0,3,7,10,1,6], [0,3,10,1,6],[0,7,10,1,6]], # minor 7 flat 9 sharp 11 variations
        'dom7add11':[[0,4,7,10,2,5], [0,4,7,10,5], [0,4,10,2,5], [0,4,10,5]], # dominant 7 add 11 variations
        'dom7#11':[[0,4,7,10,2,6], [0,4,10,2,6], [0,4,10,6]], # dominant 7 sharp 11 variations
        'dom7b9add11':[[0,4,7,10,1,6], [0,4,10,1,6], [0,7,10,1,6]], # dominant 7 flat 9 add 11 variations
        'dom7b9#11':[[0,4,7,10,1,6], [0,4,10,1,6]], # dominant 7 flat 9 sharp 11 variations
        'Maj13': [[0,4,7,11,2,5,9],    # 1–3–5–maj7–9–11–13
                  [0,4,7,11,2,9],     # omit 11
                  [0,4,7,11,5,9]],      # omit 9
        'Maj13b9': [[0,4,7,11,1,5,9], [0,4,7,11,1,9]],  # flat9 variant
        'Maj13#11': [[0,4,7,11,2,6,9], [0,4,7,11,6,9]],  # sharp11 variant
        'min13': [[0,3,7,10,2,5,9],   # 1–♭3–5–♭7–9–11–13
                  [0,3,7,10,2,9],     # omit 11
                  [0,3,7,10,5,9]],      # omit 9
        'min13b9': [[0,3,7,10,1,5,9], [0,3,7,10,1,9]],
        'min13#11': [[0,3,7,10,2,6,9], [0,3,7,10,6,9]],
        'dom13': [[0,4,7,10,2,5,9],   # 1–3–5–♭7–9–11–13
                  [0,4,7,10,2,9],     # omit 11
                  [0,4,7,10,5,9]],      # omit 9
        'dom13b9': [[0,4,7,10,1,5,9], [0,4,7,10,1,9]],
        'dom13#11': [[0,4,7,10,2,6,9], [0,4,7,10,6,9]],
        '7sus2':    [[0,2,7,10],    [0,2,10]],      # Dominant-7sus2
        '7sus4':    [[0,5,7,10],    [0,5,10]],      # Dominant-7sus4
        '9sus4':    [[0,5,7,10,2],  [0,5,10,2]],    # 9th with sus4
        'add2':     [[0,2,4,7]],                      # Major triad + 2
        'add4':     [[0,4,5,7]],                      # Major triad + 4
        '6add9':    [[0,4,7,9,2],    [0,4,7,2]],      # 6th + 9th
        '7b5':      [[0,4,6,10],     [0,6,10]],       # Dom7 with flat5
        '7#5':      [[0,4,8,10],     [0,8,10]],       # Dom7 with sharp5
        '9b5':      [[0,4,6,10,2],   [0,6,10,2]],     # 9th with flat5
        '9#5':      [[0,4,8,10,2],   [0,8,10,2]],     # 9th with sharp5
        '11b5':     [[0,4,6,10,2,5], [0,6,10,2,5]],   # 11th with flat5
        '11#5':     [[0,4,8,10,2,5], [0,8,10,2,5]],   # 11th with sharp5
        '13b5':     [[0,4,6,10,2,5,9], [0,6,10,2,5,9]],# 13th with flat5
        '13#5':     [[0,4,8,10,2,5,9], [0,8,10,2,5,9]],# 13th with sharp5
        '7b9':      [[0,4,7,10,1],   [0,4,10,1]],     # Dom7 flat9
        '7#9':      [[0,4,7,10,3],   [0,4,10,3]],     # Dom7 sharp9
        '9b9':      [[0,4,7,10,1,2], [0,4,7,10,1]],   # 9th flat9
        '9#9':      [[0,4,7,10,3,2], [0,4,7,10,3]],   # 9th sharp9
        '11b9':     [[0,4,7,10,1,2,5],  [0,4,7,10,1,5]],   # 11th flat9
        '11#9':     [[0,4,7,10,3,2,5],  [0,4,7,10,3,5]],   # 11th sharp9
        '13b9':     [[0,4,7,10,1,2,5,9],[0,4,7,10,1,5,9]], # 13th flat9
        '13#9':     [[0,4,7,10,3,2,5,9],[0,4,7,10,3,5,9]], # 13th sharp9
        '7alt': [[0,4,6,10,1,3],   # 1-3-♭5-♭7-♭9-#9
                 [0,4,6,10,1],     # omit #9
                 [0,4,10,1,3]],     # omit ♭5
        'add9':     [[0,4,7,2]],      # triad + 9
        'add11':    [[0,4,7,5]],      # triad + 11
        'add13':    [[0,4,7,9]],      # triad + 13
        'Maj6Maj7': [[0, 4, 9, 11],   # full 1-3-6-7 voicing
                     [0, 9, 11],      # drop the 3rd
                     [0, 4, 11]],     # drop the 6th
        '6maj7': [[0, 4, 9, 11],[0, 9, 11],[0, 4, 11]],
        'maj7add13': [[0, 4, 7, 11, 9],  # 1-3-5-7-13
                      [0, 4, 11, 9],     # drop the 5th
                      [0, 7, 11, 9]],     # drop the 3rd
        'Maj13no9no11': [[0, 4, 7, 11, 9], [0, 4, 11, 9], [0, 7, 11, 9]],
        '5' : [[0,7]],  # power chord
}

    chord_names = {} # empty dictionary for where chord names will go
    for root_id, root in enumerate(semitones):
        for suffix, intervals in chord_formulas.items():
            chord_name = root + suffix
            if isinstance(intervals[0], list):  # it's a list of variations
                chord_notes_variants = []
                for variant in intervals:
                    notes = [semitones[(root_id + i) % 12] for i in variant]
                    chord_notes_variants.append(notes)
                chord_names[chord_name] = chord_notes_variants
            else:  # it's just a single chord formula
                notes = [semitones[(root_id + i) % 12] for i in intervals]
                chord_names[chord_name] = [notes]
    return chord_names

big_dictionary = initialize_chord_dictionary()
STRING_ORDER = ['E_high','B','G','D','A','E_low']
STRING_ORDER_DROP_D = ['E-high', 'B', 'G', 'D', 'A', 'D_low']


def identify_chord(selected_notes, selections, chord_dict, string_order, current_map):
    sel_set = set(selected_notes)
    if not selections: return "No notes"
    root_string = max(selections.keys(), key=lambda s: string_order.index(s))
    bass_note = current_map[root_string][selections[root_string]]
    for name, voicings in chord_dict.items():
        if name.startswith(bass_note):
            for voicing in voicings:
                if sel_set == set(voicing):
                    return name
    for name, voicings in chord_dict.items():
        for voicing in voicings:
            if sel_set == set(voicing):
                return name
    return "No Match"

class FretboardGUI(tk.Tk):
    def __init__(self, chord_dict):
        super().__init__()
        self.title("Guitar Chord Identifier")
        self.use_flats = tk.BooleanVar(value=False)
        self.drop_d = tk.BooleanVar(value=False)
        self.toggle1 = tk.Checkbutton(
            self,
            text="Use Flats",
            variable=self.use_flats,
            command=self._refresh_display
        )
        self.maps = {
            False: fret_maps,
            True: fret_maps_drop_d
        }
        self.orders = {
            False: list(fret_maps.keys()),
            True: list(fret_maps_drop_d.keys())
        }
        self.toggle2 = tk.Checkbutton(self, text="Drop D", variable=self.drop_d, command=self._refresh_display)
        self.toggle1.pack()
        self.toggle2.pack(pady=(0,10))
        self.chord_dict = chord_dict
        self.canvas = tk.Canvas(self, width=800, height=240, bg='white')
        self.canvas.pack(padx=10, pady=10)
        self.info_label = tk.Label(self, text="Click frets to build a chord", font=("Arial", 14))
        self.info_label.pack(pady=(0,10))
        self.selections = {}
        self._draw_fretboard()
        self.canvas.bind("<Button-1>", self.on_click)
    
    def _current_map(self):
        return self.maps[self.drop_d.get()]
    
    def _current_order(self):
        return self.orders[self.drop_d.get()]

    def _refresh_display(self):
        self._redraw_markers()
        self._update_chord_label()

    def _draw_fretboard(self):
        self.strings = []
        height, margin = 200, 20
        for i in range(6):
            y = margin + i*(height/5)
            self.canvas.create_line(50, y, 750, y, width=2)
            self.strings.append(y)
        self.frets = []
        for fret in range(16):
            x = 50 + fret*((750-50)/15)
            self.canvas.create_line(x, margin, x, margin+height, width=1)
            self.frets.append(x)
        self.mids = [
            (self.frets[i] + self.frets[i+1]) / 2
            for i in range(len(self.frets)-1)
        ]

    def on_click(self, event):
        m = self._current_map()
        order = list(m.keys())
        for string_name, fret in list(self.selections.items()):
            i = order.index(string_name)
            y = self.strings[i]
            x = self.frets[0] if fret == 0 else self.mids[fret-1]
            if abs(event.x - x) <= 8 and abs(event.y - y) <= 8:
                del self.selections[string_name]
                self._redraw_markers()
                self._update_chord_label()
                return
        string_i = min(range(6), key=lambda i: abs(self.strings[i] - event.y))
        string_name = order[string_i]
        if event.x < self.mids[0]:
            fret_i = 0
        elif event.x > self.mids[-1]:
            fret_i = len(self.frets)-1
        else:
            fret_i = next(idx for idx, mid in enumerate(self.mids)
                          if event.x < mid)
        if self.selections.get(string_name) == fret_i:
            del self.selections[string_name]
        else:
            self.selections[string_name] = fret_i
        self._redraw_markers()
        self._update_chord_label()

    def _redraw_markers(self):
        m = self._current_map()
        order = list(m.keys())
        self.canvas.delete("mark")
        for string_name, fret in self.selections.items():
            i = order.index(string_name)
            y = self.strings[i]
            x = self.frets[0] if fret == 0 else self.mids[fret-1]
            note = m[string_name][fret]
            if self.use_flats.get():
                note = flat_conversion.get(note, note)  
            self.canvas.create_oval(x-8, y-8, x+8, y+8, fill="lightblue", tags="mark")
            self.canvas.create_text(x, y, text=note, tags="mark")
            
    def _update_chord_label(self):
        m = self._current_map()
        order = self._current_order()
        notes = [m[s][f] for s,f in self.selections.items()]
        if self.use_flats.get():
            display_notes = convert_notes_to_flat(notes)
        else:
            display_notes = notes
        chord_sharp = identify_chord(notes, self.selections, self.chord_dict, order, m)
        if self.use_flats.get():
            chord_display = convert_chord_name_to_flats(chord_sharp)
        else:
            chord_display = chord_sharp
        self.info_label.config(
            text=f"Notes: {sorted(display_notes)} → Chord: {chord_display}"
        )

if __name__ == "__main__":
    gui = FretboardGUI(big_dictionary)
    gui.mainloop()

