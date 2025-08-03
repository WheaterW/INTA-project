isis padding-hello
==================

isis padding-hello

Function
--------



The **isis padding-hello** command configures a P2P interface to send Hello packets with the padding field after the neighbor relationship is established.

The **undo isis padding-hello** command restores the default configuration.



By default, a P2P interface sends Hello packets without the padding field after the neighbor relationship is established.


Format
------

**isis padding-hello**

**undo isis padding-hello**


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

By default, P2P and broadcast interfaces send IS-IS Hello packets based on the following rules:

* P2P interface
* Before a P2P neighbor relationship is established, standard Hello packets with the padding field are sent.
* After a P2P neighbor relationship is established, small Hello packets without the padding field are sent.The length of the padding field on a P2P interface is equal to the length of the locally generated LSP.
* Broadcast InterfaceStandard Hello packets with the padding field are sent.The length of the padding field on a broadcast interface is equal to the length of the MTU.The **isis padding-hello** command enables a device to send Hello packets to neighbors based on its MTU. If the interface of the neighboring device does not support the required MTU, the neighbor relationship cannot be established. This prevents large PDU loss and asynchronous LSDBs.The MTU used by IS-IS IPv4 and IPv6 is the MTU configured using the mtu (interface view) command, not the MTU configured using the **ipv6 mtu** command.

**Prerequisites**

An IS-IS process has been created on a specified interface.

**Configuration Impact**

The **isis padding-hello** command is used to configure an interface to send the standard Hello packets with the padding field. The **isis padding-hello** command and the **isis small-hello** command are mutually exclusive. The **isis small-hello** command is used to configure an interface to send the small-sized Hello packets without the padding field.


Example
-------

# Configure 100GE1/0/1 to send the standard IS-IS Hello packets with the padding field.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis padding-hello

```