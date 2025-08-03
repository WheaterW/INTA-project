vpn-instance (BGP view)
=======================

vpn-instance (BGP view)

Function
--------



The **vpn-instance** command creates a BGP VPN instance and displays the BGP VPN instance view.

The **undo vpn-instance** command deletes a BGP VPN instance.



By default, no BGP VPN instance is created.


Format
------

**vpn-instance** *vpn-instance-name*

**undo vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Running the **vpn-instance** command creates a BGP VPN instance and displays the BGP VPN instance view. The configuration in this view takes effect for the routes and peers in all address families of the specified VPN instance.

**Prerequisites**

A VPN instance must have been created using the **ip vpn-instance** command before this command is run.

**Configuration Impact**

Running the **undo vpn-instance** command to delete a BGP VPN instance clears all the configurations in the BGP VPN instance.

**Follow-up Procedure**

After creating a BGP-VPN instance, run the **peer as-number** command in the BGP-VPN instance view to configure a BGP peer and enable the BGP peer.

**Precautions**

The BGP peers configured in the BGP VPN instance view can be used in both the BGP VPN instance IPv4 address family view and the BGP VPN instance IPv6 address family view.


Example
-------

# Create a BGP VPN instance named vpn1 and access the BGP VPN instance view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1]

```