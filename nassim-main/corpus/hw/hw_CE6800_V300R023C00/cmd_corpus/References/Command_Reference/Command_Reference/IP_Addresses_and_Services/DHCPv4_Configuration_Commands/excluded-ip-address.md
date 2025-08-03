excluded-ip-address
===================

excluded-ip-address

Function
--------

The **excluded-ip-address** command specifies the range of IP addresses that cannot be automatically assigned to clients from an address pool.

The **undo excluded-ip-address** command deletes the specified range of IP addresses that cannot be automatically assigned to clients from an address pool.

By default, all IP addresses in an address pool can be automatically assigned to clients.



Format
------

**excluded-ip-address** *start-ip-address* [ *end-ip-address* ]

**undo excluded-ip-address** *start-ip-address* [ *end-ip-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-ip-address* | Specifies the start IP address of the IP address segment where addresses cannot be automatically assigned to clients. | The value is in dotted decimal notation. |
| *end-ip-address* | Specifies the end IP address of the IP address segment where addresses cannot be automatically assigned to clients. If end-ip-address is not specified, only the IP address corresponding to start-ip-address cannot be automatically assigned. | The value is in dotted decimal notation. end-ip-address and start-ip-address must be on the same network segment and end-ip-address must be larger than start-ip-address. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The **excluded-ip-address** command applies to DHCP servers. Fixed IP addresses are allocated to some specific hosts (such as the WWW server) on the network for a long time. If these hosts' IP addresses are overlapped with IP addresses in the address pool and the DHCP server allocates these overlapped IP addresses to other hosts, IP address conflicts may occur. To prevent such IP address conflicts, you need to exclude these IP addresses from being automatically assigned in the address pool.

You can run the
**excluded-ip-address** command to specify the IP addresses or the range of IP addresses that cannot be automatically assigned to clients in the global address pool.You can run the
**dhcp server excluded-ip-address** command to specify the IP addresses or the range of IP addresses that cannot be automatically assigned to clients in the interface address pool.

**Prerequisites**

Network segment addresses that can be assigned from the global address pool have been configured using the network (IP address pool view) command.

**Precautions**

* The excluded IP address or IP address segment must be in the local address pool.
* If you run the **excluded-ip-address** command multiple times, you can specify multiple IP addresses or ranges of IP addresses that cannot be automatically assigned to clients from the specified address pool.


Example
-------

# Disable IP addresses 10.10.10.10 to 10.10.10.20 from being automatically assigned to clients from the address pool global1.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] network 10.10.10.0 mask 24
[*HUAWEI-ip-pool-global1] excluded-ip-address 10.10.10.10 10.10.10.20

```

# Disable IP address 10.10.10.30 in Used state from being automatically assigned to clients from the address pool global1.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] network 10.10.10.0 mask 24
[*HUAWEI-ip-pool-global1] excluded-ip-address 10.10.10.30
Warning: The address is in used or conflict state. Are you sure to continue excluding the address?[Y/N]:y

```