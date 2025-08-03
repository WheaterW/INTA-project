display bgp router-id
=====================

display bgp router-id

Function
--------



The **display bgp router-id** command displays the router ID.




Format
------

**display bgp router-id** [ **vpn-instance** | **vpn-instance** *vpn-instance-name* ]

**display bgp instance** *bgpName* **router-id** [ **vpn-instance** | **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the ID of a device in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **instance** *bgpName* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check router IDs on the public network and in the VPN instance, run the **display bgp router-id** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the ID of a router in the VPN instance.
```
<HUAWEI> display bgp router-id vpn-instance vrf1
 VPN-Instance Name                RouterID
 vrf1                             3.3.3.3

```

# Display the Router ID of a device on the public network.
```
<HUAWEI> display bgp router-id
BGP RouterID:2.2.2.2

```

**Table 1** Description of the **display bgp router-id** command output
| Item | Description |
| --- | --- |
| VPN-Instance Name | VPN instance name. |
| RouterID | Router ID. |
| BGP RouterID | Router ID on the public network. |