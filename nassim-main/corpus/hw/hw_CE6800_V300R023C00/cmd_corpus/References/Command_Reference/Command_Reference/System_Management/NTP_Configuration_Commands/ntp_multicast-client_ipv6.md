ntp multicast-client ipv6
=========================

ntp multicast-client ipv6

Function
--------

The **ntp multicast-client ipv6** command configures a local device to work in NTP multicast client mode.

The **undo ntp multicast-client ipv6** command removes a local device from the NTP multicast client mode.

By default, the multicast client service is disabled.



Format
------

**ntp multicast-client ipv6** [ *ipv6-address* ]

**undo ntp multicast-client ipv6** [ *ipv6-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** *ipv6-address* | Specifies a multicast IPv6 address. | The default value is FF0E::0101. |




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

If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when you delete this command.

The NTP authentication key has been set by running the
**ntp authentication-keyid authentication-mode** command.If the source interface delivered by the configuration is deleted, the NTP multicast client is deleted.

Example
-------

# Configure vlanif100 to receive NTP IPv6 multicast messages with the multicast address of FF0E::111.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWEI-vlan100] quit
[*HUAWEI] interface Vlanif 100
[*HUAWEI-Vlanif100] ipv6 enable
[*HUAWEI-Vlanif100] ntp multicast-client ipv6 FF0E::111

```