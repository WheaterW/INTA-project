display mac-address tunnel
==========================

display mac-address tunnel

Function
--------



The **display mac-address tunnel** command displays the number of MAC address entries.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mac-address tunnel** [ **verbose** ]

**display mac-address total-number tunnel** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Specifies the number of MAC address entries. | - |
| **total-number** | Number of Layer 2 tunnel MAC address entries. | - |
| **slot** *slot-id* | Displays statistics about MAC address entries in a specified slot. | The value is an integer. You can enter a question mark (?) and select a value from the displayed value range. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

A MAC address table is an interface-based Layer 2 forwarding table. It stores information about MAC addresses learned by a device. A MAC address entry contains a MAC address, an interface on which a packet is forwarded to this MAC address, and a VLAN to which the specified interface belongs or a VSI to which the specified interface is bound. Before forwarding a packet, the device searches the MAC address table based on the destination MAC address of the packet and locates the outbound interface quickly. This facilitates packet forwarding and reduces broadcast traffic.MAC address entries are divided into the following types:

* Static MAC address entries: configured by users and used to forward packets with specified destination MAC addresses. Static MAC address entries protect a device against attacks of forged MAC addresses and will not be aged.
* Dynamic MAC address entries: obtained by a device through source MAC address learning and will be aged based on the aging time.
* Static blackhole MAC address entries: manually configured by users. To prevent invalid MAC address entries (for example, those of unauthorized users) from occupying the MAC address table and prevent hackers from attacking a device or network using forged MAC addresses, MAC addresses of untrusted users can be configured as static blackhole MAC addresses. A device discards packets destined for the static blackhole MAC addresses. These address entries do not age out.If a device has a great number of different types of MAC addresses, you can run the display mac-address tunnel command to view the statistics about all MAC address entries in the system.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Displays the number of MAC address entries.
```
<HUAWEI> display mac-address total-number tunnel slot 1
Total number of mac-address : 50

```

**Table 1** Description of the **display mac-address tunnel** command output
| Item | Description |
| --- | --- |
| Total number of mac-address | Number of all MAC address entries in the system. |