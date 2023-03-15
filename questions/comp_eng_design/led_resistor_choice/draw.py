import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()
C = d.add(elm.Tag(d='left', label='GPIO'))
d.add(elm.Resistor(d='right', label='R'))
d.add(elm.LED(d='down', label='D'))
d.add(elm.Ground())
d.save('clientFilesQuestion/schematic.svg')

