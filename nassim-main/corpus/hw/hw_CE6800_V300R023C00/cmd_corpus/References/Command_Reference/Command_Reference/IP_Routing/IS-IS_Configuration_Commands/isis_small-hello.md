isis small-hello
================

isis small-hello

Function
--------



The **isis small-hello** command configures an interface to send small-sized Hello packets without the padding field.

The **undo isis small-hello** command cancels the configuration.



By default, no small Hello packet with no padding field is configured on an interface.


Format
------

**isis small-hello**

**undo isis small-hello**


Parameters
----------

None

Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, P2P and broadcast interfaces send Hello packets based on the following rules:

* P2P interface
* Before a P2P neighbor relationship is established, standard Hello packets with the padding field are sent.
* After a P2P neighbor relationship is established, small Hello packets without the padding field are sent.The length of the padding field on a P2P interface is equal to the length of the locally generated LSP.
* Broadcast InterfaceStandard Hello packets with the padding field are sent.The length of the padding field on a broadcast interface is equal to the length of the MTU.When multiple logical interfaces configured on the same interface need to establish a large number of neighbor relationships, the interface frequently sends standard IS-IS Hello packets, which wastes network bandwidth. Therefore, you can run this command to simplify the sending and receiving of Hello packets and reduce the waste of bandwidth.

The MTU used by IS-IS IPv4 and IPv6 is the MTU configured using the mtu (interface view) command, not the MTU configured using the **ipv6 mtu** command.

**Prerequisites**

An IS-IS process has been created on a specified interface.

**Precautions**

The isis small-hello and **isis padding-hello** commands are mutually exclusive and cannot be configured on the same interface.


Example
-------

# Configure 100GE1/0/1 to send the Hello packets without the padding field.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis small-hello

```