dhcp server lease
=================

dhcp server lease

Function
--------

The **dhcp server lease** command specifies the IP address lease for addresses in an interface address pool.

The **undo dhcp server lease** command restores the default IP address lease of addresses in an interface address pool.

By default, the IP address lease of addresses in an interface address pool is one day.



Format
------

**dhcp server lease** { **day** *day* [ **hour** *hour* [ **minute** *minute* ] ] | **unlimited** }

**undo dhcp server lease**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **day** *day* | Specifies the number of days. | The value is an integer ranging from 0 to 999. The default value is 1. |
| **hour** *hour* | Specifies the number of hours. | The value is an integer in the range from 0 to 23. The default value is <b>0</b>. |
| **minute** *minute* | Specifies the number of minutes in the IP address lease. | The value is an integer in the range from 0 to 59. The default value is <b>0</b>. |
| **unlimited** | Indicates that the IP address lease is unlimited. | - |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. To meet different client requirements, DHCP supports dynamic, automatic, and static address assignment.

DHCP clients require different IP address leases.

* If a host (such as the DNS server) needs to use a fixed IP address for a long time, run the **dhcp server lease unlimited** command to configure the IP address lease as unlimited.
* If a host (such as a portable computer) needs to use a temporary IP address, run the **dhcp server lease** command to specify an IP address lease. After the lease expires, the DHCP server withdraws the IP address and assigns the address to other clients.When a DHCP client starts and 50% or 87.5% of its IP address lease has passed, the DHCP client sends a DHCP Request message to the DHCP server to renew the lease.
* If the IP address can still be assigned to the client, the DHCP server informs the client of a renewed IP address lease.
* If the IP address can no longer be assigned to the client, the DHCP server informs the client that the IP address lease cannot be renewed.You can run the **display ip pool** command to view information about the IP address lease. The values of the lease and left fields in the command output indicate the configured lease time and remaining lease time, respectively.

**Prerequisites**

* The address of an interface address pool has been configured using the **ip address** command.
* The DHCP server function has been enabled on the interface using the **dhcp select interface** command.

**Precautions**

Different IP address leases can be specified for different interface address pools on a DHCP server. All IP addresses in an interface address pool have the same lease.

If the IP address lease of an address pool is changed using this command, newly assigned IP addresses use the new IP address lease. IP addresses assigned before the change still use the original IP address lease before the lease is updated, and use the new lease after the lease is updated.

Example
-------

# Set the IP address lease of the address pool on
100GE
1/0/1 to 2 days 2 hours and 30 minutes.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.10.10.10 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server lease day 2 hour 2 minute 30

```