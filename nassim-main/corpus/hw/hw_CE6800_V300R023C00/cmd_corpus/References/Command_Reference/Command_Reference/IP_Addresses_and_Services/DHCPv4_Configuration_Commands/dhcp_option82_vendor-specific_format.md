dhcp option82 vendor-specific format
====================================

dhcp option82 vendor-specific format

Function
--------



The **dhcp option82 vendor-specific format** command configures the Sub9 field in the Option 82 field.

The **undo dhcp option82 vendor-specific format** command deletes the configuration of the Sub9 field inserted into the DHCP Option 82 field.



By default, the Sub9 field inserted into the Option 82 field is not configured.


Format
------

**dhcp option82 vendor-specific format vendor-sub-option** *sub-option-num* { **ascii** *ascii-text* | **hex** *hex-text* | **ip-address** *ip-address* &<1-8> | **sysname** }

**undo dhcp option82 vendor-specific format vendor-sub-option** *sub-option-num*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ascii** *ascii-text* | Specifies the ASCII character string in the vendor-specific suboption in the Sub9 field. | The value is an ASCII character string and must be smaller than 129 characters. |
| **hex** *hex-text* | Specifies the HEX character string in the vendor-specific suboption in the Sub9 field. | The value is in hexadecimal notation. The value can contain only numerals 0 to 9, lowercase letters a to f, and uppercase letters A to F. If no space is included, the value length must be an even number smaller than 257. |
| **ip-address** *ip-address* | Specifies the IP address in the vendor-specific suboption in the Sub9 field. | The value is in dotted decimal notation. |
| **sysname** | Specifies the device name in the vendor-specific suboption in the Sub9 field. | - |
| **vendor-sub-option** *sub-option-num* | Specifies the vendor-specific suboption in the Sub9 field. | The value is an integer ranging from 1 to 255. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In authentication for wired Ethernet access using DHCP and Option 82, a device can insert suboptions (suboption 1, suboption 2, and suboption 9) to the Option 82 field in DHCP Request messages. These suboptions in DHCP Request messages carry information about user device locations. Unauthorized users cannot access the network by static IP addresses or embezzled accounts of authorized users. The dhcp option82 vendor-specific format command configures the suboptions in the Sub9 field.

**Prerequisites**

DHCP has been enabled globally using the **dhcp enable** command.


Example
-------

# Insert the device name to the vendor-specific suboption 1 in the Sub9 field.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp option82 vendor-specific format vendor-sub-option 1 sysname

```