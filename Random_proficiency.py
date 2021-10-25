import numpy as np
import sys, os

state_basic = ['Linear power supply fixed output voltage', 'Linear power supply variable output voltage', 'Active Filter', '555 Timer Oscillator', 'Amplifier by Transistor', 'Amplifier by Op-amp', 'Converter Circuits', 'Voltage multiplier', 'Buck-boost Regulator Circuits', 'Microstrip patch antenna']

lst_circuit_basic = {'Linear power supply fixed output voltage' : ['Linear power supply fixed output voltage by Zener regulator', 'Linear power supply fixed output voltage by LM78xx regulator', 'Linear power supply fixed output voltage by LM79xx regulator'], 'Linear power supply variable output voltage' : [ 'Linear Power supply variable output voltage bt LM317 regulator', 'Linear power supply variable output voltage by LM337 regulator',  'Linear power supply variable output voltage แบบขยายกระแส'], 'Active Filter' : ['Low pass filter', 'High pass filter', 'Band pass filter'], '555 Timer Oscillator' : ['555 Timer Oscillator'], 'Amplifier by Transistor' : ['Amplifier Class A', 'Amplifier Class B', 'Amplifier Class AB', 'Amplifier Class C'], 'Amplifier by Op-amp' : ['Inverting Amplifier', 'Non-Inverting Amplifier', 'Buffer or Voltage follower'], 'Converter Circuits' : ['Flyback Converter', 'Push-Pull Converter', 'Half-Bridge Converter', 'Full-Bridge Converter'], 'Voltage multiplier' : ['Voltage multiplier'], 'Buck-boost Regulator Circuits' : ['MC 34063 buck circuit', 'MC 34063 boost circuit'], 'Microstrip patch antenna' : ['Microstrip patch antenna']}

print('---------- BASIC ----------\n')
recieve = []
count = 0
while count < 9:
    random = np.random.randint(0, 10)
    msg = state_basic[random]
    random_subcircuit = lst_circuit_basic[msg]
    length_subcircuit = len(random_subcircuit)
    try:
        random = np.random.randint(0, 3)
        recieve.append(lst_circuit_basic[msg][random])
        print(f'Topic {count + 1}: {msg} ---\u2192 Circuit: {lst_circuit_basic[msg][random]}')
        lst_circuit_basic[msg].pop(random)
    except:
        continue
    
    if len(recieve) == 8:
        break

    count += 1
    
# for i in range(len(recieve)):
#     print(f'Circuit {i + 1}: {recieve[i]}')
print('\n---------- BASIC ----------')
print()

# Intermediate
state_basic = ['Linear power supply fixed output voltage', 'Linear power supply variable output voltage', 'Active Filter', 'Variable dual-polarity power supply', '555 Timer in two one-shorts produce a delayed output pulse', 'Negative feedback for gain stability', '555 IC inverter circuit', 'Wien Bridge Oscillator', 'Zero span', 'Wilkinson power divider']

lst_circuit_intermediate = {'Linear power supply fixed output voltage' : ['Linear power supply fixed output voltage by Zener regulator', 'Linear power supply fixed output voltage by LM78xx regulator', 'Linear power supply fixed output voltage by LM79xx regulator'], 'Linear power supply variable output voltage' : [ 'Linear Power supply variable output voltage bt LM317 regulator', 'Linear power supply variable output voltage by LM337 regulator',  'Linear power supply variable output voltage แบบขยายกระแส'], 'Active Filter' : ['Low pass filter', 'High pass filter', 'Band pass filter'], 'Variable dual-polarity power supply' : ['Variable dual-polarity power supply'], '555 Timer in two one-shorts produce a delayed output pulse' : ['555 Timer in two one-shorts produce a delayed output pulse'], 'Negative feedback for gain stability' : ['Negative feedback for gain stability'], '555 IC inverter circuit' : ['555 IC inverter circuit'], 'Wien Bridge Oscillator' : ['Wien Bridge Oscillator'], 'Zero span' : ['Zero span'], 'Wilkinson power divider' : ['Wilkinson power divider']}

print('---------- Intermediate ----------\n')

recieve = []
count = 0
while count < 6:
    random = np.random.randint(0, 10)
    msg = state_basic[random]
    random_subcircuit = lst_circuit_intermediate[msg]
    length_subcircuit = len(random_subcircuit)
    try:
        random = np.random.randint(0, 3)
        recieve.append(lst_circuit_intermediate[msg][random])
        print(f'Topic {count + 1}: {msg} ---\u2192 Circuit: {lst_circuit_intermediate[msg][random]}')
        lst_circuit_intermediate[msg].pop(random)
    except:
        continue
    
    if len(recieve) == 5:
        break

    count += 1

print('\n---------- Intermediate ----------')
print()

# Advance
state_advance = ['Linear power supply fixed output voltage', 'Linear power supply variable output voltage', 'Amplifier by Transistor', 'Variable dual-polarity power supply', 'The direct-coupled preamp', 'Half Bridge Converter PWM', 'BJT astable inverter circuit', 'Zero span', 'Wien bridge Oscillator', 'Microstrip tapped-hairpin dual-band pass filter']
lst_circuit_advance = {'Linear power supply fixed output voltage' : ['Linear power supply fixed output voltage by Zener regulator', 'Linear power supply fixed output voltage by LM78xx regulator', 'Linear power supply fixed output voltage by LM79xx regulator'], 'Linear power supply variable output voltage' : [ 'Linear Power supply variable output voltage bt LM317 regulator', 'Linear power supply variable output voltage by LM337 regulator',  'Linear power supply variable output voltage แบบขยายกระแส'], 'Amplifier by Transistor' : ['Amplifier by Transistor'], 'Variable dual-polarity power supply' : ['Variable dual-polarity power supply'], 'The direct-coupled preamp' : ['The direct-coupled preamp'], 'Half Bridge Converter PWM' : ['Half Bridge Converter PWM'], 'BJT astable inverter circuit' : ['BJT astable inverter circuit'], 'Zero span' : ['Zero span'], 'Wien bridge Oscillator' : ['Wien bridge Oscillator'], 'Microstrip tapped-hairpin dual-band pass filter' : ['Microstrip tapped-hairpin dual-band pass filter']}

print('---------- Advance ----------\n')
recieve = []
count = 0
while count < 4:
    random = np.random.randint(0, 10)
    msg = state_advance[random]
    random_subcircuit = lst_circuit_advance[msg]
    length_subcircuit = len(random_subcircuit)
    try:
        random = np.random.randint(0, 3)
        recieve.append(lst_circuit_advance[msg][random])
        print(f'Topic {count + 1}: {msg} ---\u2192 Circuit: {lst_circuit_advance[msg][random]}')
        lst_circuit_advance[msg].pop(random)
    except:
        continue
    
    if len(recieve) == 3:
        break

    count += 1
print('\n---------- Advance ----------')
print()