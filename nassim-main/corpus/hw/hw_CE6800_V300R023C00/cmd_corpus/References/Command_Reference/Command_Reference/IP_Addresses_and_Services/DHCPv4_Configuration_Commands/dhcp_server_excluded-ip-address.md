dhcp server excluded-ip-address
===============================

dhcp server excluded-ip-address

Function
--------

The **dhcp server excluded-ip-address** command specifies the range of IP addresses that cannot be automatically assigned to clients from an interface address pool.

The **undo dhcp server excluded-ip-address** command deletes the specified range of IP addresses that cannot be automatically assigned to clients from an interface address pool.

By default, all IP addresses in an address pool can be automatically assigned to clients.



Format
------

**dhcp server excluded-ip-address** *start-ip-address* [ *end-ip-address* ]

**undo dhcp server excluded-ip-address** *start-ip-address* [ *end-ip-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *start-ip-address* | Specifies the start IP address of the IP address segment where addresses cannot be automatically assigned to clients. | The value is in dotted decimal notation. |
| *end-ip-address* | Specifies the end IP address of the IP address segment where addresses cannot be automatically assigned to clients. If <end-ip-address> is not specified, only the IP address corresponding to <start-ip-address> cannot be automatically assigned. | The value is in dotted decimal notation. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The **dhcp server excluded-ip-address** command applies to DHCP servers. Fixed IP addresses are allocated to some specific hosts (such as the WWW server) on the network for a long time. If these hosts' IP addresses are overlapped with IP addresses in the address pool and the DHCP server allocates these overlapped IP addresses to other hosts, IP address conflicts may occur. To prevent such IP address conflicts, you need to exclude these IP addresses from being automatically assigned in the address pool.

You can run the
**dhcp server excluded-ip-address** command to specify the IP addresses or the range of IP addresses that cannot be automatically assigned to clients in the interface address pool.You can run the
**excluded-ip-address** command to specify the IP addresses or the range of IP addresses that cannot be automatically assigned to clients in the global address pool.

**Prerequisites**

1. An address segment has been configured for the interface address pool using the **ip address** command.
2. The DHCP server function has been enabled on the interface using the **dhcp select interface** command.

**Precautions**

* IP addresses that cannot be automatically assigned must be in the address pool. If IP address range in the address pool is changed using the **dhcp server ip-range** command, IP addresses that are configured not to be automatically assigned must be within the new IP address range.
* You do not need to exclude the gateway address configured using the **dhcp server gateway-list** command from being automatically allocated. The device automatically adds the gateway address into the list of IP addresses that cannot be automatically allocated.
* You do not need to exclude the IP address of a server's interface connecting to a client from being automatically allocated. The device automatically sets the status of the interface IP address to Conflict during address assignment.
* If you run this command multiple times, you can specify multiple IP addresses or ranges of IP addresses that cannot be automatically assigned to clients from the specified address pool.
* You can run the **display ip pool** command to check the IP addresses in use in the current address pool, so that you can exclude the unused IP addresses from being automatically assigned to clients. If you need to exclude IP addresses in Used and Conflict states from being automatically assigned to clients after address reclamation, you can also run the **excluded-ip-address** command.


Example
-------

# Disable IP addresses 192.168.1.1 to 192.168.1.20 from being automatically assigned to clients from the address pool on interface
100GE
1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server excluded-ip-address 192.168.1.1 192.168.1.20

```