arp gratuitous-arp send enable (interface view)
===============================================

arp gratuitous-arp send enable (interface view)

Function
--------

The **arp gratuitous-arp send enable** command enables an interface to periodically send gratuitous Address Resolution Protocol (ARP) packets.

The **undo arp gratuitous-arp send enable** command restores the default configuration.

By default, the function of periodically sending gratuitous ARP packets on an interface is not enabled or disabled. Instead, the global configuration policy is used.

* If the function of periodically sending gratuitous ARP packets is enabled globally, this function is also enabled on the interface.
* If the function of periodically sending gratuitous ARP packets is disabled globally, this function is also disabled on the interface.



Format
------

**arp gratuitous-arp send enable**

**undo arp gratuitous-arp send enable**



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

If an attacker counterfeits a gateway and sends users a forged ARP packet, these user terminals will record incorrect ARP entries and cannot send data to the correct gateway. To prevent this problem, run the arp gratuitous-arp send enable command to enable the gateway's interface to periodically send gratuitous ARP packets, thereby updating authorized users' ARP entries to be correct.

**Follow-up Procedure**

By default, after an interface is enabled to send gratuitous ARP packets, the interface sends them at an interval of 60s. To change the interval, you can run the **arp gratuitous-arp send interval** command.

**Precautions**

The periodic ARP packet sending function takes effect as follows:

* If this function is enabled in both the system view and interface view, the configuration in the interface view takes precedence.
* If this function is enabled only in the system view, the configuration in the system view takes effect.
* If this function is enabled only in the interface view, the configuration in the interface view takes effect.


Example
-------

# Enable an interface to periodically send gratuitous ARP packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/3
[~HUAWEI-100GE1/0/3] undo portswitch
[*HUAWEI-100GE1/0/3] arp gratuitous-arp send enable

```