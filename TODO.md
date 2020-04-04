# animalese.py TODO

## What is Animalese (etc.)?
**Animalese** is *Animal Crossing*'s "language" the characters speak in. What it actually is, however, is the individual letters of the words basically said aloud and ran into each other at various pitches and speeds.

**Bebebese** is another language found in *Animal Crossing*, but instead of approximating phonemes by running letter sounds together, it is comprised of various beeps.

## Basic Operation
- [ ] Takes text input and converts it to audio in Animalese.
  - [ ] Toggleable between either English or Japanese input.
    - [ ] English input outputs English Animalese.
    - [ ] Japanese input outputs Japanese Animalese.
  - [ ] Toggleable between Animalese and Bebebese.
  - [ ] Pitch / speed options
    - [ ] Presets

## Advanced Operation (Advanced Mode)
### Basic Markdown
- [ ] A basic markdown allows the user to control certain aspects of the output.
#### Audio Markdown
- [ ] Switch between Animalese and Bebebese.
- [ ] Adjust volume in the middle of input.
- [ ] Adjust pitch in the middle of input.
  - [ ] Allow for note pitches to be used<sup>?</sup>
- [ ] Add emote sounds during the speech.
#### Image Markdown
- [ ] Adjust the color of the text, even in the middle of input.
- [ ] Adjust the size of the text, even in the middle of input.
- [ ] Create "page breaks" (in static image mode, output multiple images. in animated image mode, just clear the box and keep going.)
#### Shortcut Markdown
- [ ] Mark a phrase as a "whisper" (switch to Bebebese, shrink font size, make color gray)
### Image Output
- [ ] Outputs either a static image of the textbox corrosponding to the input, or an animated one timed with the audio.
  - [ ] Player input character name and color for the textbox.
  - [ ] Responds to Image Markdown.
  - [ ] Does *something* when the text is too big to fit on the image.

## GUI
- [ ] Switch between Basic and Advanced mode.
- [ ] In Advanced mode, have buttons for inputting markdown codes.
- [ ] In Advanced mode, switch between Static Image mode and Animated Image mode.
- [ ] Make it look decent.
