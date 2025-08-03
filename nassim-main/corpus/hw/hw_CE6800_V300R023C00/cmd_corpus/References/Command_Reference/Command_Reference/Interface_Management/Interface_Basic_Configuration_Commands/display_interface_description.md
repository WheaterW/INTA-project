display interface description
=============================

display interface description

Function
--------



The **display interface description** command displays the description of the interfaces on a device.




Format
------

**display interface description** [ *interface-name* | *interface-type* [ *interface-number* ] | **slot** *slot-id* [ **card** *card-number* ] ] [ **full-name** ]

**display interface description** [ *interface-type* | **slot** *slot-id* [ **card** *card-number* ] ] [ **full-name** ] **main**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Displays the description of a specified interface. | - |
| *interface-type* | Specifies the type of an interface.  If no interface type is specified, the description of all interfaces is displayed. | The value is of the enumerated type. |
| *interface-number* | Specifies the number of an interface.  If an interface type is specified but no interface number is specified, the description of all interfaces of this type is displayed. | - |
| **slot** *slot-id* | Specifies the slot number.  If no slot number is specified, the description of all slots is displayed. | The value is a string of 1 to 23 case-sensitive characters. It cannot contain spaces. |
| **card** *card-number* | Specifies the subcard number.  If a slot ID is specified but no interface number is specified, the description of the interfaces on all the subcards in the specified slot is displayed. | - |
| **full-name** | Indicates the full name of an interface. | - |
| **main** | Displays the description of a main interface not a sub-interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



For simplifying interface management, run the **description** command to record the use of each interface. In the case of many interfaces, run the **display interface description** command to view the description of these interfaces.If the interface is Down, check whether the link connection is correct or whether interface negotiation succeeds.



**Precautions**



All activation interfaces are described in specifications. It is recommended that the interfaces be described in compliance with customer specifications.If the customer does not have the specifications, describe the interface according to the following rules: Local device name-Local port number -> Peer device name-Peer port number//Port rate.If the description of an interface displayed by running the **display interface description** command does not comply with the specifications, run the **description** command to describe the interface.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the description of all the Ethernet interfaces on a device.
```
<HUAWEI> display interface description 100GE
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(s): spoofing
(b): BFD down
(e): ETHOAM down
(d): Dampening Suppressed
(p): port alarm down
(dl): DLDP down
(c): CFM down
(ms): MACsec down
(ed): error down
Interface                     PHY     Protocol Description
100GE1/0/1                    up      down     Connecting to Nanjing
100GE1/0/1                    up      down

```

# Display the description of 100GE 1/0/1 on a device.
```
<HUAWEI> display interface description 100GE 1/0/1
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(s): spoofing
(b): BFD down
(e): ETHOAM down
(d): Dampening Suppressed
(p): port alarm down
(dl): DLDP down
(c): CFM down
(ms): MACsec down
(ed): error down
Interface                     PHY     Protocol Description
100GE1/0/1                    *down   down     Nanjing

```

# Display the description of all interfaces on a device.
```
<HUAWEI> display interface description
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(s): spoofing
(b): BFD down
(e): ETHOAM down
(d): Dampening Suppressed
(p): port alarm down
(dl): DLDP down
(c): CFM down
(ms): MACsec down
(ed): error down
Interface                     PHY     Protocol Description
100GE1/0/1                    up      down     Connecting to Nanjing
100GE1/0/1                    up      down     
100GE1/0/1.1                  up      down  
NULL0                         up      up       NULL0 Interface

```

**Table 1** Description of the **display interface description** command output
| Item | Description |
| --- | --- |
| Interface | Interface type and number. |
| PHY | Physical status of the interface. The options are as follows:   * up: indicates that the physical layer of the interface is Up. * down: indicates that the physical layer of the interface is faulty. * \*down: Administratively DOWN. The network administrator runs the shutdown command on the interface. * ^down: standby, indicating that the interface is a standby interface. * (l): loopback, indicating that the loopback function is enabled on the interface. * (E): E-Trunk down, indicating that the Eth-Trunk interface goes Down due to E-Trunk protocol negotiation. * (b): BFD down, indicating that the physical layer of the interface is in BFD Down state. * (p): port alarm down, indicating that the interface alarm is associated with the physical status Down, for example, CRC alarm. * (ed): error down, indicating that the physical layer of the interface is in Error Down state. * (ex): External-detection down, indicating that the interface goes Down when the device detects that the IP address is not allowed. For example, if 1.1.1.1 is configured using the external communication detection command and the device is connected to 1.1.1.1, the interface goes Down. * (lcs): The license of the Ethernet interface on the CM board is not activated. * (D): DF backup down, indicating that the interface is Down due to EVPN DF election.   The actual supported physical status depends on the actual device. |
| Protocol | Link layer protocol status of the interface.   * Up: The link layer protocol of this interface is working properly. * Down: The link layer protocol of this interface becomes faulty. * \*down: administratively Down. The administrator runs the shutdown network-layer command on the interface. * (l): loopback. The interface is enabled with the loopback function. * (s): spoofing. The interface is enabled with the spoofing function. * (b): BFD Down. The link layer protocol of the interface is in the BFD Down state. * (B): Bit-error-detection down. The data link layer of the interface is in the bit error Down state. * (e): ETHOAM down. The physical layer of the interface is in the EFM fault state. * (d): dampening suppressed. The protocol of the interface is suppressed. * (ld): loop-detect trigger down. The interface is set to Down to prevent a loop. * (dl): DLDP Down. The link layer of the interface is in DLDP Down state. * (c): CFM down. The interface goes Down due to the CFM configuration. * (ms): MACsec down. The link layer of the interface is in MACsec down state. * Blank: The interface is not configured with a link layer protocol. |
| Description | Interface description.  If the description command is not used to configure the interface description, the description is empty by default. |