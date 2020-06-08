from ipmisim.ipmisim import IpmiServer, IpmiServerContext
import pytest
import socketserver

from threading import Thread


@pytest.fixture(scope='session')
def ipmiserver():
    context = IpmiServerContext()
    server = socketserver.UDPServer(('0.0.0.0', 9999), IpmiServer)
    t = Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    yield server.server_address, context.bmc
    server.shutdown()
