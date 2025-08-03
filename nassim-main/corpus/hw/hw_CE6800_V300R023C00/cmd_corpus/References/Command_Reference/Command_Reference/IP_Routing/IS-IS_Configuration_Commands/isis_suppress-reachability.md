isis suppress-reachability
==========================

isis suppress-reachability

Function
--------



The **isis suppress-reachability** command suppresses the advertisement of interface IPv4 addresses so that interface addresses can be reused.

The **undo isis suppress-reachability** command restores the default configuration of an interface.



By default, interface addresses can be advertised.


Format
------

**isis suppress-reachability** [ **level-1** | **level-1-2** | **level-2** ]

**undo isis suppress-reachability**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Suppresses the advertisement of only Level-1 interface addresses. | - |
| **level-1-2** | Suppresses the advertisement of Level-1 and Level-2 interface addresses. | - |
| **level-2** | Suppresses the advertisement of only Level-2 interface addresses.  If no level is specified, the advertisement of Level-1-2 interface addresses is suppressed. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the interface is used only for topology connections, you can run the **isis suppress-reachability** command to prevent traffic from being diverted to the local device. In addition, the IPv4 address of the local interface can be hidden.


Example
-------

# Suppress the advertisement of the IPv4 address of 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis suppress-reachability

```