import os
import mouseSeal as process

def check_pid():        
    """ Check For the existence of a unix pid. """
    pid = process.getPid()
    if os.path.isdir('/proc/{}'.format(pid)):
        return True
    return False