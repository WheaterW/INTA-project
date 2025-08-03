display ip source check user-bind status
========================================

display ip source check user-bind status

Function
--------



The **display ip source check user-bind status** command displays IPSG binding entries and their status.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ip source check user-bind status** [ [ [ **dynamic** | **static** ] [ { **interface** { *interface-name* | *interface-type* *interface-number* } | **ip-address** *ip-address* | **mac-address** *mac-address* | **vlan** *vlan-id* } \* ] [ **valid** | **invalid** ] ] | **summary** ] [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dynamic** | Displays information about the IPSG dynamic binding table. | - |
| **static** | Displays information about the IPSG static binding table. | - |
| **interface** *interface-type* *interface-number* | Displays binding entries mapping a specified interface:   * interface-type. * interface-number. | The value is a string of 1 to 64 case-sensitive characters without spaces. |
| **interface** *interface-name* | Specifies an interface name. | - |
| **ip-address** *ip-address* | Displays binding entries mapping a specified IP address. | The value is in dotted decimal notation. |
| **mac-address** *mac-address* | Displays binding entries mapping a specified MAC address. | The value is in H-H-H format and an H is a hexadecimal number of 4 digits. |
| **vlan** *vlan-id* | Displays binding entries mapping a specified VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **valid** | Checks the IPSG that has taken effect. | - |
| **invalid** | Displays invalid IPSG entries. | - |
| **summary** | Displays brief information about the binding table. | - |
| **slot** *slot-id* | Displays the IPSG status in a specified slot. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can use this command to view IPSG binding entries and their status on the device. IPSG binding tables are classified into dynamic binding tables and static binding tables:· The dynamic binding table is automatically generated based on the DHCP snooping binding table after IPSG is enabled.· The static binding table is manually configured using the **user-bind static** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the dynamic binding table.
```
<HUAWEI> display ip source check user-bind status dynamic
DHCP Bind-table on slot 1:
--------------------------------------------------------------------------------
IP Address                              MAC Address     Vlan(O/I)  Interface
                                                        Type       Status 
--------------------------------------------------------------------------------
10.1.1.1                                00e0-fc12-3456  10  /-     10GE1/0/1      
                                                        Dynamic    -   /-   
--------------------------------------------------------------------------------
Total count:           1

```

# Display information about the static binding table.
```
<HUAWEI> display ip source check user-bind status static
DHCP Bind-table on slot 1:                                                                                                          
--------------------------------------------------------------------------------                                                    
IP Address                              MAC Address     Vlan(O/I)  Interface                                                          
                                                        Type       Status                                                             
--------------------------------------------------------------------------------                                                    
10.1.1.2                                00e0-fc12-3457  -   /-     10GE1/0/1                                                          
                                                        Static     -   /-                                                             
--------------------------------------------------------------------------------                                                    
Total count:           1

```

# Display information about all binding entries.
```
<HUAWEI> display ip source check user-bind status
DHCP Bind-table on slot 1:                                                                                                          
--------------------------------------------------------------------------------                                                    
IP Address                              MAC Address     Vlan(O/I)  Interface                                                          
                                                        Type       Status                                                             
--------------------------------------------------------------------------------                                                    
10.1.1.1                                00e0-fc12-3456  -   /-     10GE1/0/1                                                          
                                                        Dynamic     IPv4/-                                                             
10.1.1.2                                00e0-fc12-3457  10  /-     10GE1/0/1                                                          
                                                        Static    IPv4/-                                                             
--------------------------------------------------------------------------------                                                    
Total count:           2

```

# Display brief information about the binding table.
```
<HUAWEI> display ip source check user-bind status summary
DHCP Bind-table Summary on slot 1:                                                                                                  
---------------------------------------------------------------------------                                               
 Valid count(IPv4):  0                                                                                                              
---------------------------------------------------------------------------                                                 
 All bind-table count    :  1

```

**Table 1** Description of the **display ip source check user-bind status** command output
| Item | Description |
| --- | --- |
| DHCP Bind-table on slot | DHCP binding table on the slot of the device. |
| IP Address | IP address of the user. |
| MAC Address | User MAC address. |
| Vlan(O/I) | ID of the VLAN to which the user belongs.  O: indicates the outer VLAN.  I: indicates the inner VLAN. |
| Interface | User login interface. |
| Type | Binding table type:   * Static. * Dynamic. |
| Status | IPSG status.  -: disabled.  IPv4: enables IPv4. |
| Total count | Total number of binding entries. |
| Valid count(IPv4) | Number of IPv4 binding entries that have taken effect. |