display mac-address summary
===========================

display mac-address summary

Function
--------



The **display mac-address summary** command displays statistics about all MAC address entries on a device.




Format
------

**display mac-address summary** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Displays the usage of a MAC address table on a specified board. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



A MAC address table is an interface-based Layer 2 forwarding table. It stores information about MAC addresses learned by a device. A MAC address entry contains a MAC address, an interface on which a packet is forwarded to this MAC address, and a VLAN to which the specified interface belongs or a VSI to which the specified interface is bound. Before forwarding a packet, the device searches the MAC address table based on the destination MAC address of the packet and locates the outbound interface quickly. This facilitates packet forwarding and reduces broadcast traffic.If a device learns a great number of MAC addresses of different types, run the **display mac-address summary** command to view statistics about the MAC address entries on the device.



**Precautions**



If no static or static blackhole MAC address entries are configured on a device, statistics about the two types of MAC address entries are 0.If MAC address learning is disabled on a device, statistics about dynamic MAC address entries are 0. You can run the **undo mac-address learning disable** command in the VLAN view to enable MAC address learning.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about the MAC address entries on the device.
```
<HUAWEI> display mac-address summary
Summary information of slot 1:
Capacity of this slot : 32768      
-----------------------------------
Static     :               1
Blackhole  :               1
Dyn-Local  :               13
Dyn-Remote :               0
Dyn-Trunk  :               0
OAM        :               0
Sticky     :               0
Security   :               0
Authen     :               0
Guest      :               0
Mux        :               0
Tunnel     :               0
Snooping   :               0
Evn        :               0
Ovsdb      :               0
Dyn-blackhole :            0
In-used    :               15
-----------------------------------

```

# Display statistics about MAC address entries on a board.
```
<HUAWEI> display mac-address summary slot 1
Summary information of slot 1:
Capacity of this slot : 32768      
-----------------------------------
Static     :               1
Blackhole  :               1
Dyn-Local  :               13
Dyn-Remote :               0
Dyn-Trunk  :               0
OAM        :               0
Sticky     :               0
Security   :               0
Authen     :               0
Guest      :               0
Mux        :               0
Tunnel     :               0
Snooping   :               0
Evn        :               0
Ovsdb      :               0
Dyn-blackhole :            0
In-used    :               15
-----------------------------------

```

**Table 1** Description of the **display mac-address summary** command output
| Item | Description |
| --- | --- |
| Summary information of slot | Number of the slot where the board is installed. |
| Capacity of this slot | Maximum number of MAC address entries that can be stored on the current board. |
| Dyn-Local | Number of MAC address entries learned by the local slot. |
| Dyn-Remote | Number of MAC address entries synchronized from other boards. |
| Dyn-Trunk | Total number of MAC address entries learned by all Eth-Trunk interfaces. |
| OAM | Number of OAM MAC address entries. |
| Sticky | Number of sticky MAC address entries.  The device does not support sticky MAC address. |
| Security | Number of secure-dynamic MAC address entries.  The device does not support secure-dynamic MAC address. |
| Authen | Number of MAC address entries corresponding to authentication users. |
| Guest | Number of MAC address entries learned by interfaces in the guest VLAN. |
| Mux | Number of MAC address entries learned by interfaces that have the MUX VLAN function enabled. |
| Tunnel | Number of MAC address entries learned by Layer 2 tunnel. |
| Snooping | Number of Snooping MAC address entries. |
| Evn | Number of Ethernet Virtual Network (EVN) MAC address entries. |
| Ovsdb | Number of Ovsdb MAC address entries.  The device does not support Ovsdb MAC address. |
| In-used | Total number of existing MAC address entries. |
| Dyn-blackhole | Total number of dynamic blackhole entries. |