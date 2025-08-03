stp agreement-legacy
====================

stp agreement-legacy

Function
--------



The **stp agreement-legacy** command configures an interface to discard non-standard STP/RSTP packets sent by the HanDreamnet switch.

The **undo stp agreement-legacy** command cancels the configuration.



By default, an interface does not discard non-standard STP/RSTP packets sent by the HanDreamnet switch.


Format
------

**stp agreement-legacy**

**undo stp agreement-legacy**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a Huawei device and a HanDreamnet switch are deployed on a VBST network, non-standard STP/RSTP packets sent by the HanDreamnet switch may cause temporary loops. You can run the **stp agreement-legacy** command to configure an interface to discard non-standard STP/RSTP packets to prevent temporary loops.


Example
-------

# Configure the interface to discard non-standard STP/RSTP packets sent by the HanDreamnet switch.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp agreement-legacy

```