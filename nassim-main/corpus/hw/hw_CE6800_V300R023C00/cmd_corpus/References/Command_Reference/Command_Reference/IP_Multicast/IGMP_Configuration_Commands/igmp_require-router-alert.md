igmp require-router-alert
=========================

igmp require-router-alert

Function
--------



The **igmp require-router-alert** command configures an interface to accept only IGMP messages containing the Router-Alert option in IP headers.

The **undo igmp require-router-alert** command restores the default configuration.



By default, an interface accepts and processes all received IGMP messages, including the IGMP messages without the Router-Alert option.


Format
------

**igmp require-router-alert**

**undo igmp require-router-alert**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a packet carries the Router-Alert option, the packet needs to be sent to the routing protocol layer for processing. The **igmp require-router-alert** command enables a device to accept only IGMP messages carrying the Router-Alert option, thus improving IGMP security.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

After the **igmp require-router-alert** command is run on an interface, the interface checks whether a received IGMP message carries the Router-Alert option. If the IGMP message does not carry the Router-Alert option, the interface discards the IGMP message.NOTE:The **igmp require-router-alert** command is valid for IGMPv2 and IGMPv3. In IGMPv1, an interface does not check whether a received IGMP message carries the Router-Alert option, even if the **igmp require-router-alert** command is run on the interface.

**Precautions**

The function of the **igmp require-router-alert** command is the same as the function of the **require-router-alert** command in the IGMP view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Configure VLANIF 1 to discard IGMP messages without the Router-Alert option.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp require-router-alert

```