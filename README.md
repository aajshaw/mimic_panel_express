# mimic_panel_express

mimic_panel_express is a Python 3 library to enable schematic railway layouts to created with
a mimimum of coding.

![turnout demo](simple_turnout.png)

```python
from mimic_panel_express import Track, Stub, Turnout, Signal

# Define the individual items
main = Track('Main Line', (25, 200), (1175, 200))
turnout = Turnout('Turnout', (500, 200))
siding = Stub('Siding', (600, 150), (800, 150))
signal = Signal('Signal', (400, 225))

# Create the layout and add the items
layout = Layout('Simple Turnout')
layout.add(main)
layout.add(signal)
layout.add(turnout)
layout.add(siding)

# Run the layout with all defaults
layout.run()
```
## Dependencies
PySimpleGUI is used for the display simply because it is far easier to construct
the display letting PtSimpleGUI do the heavy lifting, in exactly the same way
that mimic_panel_express does the heavy lifting of providing schematic elements of a railway layout.

To install PySimpleGUI use pip:

```
pip install pysimplegui
```
