ntp receive disable
===================

ntp receive disable

Function
--------

The **ntp receive disable** command disables receiving NTP packets.

The **undo ntp receive disable** command enables receiving NTP packets.

By default, an interface is enabled to receive NTP packets.



Format
------

**ntp receive disable**

**undo ntp receive disable**



Parameters
----------

None


Views
-----

100GE interface view,10GE interface view,25GE interface view,400GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The **ntp receive disable** command provides a method for access control. When the device does not need to synchronize with the external clock or provide the reference clock source for the external clock, you can run this command on the interface connected to the external clock to disable the interface from receiving NTP packets.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command in the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file.



Example
-------

# Disable Vlanif 100 from receiving NTP packets.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ntp receive disable

```