import numpy as np
#np.random.seed(10)
import smtplib

nombres = ['manolo', 'victor', 'paola'] #'juan carlos', 'ana Maria', 'Victor', 'blanca barreto', 'valeria gomez', 'paola', 'camilo moran', 'vicky', 'amelia alias yeyo']
nombres_2 = nombres[:]

correos = {'manolo': 'juanvalenciaen@gmail.com','victor':'vhgv1000@gmail.com', 'paola':'pcbsolinfo@gmail.com' } #'juan carlos':'jcvsolinfo@gmail.com', 'ana Maria':'anitavalencia-2@hotmail.com',
           #'Victor':'vhvg1000@hotmail.com', 'blanca barreto':'blanquitabarreto1968@gmail.com', 'valeria gomez':'valeriagg4215@gmail.com', 
           #'paola':'yeinycontreras@hotmail.com', 'camilo moran':'camilo.moran06965@gmail.com', 'vicky':'vickyencinales@hotmail.com', 'amelia alias yeyo':'amencinales@hotmail.com'}

class participante:

  def __init__(self, nombre):
    self.nombre = nombre
    self.nombres = nombres_2[:]

    if self.nombre in self.nombres:
      self.nombres.remove(self.nombre)

    self.random = np.random.choice(self.nombres, 1)[0]
    nombres_2.remove(self.random)

    mensaje = (self.nombre + '   sacó a:   ' + self.random)
    from_addr = 'juanvalenciaencinales@gmail.com'
    to = correos[self.nombre]
    message = """From: Amigo Secreto <{}>
To: {} <{}>
Subject: {}

{}.
""".format(from_addr, self.nombre, to, mensaje, mensaje)
    username = 'juanvalenciaencinales@gmail.com'
    password = '@Emiliano2'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username, password)
        server.sendmail(from_addr, to, message)
        server.quit()
        print('success sent: ' + self.nombre)
    except:
        print('error not sent')


participantes = {}

for persona in nombres:
  participantes[persona] = participante(persona)
  print(participantes[persona].nombre + '   saco a:   ' + participantes[persona].random)

