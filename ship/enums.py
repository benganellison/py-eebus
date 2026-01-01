from enum import Enum


class MessageType(bytes, Enum):
    MSG_TYPE_INIT = b'\x00'
    MSG_TYPE_CONTROL = b'\x01'
    MSG_TYPE_DATA = b'\x02'
    MSG_TYPE_END = b'\x03'

    def __str__(self):
        return self.value


class ConnectionHelloPhaseType(str, Enum):
    PENDING = 'pending'
    READY = 'ready'
    ABORTED = 'aborted'

    def __str__(self):
        return self.value


class ProtocolHandshakeTypeType(str, Enum):
    ANNOUNCEMAX = 'announceMax'
    SELECT = 'select'

    def __str__(self):
        return self.value


class PinStateType(str, Enum):
    REQUIRED = 'required'
    OPTIONAL = 'optional'
    PINOK = 'pinOk'
    NONE = 'none'

    def __str__(self):
        return self.value


class PinInputPermissionType(str, Enum):
    BUSY = 'busy'
    OK = 'ok'

    def __str__(self):
        return self.value


class ConnectionClosePhaseType(str, Enum):
    ANNOUNCE = 'announce'
    CONFIRM = 'confirm'

    def __str__(self):
        return self.value


class ConnectionCloseReasonType(str, Enum):
    UNSPECIFIC = 'unspecific'
    REMOVEDCONNECTION = 'removedConnection'

    def __str__(self):
        return self.value

