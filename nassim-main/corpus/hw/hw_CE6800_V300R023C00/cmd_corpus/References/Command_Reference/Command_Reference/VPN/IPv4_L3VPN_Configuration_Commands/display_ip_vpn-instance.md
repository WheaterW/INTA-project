display ip vpn-instance
=======================

display ip vpn-instance

Function
--------

The **display ip vpn-instance** command displays VPN instance information.



Format
------

**display ip vpn-instance** [ *vpn-instance-name* ]

**display ip vpn-instance verbose**

**display ip vpn-instance interface**

**display ip vpn-instance verbose** *vpn-instance-name*

**display ip vpn-instance** *vpn-instance-name* **interface**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **verbose** | Displays detailed information about VPN instances. | - |
| **interface** | Displays information about the interfaces bound to the VPN instance. | - |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

To view the configurations of VPN instances, interfaces bound to them, and LSPs associated with them, run the **display ip vpn-instance** command. Since VPN instances support IPv4 and IPv6 address families, the **display ip vpn-instance** command displays the information of different address families separately.

If vpn-instance-name is not specified, the command displays information about all configured VPN instances.If interface is specified, the command displays all interfaces bound to the specified VPN instance.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display brief information about all VPN instances.
```
<HUAWEI> display ip vpn-instance
 Total VPN-Instances configured : 5                                             
 Total IPv4 VPN-Instances configured : 3 
 Total IPv6 VPN-Instances configured : 1

  VPN-Instance Name               RD                             Address family
  vrf1                            1:1                            IPv4
  vrf2                            2:2                            IPv4
  vrf3
  vrf4                                                           IPv4
  vrf5                                                           IPv6

```

# Display detailed information about all VPN instances.
```
<HUAWEI> display ip vpn-instance verbose
Total VPN-Instances configured : 1  
Total IPv4 VPN-Instances configured : 1 
Total IPv6 VPN-Instances configured : 1

VPN-Instance Name and ID : vpn1, 1
  Description : vrf1
  Interfaces : LoopBack1 
Address family ipv4  
  Create date : 2010/03/05 16:26:27
  Up time : 0 days, 00 hours, 09 minutes and 12 seconds
  Vrf Status : UP
  Route Distinguisher : 100:1
  Export VPN Targets :  1:1
  Import VPN Targets :  1:1
  Label Policy :  label per route 
  Import Route Policy : rp1
  The diffserv-mode Information is : uniform
  The ttl-mode Information is : uniform
  Export Route Policy : rp2
  Tunnel Policy : tp1
  Maximum Routes Limit : 200
  Threshold Routes Limit : 80%
Address family ipv6
  Create date : 2010/03/05 16:26:31
  Up time : 0 days, 00 hours, 09 minutes and 08 seconds 
  Vrf Status : UP
  Route Distinguisher : 100:1
  Export VPN Targets :  1:1
  Import VPN Targets :  1:1
  Label Policy :   label per route
  Import Route Policy : p1
  Export Route Policy : p2
  Tunnel Policy : tnlpolicy1
  Maximum Routes Limit : 300
  Threshold Routes Limit : 80%

```


**Table 1** Description of the
**display ip vpn-instance** command output

| Item | Description |
| --- | --- |
| Total VPN-Instances configured | Total number of VPN instances locally configured. |
| Total IPv4 VPN-Instances configured | Total number of locally configured VPN instances for which IPv4 address families are enabled. |
| Total IPv6 VPN-Instances configured | Total number of locally configured VPN instances for which IPv6 address families are enabled. |
| VPN-Instance Name | VPN instance name. |
| VPN-Instance Name and ID | Name and ID of the VPN instance. The ID is allocated by the system and is easy to find. |
| Address family | Address family enabled for the VPN instance. The available options are as follows:   * No address family is enabled (no information is displayed). * Only the IPv4 address family is enabled (ipv4 is displayed). * Only the IPv6 address family is enabled (ipv6 is displayed). * Both the IPv4 and IPv6 address families are enabled (ipv4 ipv6 is displayed). |
| Address family ipv4 | Information about the IPv4 address family enabled for the VPN instance. |
| Address family ipv6 | Information about the IPv6 address family enabled for the VPN instance. |
| RD | RD of the VPN instance IPv4 address family or IPv6 address family. |
| ID | ID of a tunnel used in the VPN instance address family. |
| Description | Description of the VPN instance. This field is displayed only when the description (VPN instance view) command is used in the VPN instance view. |
| Interfaces | Interfaces bound to the VPN instance. This field is displayed only after the ip binding vpn-instance command is configured on these interfaces. |
| Create date | Time when the VPN instance is created. |
| Up time | Period during which the VPN instance stays in the up state. |
| Route Distinguisher | RD of the VPN instance IPv4 or IPv6 address family. |
| Export VPN Targets | List of the export route targets. |
| Export Route Policy | Export route-policy applied to the IPv4 or IPv6 address family of the VPN instance. This field is displayed only after the export route-policy command is run in the VPN instance IPv4 or IPv6 address family view. |
| Import VPN Targets | List of import route targets (IRTs). |
| Import Route Policy | Import route-policy applied to the IPv4 or IPv6 address family of the VPN instance. This field is displayed only after the import route-policy command is run in the VPN instance IPv4 or IPv6 address family view. |
| Label Policy | Label policy:   * label per route: Each route in a VPN instance is assigned a label. By default, a VPN instance assigns labels in this mode. |
| The diffserv-mode Information is | DiffServ mode, in which resources such as bandwidth are allocated in real time.  The available options are as follows:   * uniform. * pipe. |
| The ttl-mode Information is | TTL processing mode:   * uniform. * pipe. |
| Tunnel Policy | Tunnel policy applied to the VPN instance. |
| Maximum Routes Limit | Maximum number of prefixes supported by the current address family. This field is displayed only after the prefix limit command is run in the VPN instance IPv4 or IPv6 address family view. |
| Threshold Routes Limit | Percentage of the maximum number of prefixes specified in the current address family. When the percentage is reached, an alarm is generated. This field is displayed only after the prefix limit command is run in the VPN instance IPv4 or IPv6 address family view. |
| Vrf Status | Status of the VPN:   * UP. * DOWN. |