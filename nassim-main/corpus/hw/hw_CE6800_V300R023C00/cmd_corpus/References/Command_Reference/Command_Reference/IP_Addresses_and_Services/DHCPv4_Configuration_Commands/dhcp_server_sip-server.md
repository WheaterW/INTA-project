dhcp server sip-server
======================

dhcp server sip-server

Function
--------

The **dhcp server sip-server** command configures the SIP server IP address assigned to a DHCP client on an interface address pool.

The **undo dhcp server sip-server** command deletes the configured SIP server IP address assigned to a DHCP client on an interface address pool.

By default, the SIP server IP address assigned to a DHCP client on an interface address pool is not configured.



Format
------

**dhcp server sip-server** { **ip-address** *ip-address* &<1-2> | **list** *domain-name* &<1-2> }

**undo dhcp server sip-server**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** *ip-address* | Specifies an IP address for the SIP server. | The value is in dotted decimal notation. |
| **list** *domain-name* | Specifies the domain name of the SIP server. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. When quotation marks are used around the string, spaces are allowed in the string. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to the DHCP server. To enable DHCP clients to normally access the Internet, the DHCP server needs to specify the SIP server IP address in the interface address pool when assigning IP addresses to the clients.

**Prerequisites**

1.execute command dhcp enable to enable DHCP under system view.

2.execute command ip address to configure the IP address of IP pool of this interface.3.execute dhcp select interface to enable DHCP server in this interface.

**Precautions**

* A maximum of two SIP server addresses can be configured in each address pool. The first assigned address functions as the primary address, and the other address functions as a secondary address.
* Before specifying the IP address or name for a SIP server, ensure that the SIP server exists.
* If you run this command repeatedly, the latest configuration overrides the previous ones.


Example
-------

# Specify 10.1.1.1 as the IP address of the SIP server when addresses in the interface
100GE
1/0/1 address pool are assigned to clients.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 10.1.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server sip-server ip-address 10.1.1.1

```