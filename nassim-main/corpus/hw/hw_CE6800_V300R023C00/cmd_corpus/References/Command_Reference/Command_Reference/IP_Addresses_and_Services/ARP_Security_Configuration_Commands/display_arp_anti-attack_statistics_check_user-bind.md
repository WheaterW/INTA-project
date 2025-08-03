display arp anti-attack statistics check user-bind
==================================================

display arp anti-attack statistics check user-bind

Function
--------



The **display arp anti-attack statistics check user-bind** command displays statistics about discarded ARP packets.




Format
------

For CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**display arp anti-attack statistics check user-bind** [ **vlan** [ *vlan-id* ] | **interface** [ *interface-name* | *interface-type* *interface-number* ] | **bridge-domain** [ *bd-id* ] ]

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-LL (low latency mode), CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**display arp anti-attack statistics check user-bind** [ **vlan** [ *vlan-id* ] | **interface** [ *interface-name* | *interface-type* *interface-number* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vlan** *vlan-id* | Displays DAI statistics in a specified VLAN.  If vlan-id is not specified, DAI statistics in all VLANs are displayed. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Displays DAI configurations on a specified interface.   * interface-type specifies the interface type. * interface-number specifies the interface number.   If interface-type interface-number is not specified, DAI configurations on all interfaces are displayed. | - |
| **bridge-domain** *bd-id* | Displays DAI statistics in a specified BD.  If bd-id is not specified, DAI statistics in all BDs are displayed.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H and CE6881H-K. | The value is an integer ranging from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After DAI is enabled in the interface view, VLAN view, or BD view, you can run the display arp anti-attack check user-bind alarm statistics command to check statistics about ARP packets discarded because they do not match binding entries. If the alarm function for ARP packets discarded because of DAI is enabled, you can also view the statistics on the ARP packets that do not match the binding table and are discarded on the interface after the last alarm is generated.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on discarded ARP packets that do not match the binding table on an interface.
```
<HUAWEI> display arp anti-attack statistics check user-bind interface
-------------------------------------------------------------------------------
Type            View                 Total Dropped        Last Dropped
-------------------------------------------------------------------------------
Interface       10GE1/0/2            966                  605                   
Interface       10GE1/0/3            0                    0                   
-------------------------------------------------------------------------------

```

# Display statistics about ARP packets discarded in VLAN 100 because they do not match the binding table.
```
<HUAWEI> display arp anti-attack statistics check user-bind vlan 100
-------------------------------------------------------------------------------                                                     
Type            View                 Total Dropped        Last Dropped                                                              
-------------------------------------------------------------------------------                                                     
Vlan            100                  0                    0                                                                         
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display arp anti-attack statistics check user-bind** command output
| Item | Description |
| --- | --- |
| Type | Type of the view in which DAI is enabled. |
| View | Name of the view in which DAI is enabled. |
| Total Dropped | Number of discarded ARP packets matching no DHCP snooping binding entry. |
| Last Dropped | Statistics on discarded ARP packets matching no DHCP snooping binding entry after the latest alarm is generated. |