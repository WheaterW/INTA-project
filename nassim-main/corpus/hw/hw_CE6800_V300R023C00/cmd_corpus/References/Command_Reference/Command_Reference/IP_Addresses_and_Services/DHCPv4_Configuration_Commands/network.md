network
=======

network

Function
--------

The **network** command sets a network segment address for a global address pool.

The **undo network** command restores the default network segment address.

By default, no network segment address is specified.



Format
------

**network** *ip-address* [ **mask** { *mask* | *mask-length* } ]

**undo network**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies a network segment address. | The value is in dotted decimal notation, and must be class A, B, or C IP addresses. |
| **mask** | Indicates the mask of a network segment address for a global address pool. If this parameter is not configured, a natural mask is used. | - |
| *mask* | Specifies the mask of a network segment address for a global address pool. | It is in dotted decimal notation. |
| *mask-length* | Specifies a network mask length. | The value is an integer that ranges from 0 to 32, excluding 0-7, 31, and 32. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. Before a DHCP server assigns IP addresses to clients from a global address pool, run the **network** command to set a network segment address for the global address pool so that the DHCP server can select and assign IP addresses on this network segment to clients. When a DHCP server assigns an IP address to the client from the interface address pool, the network segment of the interface IP address is that of the interface address pool.

**Precautions**

* Each IP address pool can be configured with only one network segment, which can be any required network segment. If multiple network segments are required, multiple IP address pools need to be configured.
* The size of an address pool can be controlled by setting the mask length. The mask length is in reverse proportion to the address pool size.
* When configuring an address pool, ensure that IP addresses on the network segment must be class A, B, or C IP addresses, and the mask cannot be set to 0 to 7, 31, or 32.
* If you need to assign IP addresses with an 18-bit mask in the network segment 10.1.1.0 to clients, the number of IP addresses in an IP address pool is 16K after the network 10.1.1.**0 mask 18** command is executed in the view of the IP address pool. If the number of IP addresses in the IP address pool is less than 16K, the command cannot be executed in the view of the IP address pool.


Example
-------

# Set the network segment address of the IP address pool global1 to 192.168.1.0 and mask length to 24.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] network 192.168.1.0 mask 24

```