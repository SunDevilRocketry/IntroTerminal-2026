#terminalserial.py
import serial
import serial.tools.list_ports


class SerialTerminal:
    def __init__(self, comport = None, baudrate = None, timeout = None):
        self.__comport = comport
        self.__baudrate = baudrate
        self.__timeout = timeout
        self.serialinfo = None

    def read(self, num_bytes):
        #pyserial read
        return self.serialinfo.read(num_bytes)
    
    def write(self, write_byte):
        #pyserial write
        self.serialinfo.write(write_byte)
    
    def connect(self, comport ,baudrate):
        #open com ports
        open(comport,baudrate)

        self.serialinfo = serial.Serial(comport, baudrate)

    def get_available_ports(self):
        ports = serial.tools.list_ports.comports()
        return ports

    def getSerialObject(self):
        return self.serialinfo
    
    def setComport(self, comport):
        self.__comport = comport
    
    def getComport(self):
        return self.__comport
    
    def setBaudrate(self, baudrate):
        self.__baudrate = baudrate\
        
    def getBaudrate(self):
        return self.__baudrate