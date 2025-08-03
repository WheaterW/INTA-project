arp gratuitous-arp send disable
===============================

arp gratuitous-arp send disable

Function
--------

The **arp gratuitous-arp send disable** command disables an interface from sending gratuitous ARP packets.

The **undo arp gratuitous-arp send disable** command restores the default configuration.

By default, the function of periodically sending gratuitous ARP packets on an interface is not enabled or disabled. Instead, the global configuration policy is used.

* If the function of periodically sending gratuitous ARP packets is enabled globally, this function is also enabled on the interface.
* If the function of periodically sending gratuitous ARP packets is disabled globally, this function is also disabled on the interface.



Format
------

**arp gratuitous-arp send disable**

**undo arp gratuitous-arp send disable**



Parameters
----------

None


Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Sub-interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

If a device has a lot of interfaces that are Up and have IP addresses configured, enabling the device to send gratuitous ARP packets will consume excessive CPU resources, affecting services. To resolve this problem, run the arp gratuitous-arp send disable command on a specified interface to disable the interface from sending gratuitous ARP packets.

**Configuration Impact**

Using the arp gratuitous-arp send disable command will prevent sending gratuitous arp packet, and may cause IP collision detection failure and services to be interrupted. Exercise caution when running this command.



Example
-------

# Disable an interface from sending gratuitous ARP packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/3
[~HUAWEI-100GE1/0/3] undo portswitch
[*HUAWEI-100GE1/0/3] arp gratuitous-arp send disable

```