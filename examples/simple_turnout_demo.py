import mimic_panel_express as mpe

# Define the individual items
main = mpe.Track('Main Line', (25, 200), (1175, 200))
turnout = mpe.Turnout('Turnout', (500, 200))
siding = mpe.Stub('Siding', (600, 150), (800, 150))
signal = mpe.Signal('Signal', (400, 225))

# Create the layout and add the items
layout = mpe.Layout('Simple Turnout')
layout.add(main)
layout.add(signal)
layout.add(turnout)
layout.add(siding)

# Run the layout with all defaults
layout.run()