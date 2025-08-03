multicast routing-enable (VPN instance view)
============================================

multicast routing-enable (VPN instance view)

Function
--------



The **multicast routing-enable** command enables the multicast function.

The **undo multicast routing-enable** command restores the default configuration.



By default, the multicast function is disabled. When the multicast function is not enabled, the Router cannot forward multicast packets.


Format
------

**multicast routing-enable**

**undo multicast routing-enable**


Parameters
----------

None

Views
-----

VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The multicast function should be enabled before you configure all the multicast commands.

**Precautions**

After the **undo multicast routing-enable** command is run, all the multicast configurations of the public network instance is cleared. If the multicast services are running in the instance, the multicast services are interrupted when this command is executed. To restore the multicast service on the instance, you must re-configure the corresponding commands.


Example
-------

# Enable the multicast function in a VPN instance mytest.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance mytest
[*HUAWEI-vpn-instance-mytest] ipv4-family
[*HUAWEI-vpn-instance-mytest-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-mytest-af-ipv4] quit
[*HUAWEI-vpn-instance-mytest] multicast routing-enable

```