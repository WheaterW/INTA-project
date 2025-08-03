dhcp server static-bind
=======================

dhcp server static-bind

Function
--------

The **dhcp server static-bind** command binds an IP address in an interface address pool to a MAC address.

The **undo dhcp server static-bind** command unbinds the IP address in an interface address pool from a MAC address.

By default, an IP address in an interface address pool is not bound to any MAC address.



Format
------

**dhcp server static-bind ip-address** *ip-address* **mac-address** *mac-address* [ **description** *description* ]

**undo dhcp server static-bind** [ **ip-address** *ip-address* | **mac-address** *mac-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** *ip-address* | Specifies the IP address to be bound. The IP address must be valid in an interface address pool. | The value is in dotted decimal notation. |
| **mac-address** *mac-address* | Specifies the MAC address of a user. | The value is in the format of H-H-H. Each H indicates one to four hexadecimal digits. |
| **description** *description* | Specifies the user description. | The value is a string of 1 to 256 case-sensitive characters. It can contain spaces. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The **dhcp server static-bind** command applies to DHCP servers. When planning a network, you need to allocate fixed IP addresses to some important hosts to ensure reliability. In this case, you can bind IP addresses in the address pool to the MAC addresses of these hosts. After the preceding configuration is complete, if the host of the MAC address to which the IP address is bound request an IP address from the DHCP server, the DHCP server finds the bound IP address based on the host's MAC address and allocates this IP address to the host, ensuring that the IP address obtained by the host is fixed.

You can run the
**dhcp server static-bind** command to bind an IP address in an interface address pool to a MAC address.You can run the
**static-bind** command to bind an IP address in a global address pool to a MAC address.

**Prerequisites**

* The address of an interface address pool has been configured using the **ip address** command.
* Enable the DHCP server function based on the interface address pool on the interface using the **dhcp select interface** command.

**Precautions**

* Ensure that the bound IP address is not configured as the IP address that cannot be allocated using the **dhcp server excluded-ip-address** command.
* IP addresses that are used can also be statically bound to MAC addresses or unbound from MAC addresses. When an IP address is statically bound to a MAC address, ensure that the MAC address to be bound is the same as the MAC address of the user who actually uses the IP address.
* The DHCP server preferentially allocates the IP address that has been statically bound to the client's MAC address.
* After an IP address is bound to a MAC address, the IP address does not expire. After an automatically allocated IP address is statically bound to a MAC address, the lease time of the IP address becomes unlimited. After the static binding between the IP address and the MAC address is deleted, the lease time of the IP address becomes the same as that configured in the address pool.


Example
-------

# Configure a DHCP server to assign a fixed IP address 10.10.10.20 in the interface address pool on
100GE
1/0/1 to a host with the MAC address 00e0-fc12-3456.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.10.10.10 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server static-bind ip-address 10.10.10.20 mac-address 00e0-fc12-3456

```