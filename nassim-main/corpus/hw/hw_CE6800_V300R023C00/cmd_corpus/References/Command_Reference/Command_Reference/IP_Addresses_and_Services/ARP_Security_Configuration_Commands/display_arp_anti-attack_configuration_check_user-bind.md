display arp anti-attack configuration check user-bind
=====================================================

display arp anti-attack configuration check user-bind

Function
--------



The **display arp anti-attack configuration check user-bind** command displays the dynamic ARP inspection (DAI) configuration.




Format
------

For CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**display arp anti-attack configuration check user-bind** [ **vlan** [ *vlan-id* ] | **interface** [ *interface-name* | *interface-type* *interface-number* ] | **bridge-domain** [ *bd-id* ] ]

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-LL (low latency mode), CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**display arp anti-attack configuration check user-bind** [ **vlan** [ *vlan-id* ] | **interface** [ *interface-name* | *interface-type* *interface-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** [ *vlan-id* ] | Displays DAI configuration in the specified VLAN.  If vlan-id is not specified, the DAI configurations in all VLANs are displayed. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** [ *interface-type* *interface-number* ] | Displays DAI configurations on a specified interface.   * interface-type specifies the interface type. * interface-number specifies the interface number.   If interface-type interface-number is not specified, DAI configurations on all interfaces are displayed. | - |
| **bridge-domain** *bd-id* | Displays DAI configurations in a specified BD.  If bd-id is not specified, DAI configurations in all BDs are displayed.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H and CE6881H-K. | The value is an integer ranging from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to view the DAI configuration in a BD, in a VLAN, or on an interface, including whether the DAI function is enabled, check items, whether the alarm function is enabled, and alarm threshold.Output of this command is displayed only after DAI and the alarm function are enabled.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the DAI configuration on 10GE1/0/1.
```
<HUAWEI> display arp anti-attack configuration check user-bind interface 10GE 1/0/1
 arp anti-attack check user-bind enable
 arp anti-attack check user-bind alarm enable
 arp anti-attack check user-bind alarm threshold 50 
 arp anti-attack check user-bind check-item ip-address

```

# Display DAI configurations in all VLANs and on all interfaces.
```
<HUAWEI> display arp anti-attack configuration check user-bind
#                                                                               
vlan 2                                                                         
 arp anti-attack check user-bind enable                                         
 arp anti-attack check user-bind check-item ip-address 
#                                                                               
vlan 3                                                                         
 arp anti-attack check user-bind enable                                         
#                                                                               
10GE1/0/1                                                           
 arp anti-attack check user-bind enable
 arp anti-attack check user-bind alarm enable
 arp anti-attack check user-bind alarm threshold 50 
 arp anti-attack check user-bind check-item ip-address
#

```

**Table 1** Description of the **display arp anti-attack configuration check user-bind** command output
| Item | Description |
| --- | --- |
| arp anti-attack check user-bind enable | DAI has been enabled.  This function can be configured using the arp anti-attack check user-bind enable command. |
| arp anti-attack check user-bind alarm enable | The alarm function for ARP packets discarded by DAI has been enabled.  This function can be configured using the arp anti-attack check user-bind alarm enable command. |
| arp anti-attack check user-bind alarm threshold 50 | Alarm threshold for the number of ARP packets discarded by DAI on an interface.  This function can be configured using the arp anti-attack check user-bind alarm threshold command. |
| arp anti-attack check user-bind check-item ip-address | Only the IP address of an ARP packet is checked based on the binding table.  To configure this function, run the arp anti-attack check user-bind check-item (interface view) or arp anti-attack check user-bind check-item (VLAN view) command. |