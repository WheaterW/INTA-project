display mac-address dynamic
===========================

display mac-address dynamic

Function
--------



The **display mac-address dynamic** command displays information about dynamic MAC address entries.




Format
------

**display mac-address dynamic** [ **slot** *slot-id* ] [ **interface** { *interface-type* *interface-number* | *interface-name* } ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the interface name. | - |
| *interface-type* | Specifies the interface type. | - |
| *interface-number* | Specifies the interface number. | - |
| **verbose** | Displays detailed information about dynamic MAC address entries. | - |
| **slot** *slot-id* | Specifies the slot ID. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



A MAC address table is an interface-based Layer 2 forwarding table. It stores information about MAC addresses learned by a device. A MAC address entry contains a MAC address, an interface on which a packet is forwarded to this MAC address, and a VLAN to which the specified interface belongs or a VSI to which the specified interface is bound. Before forwarding a packet, the device searches the MAC address table based on the destination MAC address of the packet and locates the outbound interface quickly. This facilitates packet forwarding and reduces broadcast traffic.Dynamic MAC address entries: obtained by a device through source MAC address learning and will be aged based on the aging time.A MAC address table needs to be updated constantly to meet requirements for network changes. To view information about dynamic MAC address entries learned by a device, run the **display mac-address dynamic** command.



**Prerequisites**



MAC address learning has been enabled on a device.If MAC address learning is disabled on a device, run the **undo mac-address learning disable** command in the VLAN view to enable MAC address learning.



**Precautions**

If a device has learned a large number of dynamic MAC addresses, specifying parameters, such as interface, in the **display mac-address dynamic** command is recommended; otherwise, excessive output information causes the following problems:

* The displayed information is repeatedly refreshed, and required information cannot be obtained.
* The system does not respond because of long-time information traversing and searching.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display dynamic MAC address entries of a interface.
```
<HUAWEI> display mac-address dynamic
Flags: * - Backup  
       # - forwarding logical interface, operations cannot be performed based 
           on the interface.
BD   : bridge-domain   Age : dynamic MAC learned time in seconds
-------------------------------------------------------------------------------
MAC Address    VLAN/VSI/BD   Learned-From        Type                Age
-------------------------------------------------------------------------------
00e0-fc12-3456  -/-/10       Eth-Trunk2         dynamic              10
-------------------------------------------------------------------------------
Total items: 1

```

**Table 1** Description of the **display mac-address dynamic**  command output
| Item | Description |
| --- | --- |
| BD | BD domain. |
| Age | Dynamic MAC learned time in seconds. |
| MAC Address | Learned dynamic MAC address. |
| VLAN/VSI/BD | * VLAN: ID of the VLAN to which the outbound interface belongs. * VSI: name of the VSI to which the outbound interface belongs. * BD: ID of the BD to which the outbound interface belongs. |
| Learned-From | MAC address learned on this interface when the MAC address type is dynamic. |
| Type | Type of MAC address entries. dynamic indicates that MAC address entries are obtained by learning source MAC addresses. MAC address entries age after a specified aging time elapses. MAC address entries are lost after the system is reset or the board is hot swapped. |
| Total items | Total number of MAC address entries. |
| Flags | Flags. |