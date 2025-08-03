ldap-server source
==================

ldap-server source

Function
--------

The **ldap-server source** command configures the source IP address that a device uses when sending packets to the LDAP server.

The **undo ldap-server source** command restores the default configuration.

By default, when a device sends packets to the LDAP server, the IP address of the actual outbound interface is used as the source IP address.



Format
------

**ldap-server source** { **loopback** *interface-number1* | **ip-address** *ip-address* | **vlanif** *interface-number2* }

**undo ldap-server source**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **loopback** *interface-number1* | Specifies the IP address of a loopback interface as the source IP address that the device uses when sending packets to the LDAP server. | - |
| **ip-address** *ip-address* | Specifies an IP address as the source IP address that the device uses when sending packets to the LDAP server. | The value must be a valid unicast address in dotted decimal notation. |
| **vlanif** *interface-number2* | Specifies the IP address of a VLANIF interface as the source IP address that the device uses when sending packets to the LDAP server. The interface-number parameter indicates the VLANIF interface number. | - |




Views
-----

LDAP server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

By default, when a device sends packets to the LDAP server, the IP address of the actual outbound interface is used as the source IP address. In some scenarios where the IP address of the actual outbound interface is used, the device cannot communicate with the LDAP server.



Example
-------

# Set the source IP address that the device uses when sending packets to the LDAP server to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] ldap-server template t1
[*HUAWEI-ldap-t1] ldap-server source ip-address 10.1.1.1

```