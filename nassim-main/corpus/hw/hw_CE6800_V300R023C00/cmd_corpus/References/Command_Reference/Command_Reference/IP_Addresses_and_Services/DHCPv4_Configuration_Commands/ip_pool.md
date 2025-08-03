ip pool
=======

ip pool

Function
--------

The **ip pool** command creates a global address pool.

The **undo ip pool** command deletes a global address pool.

By default, no global address pool is created.



Format
------

**ip pool** *pool-name*

**undo ip pool** *pool-name*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *pool-name* | Specifies the name of an address pool. | The value is a string of 1 to 64 case-insensitive characters without spaces. It can contain digits, letters, and special characters underscores (\_), hyphens (-), and periods (.). It cannot be set to - or --. |




Views
-----

System view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. When configuring a DHCP server, run the ip pool (system view) command in the system view to create a global IP address pool and set parameters for the global IP address pool, including a gateway address, the IP address lease, and a VPN instance. Then the configured DHCP server can assign IP addresses in the IP address pool to clients.

**Follow-up Procedure**

Run the network or section command in the IP address pool view to specify the range of the IP addresses in the pool.



Example
-------

# Create a global address pool named global1.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1

```