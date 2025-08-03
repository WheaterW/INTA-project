static-bind
===========

static-bind

Function
--------

The **static-bind** command binds an IP address in a global address pool to a MAC address of a client.

The **undo static-bind** command unbinds the IP address in a global address pool from a MAC address.

By default, the IP address in a global address pool is not bound to any MAC address.



Format
------

**static-bind ip-address** *ip-address* **mac-address** *mac-address* [ **description** *description* ]

**undo static-bind** [ **ip-address** *ip-address* | **mac-address** *mac-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** *ip-address* | Specifies the IP address to be bound. The IP address must be a valid IP address in the global address pool. | The value is in dotted decimal notation. |
| **mac-address** *mac-address* | Specifies a user MAC address. | The value is in the format of H-H-H, in which H is a hexadecimal number of 1 to 4 digits. |
| **description** *description* | Specifies the user description. | The value is a string of 1 to 256 case-sensitive characters. It can contain spaces. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The **static-bind** command applies to DHCP servers. When planning a network, you need to allocate fixed IP addresses to some important hosts to ensure reliability. In this case, you can bind IP addresses in the address pool to the MAC addresses of these hosts. After the preceding configuration is complete, if the host of the MAC address to which the IP address is bound request an IP address from the DHCP server, the DHCP server finds the bound IP address based on the host's MAC address and allocates this IP address to the host, ensuring that the IP address obtained by the host is fixed.

You can run the
**static-bind** command to bind an IP address in a global address pool to a MAC address.You can run the
**dhcp server static-bind** command to bind an IP address in an interface address pool to a MAC address.

**Prerequisites**

Network segment addresses that can be assigned from the global address pool have been configured using the network (IP address pool view) command.

**Precautions**

* Ensure that the bound IP address is not configured as the IP address that cannot be allocated using the **excluded-ip-address** command.
* IP addresses that are used can also be statically bound to MAC addresses or unbound from MAC addresses. When an IP address is statically bound to a MAC address, ensure that the MAC address to be bound is the same as the MAC address of the user who actually uses the IP address.
* The DHCP server preferentially allocates the IP address that has been statically bound to the client's MAC address.
* After an IP address is bound to a MAC address, the IP address does not expire. After an automatically allocated IP address is statically bound to a MAC address, the lease time of the IP address becomes unlimited. After the static binding between the IP address and the MAC address is deleted, the lease time of the IP address becomes the same as that configured in the address pool.


Example
-------

# Configure a DHCP server to assign a fixed IP address 192.168.1.10 in the global address pool global1 to a host with the MAC address 00e0-fc12-3456.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] network 192.168.1.10 mask 24
[*HUAWEI-ip-pool-global1] static-bind ip-address 192.168.1.10 mac-address  00e0-fc12-3456

```