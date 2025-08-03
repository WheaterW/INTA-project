stp config-digest-snoop (Layer 2 interface view)
================================================

stp config-digest-snoop (Layer 2 interface view)

Function
--------



The **stp config-digest-snoop** command enables digest snooping.

The **undo stp config-digest-snoop** command disables digest snooping.



By default, digest snooping is disabled.


Format
------

**stp config-digest-snoop**

**undo stp config-digest-snoop**


Parameters
----------

None

Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a Multiple Spanning Tree Protocol (MSTP) network where Huawei and non-Huawei devices are interconnected, if the Huawei and non-Huawei devices have the same region name, revision level, and VLAN mapping table but different bridge protocol data unit (BPDU) keys, the two devices cannot communicate. To enable the two devices to communicate with each other, run the stp config-digest-snoop command.




Example
-------

# Enable digest snooping on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp config-digest-snoop

```