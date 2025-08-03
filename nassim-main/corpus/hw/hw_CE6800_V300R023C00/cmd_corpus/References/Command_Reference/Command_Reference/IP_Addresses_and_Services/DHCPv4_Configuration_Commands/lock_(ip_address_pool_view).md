lock (ip address pool view)
===========================

lock (ip address pool view)

Function
--------

The **lock** command locks an address pool.

The **undo lock** command restores the default configuration.

By default, no IP address pool is locked.



Format
------

**lock**

**undo lock**



Parameters
----------

None


Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

After the **lock** command is run, the specified IP address pool is locked and IP addresses in this address pool cannot be assigned to clients. When a DHCP server needs to be redeployed, you need to migrate address pools on the DHCP server to another DHCP server on the live network. To retain the addresses that have been assigned to clients from a global address pool, run the **lock** command to lock the global address pool. When new users get online after the address pool migration, they apply for IP addresses from a new address pool.



Example
-------

# Lock the IP address pool global1.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] lock

```