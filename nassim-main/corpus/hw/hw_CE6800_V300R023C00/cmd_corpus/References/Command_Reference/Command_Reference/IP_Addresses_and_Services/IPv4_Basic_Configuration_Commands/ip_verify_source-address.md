ip verify source-address
========================

ip verify source-address

Function
--------



The **ip verify source-address** command configures source address validity check on the packets received from an interface so that packets with invalid source address can be dropped.

The **undo ip verify source-address** command cancels the configuration.



By default, an interface does not perform source address validity check on the packets received.


Format
------

**ip verify source-address**

**undo ip verify source-address**


Parameters
----------

None

Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Standard protocols define the IP source address scope as follows:

* Broadcast addresses of Class A through Class C cannot be used as the source address.
* Class D addresses, which are used for IP multicasting, cannot be used as the source address.
* Class E addresses are reserved for experimental use and therefore cannot be used as the source address.
* All Fs addresses cannot be used as the source address.
* The address on network 127 cannot be used as the source address on the network outside the host.In actual situations, these addresses may still be used as the source address. For example, Class A through Class C addresses may have a 32-bit mask, and the broadcast addresses of Class A through Class C are available. By default, the source address filtering function is disabled.If a user discovers that a device has encountered a malicious packet attack with the source address as a broadcast or multicast address, run the ip verify source-address command to filter this type of address in packets in order to improve device security.

Example
-------

# Enable source address validity check on the packets received from the 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip verify source-address

```