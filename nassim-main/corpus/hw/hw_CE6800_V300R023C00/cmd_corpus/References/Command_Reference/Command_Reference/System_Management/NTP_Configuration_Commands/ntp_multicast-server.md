ntp multicast-server
====================

ntp multicast-server

Function
--------

The **ntp multicast-server** command configures an interface on the local device to send NTP multicast packets. The local device runs in the multicast server mode.

The **undo ntp multicast-server** command removes the local device from the NTP multicast server mode.

By default, the multicast service is not configured.



Format
------

**ntp multicast-server** [ *ip-address* ] [ **authentication-keyid** *key-id* | **ttl** *ttl-number* | **version** *number* | **port** *port-number* ] \*

**undo ntp multicast-server** [ *ip-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **authentication-keyid** *key-id* | Specifies a key ID used when sending messages to a multicast client. | The value is an integer ranging from: 1 to 4294967295 (version 1 to 3), or 1 to 65535 (version 4). |
| **ttl** *ttl-number* | Specifies the life span of multicast packets. | The value is an integer ranging from 1 to 255. |
| **version** *number* | Specifies an NTP version number. | The value is an integer ranging from 1 to 4. The default value is 3. |
| **port** *port-number* | Specifies the port number to be used as the destination port in NTP multicast packets. | The number is an integer that can be 123, or ranges from 1025 to 65535. The default value is 123. |
| **multicast-server** *ip-address* | Specifies a multicast IPv4 address, which is a Class D address. | The value is in dotted decimal notation. The default IP address is 224.0.1.1. |




Views
-----

100GE interface view,10GE interface view,25GE interface view,400GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

You can configure a device to determine whether NTP multicast packets need to be sent through an existing interface to a configured multicast group address or not. Based on this, the local device acts as multicast server and sends multicast messages periodically for time synchronization to multicast clients.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command in the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when this command is deleted.

If the source interface through which the configuration is delivered is deleted, the NTP multicast server is deleted.

Example
-------

# Configure Vlanif 100 to send NTP multicast packets through port 5000.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ntp multicast-server port 5000

```

# Configure Vlanif 100 to send NTP multicast packets. The multicast address is 224.0.1.1.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ip address 10.1.1.1 24
[~HUAWEI-Vlanif100] ntp multicast-server 224.0.1.1

```