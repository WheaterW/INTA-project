vpn-instance(BGP multi-instance view)
=====================================

vpn-instance(BGP multi-instance view)

Function
--------



The **vpn-instance** command creates a BGP multi-instance VPN instance view and displays the BGP multi-instance VPN instance view.

The **undo vpn-instance** command deletes the BGP multi-instance VPN instance view.



By default, BGP multi-instance VPN instance view is not created.


Format
------

**vpn-instance** *vpn-instance-name*

**undo vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Running the **vpn-instance** command creates a BGP multi-instance VPN instance and displays the BGP multi-instance VPN instance view. The configuration in this view takes effect for the routes and peers in all address families of the specified VPN instance.

**Prerequisites**

A VPN instance has been created using the **ip vpn-instance** command.


Example
-------

# Create a BGP multi-instance VPN instance view named vpn3 and access the BGP multi-instance VPN instance view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn3
[*HUAWEI-vpn-instance-vpn3] ipv4-family
[*HUAWEI-vpn-instance-vpn3-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn3] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] vpn-instance vpn3
[*HUAWEI-bgp-instance-a-instance-vpn3]

```