nbns-list
=========

nbns-list

Function
--------

The **nbns-list** command configures the NetBIOS server address in the IP address pool view.

The **undo nbns-list** command deletes a configured NetBIOS server address.

By default, no NetBIOS server address is configured.



Format
------

**nbns-list** *ip-address* &<1-8>

**undo nbns-list** { *ip-address* | **all** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the NetBIOS server address. | The value is in dotted decimal notation. A maximum of eight NetBIOS server addresses can be configured. These IP addresses are separated by spaces. |
| **all** | Deletes all NetBIOS server addresses. | - |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. Before hosts communicate with each other, a NetBIOS server needs to resolve the accessedNetBIOS hostname to an IP address. To enable hosts to communicate with each other, run the **nbns-list** command to configure NetBIOS server addresses. When assigning IP addresses to clients, a DHCP server also assigns the configured NetBIOS server addresses to clients. To configure NetBIOS server addresses for an interface address pool, run the **dhcp server nbns-list** command.

**Prerequisites**

A global IP address pool has been created using the ip pool command.

**Precautions**

In the IP address pool view, a device can be configured with a maximum of eight NetBIOS server addresses respectively. The first assigned address functions as the primary address, and the other seven addresses function as secondary addresses.



Example
-------

# In the IP address pool view, set the IP address of the NetBIOS server to 192.168.1.1.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] nbns-list 192.168.1.1

```