called-station-id mac-format
============================

called-station-id mac-format

Function
--------



The **called-station-id mac-format** command sets the encapsulation format of the MAC address in the called-station-id (Type 30) attribute of RADIUS packets.

The **undo called-station-id mac-format** command restores the default encapsulation format of the MAC address in the called-station-id (Type 30) attribute of RADIUS packets.



By default, the encapsulation format of the MAC address in the called-station-id attribute of RADIUS packets is XX-XX-XX-XX-XX-XX, in uppercase.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**called-station-id mac-format** { **dot-split** | **hyphen-split** } [ **mode1** | **mode2** ] [ **lowercase** | **uppercase** ]

**called-station-id mac-format unformatted** [ **lowercase** | **uppercase** ]

**undo called-station-id mac-format**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dot-split** | Indicates that the dot (.) is used as the separator in a MAC address in the called-station-id attribute. | - |
| **hyphen-split** | Indicates that the hyphen (-) is used as the separator in a MAC address in the called-station-id attribute. | - |
| **mode1** | Indicates that the MAC address in the called-station-id attribute uses the XXXX-XXXX-XXXX or XXXX.XXXX.XXXX format. | - |
| **mode2** | Indicates that the MAC address in the called-station-id attribute uses the XX-XX-XX-XX-XX-XX or XX.XX.XX.XX.XX.XX format. | - |
| **lowercase** | Indicates that the MAC address in the called-station-id attribute is in lowercase. | - |
| **uppercase** | Indicates that the MAC address in the called-station-id attribute is in uppercase. | - |
| **unformatted** | Indicates that no separator is used in a MAC address in the called-station-id attribute. | - |



Views
-----

RADIUS server template view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The default encapsulation format of the MAC address in the called-station-id (Type 30) attribute of RADIUS packets from the device is XX-XX-XX-XX-XX-XX. If the RADIUS server does not support the default format, run the **called-station-id mac-format** command to change the format.


Example
-------

# Set the dot as the separator in a MAC address and the encapsulation format of the MAC address in the called-station-id attribute to XX.XX.XX.XX.XX.XX in uppercase.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template huawei
[*HUAWEI-radius-huawei] called-station-id mac-format dot-split mode2 uppercase

```