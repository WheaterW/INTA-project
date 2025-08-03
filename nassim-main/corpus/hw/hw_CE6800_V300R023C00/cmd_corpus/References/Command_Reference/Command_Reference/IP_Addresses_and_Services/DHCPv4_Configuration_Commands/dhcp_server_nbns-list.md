dhcp server nbns-list
=====================

dhcp server nbns-list

Function
--------

The **dhcp server nbns-list** command configures Network Basic Input Output System (NetBIOS) server addresses for an interface address pool.

The **undo dhcp server nbns-list** command deletes the NetBIOS server address from an interface address pool.

By default, no NetBIOS server address is configured for an interface address pool.



Format
------

**dhcp server nbns-list** *ip-address* &<1-8>

**undo dhcp server nbns-list** { *ip-address* | **all** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the NetBIOS server address. | The value is in dotted decimal notation. |
| **all** | Deletes all NetBIOS server addresses. | - |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. Before hosts communicate with each other, a NetBIOS server needs to resolve the accessed NetBIOS hostname to an IP address. To enable hosts to communicate with each other, run the **dhcp server nbns-list** command to configure NetBIOS server addresses for an interface address pool. When assigning IP addresses to clients, a DHCP server also assigns the configured NetBIOS server addresses to clients. To configure NetBIOS server addresses for a global address pool, run the **nbns-list** command.

**Prerequisites**

* The address of an interface address pool has been configured using the **ip address** command.
* The DHCP server function has been enabled on the interface using the **dhcp select interface** command.

**Precautions**

Each interface can be configured with a maximum of eight NetBIOS server addresses. The first assigned address functions as the primary address, and other addresses function as secondary addresses.



Example
-------

# Specify a NetBIOS server at 192.168.1.99 for domain name resolution when IP addresses in the interface address pool on
100GE
1/0/1 are assigned to clients.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.10.10.10 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server nbns-list 192.168.1.99

```