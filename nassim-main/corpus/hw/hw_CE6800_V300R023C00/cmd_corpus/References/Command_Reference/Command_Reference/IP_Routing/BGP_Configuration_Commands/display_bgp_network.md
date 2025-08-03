display bgp network
===================

display bgp network

Function
--------



The **display bgp network** command displays the routes imported into the BGP routing table using the network command.




Format
------

**display bgp network**

**display bgp vpnv4 all network**

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **network**

**display bgp instance** *instance-name* **vpnv4** **all** **network**

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **network**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpnv4** | Displays the VPNv4 routes that are advertised using the network command. | - |
| **all** | Displays all the VPNv4 routes that are advertised using the network command. | - |
| **vpn-instance** *vpn-instance-name* | Displays the routes of a specified VPN instance that are advertised using the network command. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **instance** *instance-name* | Specifies a BGP instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check the routes imported into the BGP routing table using the **network** command, run the **display bgp network** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about routes that are imported using the network command.
```
<HUAWEI> display bgp network
BGP Local Router ID is 10.1.1.9
Local AS Number is 10(Public)

Network          Mask            Route-policy
10.2.0.0          255.255.0.0
10.0.0.0          255.0.0.0       Policy1
10.4.4.0          255.255.255.0

```

# Display information about BGP VPNv4 routes that are imported using the network command.
```
<HUAWEI> display bgp vpnv4 all network
BGP Local Router ID is 10.2.2.9
Local AS Number is 100

Route Distinguisher: 1:1
(vpn1)
Network          Mask            Route-policy
419.4.4.4          255.255.255.255

Route Distinguisher: 2:2
(vpn2)
Network          Mask            Route-policy
10.5.5.5          255.255.255.255

```

**Table 1** Description of the **display bgp network** command output
| Item | Description |
| --- | --- |
| BGP Local Router ID is | ID of the local BGP device. The ID is in the same format as an IPv4 address. |
| Local AS Number is | Local AS number. |
| Router ID | Router ID of the device. |
| Network | Locally-imported network address. |
| Mask | Mask of the network address. |
| Route-policy | Route-policy. |
| Route Distinguisher | Route Distinguisher. |