# 🎸 guitarchord
This Python project provides foundational data structures for mapping a guitar's fretboard and defining a wide variety of chord formulas. It's designed as a backend utility for music theory applications, guitar learning tools, and chord generation programs. The script is written using standard Python and includes chord variations ranging from simple triads to complex jazz extensions.

## 📁 Features
Guitar Fretboard Mapping  
Each of the six strings (E, A, D, G, B, E) is represented with its notes from the open string up to the 15th fret.  
User can choose between displaying notes in Sharps or Flats  
User can select Drop D setting (more tunings coming soon!)  

## Extensive Chord Dictionary
Includes:

Major, minor, diminished, and augmented triads

7th, 9th, 11th, and 13th chords with extensions and alterations

Suspended, added tone, and altered fifth variants

Jazz chords with complex voicings and optional tones

## Modular Data Representation
Easy to extend or adapt for chord recognition, diagram generation, or theory education tools.

## 🧠 How It Works
The fret_maps dictionary holds six string-note mappings from open (0) to 15th fret.

The initialize_chord_dictionary() function defines a global dictionary of chord names and their corresponding intervals (as semitone offsets from a root note).

Chords can include multiple voicing variations using sublists of semitone positions.

## 🛠️ Usage
You can import this module into a music tool or GUI app. For example:

- python
- Copy code
- from your_module import fret_maps, initialize_chord_dictionary

- chords = initialize_chord_dictionary()
- e_string_notes = fret_maps["E_low"]
- Integrate it with a user interface (e.g., Tkinter, PyGame) or audio/midi library for enhanced functionality.

## 🧱 Dependencies
Python 3.13.3

No external libraries required 

##  🖥️  GUI
The GUI for this project is mostly vibe-coded. In the future I'd like to get more familiar with tkinter. 

## 🤝 Contributing
Feel free to fork this project, suggest features, or submit pull requests. Especially helpful would be:



Additional chord types or tunings

📜 License
This project is open-source and available under the MIT License. Do what you want, just give credit where it’s due.

