
import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()

pins=[
      elm.IcPin(name='VCC2', pin='8', side='left'),
      elm.IcPin(name='IN2', pin='7', side='left'),
      elm.IcPin(name='OUT2', pin='6', side='left'),
      elm.IcPin(name='GND', pin='5', side='left'),
      elm.IcPin(name='GND', pin='4', side='left'),
      elm.IcPin(name='OUT1', pin='3', side='left'),
      elm.IcPin(name='IN1', pin='2', side='left'),
      elm.IcPin(name='ENA', pin='1', side='left'),
      elm.IcPin(name='ENB', pin='9', side='right'),
      elm.IcPin(name='IN3', pin='10', side='right'),
      elm.IcPin(name='OUT3', pin='11', side='right'),
      elm.IcPin(name='GND', pin='12', side='right'),
      elm.IcPin(name='GND', pin='13', side='right'),
      elm.IcPin(name='OUT4', pin='14', side='right'),
      elm.IcPin(name='IN4', pin='15', side='right'),
      elm.IcPin(name='VCC1', pin='16', side='right')
      ]

D = elm.Ic(w=4,pins=pins, pinspacing = 1, edgepadW=.5, edgepadH=1).label('L293D', 'top')
d += D

d += elm.Line(d='left', l=3).at(D.OUT1).label("Motor A", loc='left')
d += elm.Motor(d='down')
d += elm.Line(d='right').tox(D.OUT2)

d += elm.Line(d='right', l=1).at(D.GND)
d.push()
d+= elm.Ground().label("Pi")
d.pop()
d += elm.Line(d='right', l=1)
d+= elm.Ground().label("BAT")


d += elm.Line(d='right', l=3).at(D.OUT4).label("Motor B", loc='right')
d += elm.Motor(d='down')
d += elm.Line(d='left').tox(D.OUT3)

d += elm.Line(d='right', l=3.5).at(D.VCC1)
d += elm.Vdd(label='5V', width=2)

d += elm.Line(d='right', l=0.5).at(D.ENB)
d += elm.Tag(label='GPIO13', width=2)

d += elm.Line(d='right', l=0.5).at(D.IN4)
d += elm.Tag(label='GPIO24', width=2)
d += elm.Line(d='right', l=0.5).at(D.IN3)
d += elm.Tag(label='GPIO23', width=2)

d += elm.Line(d='left', l=0.5).at(D.ENA)
d += elm.Tag(label='GPIO12', width=2)

d += elm.Line(d='left', l=0.5).at(D.IN1)
d += elm.Tag(label='GPIO5', width=2)
d += elm.Line(d='left', l=0.5).at(D.IN2)
d += elm.Tag(label='GPIO6', width=2)

d += elm.Line(d='left', l=3.5).at(D.VCC2)
d += elm.Vdd(label='VBAT', width=2)

d.save('clientFilesQuestion/schematic-h-bridge.svg')

