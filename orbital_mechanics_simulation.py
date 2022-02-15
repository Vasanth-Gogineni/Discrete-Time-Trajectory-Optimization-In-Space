from vpython import *
from vpython import sphere
from skyfield.api import load

scene.height = 800
scene.width = 1500
ts = load.timescale()
tx = ts.utc(2010, 1, 1)
planets = load('de421.bsp')
sunx, mercuryx, venusx, earthx, marsx, jupiterx, saturnx, uranusx, neptunex, plutox, moonx = \
    planets['sun'], \
    planets['mercury'], planets['venus'], planets['earth'], \
    planets['mars'], planets['JUPITER BARYCENTER'], planets['SATURN BARYCENTER'], \
    planets['URANUS BARYCENTER'], planets['NEPTUNE BARYCENTER'], planets['PLUTO BARYCENTER'], \
    planets['moon']
Re = 6.3781e6
Rs = 696340000
t = 0
dt = 10000
G = 6.67e-11  # variable init
earth = sphere(radius=Re*40,
               pos=vector((earthx.at(tx)).position.m[0], (earthx.at(tx)).position.m[1], (earthx.at(tx)).position.m[2]),
               texture=textures.earth, make_trail=True)
moon = sphere(radius=Re*20,
              pos=vector((moonx.at(tx)).position.m[0], (moonx.at(tx)).position.m[1], (moonx.at(tx)).position.m[2]),
              color=color.red, make_trail=False)
mercury = sphere(radius=Re * 600,
                 pos=vector((mercuryx.at(tx)).position.m[0], (mercuryx.at(tx)).position.m[1],
                            (mercuryx.at(tx)).position.m[2]),
                 color=color.gray(60), make_trail=True, lw=0.4)
venus = sphere(radius=Re * 600,
               pos=vector((venusx.at(tx)).position.m[0], (venusx.at(tx)).position.m[1],
                          (venusx.at(tx)).position.m[2]),
               color=color.yellow, make_trail=True, lw=0.4)
mars = sphere(radius=Re * 600,
              pos=vector((marsx.at(tx)).position.m[0], (marsx.at(tx)).position.m[1],
                         (marsx.at(tx)).position.m[2]),
              color=color.red, make_trail=True, lw=0.4)
jupiter = sphere(radius=Rs * 50,
                 pos=vector((jupiterx.at(tx)).position.m[0], (jupiterx.at(tx)).position.m[1],
                            (jupiterx.at(tx)).position.m[2]),
                 color=color.yellow, make_trail=True, lw=0.4)
saturn = sphere(radius=Re * 600,
                pos=vector((saturnx.at(tx)).position.m[0], (saturnx.at(tx)).position.m[1],
                           (saturnx.at(tx)).position.m[2]),
                color=color.orange, make_trail=True, lw=0.4)
uranus = sphere(radius=Re * 600,
                pos=vector((uranusx.at(tx)).position.m[0], (uranusx.at(tx)).position.m[1],
                           (uranusx.at(tx)).position.m[2]),
                color=color.orange, make_trail=True, lw=0.4)
neptune = sphere(radius=Re * 600,
                 pos=vector((neptunex.at(tx)).position.m[0], (neptunex.at(tx)).position.m[1],
                            (neptunex.at(tx)).position.m[2]),
                 color=color.blue, make_trail=True, lw=0.4)
pluto = sphere(radius=Re * 600,
               pos=vector((plutox.at(tx)).position.m[0], (plutox.at(tx)).position.m[1],
                          (plutox.at(tx)).position.m[2]),
               color=color.gray(70), make_trail=True, lw=0.4)
sat = sphere(radius=Re * 20, #-6378100
             pos=vector(((earthx.at(tx)).position.m[0]-30000), (earthx.at(tx)).position.m[1], (earthx.at(tx)).position.m[2]),
             color=color.green, make_trail=True)
arrow(pos = vector(earth.pos.x, earth.pos.y, earth.pos.z), axis=vector(0,1,0),
      color = vector(0, 1, 0), shaftwidth=Re*600, length=Re*600)
sun = sphere(radius=Rs*60,
             pos=vector(sunx.at(tx).position.m[0], sunx.at(tx).position.m[1], sunx.at(tx).position.m[2]),
             color=color.yellow, lw=0.4, emmisive=True, shininess=100)
lamp=local_light(pos=vector(0,0,0), color=vector(1000000,10000000,10000000))  # planet sphere definition


mercury.mass = 3.285e23
venus.mass = 4.867e24
earth.mass = 5.972e24
mars.mass = 6.39e23
jupiter.mass = 1.898e27
saturn.mass = 5.683e26
uranus.mass = 8.681e25
neptune.mass = 1.024e26
pluto.mass = 1.30900e23
sat.mass = 500
moon.mass = 7.34767309e22
sun.mass = 1.989e30  # planet masses
names = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto, moon]
earth.momentum = earth.mass * vector((earthx.at(tx)).velocity.m_per_s[0],
                                     (earthx.at(tx)).velocity.m_per_s[1],
                                     (earthx.at(tx)).velocity.m_per_s[2])
sun.momentum = sun.mass * vector((sunx.at(tx)).velocity.m_per_s[0],
                                 (sunx.at(tx)).velocity.m_per_s[1],
                                 (sunx.at(tx)).velocity.m_per_s[2])
mercury.momentum = mercury.mass * vector((mercuryx.at(tx)).velocity.m_per_s[0],
                                         (mercuryx.at(tx)).velocity.m_per_s[1],
                                         (mercuryx.at(tx)).velocity.m_per_s[2])
venus.momentum = venus.mass * vector((venusx.at(tx)).velocity.m_per_s[0],
                                     (venusx.at(tx)).velocity.m_per_s[1],
                                     (venusx.at(tx)).velocity.m_per_s[2])
mars.momentum = mars.mass * vector((marsx.at(tx)).velocity.m_per_s[0],
                                   (marsx.at(tx)).velocity.m_per_s[1],
                                   (marsx.at(tx)).velocity.m_per_s[2])
jupiter.momentum = jupiter.mass * vector((jupiterx.at(tx)).velocity.m_per_s[0],
                                         (jupiterx.at(tx)).velocity.m_per_s[1],
                                         (jupiterx.at(tx)).velocity.m_per_s[2])
saturn.momentum = saturn.mass * vector((saturnx.at(tx)).velocity.m_per_s[0],
                                       (saturnx.at(tx)).velocity.m_per_s[1],
                                       (saturnx.at(tx)).velocity.m_per_s[2])
uranus.momentum = uranus.mass * vector((uranusx.at(tx)).velocity.m_per_s[0],
                                       (uranusx.at(tx)).velocity.m_per_s[1],
                                       (uranusx.at(tx)).velocity.m_per_s[2])
neptune.momentum = neptune.mass * vector((neptunex.at(tx)).velocity.m_per_s[0],
                                         (neptunex.at(tx)).velocity.m_per_s[1],
                                         (neptunex.at(tx)).velocity.m_per_s[2])
moon.momentum = moon.mass * (vector((moonx.at(tx)).velocity.m_per_s[0],
                                   (moonx.at(tx)).velocity.m_per_s[1],
                                   (moonx.at(tx)).velocity.m_per_s[2]))
sat.momentum = sat.mass * vector((earthx.at(tx)).velocity.m_per_s[0],
                                 (earthx.at(tx)).velocity.m_per_s[1]-6023,
                                 (earthx.at(tx)).velocity.m_per_s[2])  # 7723
pluto.momentum = pluto.mass * vector((plutox.at(tx)).velocity.m_per_s[0],
                                     (plutox.at(tx)).velocity.m_per_s[1],
                                     (plutox.at(tx)).velocity.m_per_s[2])  # Skyfield Momentum


def gravitationalForce(p1, p2):
    rVector = p1.pos - p2.pos
    rMagnitude = mag(rVector)
    sign = rVector / rMagnitude
    F = - sign * G * p1.mass * p2.mass / rMagnitude ** 2
    return F


while 1 == 1:
    rate(1000)
    sun.force = gravitationalForce(sun, earth)  # TODO- BARYCENTER THIS
    sun.momentum = sun.momentum + sun.force * dt
    sun.pos = sun.pos + sun.momentum / sun.mass * dt
    mercury.force = gravitationalForce(mercury, sun)  # TODO - 1
    mercury.momentum = mercury.momentum + mercury.force * dt
    mercury.pos = mercury.pos + mercury.momentum / mercury.mass * dt
    venus.force = gravitationalForce(venus, sun)  # TODO - 2
    venus.momentum = venus.momentum + venus.force * dt
    venus.pos = venus.pos + venus.momentum / venus.mass * dt
    earth.force = gravitationalForce(earth, sun)  # TODO - 3
    earth.momentum = earth.momentum + earth.force * dt
    earth.pos = earth.pos + earth.momentum / earth.mass * dt
    mars.force = gravitationalForce(mars, sun)  # TODO - 4
    mars.momentum = mars.momentum + mars.force * dt
    mars.pos = mars.pos + mars.momentum / mars.mass * dt
    jupiter.force = gravitationalForce(jupiter, sun)  # TODO - 5
    jupiter.momentum = jupiter.momentum + jupiter.force * dt
    jupiter.pos = jupiter.pos + jupiter.momentum / jupiter.mass * dt
    saturn.force = gravitationalForce(saturn, sun)  # TODO - 6
    saturn.momentum = saturn.momentum + saturn.force * dt
    saturn.pos = saturn.pos + saturn.momentum / saturn.mass * dt
    uranus.force = gravitationalForce(uranus, sun)  # TODO - 7
    uranus.momentum = uranus.momentum + uranus.force * dt
    uranus.pos = uranus.pos + uranus.momentum / uranus.mass * dt
    neptune.force = gravitationalForce(neptune, sun)  # TODO - 8
    neptune.momentum = neptune.momentum + neptune.force * dt
    neptune.pos = neptune.pos + neptune.momentum / neptune.mass * dt
    pluto.force = gravitationalForce(pluto, sun)  # TODO - 9
    pluto.momentum = pluto.momentum + pluto.force * dt
    pluto.pos = pluto.pos + pluto.momentum / pluto.mass * dt
    moon.force = gravitationalForce(moon, earth)
    moon.force = moon.force + gravitationalForce(moon, sun)  # TODO - 10
    moon.momentum = moon.momentum + moon.force * dt
    moon.pos = moon.pos + moon.momentum / moon.mass * dt
    #sat.force = gravitationalForce(sat, earth)
    #sat.force = sat.force + gravitationalForce(sat, sun)  # TODO - 10
    #sat.momentum = sat.momentum + sat.force * dt
    #sat.pos = sat.pos + (sat.momentum / sat.mass * dt)
    t += dt
    print(earth.pos)
    #if (t>((3.154e+7)/4)):
    #    dt=10000
     #   earth.make_trail=True
