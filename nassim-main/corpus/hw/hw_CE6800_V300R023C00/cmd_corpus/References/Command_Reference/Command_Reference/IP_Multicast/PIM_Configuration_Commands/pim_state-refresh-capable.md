pim state-refresh-capable
=========================

pim state-refresh-capable

Function
--------



The **pim state-refresh-capable** command enables State-Refresh on an interface.

The **undo pim state-refresh-capable** command disables State-Refresh on an interface.



By default, PIM-DM State-Refresh is enabled on an interface. The default configuration takes effect only after the pim dm command is run on the interface.


Format
------

**pim state-refresh-capable**

**undo pim state-refresh-capable**


Parameters
----------

None

Views
-----

100ge sub-interface view,10GE sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The PIM-DM status is refreshed based on Status-Refresh messages periodically sent on the network. Upon receipt of a Status-Refresh message, a Router in the Prune state resets the Prune status timer. This implementation prevents the downstream interfaces from forwarding data when the timer expires.When Status-Refresh is disabled, interfaces start to forward multicast data when the Prune timer expires. The downstream Router that rejects the data then sends Prune messages. However, this process repeats itself periodically, occupying a lot of network resources. It is advised to enable Status-Refresh, because this allows you to save network resources. If all users receive multicast data, State-Refresh can be disabled.

**Prerequisites**

Multicast has been enabled using the **multicast routing-enable** command.

**Precautions**

The **pim state-refresh-capable** command does not apply to interfaces bound to VPNs.


Example
-------

# Disable PIM-DM State-Refresh on VLANIF 1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] undo pim state-refresh-capable

```