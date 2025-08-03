dhcp server domain-name
=======================

dhcp server domain-name

Function
--------

The **dhcp server domain-name** command configures a DNS domain name assigned to a DHCP client.

The **undo dhcp server domain-name** command deletes a specified domain name.

By default, no domain name is configured for the DHCP client.



Format
------

**dhcp server domain-name** *domain-name*

**undo dhcp server domain-name**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *domain-name* | Specifies the DNS domain name that the DHCP server assigns to the client. | The value is a string of 1 to 63 case-sensitive characters. If the string is enclosed in double quotation marks ("), spaces are allowed in the string. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. Run the **dhcp server domain-name** command on a DHCP server to specify a domain name for each interface address pool. When allocating IP addresses to clients, the DHCP server also sends the domain names to the clients.

**Prerequisites**

1. The address of an interface address pool has been configured using the **ip address** command.
2. DHCP has been enabled using the **dhcp enable** command.
3. The DHCP server function has been enabled on the interface using the **dhcp select interface** command.

**Precautions**

If no domain name is specified for an interface address pool, a DHCP server does not send a domain name to clients, and users cannot access the Web service by using a domain name.

To configure a domain name for the global address pool, run the
**domain-name** command.

Example
-------

# Set the domain name on interface
100GE
1/0/1 assigned by the DHCP address pool on the interface to huawei.com.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.1.10 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server domain-name huawei.com

```