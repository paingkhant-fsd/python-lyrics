# Lyrics Scripts Collection

Overview
- This folder contains three small Python scripts that print and animate song lyrics in the console:
  - `chris.brown.py`
  - `lil'star.py`
  - `RockThatBody.py`

Requirements
- Python 3.6+ (scripts use f-strings)
- `rich` library required for `chris.brown.py` and `RockThatBody.py` (colorized output)

Install dependencies
```bash
pip install rich
```

Script Summary

- `chris.brown.py`:
  - Description: Prints a short set of lyrics, character-by-character, using the `rich.print` function with a yellow hex color for each character. Uses `time.sleep` to control the pace.
  - Dependencies: `rich` (for color printing)
  - Run: `python chris.brown.py`
  - Customization: Modify the `lines` list or the `delay` values within the `lines` array to change text and pacing.

- `lil'star.py`:
  - Description: Prints song lyrics character-by-character with delays (typewriter-like) and additional per-line pauses. Only uses standard library `sys` and `time`.
  - Dependencies: None (standard library only)
  - Run: `python "lil'star.py"`
  - Customization: `lines` and `delays` lists inside `print_lyrics()` are used to change text and timing.

- `RockThatBody.py`:
  - Description: Prints song lyrics with colorized characters using `rich`. Special styling for the `(Rock your body)` line.
  - Dependencies: `rich`
  - Run: `python RockThatBody.py`
  - Customization: `lines` and `delays` lists in `printLyrics()` control the text and pacing. The script prints lines with different color tags; edit the conditional to change styling.

Notes & Troubleshooting
- If you see a `ModuleNotFoundError` for `rich`, run `pip install rich`.
- Ensure you're using an appropriate Python executable if multiple versions are present (for example: `python3`, `py -3`, or absolute path to your interpreter).
- On Windows, wrap the filename in quotes if it contains an apostrophe: `python "lil'star.py"`.

Contributing
- Update the `lines` and `delays` lists to alter the songs or pacing.
- Feel free to add new lyrics scripts or adjust colors and timing for different visual effects.