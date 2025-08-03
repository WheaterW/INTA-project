igmp enable
===========

igmp enable

Function
--------



The **igmp enable** command enables IGMP on an interface.

The **undo igmp enable** command disables IGMP on an interface.



By default, IGMP is disabled on an interface.


Format
------

**igmp enable**

**undo igmp enable**


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

To enable a Router interface that connects to user hosts to process IGMP messages, run the **igmp enable** command to enable IGMP on the interface. IGMP must be enabled both on user hosts and Router interfaces that connect to the user hosts.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

IGMP parameters that are configured on an interface before IGMP is enabled on this interface take effect only after the **igmp enable** command is run on the interface.

**Precautions**



During the upgrade in CFG mode, if the **igmp enable** command has been run on the interface connected to users, the device automatically enables the **pim sm** command to prevent traffic interruption caused by PIM disabling.After the **undo igmp enable** command is run on a VBDIF interface, Layer 2 multicast configurations in the BD are also deleted.When a BD is bound to a VNI and a multicast group is configured for the VNI, IGMP cannot be enabled in the VBDIF interface view.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Enable IGMP on VLANIF 1 connected to user hosts.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] quit
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim sm
[*HUAWEI-Vlanif1] igmp enable

```