lease
=====

lease

Function
--------

The **lease** command sets the lease for IP addresses in a global IP address pool.

The **undo lease** command restores the default lease of IP addresses in a global IP address pool.

By default, the lease of IP addresses is one day.



Format
------

**lease** { **day** *day* [ **hour** *hour* [ **minute** *minute* ] ] | **unlimited** }

**undo lease**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **day** *day* | Specifies the number of days in the IP address lease. | The value is an integer ranging from 0 to 999. The default value is 1. |
| **hour** *hour* | Specifies the number of hours in the IP address lease. | The value is an integer in the range from 0 to 23. The default value is <b>0</b>. |
| **minute** *minute* | Specifies the number of minutes for an IP address lease. | The value is an integer in the range from 0 to 59. The default value is <b>0</b>. |
| **unlimited** | Indicates that the IP address lease is unlimited. | - |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. To meet different client requirements, DHCP supports dynamic, automatic, and static address assignment.Different hosts require different IP address leases. For example, if some hosts such as a DNS server need to use certain IP addresses for a long time, run the **lease** command to set the IP address lease of the current global address pool to unlimited. If some hosts such as a portable computer just need to use temporary IP addresses, run the **lease** command to set the IP address lease of the current global address pool to the required time so that the expired IP addresses can be released and assigned to other clients.When a DHCP client starts and 50% or 87.5% of its IP address lease has passed, the DHCP client sends a DHCP Request message to the DHCP server to renew the lease.- If the IP address can be assigned to the client, the DHCP server informs the client that the IP address lease can be renewed.- If the IP address can no longer be assigned to the client, the DHCP server informs the client that the IP address lease cannot be renewed. The client needs to request for another IP address.You can run the **display ip pool** command to view information about the IP address lease. The values of the lease and left fields in the command output indicate the configured lease time and remaining lease time, respectively.

**Prerequisites**

A global IP address pool has been created using the ip pool command.

**Precautions**

Different IP address leases can be specified for different global address pools on a DHCP server. In a global address pool, all addresses have the same lease.

To specify the IP address lease for an interface address pool, run the
**dhcp server lease** command.If the IP address lease of an address pool is changed using this command, newly assigned IP addresses use the new IP address lease. IP addresses assigned before the change still use the original IP address lease before the lease is updated, and use the new lease after the lease is updated.

Example
-------

# Set the lease of a global address pool global1 to 2 days 2 hours and 30 minutes.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] lease day 2 hour 2 minute 30

```