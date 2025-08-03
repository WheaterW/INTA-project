bfd session-up check
====================

bfd session-up check

Function
--------



The **bfd session-up check** command enables the BFD session establishment check function.

The **undo bfd session-up check** command disables the BFD session establishment check function.



By default, the BFD session establishment check function is disabled.


Format
------

**bfd session-up check**

**undo bfd session-up check**


Parameters
----------

None

Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the Layer 2 network is normal, the IS-IS neighbor relationship can be established and routes can be delivered. However, the Layer 3 network is unreachable. As a result, upper-layer traffic is lost. To resolve Layer 3 network faults, run the **bfd session-up check** command in the IS-IS process view so that the IS-IS neighbor relationship can be established only after a BFD session is established on the corresponding interface. After this function is configured, it applies only to the neighbor relationships to be established (it does not apply to existing neighbor relationships).

**Precautions**

* After this command is run, a BFD session may be successfully established before the upgrade, but an abnormal BFD session fails to be established after the upgrade. As a result, the IS-IS neighbor relationship cannot be established after the upgrade. Therefore, exercise caution when running this command.
* After the command is run, the time for establishing a neighbor relationship is affected by the time for establishing a BFD session.
* On an IS-IS broadcast network, P2P two-way handshake, IS-IS multi-instance, or IS-IS multi-topology network, BFD session establishment check does not take effect even if the **bfd session-up check** command is run.

Example
-------

# Configure BFD for IS-IS.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] bfd session-up check

```