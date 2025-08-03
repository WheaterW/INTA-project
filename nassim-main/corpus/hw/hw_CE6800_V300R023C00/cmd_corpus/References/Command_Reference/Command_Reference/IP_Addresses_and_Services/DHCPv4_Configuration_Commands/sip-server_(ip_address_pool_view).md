sip-server (ip address pool view)
=================================

sip-server (ip address pool view)

Function
--------

The **sip-server** command configures the SIP server IP address assigned to a DHCP client in a global address pool.

The **undo sip-server** command deletes the configured SIP server IP address assigned to a DHCP client in a global address pool.

By default, the SIP server IP address assigned to a DHCP client in a global address pool is not configured.



Format
------

**sip-server** { **ip-address** *ip-address* &<1-2> | **list** *domain-name* &<1-2> }

**undo sip-server**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** *ip-address* | Specifies an IP address for the SIP server. | The value is in dotted decimal notation. |
| **list** *domain-name* | Specifies the domain name of the SIP server. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. When quotation marks are used around the string, spaces are allowed in the string. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to the DHCP server. To enable DHCP clients to normally access the Internet, the DHCP server needs to specify the SIP server IP address in the address pool when assigning IP addresses to the clients.

**Precautions**

* A maximum of two SIP server addresses can be configured in each address pool. The first assigned address functions as the primary address, and the other address functions as a secondary address.
* Before specifying the IP address or name for a SIP server, ensure that the SIP server exists.
* If you run this command repeatedly, the latest configuration overrides the previous ones.


Example
-------

# Specify 192.168.1.1 as the IP address of the SIP server when addresses in the global address pool global1 are assigned to clients.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] sip-server ip-address 192.168.1.1

```