igmp send-router-alert disable
==============================

igmp send-router-alert disable

Function
--------



The **igmp send-router-alert disable** command configures an interface to send IGMP messages without the Router-Alert option in IP headers.

The **undo igmp send-router-alert disable** command restores the default setting.



By default, the IP headers of IGMP messages sent by an interface contain the Router-Alert option.


Format
------

**igmp send-router-alert disable**

**undo igmp send-router-alert disable**


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

The igmp send-router-alert command generally works together with the **igmp require-router-alert** command.The function of the igmp send-router-alert command is the same as the function of the **send-router-alert disable** command in the IGMP view. The configuration in the IGMP view is effective for all interfaces, whereas the configuration in the interface view is effective only for the specified interface. The configuration in the interface view takes precedence over the configuration in the IGMP view. The configuration in the IGMP view is used only when the configuration in the interface view is not available.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Configure vlanif 1 to send IGMP messages without the Router-Alert option in IP headers.
```
<HUAWEI> system-view
[~HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] igmp send-router-alert disable

```