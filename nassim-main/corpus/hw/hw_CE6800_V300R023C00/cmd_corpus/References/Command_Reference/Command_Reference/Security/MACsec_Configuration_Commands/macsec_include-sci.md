macsec include-sci
==================

macsec include-sci

Function
--------



The **macsec include-sci** command configures the device to add an SCI to the MACsec frame header.

The **undo macsec include-sci** command configures the device not to add an SCI to the MACsec frame header.



By default, a MACsec frame header contains an SCI.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**macsec include-sci**

**undo macsec include-sci**


Parameters
----------

None

Views
-----

mac security profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

An SCI identifies the source of a packet. It consists of the MAC address of an interface and the last two bytes of the interface index. When the device is connected to a non-Huawei device and MACsec is configured on them, the MACsec frame header may need to contain the SCI to identify the source of packets because the implementation of MACsec on the device is different from that on the non-Huawei device. Currently, the device supports only device-to-device MACsec. The two MACsec-enabled interfaces on both devices only establish a session with each other. In this case, the MACsec frame header does not need to contain an SCI.

**Precautions**



The settings of whether MACsec frame headers contain SCI must be the same at both ends. That is, MACsec frame headers contain SCI or do not contain SCI at both ends.




Example
-------

# Configure the device to add an SCI to the MACsec frame header in the MACsec profile named test.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test] macsec include-sci

```