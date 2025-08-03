display mac-address bridge-domain
=================================

display mac-address bridge-domain

Function
--------



The **display mac-address bridge-domain** command displays MAC address entries in a specified bridge domain (BD).



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mac-address** { *mac-address* **bridge-domain** *bd-id* | **bridge-domain** *bd-id* } [ **verbose** ]

**display mac-address static bridge-domain** *bd-id* [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Displays an entry with a specified MAC address. | The value is a 12-digit hexadecimal number, in the format of H-H-H. Each H is 4 digits. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF or a multicast MAC address starting with 01. |
| *bd-id* | Displays MAC address entries in a BD with a specified ID. | The value is an integer that ranges from 1 to 16777215. |
| **verbose** | Displays detailed information about MAC address entries in a BD with a specified ID. | - |
| **static** | Displays static MAC address entries.  The static parameter configured in this command helps verify that a user device is correctly bound to an interface so that authorized users' communication can be ensured. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

A MAC address table is an interface-based Layer 2 forwarding table. It stores information about MAC addresses learned by a device. A MAC address entry contains a MAC address, an interface on which a packet is forwarded to this MAC address, and a VLAN to which the specified interface belongs or a VSI to which the specified interface is bound. Before forwarding a packet, the device searches the MAC address table based on the destination MAC address of the packet and locates the outbound interface quickly. This facilitates packet forwarding and reduces broadcast traffic.Static MAC address entries: configured by users and used to forward packets with specified destination MAC addresses. Static MAC address entries protect a device against attacks of forged MAC addresses and will not be aged.To view MAC address entries in a specified bridge domain (BD), run the display mac-address bridge-domain.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all MAC address entries in BD 10.
```
<HUAWEI> display  mac-address bridge-domain 10
Flags: * - Backup  
       # - forwarding logical interface, operations cannot be performed based 
           on the interface.
BD   : bridge-domain   Age : dynamic MAC learned time in seconds
-------------------------------------------------------------------------------
MAC Address    VLAN/VSI/BD   Learned-From        Type                Age
-------------------------------------------------------------------------------
00e0-fc12-3456  -/-/10       Eth-Trunk20.1       static                -
-------------------------------------------------------------------------------
Total items: 1

```

# Display detailed information about MAC address.
```
<HUAWEI> display mac-address verbose
BD: bridge-domain Age: dynamic MAC learned time in seconds
MAC address table:
-------------------------------------------------------------------------------
MAC Address: 00e0-fc12-3456 VLAN/VSI/BD : 2/-/- 
Type : static Learned-From : - 
PEVLAN : - CEVLAN : - 
Aging time : - 
-------------------------------------------------------------------------------
Total items displayed = 1

```

**Table 1** Description of the **display mac-address bridge-domain** command output
| Item | Description |
| --- | --- |
| BD | BD domain. |
| Age | Dynamic MAC learned time in seconds. |
| MAC Address | MAC address. |
| MAC address table | MAC address table. |
| VLAN/VSI/BD | * VLAN: ID of a VLAN to which an outbound interface belongs. * BD: ID of a BD to which an outbound interface belongs. * VSI: ID of a virtual switching instance (VSI) to which an outbound interface belongs. |
| Learned-From | Current MAC address that is learned from the interface. |
| Type | Types of MAC address entries:   * static: Static MAC address entries which are configured by users. They will not age out. They remain in the MAC address table after the system is restarted or a board is hot swapped. * blackhole: Static blackhole MAC address entries which are configured by users. They will not age out. They remain in the MAC address table after the system is restarted or a board is hot swapped. * dynamic: Dynamic MAC address entries which are obtained by learning source MAC addresses. They will age out after the aging time expires. They are removed from the MAC address table after the system is restarted or a board is hot swapped. * dyn-blackhole: indicates dynamic blackhole MAC address entries. Dynamic blackhole MAC addresses are configured by users, and the entries will not be aged. They are removed from the MAC address table after the system is restarted or a board is hot swapped. |
| Total items | Total number of static MAC address entries that are displayed. |
| PEVLAN | Single VLAN tag or outer VLAN tag in the packet received by the interface.  No meaning on an EVPN and always displayed as a hyphen (-). |
| CEVLAN | Inner VLAN tag carried in packets received by an interface.  If there is no inner VLAN tag, a hyphen (-) is displayed. |
| Aging time | Aging time. |
| Flags | Flags. |