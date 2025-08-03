rip version 2 broadcast
=======================

rip version 2 broadcast

Function
--------



The **rip version 2 broadcast** command sets that RIP-2 packets are sent in broadcast mode.

The **undo rip version** command restores the default RIP version.



By default, the version running on an interface is 1.


Format
------

**rip version 2 broadcast**

**undo rip version**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **2** | Indicates RIP-2. | - |
| **broadcast** | Indicates that RIP-2 packets are sent in broadcast mode. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The versions of request and response packets vary with the configured RIP version.

* If the version of RIP is not set, a device sends RIP-1 packets in broadcast mode and receives the RIP-1 and RIP-2 packets that are sent in broadcast mode.
* If the RIP version is set to RIP-2, a device sends only RIP-2 packets in multicast mode and receives RIP-2 packets that are sent in multicast or broadcast mode.
* If the RIP version is set to broadcast RIP-2, a device sends RIP-2 packets in broadcast mode and receives RIP-1 and RIP-2 packets.

**Precautions**



You can also set a RIP version in a RIP process, but the RIP version that is set on an interface has a higher priority.




Example
-------

# Configure 100GE 1/0/1 to broadcast RIP-2 packets.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] rip version 2 broadcast

```