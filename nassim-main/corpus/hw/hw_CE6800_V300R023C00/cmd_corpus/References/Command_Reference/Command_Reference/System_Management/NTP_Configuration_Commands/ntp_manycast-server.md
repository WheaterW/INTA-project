ntp manycast-server
===================

ntp manycast-server

Function
--------

The **ntp manycast-server** command enables the manycast server mode configures on an interface of a local device to send NTP manycast packets.

The **undo ntp manycast-server** command disables the NTP manycast server mode.

By default, the manycast service is not configured.



Format
------

**ntp manycast-server** [ *ip-address* ]

**undo ntp manycast-server** [ *ip-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a manycast IPv4 address, which is a Class D address. | The default value is 224.0.1.1. |




Views
-----

100GE interface view,10GE interface view,25GE interface view,400GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The manycast server responds to manycast client packets. Based on the response, manycast client creates ephemeral association and work in client/server mode.

If you configure a manycast server on the current interface, it is ready to receive NTP manycast packets, and the local device runs in the server mode.If you execute the
**undo ntp manycast-server** command without specifying the multicast IP address, the local device searches for default IP addresses. In IPv4 networks, the default IP address of the manycast server is 224.0.1.1. In IPv6 networks, the default IP address of the manycast server is FF0E::101. If the local device finds the default IP address, the
**undo ntp manycast-server** command takes effect; otherwise, the undo ntp manycast-server does not take effect.If the source interface delivered by the configuration is deleted, the NTP manycast server is deleted.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command in the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file.



Example
-------

# Configure Vlanif 100 to receive NTP manycast packets with the multicast address of the manycast packets being 224.0.1.1.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ntp manycast-server 224.0.1.1

```

# Configure multiple servers on the same interface. (The interface is capable to respond to manycast client requests sent by different multicast addresses.)
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ntp manycast-server 224.1.1.4
[*HUAWEI-Vlanif100] ntp manycast-server 224.1.1.5

```