display user-bind static
========================

display user-bind static

Function
--------



The **display user-bind static** command displays information about a static DHCP snooping binding table.




Format
------

**display user-bind static** { { **interface** { *interface-type* *interface-number* | *interface-name* } | **ip-address** *ip-address* | **mac-address** *mac-address* | **vlan** *vlan-id* } \* | **all** } [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays static binding entries on a specified interface.  â¢interface-type specifies the interface type.  â¢interface-number specifies the interface number. | - |
| *interface-name* | interface-name specifies the name of an interface. | The value is a string of 1 to 128 case-sensitive characters, spaces not supported. |
| **ip-address** *ip-address* | Displays information about the static binding table with a specified IP address. | The value is in dotted decimal notation. |
| **mac-address** *mac-address* | Displays information about the static binding table with a specified MAC address. | The value is in hexadecimal notation. |
| **vlan** *vlan-id* | Displays information about the static binding table with a specified VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **all** | Displays static binding entries of all users. | - |
| **verbose** | Displays detailed information about the static binding table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

For static IP users, you can run the display static-bind command to view information about the configured static binding table, including the IP address, MAC address, VLAN, and interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the static binding table.
```
<HUAWEI> display user-bind static all
DHCP static Bind-table:                                  
Flags:O - outer vlan ,I - inner vlan
IP Address           MAC Address   VLAN(O/I)         Interface
--------------------------------------------------------------------------------
10.1.1.1            00e0-fc02-0003 10/--             GE1/0/1
--------------------------------------------------------------------------------
Print count:      1     Total count:      1

```

# Display detailed information about the static binding table.
```
<HUAWEI> display user-bind static all verbose
DHCP static Bind-table:                                  
Flags:O - outer vlan ,I - inner vlan
--------------------------------------------------------------------------------
 IP Address  : 10.21.21.254                                                     
 MAC Address : --                                                                                                                          
 VLAN(O/I)   : 10/--                                                     
 Interface   : GE1/0/1                                                         
--------------------------------------------------------------------------------
Print count:           1          Total count:           1

```

**Table 1** Description of the **display user-bind static** command output
| Item | Description |
| --- | --- |
| DHCP static Bind-table | Static DHCP binding entries.  To configure this parameter, run the user-bind static command. |
| IP Address | IP address of the user. |
| MAC Address | User MAC address. |
| VLAN(O/I) | Outer VLAN ID and inner VLAN ID when a user goes online. |
| Interface | Interface from which a user went online. |
| Print count | Number of printed binding tables. |
| Flags | VLAN ID.  â¢O: Outer VLAN.  â¢I: Inner VLAN.  â¢P: Vlan-mapping. |