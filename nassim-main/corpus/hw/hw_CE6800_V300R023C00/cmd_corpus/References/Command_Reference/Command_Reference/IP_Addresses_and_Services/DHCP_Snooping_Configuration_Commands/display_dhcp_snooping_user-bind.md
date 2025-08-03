display dhcp snooping user-bind
===============================

display dhcp snooping user-bind

Function
--------



The **display dhcp snooping user-bind** command displays information about the DHCP snooping dynamic binding table.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display dhcp snooping user-bind** { { **interface** { *interface-type* *interface-number* | *interface-name* } | **ip-address** *ip-address* | **mac-address** *mac-address* | **vlan** *vlan-id* | **bridge-domain** *bd-id* } \* | **all** } [ **verbose** ]

For CE6820H, CE6820H-K, CE6820S, CE6885-LL (low latency mode):

**display dhcp snooping user-bind** { { **interface** { *interface-type* *interface-number* | *interface-name* } | **ip-address** *ip-address* | **mac-address** *mac-address* | **vlan** *vlan-id* } \* | **all** } [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* | Interface type. | - |
| *interface-number* | Specifies an interface number. | - |
| *interface-name* | interface-name specifies the name of an interface. | The value is a string of 1 to 128 case-sensitive characters, spaces not supported. |
| **ip-address** *ip-address* | Displays binding entries mapping a specified IP address. | The value is in dotted decimal notation. |
| **mac-address** *mac-address* | Displays binding entries mapping a specified MAC address. | The value is in H-H-H format. Each H is a hexadecimal number of 4 digits. |
| **vlan** *vlan-id* | Displays binding entries mapping a specified VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **bridge-domain** *bd-id* | Displays DHCP snooping running information in a specified BD.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer ranging from 1 to 16777215. |
| **all** | Displays all entries in the binding table. | - |
| **verbose** | Displays detailed information about the binding table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After DHCP snooping is enabled, the device generates a DHCP snooping binding table. A binding entry contains the MAC address, IP address, interface connected to the DHCP client, and VLAN to which the interface belongs. You can run the display dhcp snooping user-bind command to view the binding entries generated for DHCP users on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the DHCP snooping binding table.
```
<HUAWEI> display dhcp snooping user-bind all verbose
DHCP Dynamic Bind-table:                                                        
Flags:O - outer vlan ,I - inner vlan
--------------------------------------------------------------------------------
 IP Address     : 10.10.21.254                                                     
 MAC Address    : 00e0-fc00-00e8
 Bridge-domain  : 1                                                     
 VLAN(O/I)      : 10/--                                              
 Interface      : GE1/0/1                               
 Renew time     : 2020.08.26-11:58                                                 
 Expire time    : 2019.08.27-11:58                                                 
 Gateway        : 10.10.21.1                                                       
 Server-ip      : 10.10.21.1
 Discover time  : 2020.08.26-11:58:20:920
 Ack time       : 2020.08.26-11:58:23:660  
--------------------------------------------------------------------------------
Print count:           1          Total count:           1

```

# Display information about the DHCP snooping binding table.
```
<HUAWEI> display dhcp snooping user-bind all
DHCP Dynamic Bind-table:
Flags:O - outer vlan ,I - inner vlan
IP Address       MAC Address     VLAN(O/I)/(BD-VLAN)      Interface      Lease            
----------------------------------------------------------------------------------------- 
10.1.28.141      00e0-fcb5-b858  10                        GE1/0/1       2008.10.17-07:31 
----------------------------------------------------------------------------------------- 
Print count:           1          Total count:           1

```

**Table 1** Description of the **display dhcp snooping user-bind** command output
| Item | Description |
| --- | --- |
| DHCP Dynamic Bind-table | DHCP snooping dynamic binding table. |
| IP Address | IP address of the user. |
| MAC Address | User MAC address. |
| Bridge-domain | BD. |
| VLAN(O/I) | Outer VLAN ID and inner VLAN ID when a user goes online. |
| Interface | Interface through which a user goes online. |
| Renew time | Entry update time. |
| Expire time | Aging time of entries. |
| Gateway | Gateway address. |
| Server-ip | IP address of the DHCP server. |
| Discover time | Indicates the time when the access device receives the DHCP request packet. |
| Ack time | Indicates the time when the access device receives the DHCP ACK packet. |
| Print count | Number of printed binding entries. |
| VLAN(O/I)/(BD-VLAN) | Outer and inner VLAN information or BD and VLAN information when a user goes online. |
| Lease | Time when the lease of the IP address used by a user expires. |
| Flags | The letter O indicates the outer VLAN ID, and the letter I indicates the inner VLAN ID. |