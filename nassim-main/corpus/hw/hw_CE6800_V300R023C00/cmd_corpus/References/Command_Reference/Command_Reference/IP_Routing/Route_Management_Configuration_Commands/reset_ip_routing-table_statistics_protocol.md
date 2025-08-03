reset ip routing-table statistics protocol
==========================================

reset ip routing-table statistics protocol

Function
--------



The **reset ip routing-table statistics protocol** command clears statistics in the IPv4 routing table.




Format
------

**reset ip routing-table statistics protocol** [ **vpn-instance** *vpn-instance-name* ] { **all** | **bgp** | **direct** | **isis** | **ospf** | **rip** | **static** }

**reset ip routing-table all-vpn-instance statistics protocol** { **all** | **bgp** | **direct** | **isis** | **ospf** | **rip** | **static** }

**reset ip routing-table all-routes statistics protocol** { **all** | **bgp** | **direct** | **isis** | **ospf** | **rip** | **static** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **all** | Clears the statistics of all routing protocols in the routing table. | - |
| **bgp** | Clears the statistics about the bgp route. | - |
| **direct** | Clears the statistics about the direct route. | - |
| **isis** | Clears the statistics about the isis route. | - |
| **ospf** | Clears the statistics about the ospf route. | - |
| **rip** | Clears the statistics about the RIP route. | - |
| **static** | Clears the statistics about the static route. | - |
| **all-vpn-instance** | Clears the statistics in the IPv4 routing tables of all VPN instances. | - |
| **all-routes** | Clears the statistics of all IPv4 routes. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The reset ip routing-table statistics protocol command clears historical statistics about protocol routes in the IPv4 routing table. This command enables the router to re-collect statistics about protocol routes, facilitating route monitoring and fault location.

**Precautions**

Statistics in the IPv4 routing table cannot be restored after you clear them. Therefore, exercise caution when running the command.


Example
-------

# Clear the statistics in the IPv4 routing tables of all VPN instances.
```
<HUAWEI> reset ip routing-table all-vpn-instance statistics protocol all

```

# Clear the statistics of all routing protocols in the IPv4 routing table.
```
<HUAWEI> reset ip routing-table statistics protocol all

```