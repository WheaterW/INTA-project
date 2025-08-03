display trace instance
======================

display trace instance

Function
--------



The **display trace instance** command displays diagnosis instances on a device.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display trace instance** [ *instance-start-id* [ *instance-end-id* ] | **mac-address** *mac-address* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] ]

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**display trace instance** [ *instance-start-id* [ *instance-end-id* ] | **mac-address** *mac-address* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] | **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *instance-start-id* | Specifies the ID of the first instance whose information is displayed, that is, start ID. | The value is an integer ranging from 0 to 1023. |
| *instance-end-id* | Specifies the number of instances to be displayed. | The value is an integer ranging from 1 to 1023. |
| **mac-address** *mac-address* | Specifies a MAC address. | The value is in H-H-H format. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |
| **ip-address** *ip-address* | Specifies an IP address. | The value is in dotted decimal notation. |
| **interface** | Specifies an interface.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| *interface-name* | Specifies the name of an interface.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| *interface-type* | Specifies the type of an interface.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| *interface-number* | Specifies an interface number.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If you specify no parameter, all diagnosis instances are displayed in sequence. Each time you run this command, 10 diagnosis instances are displayed. For example, all diagnosis instances have been created on the device. When you run the **display trace instance** command for the first time, information about diagnosis instances 0 to 9 is displayed. When you run this command again, information about instances 10 to 19 is displayed. This process is repeated until information about all the diagnosis instances is displayed. If you specify the value of instance-start-id , information about 10 diagnosis instances from this ID is displayed.To view information about diagnosis instances within a specified range, run the **display trace instance** command to specify the start IDs of diagnosis instances and the total number of displayed instances.

**Precautions**

If only one service is online, an instance is created for this service but it is released immediately and cannot be statically queried. If multiple services are online concurrently, you can check the instances that are being created. However, debugging information cannot be displayed for services that exceed the instance upper limit. After the debugging output is complete, the instances are released and cannot be viewed anymore.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about diagnosis instances on the interface with the MAC address of 00e0-fc12-3456.
```
<HUAWEI> display trace instance mac-address 00e0-fc12-3456
Trace Instance:
------------------------------------------------------------
  ID             : 0                                                            
  MAC Address    : 00e0-fc12-3456                                               
  IP Flag        : -                                                            
  Session ID     : -                                                            
  IP Address     : 10.10.10.1                                                   
  VRF Index      : -                                                            
  CID            : 100                                                          
  User Name      : -                                                            
  Interface      : -                                                            
  QinQ VLAN ID   : -                                                            
  User VLAN ID   : -                                                            
  Access Mode    : dot1x
  Modules online : EAPoL  :0	WEBS   :0	WEB    :0	WEBMNG :0	AAA    :0
                   CM     :0	TM     :0	SAM    :0	RADIUS :0
                   DHCPS  :0	DHCPC  :0	DHCPR  :0	DHCPP  :0
                   TACACS :0	AM     :0	SAVI   :0	WLAN_AC:0
                   L2TP   :0	LNS    :0	PPP    :0	PPPOE  :0	
                   PPPOLNS:0	
                   AD     :0	
                   LDAP   :0                                                           
 ------------------------------------------------------------
  Total 1, 1 printed

```

**Table 1** Description of the **display trace instance** command output
| Item | Description |
| --- | --- |
| ID | ID of the diagnosis instance. |
| MAC Address | MAC address. |
| IP Flag | Flag of the IP address. |
| IP Address | IP address. |
| Session ID | Session Id. |
| VRF Index | User VRF index. |
| CID | User connect ID. |
| User Name | User name. |
| User VLAN ID | User VLAN ID. |
| Interface | Index of the interface. |
| QinQ VLAN ID | QinQ VLAN ID. |
| Access Mode | User access mode. |
| Modules online | User status on a module:  0: The user is offline on the module.  1: The user is online on the module. |