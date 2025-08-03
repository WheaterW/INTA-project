if-match destination-mac
========================

if-match destination-mac

Function
--------



The **if-match destination-mac** command configures a matching rule based on the destination MAC address in a traffic classifier.

The **undo if-match destination-mac** command deletes a matching rule based on the destination MAC address in a traffic classifier.



By default, a matching rule based on the destination MAC address is not configured in a traffic classifier.


Format
------

**if-match destination-mac** *mac-address* [ *mac-address-mask* ]

**undo if-match destination-mac**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *mac-address* | Specifies the destination MAC address. | The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits. |
| *mac-address-mask* | Specifies the mask of the destination MAC address. The mask of the MAC address is similar to the mask of the IP address. The value 1 indicates that the bit is matched, and the value 0 indicates that the bit is not matched. The mask can be used to determine a group of MAC addresses. You can use the mask of the MAC address to accurately match certain bits in the destination MAC address. You can set these bits to 1 in the mask of the destination MAC address. | The value is in H-H-H format. An H is a hexadecimal number of 1 to 4 digits. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the if-match destination-mac command to configure a matching rule based on the destination MAC address in a traffic classifier so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

If you run the if-match destination-mac command in the same traffic classifier view multiple times, only the latest configuration takes effect.


Example
-------

# Configure a matching rule based on the destination MAC address of 00e0-fc12-3456 in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match destination-mac 00e0-fc12-3456

```