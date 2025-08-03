checkzero
=========

checkzero

Function
--------



The **checkzero** command enables the check on the Must-Be-Zero field in RIP packets.

The **undo checkzero** command cancels the check on the Must-Be-Zero field to save CPU resources. When the check is not required (that is, all neighbors are trusted), you can run this command to cancel the check.



By default, the check on the Must-Be-Zero field in RIP packets is enabled.


Format
------

**checkzero**

**undo checkzero**


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

The checkzero command is valid for RIP packets. For RIP-2 packets, only the packet header contains the Must-Be-Zero field.

**Configuration Impact**

By default, the device rejects all RIP packets whose MBZ field is not 0.To allow a Huawei device to communicate with a non-Huawei device that allows non-zero values in the MBZ field, run the **undo checkzero** command on the Huawei device. This configuration is not recommended because it may increase security risks.


Example
-------

# Enable the check on the Must-Be-Zero field in RIP packets.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] checkzero

```