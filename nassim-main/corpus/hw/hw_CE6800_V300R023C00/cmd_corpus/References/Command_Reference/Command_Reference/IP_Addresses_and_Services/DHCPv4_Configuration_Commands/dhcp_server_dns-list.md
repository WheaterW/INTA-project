dhcp server dns-list
====================

dhcp server dns-list

Function
--------

The **dhcp server dns-list** command configures DNS server addresses for an interface address pool.

The **undo dhcp server dns-list** command deletes the specified DNS server addresses of an interface address pool.

By default, no DNS server address is configured in an interface address pool.



Format
------

**dhcp server dns-list** *ip-address* &<1-8>

**undo dhcp server dns-list** { **all** | *ip-address* }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of the DNS server. You can configure up to eight IP addresses for the DNS servers and separate two IP addresses with a space. | The value is in dotted decimal notation. |
| **all** | Deletes all DNS server IP addresses. | - |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. If user hosts access hosts on the network through the domain name, user hosts need to send DNS Request messages to the DNS server and resolve the domain name. To enable DNS services on the DHCP client, specify the DNS server address for the interface address pool on the DHCP server. The DHCP server can assign both the specified DHCP server address and an IP address to the client. To configure DNS server addresses for a global address pool, run the **dns-list** command.

**Prerequisites**

1. DHCP has been enabled using the **dhcp enable** command.
2. The address of an interface address pool has been configured using the **ip address** command.
3. The DHCP server function has been enabled on the interface using the **dhcp select interface** command.

**Precautions**

* Each address pool can be configured with a maximum of eight DNS server addresses. If multiple DNS server addresses are configured, the first DNS server address assigned to the DHCP client functions as the primary address and other addresses are secondary addresses.
* To specify multiple DNS servers, enter multiple DNS server addresses in the dhcp server **dns-list** command.


Example
-------

# Specify a DNS server at 10.10.1.254 for domain name resolution when IP addresses in the interface address pool on interface
100GE
1/0/1 are assigned to clients.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server dns-list 10.10.1.254

```