arp proxy intra-vlan enable
===========================

arp proxy intra-vlan enable

Function
--------



The **arp proxy intra-vlan enable** command enables intra-VLAN proxy ARP.

The **undo arp proxy intra-vlan enable** command disables intra-VLAN proxy ARP.



By default, intra-VLAN proxy ARP is disabled.


Format
------

**arp proxy intra-vlan enable**

**undo arp proxy intra-vlan enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,10GE sub-interface view,1200ge sub-interface view,200GE sub-interface view,25GE sub-interface view,400GE sub-interface view,50GE sub-interface view,Eth-Trunk sub-interface view,VLANIF interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If two hosts are within the same isolate-user-VLAN, communication between them on the Layer 2 network cannot be implemented. In this case, run the **arp proxy intra-vlan enable** command on the associated VLAN interface to enable intra-VLAN proxy ARP. This configuration implements communication between the hosts within an isolate-user-VLAN.



**Prerequisites**



Hosts that require communication are within the same VLAN, and it is an isolate-user-VLAN.




Example
-------

# Enable intra-VLAN proxy ARP on a VLANIF interface.
```
<HUAWEI> system-view
[~HUAWEI] vlan 20
[*HUAWEI-vlan20] quit
[*HUAWEI] interface vlanif 20
[*HUAWEI-vlanif20] arp proxy intra-vlan enable

```