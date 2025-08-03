ntp ipv6 receive disable
========================

ntp ipv6 receive disable

Function
--------

The **ntp ipv6 receive disable** command disables an interface from receiving NTP packets.

The **undo ntp ipv6 receive disable** command enables an interface to receive NTP packets.

By default, an interface is enabled to receive NTP packets.



Format
------

**ntp ipv6 receive disable**

**undo ntp ipv6 receive disable**



Parameters
----------

None


Views
-----

100GE interface view,10GE interface view,25GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

When a device does not need to synchronize with an external clock or provide the reference clock source for the external clock, to disable an interface connected to the external device from receiving NTP packets, run the **ntp ipv6 receive disable** command.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command in the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file.



Example
-------

# Disable Vlanif 100 from receiving NTP packets.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ipv6 enable
[~HUAWEI-Vlanif100] ntp ipv6 receive disable

```