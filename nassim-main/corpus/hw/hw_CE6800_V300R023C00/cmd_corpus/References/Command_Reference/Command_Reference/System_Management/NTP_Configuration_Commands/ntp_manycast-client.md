ntp manycast-client
===================

ntp manycast-client

Function
--------

The **ntp manycast-client** command enables the NTP manycast client mode.

The **undo ntp manycast-client** command disables the NTP manycast client mode.

By default, the manycast client service is disabled.



Format
------

**ntp manycast-client** [ *ip-address* ] [ **authentication-keyid** *key-id* | **ttl** *ttl-number* | **port** *port-number* ] \*

**undo ntp manycast-client** [ *ip-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a manycast IPv4 address, which is a Class D address. | The value is in dotted decimal notation. The default value is 224.0.1.1. |
| **authentication-keyid** *key-id* | Specifies an authentication key ID number carried in messages to be sent to multicast clients. | The value is an integer ranging from 1 to 65535. |
| **ttl** *ttl-number* | Specifies the life span of the manycast packet. | The value is an integer ranging from 1 to 255. The default value is 255. |
| **port** *port-number* | Sets the port number to be used as the destination port in NTP manycast packets. | The value is 123 or an integer ranging from 1025 to 65535. The default value is 123. |




Views
-----

100GE interface view,10GE interface view,25GE interface view,400GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

An interface can be specified on the local device and used to send NTP manycast messages after a timeout period elapses. The local device runs in manycast client mode and periodically sends manycast messages to a manycast server. Based on the message sent by the manycast server, a dynamic client-server association is established.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when this command is deleted.

If the source interface through which the configuration is delivered is deleted, the NTP manycast client is deleted.

Example
-------

# Configure vlanif100 to receive NTP manycast messages with the manycast address being 224.0.1.2.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ntp manycast-client 224.0.1.2

```