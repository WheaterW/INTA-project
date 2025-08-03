ntp broadcast-client
====================

ntp broadcast-client

Function
--------

The **ntp broadcast-client** command configures a device to work in NTP broadcast client mode.

The **undo ntp broadcast-client** command removes a device from NTP broadcast client mode.

By default, a device is not configured in NTP broadcast client mode.



Format
------

**ntp broadcast-client**

**undo ntp broadcast-client**



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

A local device automatically runs as a broadcast client once it is configured to receive NTP broadcast messages on a current interface.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the **ntp server disable** command to the configuration file to disable the NTP service. To enable the NTP service, run the **undo ntp server disable** command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the **ntp server disable** command from the configuration file when this command is deleted.

If the source interface through which the configuration is delivered is deleted, the NTP broadcast client is deleted.

Example
-------

# Configure Vlanif 100 to receive NTP broadcast messages.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ip address 10.1.1.1 24
[*HUAWEI-Vlanif100] ntp broadcast-client

```