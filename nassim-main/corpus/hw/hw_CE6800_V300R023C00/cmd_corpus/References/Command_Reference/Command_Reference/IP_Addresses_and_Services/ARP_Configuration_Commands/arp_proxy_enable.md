arp proxy enable
================

arp proxy enable

Function
--------



The **arp proxy enable** command enables routed proxy Address Resolution Protocol (ARP) on an interface.

The **undo arp proxy enable** command disables routed proxy ARP on an interface.



By default, routed proxy ARP is disabled on interfaces.


Format
------

**arp proxy enable**

**undo arp proxy enable**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When two hosts reside on different network segments and do not have default gateways configured, run this command on the device that connects to the two hosts to enable routed proxy ARP. This configuration implements IP address resolution between the two hosts.

**Precautions**



The network IDs of the IP addresses of the hosts on each subnet must be the same. The default gateway does not need to be configured on the hosts.This command supports routed proxy for interfaces on different gateways.Routed proxy ARP is not supported in the following situations:The arp l2-proxy enable command has been run in the BD view of the VBDIF interface on which routed proxy ARP needs to be configured.




Example
-------

# Enable routed proxy ARP on the interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] arp proxy enable

```