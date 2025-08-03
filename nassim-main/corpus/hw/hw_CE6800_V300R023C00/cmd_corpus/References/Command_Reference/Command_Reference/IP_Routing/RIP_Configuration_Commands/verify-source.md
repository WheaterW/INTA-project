verify-source
=============

verify-source

Function
--------



The **verify-source** command verifies the source IP address of each received RIP Update packet.

The **undo verify-source** command disables the source IP address verification.



By default, source IP address verification is enabled.


Format
------

**verify-source**

**undo verify-source**


Parameters
----------

None

Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the source address verification is enabled, the device checks the source addresses of packets to determine whether the source addresses are in the same subnet as the local interface. Packets from different subnets are rejected by the device.

**Precautions**

You are advised not to disable this feature in normal conditions.


Example
-------

# Enable source IP address verification for all RIP packets received in RIP process 100.
```
<HUAWEI> system-view
[~HUAWEI] rip 100
[*HUAWEI-rip-100] verify-source

```