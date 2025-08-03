display system mac-address
==========================

display system mac-address

Function
--------



The **display system mac-address** command displays the system MAC address.




Format
------

**display system mac-address** [ **all** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays the MAC addresses of all devices in the system, including the MAC addresses of the devices that are unavailable but configured offline. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can display the system MAC address, including the offline configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the system MAC address.
```
<HUAWEI> display system mac-address
Current System MAC address: 00e0-fc12-3456
Current System MAC number : 16
User-configured MAC address: --
User-configured MAC number : --
Manufacture MAC Information:
-------------------------------------
Slot       MAC               Number
-------------------------------------
1          00e0-fc12-3456    16

```

# Display the system MAC address, including the offline configuration.
```
<HUAWEI> display system mac-address all
Current System MAC address: 00e0-fc12-4567
Current System MAC number : 16
User-configured MAC address: --
User-configured MAC number : --
Note: (Offline): Offline slot
Manufacture MAC Information:
------------------------------------------
Slot       MAC               Number
------------------------------------------
1          00e0-fc12-4567    16

```

**Table 1** Description of the **display system mac-address** command output
| Item | Description |
| --- | --- |
| Current System MAC address | Current system MAC address. |
| Current System MAC number | Number of system MAC addresses. |
| MAC | MAC address of a DHCP client. |
| User-configured MAC address | Configured MAC address. |
| User-configured MAC number | Number of configured MAC addresses. |
| Manufacture MAC Information | Default MAC address of the switch. |
| Number | Number of MAC addresses. |
| Slot | Slot ID of the device.  Offline indicates the offline configuration. |