dns-list
========

dns-list

Function
--------

The **dns-list** command configures the DNS server address for the DHCP client.

The **undo dns-list** command deletes a configured DNS server address.

By default, no DNS server address is configured.



Format
------

**dns-list** *ip-address* &<1-8>

**undo dns-list** { *ip-address* | **all** }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of a DNS server. | The value is in dotted decimal notation. A maximum of eight DNS server addresses can be configured. These IP addresses are separated by spaces. |
| **all** | Deletes all DNS server addresses. | - |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. If user hosts access hosts on the network by domain names, user hosts need to send DNS requests to the DNS server and resolve the domain name to access for communication. To connect a DHCP client to the network, configure a DHCP server address so that the DHCP server can assign both the specified DNS server address and an IP address to the client. To configure DNS server addresses for an interface address pool, run the **dhcp server dns-list** command.

**Precautions**

In the IP address pool view, a device can be configured with a maximum of eight DNS server addresses respectively. The address first assigned to the clients functions as the primary address, and the other seven addresses function as secondary addresses.



Example
-------

# In the IP address pool view, set the IP address of the DNS server to 10.10.10.10.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] dns-list 10.10.10.10

```