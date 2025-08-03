vpn-instance(global address pool view)
======================================

vpn-instance(global address pool view)

Function
--------

The **vpn-instance** command configures a VPN instance for an address pool.

The **undo vpn-instance** command deletes the configuration.

By default, no VPN instance is configured for an address pool.



Format
------

**vpn-instance** *vpn-instance-name*

**undo vpn-instance**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |




Views
-----

Global address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. To apply DHCP services in a VPN instance, you need to run the **vpn-instance** command to bind the created IP address pool to the VPN instance.

**Prerequisites**

A VPN instance has been created using the **ip vpn-instance** command.

**Precautions**

* The VPN instance bound to the IP address pool on the DHCP server must be the same as the VPN instance bound to the DHCP server group on the DHCP relay agent; otherwise, users in the IP address pool cannot go online using this DHCP server group.
* If an IP address pool is bound to a VPN instance, IP addresses assigned from this address pool are VPN addresses.
* To bind an interface address pool to a VPN instance, run the **ip binding vpn-instance** command in the interface view.


Example
-------

# Bind the address pool global1 to the VPN instance huawei.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance huawei
[*HUAWEI-vpn-instance-huawei] ipv4-family
[*HUAWEI-vpn-instance-huawei-af-ipv4] quit
[*HUAWEI-vpn-instance-huawei] quit
[*HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] vpn-instance huawei

```