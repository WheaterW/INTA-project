ntp multicast-client
====================

ntp multicast-client

Function
--------

The **ntp multicast-client** command configures a local device to work in NTP multicast client mode.

The **undo ntp multicast-client** command removes a local device from the NTP multicast client mode.

By default, the multicast client service is disabled.



Format
------

**ntp multicast-client** [ *ip-address* ]

**undo ntp multicast-client** [ *ip-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a multicast IPv4 address, which is a Class D address. | The value is in dotted decimal notation. The default IP address is 224.0.1.1. |




Views
-----

100GE interface view,10GE interface view,25GE interface view,400GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

If a device is configured to receive NTP multicast packets on an interface, the local device is in multicast-client mode.

If the valid multicast server is configured, the local device gets synchronized with the multicast server. The local device time is updated with the time of the server.

**Follow-up Procedure**

Run the **display ntp sessions** commands to check the sessions formed between the multicast server and local device.

NOTE: You can configure more than one multicast client each with a specific multicast IP addresses on the same interface.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when this command is deleted.

If the source interface through which the configuration is delivered is deleted, the NTP multicast client is deleted.

Example
-------

# Configure Vlanif 100 to receive NTP multicast messages with the multicast address being 224.0.1.2.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ip address 10.1.1.1 24
[~HUAWEI-Vlanif100] ntp multicast-client 224.0.1.2

```