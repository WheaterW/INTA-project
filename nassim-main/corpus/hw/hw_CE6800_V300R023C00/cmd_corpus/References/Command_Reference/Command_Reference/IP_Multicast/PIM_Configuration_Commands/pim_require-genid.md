pim require-genid
=================

pim require-genid

Function
--------



The **pim require-genid** command configures a PIM interface to reject a Hello message without a generation ID.

The **undo pim require-genid** command restores the default configuration.



By default, a PIM interface permits a Hello message without a generation ID.


Format
------

**pim require-genid**

**undo pim require-genid**


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

After PIM-SM is enabled on an interface of a router, the router generates a random number as the generation ID for Hello messages. Each time the router status changes, the router generates a new generation ID.If a router receives a Hello message that contains a changed generation ID from the same PIM neighbor, the router considers that the PIM neighbor status has changed. In this manner, the router can detect status changes of its neighbors. To configure a PIM interface to reject Hello messages without a generation ID, run the pim require-genid command, improving communication security.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

After the pim require-genid command s run, the Router sets up PIM neighbor relationships only with devices that send Hello messages with a generation ID.

**Precautions**



Only CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885-SAN, CE6885, CE6885-LL(standard forwarding mode), CE6885-T, CE6863E-48S8CQ support this command in the VBDIF interface view.




Example
-------

# Configure vlanif 1 to reject the Hello messages without the Generation ID.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] vlan 1
[*HUAWEI-vlan1] quit
[*HUAWEI] interface Vlanif 1
[*HUAWEI-Vlanif1] pim require-genid

```