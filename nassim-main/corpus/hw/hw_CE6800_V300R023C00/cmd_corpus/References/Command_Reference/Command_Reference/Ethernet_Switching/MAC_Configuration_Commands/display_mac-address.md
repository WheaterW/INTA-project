display mac-address
===================

display mac-address

Function
--------



The **display mac-address** command displays information about MAC address entries.

The **display mac-address blackhole** command displays information about static blackhole MAC address entries.

The **display mac-address static** command displays information about static MAC address entries.

The **display mac-address dynamic** command displays dynamic MAC address entries.

The **display mac-address authen** command displays information about authentication MAC address entries.

The **display mac-address total-number** command displays the number of MAC address entries of a specified type.

The **display mac-address total-number authen** command displays the number of authentication MAC address entries.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display mac-address dynamic** [ **slot** *slot-id* ] { **interface** { *interface-type* *interface-number* | *interface-name* } **vlan** *vlan-id* | **vlan** *vlan-id* [ **interface** { *interface-type* *interface-number* | *interface-name* } ] } [ **verbose** ]

**display mac-address** *mac-address* [ **vlan** *vlan-id* ] [ **verbose** ]

**display mac-address blackhole** [ **vlan** *vlan-id* ] [ **verbose** ]

**display mac-address** { [ **vlan** *vlan-id* ] | [ **interface** { *interface-type* *interface-number* | *interface-name* } ] } \* [ **verbose** ]

**display mac-address static** { [ **vlan** *vlan-id* ] | [ **interface** { *interface-type* *interface-number* | *interface-name* } ] } \* [ **verbose** ]

**display mac-address authen** { [ **vlan** *vlan-id* ] | [ **interface** { *interface-type* *interface-number* | *interface-name* } ] } \* [ **verbose** ]

**display mac-address total-number authen** { [ **vlan** *vlan-id* ] | [ **interface** { *interface-type* *interface-number* | *interface-name* } ] } \*

For CE8855, CE8851-32CQ4BQ, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display mac-address total-number** { [ **static** | **mux** | **security** | **sticky** | **dynamic** ] { [ **vlan** *vlan-id* ] | [ **interface** { *interface-type* *interface-number* | *interface-name* } ] } \* | { **blackhole** | **evn** } [ **vlan** *vlan-id* ] | [ **dynamic** ] **slot** *slot-id* }

**display mac-address** { **mux** | **security** | **sticky** } { [ **vlan** *vlan-id* ] | [ **interface** { *interface-type* *interface-number* | *interface-name* } ] } \* [ **verbose** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K:

**display mac-address total-number** { [ **static** | **mux** | **dynamic** ] { [ **vlan** *vlan-id* ] | [ **interface** { *interface-type* *interface-number* | *interface-name* } ] } \* | { **blackhole** | **evn** } [ **vlan** *vlan-id* ] | [ **dynamic** ] **slot** *slot-id* }

**display mac-address mux** { [ **vlan** *vlan-id* ] | [ **interface** { *interface-type* *interface-number* | *interface-name* } ] } \* [ **verbose** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display mac-address evn** [ **vlan** *vlan-id* ] [ **verbose** ]

**display mac-address total-number dynamic-blackhole**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**display mac-address total-number** [ **static** ] **bridge-domain** *bd-id*

**display mac-address dynamic-blackhole** [ **bridge-domain** *bd-id* ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **vlan** *vlan-id* | Displays the number of MAC address entries in a specified VLAN. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **verbose** | Display detailed information of the static MAC address entries. | - |
| *mac-address* | Displays a specified MAC address entry. | The value is a hexadecimal number in the format of H-H-H. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. |
| **total-number** | Displays the total number of MAC address entries with multiple outbound interfaces. | - |
| **static** | Displays the number of static MAC address entries. | - |
| **mux** | Displays the number of MUX MAC address entries. | - |
| **security** | Displays the number of secure-dynamic MAC address entries.  This parameter is supported only by CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H and CE6881H-K.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **sticky** | Displays the number of sticky MAC address entries.  This parameter is supported only by CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H and CE6881H-K.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **dynamic** | Displays the number of dynamic MAC address entries. | - |
| **blackhole** | Number of blackhole MAC address entries. | - |
| **evn** | Displays the number of EVN MAC address entries.  This parameter is supported only on the CE6866, CE6860-HAM, CE6860-SAN, CE6866K, CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8850-HAM, CE8850-SAN, CE8851K, CE6863H, CE6863H-K, CE6881H and CE6881H-K. | - |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 23 case-sensitive characters, spaces not supported. |
| **authen** | Displays the number of authenticated MAC address entries. | - |
| **dynamic-blackhole** | Displays dynamic blackhole entries.  This parameter is supported only on the CE6866, CE6860-HAM, CE6860-SAN, CE6866K, CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8850-HAM, CE8850-SAN, CE8851K, CE6863H, CE6863H-K, CE6881H and CE6881H-K. | - |
| **bridge-domain** *bd-id* | Specifies a BD ID.  This parameter is supported only on the CE6866, CE6860-HAM, CE6860-SAN, CE6866K, CE6885, CE8851-32CQ4BQ, CE8851-32CQ8DQ-P, CE8855, CE8850-HAM, CE8850-SAN, CE8851K, CE6863H, CE6863H-K, CE6881H and CE6881H-K.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

A MAC address table is a port-based Layer 2 forwarding table. It stores MAC addresses learned by a device from other devices, including MAC addresses, ports associated with the MAC addresses, and VLAN IDs or VSIs to which the specified ports belong. When forwarding data, the device searches the MAC address table for the outbound interface based on the destination MAC address in the packet. This reduces broadcast traffic.MAC address entries are classified into the following types:

* Static MAC address entries: They are manually configured so that packets with specified destination MAC addresses are forwarded by specified interfaces. Static MAC address entries protect devices against attacks with forged MAC addresses. Static MAC address entries will not be aged out.
* Dynamic MAC address entries: obtained by learning source MAC addresses. Dynamic MAC address entries can be aged out after the aging time expires.
* Static blackhole MAC address entries: manually configured by users. To prevent useless MAC address entries (such as MAC address entries of unauthorized users) from occupying the MAC address table and prevent hackers from using MAC addresses to attack user devices or networks, you can configure MAC addresses of untrusted users as static blackhole MAC addresses. Packets destined for these untrusted MAC addresses are discarded. These entries will not be aged out.

**Prerequisites**

A static blackhole MAC address entry has been configured using the **mac-address blackhole** command in the system view, a static MAC address entry has been configured using the **mac-address static vlan** command, or a MAC address entry has been configured using another command.

**Precautions**

If a device has a large number of MAC address entries, it is recommended that you specify a VLAN or VSI in the **display mac-address** command to filter the output information. Otherwise, excessive output information may cause the following problems:

* The terminal screen is refreshed continuously and the required information cannot be obtained.
* The system traverses and retrieves information for a long time. As a result, the system does not respond.If a large number of static MAC address entries are configured on a device, it is recommended that you specify a VLAN or VSI in the **display mac-address static** command to filter the output information. Otherwise, excessive output information may cause the following problems:
* The terminal screen is refreshed continuously and the required information cannot be obtained.
* The system traverses and retrieves information for a long time. As a result, the system does not respond.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all static blackhole MAC address entries.
```
<HUAWEI> display mac-address blackhole
---- Flags: * - Backup                                                                                                              
     BD: bridge-domain         Age: dynamic MAC learned time in seconds                                                                   
-------------------------------------------------------------------------------                                                     
MAC Address       VLAN/VSI/BD                 Learned-From        Type        Age                                                   
-------------------------------------------------------------------------------                                                     
00-e0-fc-12-34-56 200/-/-                     -                   blackhole      -                                                
-------------------------------------------------------------------------------                                                     
Total items: 1

```

# Display the number of dynamic MAC addresses in VLAN 100.
```
<HUAWEI> display mac-address total-number dynamic vlan 100
Total number of mac-address : 50

```

# Display the detailed information about static blackhole MAC address entries.
```
<HUAWEI> display mac-address blackhole verbose
BD: bridge-domain    Age: dynamic MAC learned time in seconds
MAC address table:
-------------------------------------------------------------------------------
MAC Address: 00-e0-fc-12-34-56      VLAN/VSI/BD        : 10/-/-                    
Type       : blackhole              Learned-From       : -                         
PEVLAN     : 10                     CEVLAN             : -                         
Aging time : -                 
-------------------------------------------------------------------------------
Total items displayed = 1

```

# Display the number of static MAC address entries.
```
<HUAWEI> display mac-address total-number static
Total number of mac-address : 600

```

# Display detailed information about static MAC address entries.
```
<HUAWEI> display mac-address static verbose
BD: bridge-domain    Age: dynamic MAC learned time in seconds
MAC address table:
-------------------------------------------------------------------------------
MAC Address: 00-e0-fc-12-34-56      VLAN/VSI/BD        : 10/-/-                    
Type       : static                 Learned-From       : 100GE1/0/1                   
PEVLAN     : 10                     CEVLAN             : -                         
Aging time : -                 
-------------------------------------------------------------------------------
Total items displayed = 1

```

# Display the number of dynamic MAC address entries on 100GE 1/0/1.
```
<HUAWEI> display mac-address total-number dynamic interface 100ge 1/0/1
Total number of mac-address : 5000

```

**Table 1** Description of the **display mac-address**  command output
| Item | Description |
| --- | --- |
| MAC Address | Configured static MAC address, MAC address in a specific entry, or configured static blackhole MAC address. |
| MAC address table | MAC address table. |
| VLAN/VSI/BD | * VLAN: ID of the VLAN to which the outbound interface belongs. * VSI: name of the VSI to which the outbound interface belongs. * BD: ID of the BD to which the outbound interface belongs. |
| Learned-From | * Static MAC address configured on this interface when the MAC address type is static. * MAC address learned on this interface when the MAC address type is dynamic. * A hyphen (-) is displayed when the MAC address type is blackhole. |
| Type | Type of a MAC address.   * static: Static MAC address entries which are configured by users. They will not age out. They remain in the MAC address table after the system is restarted or a board is hot swapped. * blackhole: Static blackhole MAC address entries which are configured by users. They will not age out. They remain in the MAC address table after the system is restarted or a board is hot swapped. * dynamic: Dynamic MAC address entries which are obtained by learning source MAC addresses. They will age out after the aging time expires. They are removed from the MAC address table after the system is restarted or a board is hot swapped. |
| Age | Dynamic MAC learned time in seconds. |
| Total number of mac-address | Number of MAC address entries in the system. |
| Total items | Total number of MAC address entries that match specific rules. |
| PEVLAN | Single or outer VLAN tag carried in the packets received by the interface. |
| CEVLAN | Inner VLAN tag in the double VLAN tags of packets received by an interface. |
| Aging time | Aging time of MAC address entries. |
| BD | BD ID. |