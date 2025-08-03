display arp track
=================

display arp track

Function
--------



The **display arp track** command displays detailed information about the outbound interface changes in ARP entries learned by the VLANIF/VBDIF interface.




Format
------

**display arp track**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



When the outbound interface information in an ARP entry learned by an interface changes, traffic is interrupted frequently and randomly. To quickly locate the fault, run the **display arp track** command to check records about the change of outbound interface information and check the time of change.



**Prerequisites**



ARP entries have been learned by the interface, and the outbound interface information in an ARP entry changes.



**Precautions**

After the **display arp track** command is run, information about the change of ARP entries due to the following reasons will be displayed:

* The interface learns dynamic ARP entries, and the outbound interface is updated.
* The outbound interface information in a short static ARP entry changes.
* A dynamic ARP entry or a short static ARP entry is deleted.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the change of ARP entries.
```
<HUAWEI> display arp track
Operate Flags: M - Modify, D - Delete
-------------------------------------------------------------------------------------------------------------------
Op IP-Address      MAC-Address    VLAN/BD    Old-Vlan    New-Vlan    Old-Port       New-Port       System-Time
-------------------------------------------------------------------------------------------------------------------
M  10.1.1.1        00e0-fc12-3456 1000                               100GE1/0/1     100GE1/0/2     08-19 12:10:12

```

**Table 1** Description of the **display arp track** command output
| Item | Description |
| --- | --- |
| Operate Flags | Operation identifier, which can be:   * M: Modify, indicating that the outbound interface information changes. * D: Delete, indicating that the ARP entry is deleted. |
| Op | Operation identifier, which can be:   * M: Modify, indicating that the outbound interface information changes. * D: Delete, indicating that the ARP entry is deleted. |
| IP-Address | IP address in an ARP entry. |
| MAC-Address | MAC address in an ARP entry. |
| VLAN | ID of the VLAN to which the VLANIF interface belongs. |
| Old-Port | Previous outbound interface in an ARP entry. |
| New-Port | New outbound interface in an ARP entry. |
| System-Time | System time when the outbound interface information changes. |
| VLAN/BD | ID of the BD to which the VBDIF interface belongs. |
| Old-Vlan | Old VLAN ID bound to the BD. |
| New-Vlan | New VLAN ID bound to the BD. |