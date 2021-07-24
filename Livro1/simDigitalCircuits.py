# Application to simulate digital circuits.
# This is to develop the knowledge of OOP and inheritance.
class LogicGate :

  def __init__(self, n):
    self.label = n
    self.output = None

  def getLabel(self):
    return self.label

  def getOutput(self):
    self.output = self.performGateLogic()
    return self.output


class BinaryGate(LogicGate):

  def __init__(self, n):
    LogicGate.__init__(self, n)

    self.pinA = None
    self.pinB = None

  def getPinA(self):
    if self.pinA == None:
      return int(input("Digite a entrada do Pino A para a porta " +
              self.getLabel() + "-->"))
    else:
      return self.pinA.getFrom().getOutput()

  def getPinB(self):
    if self.pinB == None:
      return int(input("Digite a entrada do Pino B para a porta " +
              self.getLabel() + "-->"))
    else:
      return self.pinB.getFrom().getOutput()
  

class UnaryGate(LogicGate):
  
  def __init__(self, n):
    LogicGate.__init__(self, n)

    self.pin = None

  def getPin(self):
    return int(input("Digite a entrada do Pino para a porta " + self.getLabel() + "-->"))

class AndGate(BinaryGate):

  def __init__(self, n):
    BinaryGate.__init__(self, n)

  def performGateLogic(self):

    a = self.getPinA()
    b = self.getPinB()
    if a == 1 and b == 1:
      return 1
    else:
      return 0

class OrGate(BinaryGate):
  def __init__(self, n):
    BinaryGate.__init__(self, n)

  def performGateLogic(self):

    a = self.getPinA()
    b = self.getPinB()
    if a == 0 and b == 0:
      return 0
    else:
      return 1

class NotGate(UnaryGate):
  def __init__(self, n):
    UnaryGate.__init__(self, n)

  def performGateLogic(self):
    p = self.getPin()

    if p == 0:
      return 1
    else:
      return 0

class Connector:

  def __init__(self, fgate, tgate):
    self.fromgate = fgate
    self.togate = tgate

    tgate.setNextPin(self)

  def getFrom(self):
    return self.fromgate

  def getTo(self):
    return self.togate

  def setNextPin(self, source):
    if self.pinA == None:
      self.pinA = source
    else:
      if self.pinB == None:
        self.pinB = source
      else:
        raise RuntimeError("Erro: NÃO HÁ PINO LIVRE")

