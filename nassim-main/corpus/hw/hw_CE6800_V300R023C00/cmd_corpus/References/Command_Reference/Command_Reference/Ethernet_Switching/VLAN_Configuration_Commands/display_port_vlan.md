display port vlan
=================

display port vlan

Function
--------



The **display port vlan** command displays information about interfaces in a VLAN.




Format
------

**display port vlan** [ *interface-type* *interface-number* | *interface-name* ]

**display port vlan** [ *interface-type* *interface-number* | *interface-name* ] **active**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-type* | Specifies an interface type. | - |
| *interface-number* | Specifies an interface number. | - |
| *interface-name* | Specifies the name of an interface. | - |
| **active** | Displays information about interfaces with specified types and numbers in successfully created VLANs. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view information about interfaces in all VLANs configured on a device, run the display port vlan [ interface-type interface-number ] command. If you want to view information only about interfaces with specified types and numbers in successfully created VLANs, specify active in the preceding command. If a fault occurs on an interface, you can locate the fault based on the information about the interface and VLAN.



**Precautions**

If a large amount of information about interfaces and VLANs is displayed on a device, specifying an interface when you run the display port vlan command is recommended. Otherwise, the following problems may occur due to excessive output information:

* The displayed information is continuously refreshed, and locating desired information is difficult.
* The system fails to respond to other requests because it is busy searching information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about interfaces with specified types and numbers in successfully created VLANs.
```
<HUAWEI> display port vlan 100ge 1/0/1 active
T=TAG U=UNTAG
Port                    Link Type    PVID        VLAN List
-------------------------------------------------------------------------------
100GE1/0/1              hybrid       1           U:25

```

# Display information about interfaces in all VLANs configured on a device.
```
<HUAWEI> display port vlan
Port                    Link Type    PVID  Trunk VLAN List                      Port Description
---------------------------------------------------------------------------------------------------------------
Eth-Trunk1              hybrid       1     1-11                                 
Eth-Trunk2              hybrid       1     2-3                                  
100GE1/0/1              hybrid       0     -

```

**Table 1** Description of the **display port vlan** command output
| Item | Description |
| --- | --- |
| T=TAG | Tagged. |
| U=UNTAG | Untagged. |
| Port | Interface type and number. |
| Port Description | The description of a Layer 2 interface. You can run the description (interface view) command to configure the description of an interface. |
| Link Type | Type of the interface link:   * access. * trunk. * hybrid. * dot1q-tunnel. |
| PVID | Default VLAN ID of the interface. |
| VLAN List | Interface's ID list of successfully created VLANs. |
| Trunk VLAN List | ID of the permitted VLAN that is configured using the command. |