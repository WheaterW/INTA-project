netstream export packet-len ethernet-crc
========================================

netstream export packet-len ethernet-crc

Function
--------



The **netstream export packet-len ethernet-crc** command configures the IN\_BYTES field value in NetStream packets to include the Ethernet header and CRC lengths.

The **undo netstream export packet-len ethernet-crc** command restores the default setting.



By default, the value of the IN\_BYTES field in the NetStream packet sent by the device is the value of the len field in the IP packet header.


Format
------

**netstream export packet-len ethernet-crc**

**undo netstream export packet-len ethernet-crc**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

By default, the **IN\_BYTES** field value in NetStream packets is the **len** field value in the IP packet header. Some servers do not count the Ethernet header and CRC lengths when parsing NetStream packets. As a result, the traffic statistics are incorrect. To resolve this problem, run the **netstream export packet-len ethernet-crc** command to configure the **IN\_BYTES** field value in NetStream packets to include the Ethernet header and CRC lengths.


Example
-------

# Configure the IN\_BYTES field value in exported NetStream packets to include the Ethernet header and CRC length.
```
<HUAWEI> system-view
[~HUAWEI] netstream export packet-len ethernet-crc

```