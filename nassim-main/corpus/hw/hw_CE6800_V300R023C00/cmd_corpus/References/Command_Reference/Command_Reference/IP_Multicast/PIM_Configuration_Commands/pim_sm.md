pim sm
======

pim sm

Function
--------



The **pim sm** command enables PIM-SM on an interface.

The **undo pim sm** command restores the default configuration.



By default, PIM-SM is disabled on an interface.


Format
------

**pim sm**

**undo pim sm**


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

Enabling PIM-SM on an interface is the prerequisite for the interface to set up PIM neighbor relationships with other Routers and to process PIM messages. To enable PIM-SM on an interface, run the **pim sm** command.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Precautions**

* This command does not apply to MTunnel interfaces.
* The pim sm and **pim dm** commands are mutually exclusive.
* Running the **undo pim sm** command deletes PIM-SM configurations on an interface, affecting PIM services. Therefore, exercise caution when running this command.
* This command applies only to the tunnel interface view in GRE or TE encapsulation mode.
* PIM creates multicast routing entries based on unicast routes. If PIM is not configured on interfaces on the path after unicast route switching, PIM multicast routing entries cannot be created.



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Enable PIM-SM on VLANIF 1.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim sm

```