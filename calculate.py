import math
import sys

default = input('Do you want to use default for FoV? (60° horisontal Fov, 10° vertica and 100m range) (y/n) ')

if default == 'y':
    h_deg = 60
    v_deg = 10
    rang = 100
elif default == 'n':
    h_deg = int(input('enter horisontal FoV in degrees: ')) #how much deg the drone can see horisontally
    v_deg = int(input('enter vertical FoV in degrees: '))#how much deg the drone can see horisontally
    rang = int(input('enter range: '))
else:
    sys.exit('invalid input')

rh = h_deg / 2 
rv = v_deg / 2 

def convert(degrees):
    radians = degrees * 0.0174533
    return radians

cos_r = convert(rh) #calculates cos in radians


custom_h = input('do you want to use the maximum effective height (calculated from previous values))? (y/n) ')

# h = heigt

if custom_h == 'n':
    h = int(input('input the custom height: '))
elif custom_h == 'y':
    h =math.cos(cos_r) * rang 
else:
    sys.exit('invalid input')


print('maximum usable height = {0}m'.format(h))

#rg = ground half-radius
#Rg = ground radius
tan_r = convert(rh)
rg = math.tan(tan_r) * h
Rg = rg *2

tan_r2 = convert(rv)
rg2 = math.tan(tan_r2) * h
Rg2 = rg2 * 2

print('Horisontal FoV radius= {}'.format(Rg))
print('Vertical Fov radius = {}'.format(Rg2))

Fov = Rg * Rg2
print('Visible surface= {}m'.format(Fov))