arp learning disable
====================

arp learning disable

Function
--------



The **arp learning disable** command disables the dynamic Address Resolution Protocol (ARP) entry learning function on an interface.

The **undo arp learning disable** command enables the dynamic ARP entry learning function on an interface.



By default, the dynamic ARP entry learning function is enabled on an interface.


Format
------

**arp learning disable**

**undo arp learning disable**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To ensure network security or facilitate network management, you can enable or disable dynamic ARP entry learning on an interface. You can run the arp learning disable command together with the arp-limit or arp learning strict command to better control dynamic ARP entry learning on an interface.



**Configuration Impact**

If dynamic ARP entry learning is disabled on an interface, traffic forwarding may fail on this interface.

**Precautions**

After dynamic ARP entry learning is disabled on an interface, the system will not automatically delete the ARP entries that were learnt previously on this interface. You can choose to delete or retain these dynamic ARP entries as required.


Example
-------

# Enable dynamic ARP entry learning on the specified interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] undo arp learning disable

```

# Disable dynamic ARP entry learning on the specified interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] arp learning disable

```