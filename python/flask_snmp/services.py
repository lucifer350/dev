from pysnmp.hlapi import *

def get_bulk(target, mib):
    iterator = nextCmd(
        SnmpEngine(),
        CommunityData('public'),
        UdpTransportTarget((target, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(mib))
    )
    results = {}
    for errorIndication, errorStatus, errorIndex, varBinds in iterator :
        if errorIndex or errorIndication or errorStatus:
            return 'snmp get error'
        for var in varBinds :
            key = str(var).split('=')[0]
            value = str(var).split('=')[1]
            results[key] = value
    return results


def get_snmp(target, mib, var):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('public'),
        UdpTransportTarget((target, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(mib, var, 0))
    )
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndex or errorIndication or errorStatus:
        return 'snmp get error'
    return str(varBinds[0])

if __name__=='__main__':
    #print(get_snmp('www.esisa.ac.ma', 'SNMPv2-MIB', 'sysName'))
    print(get_bulk('www.esisa.ac.ma', 'SNMPv2-MIB'))
    '''sysORID'''