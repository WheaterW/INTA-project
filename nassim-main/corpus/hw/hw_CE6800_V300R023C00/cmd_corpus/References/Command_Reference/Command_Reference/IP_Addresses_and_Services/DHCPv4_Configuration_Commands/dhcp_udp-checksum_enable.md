dhcp udp-checksum enable
========================

dhcp udp-checksum enable

Function
--------



The **dhcp udp-checksum enable** command enables a device to add the UDP header checksum to DHCP packets to be sent.

The **undo dhcp udp-checksum enable** command disables a device from adding the UDP header checksum to DHCP packets to be sent.



By default, the UDP header checksum carried in DHCP packets sent by a device is 0, and the peer device does not verify the checksum.


Format
------

**dhcp udp-checksum enable**

**undo dhcp udp-checksum enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the peer device does not comply with protocol standards, the peer device still verifies the UDP header checksum when the checksum carried in DHCP packets is 0. In this case, you can run the **dhcp udp-checksum enable** command to enable the device to add the UDP header checksum to DHCP packets to be sent.

**Precautions**

A device can add the UDP header checksum to DHCP packets to be sent only if the device functions as a DHCP server.


Example
-------

# Enable a device to add the UDP header checksum to DHCP packets to be sent.
```
<HUAWEI> system-view
[~HUAWEI] dhcp udp-checksum enable

```