ntp manycast-server ipv6
========================

ntp manycast-server ipv6

Function
--------

The **ntp manycast-server ipv6** command enables the manycast server mode configures on an interface of a local device to send NTP manycast packets.

The **undo ntp manycast-server ipv6** command disables the NTP manycast server mode.

By default, the manycast service is not configured.



Format
------

**ntp manycast-server ipv6** [ *ipv6-address* ]

**undo ntp manycast-server ipv6** [ *ipv6-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** *ipv6-address* | Specifies a manycast IPv6 address. | The default value is FF0E::0101. |




Views
-----

100GE interface view,10GE interface view,25GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

A manycast server responds to manycast client packets. Based on the responses, a manycast client creates an ephemeral association and works in client server mode.

If you configure a manycast server on an interface, the interface can receive NTP manycast messages, and the local device runs in server mode.If you execute the
**undo ntp manycast-server ipv6** command and do not specify a multicast IP address, a local device searches for default IP addresses. The multicast server with default IP address is FF0E::101 on an IPv6 address. If the local device finds a default IP address, this command deletes the manycast server configuration, or it does not perform any action.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when you delete this command.

On an IPv6 network, multiple primary IPv6 addresses can be configured for a source interface. By default, the system uses the latest updated IPv6 address as the source address of the NTP manycast server. To ensure that the server can receive and process packets from clients, you need to configure this address as the source address for listening on the NTP server.If the source interface through which the configuration is delivered is deleted, the NTP manycast server is deleted.

Example
-------

# Configure Vlanif 100 to receive NTP multicast packets with the multicast address of FF0E::0101.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[*HUAWEI] interface Vlanif 100
[*HUAWEI-Vlanif100] ipv6 enable
[*HUAWEI-Vlanif100] ntp manycast-server ipv6 FF0E::0101

```