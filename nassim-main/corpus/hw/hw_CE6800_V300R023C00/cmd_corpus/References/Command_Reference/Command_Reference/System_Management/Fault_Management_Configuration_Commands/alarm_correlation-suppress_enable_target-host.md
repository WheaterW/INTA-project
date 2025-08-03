alarm correlation-suppress enable target-host
=============================================

alarm correlation-suppress enable target-host

Function
--------



The **alarm correlation-suppress enable target-host** command enables NMS-based correlative alarm suppression.

The **undo alarm correlation-suppress enable target-host** command disables NMS-based correlative alarm suppression.



By default, NMS-based correlative alarm suppression is enabled. The system does not report correlative alarms to any NMS.


Format
------

**alarm correlation-suppress enable target-host** *ip-address* **securityname** { *security-name* | **cipher** *security-string* } [ **vpn-instance** *vpn-instance-name* ]

**alarm correlation-suppress enable target-host ipv6** *ip-address* **securityname** { *security-name* | **cipher** *security-string* } [ **vpn-instance** *vpn-instance-name* ]

**undo alarm correlation-suppress enable target-host** *ip-address* **securityname** { *security-name* | **cipher** *security-string* } [ **vpn-instance** *vpn-instance-name* ]

**undo alarm correlation-suppress enable target-host ipv6** *ip-address* **securityname** { *security-name* | **cipher** *security-string* } [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IPv4 address of an NMS. | The value is in dotted decimal notation. |
| **securityname** *security-name* | Specifies the name of an NMS. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| **cipher** *security-string* | Specifies the cipher name of an NMS. | The value is a string of case-sensitive characters, spaces not supported. A simple text password is a string of 1 to 32 case-sensitive characters. A ciphertext password is a string of 32, 48, 56, 68, or 68 to 168 characters.  If quotation marks are used around the string, spaces are allowed in the string.  During the upgrade, the device is compatible with the cipher-text passwords with different lengths before the upgrade. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a virtual private network (VPN) instance. | The value is a string of 1 to 31 case-sensitive characters, which do not contain spaces. The VPN instance name cannot be <b>\_public\_</b>. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **ipv6** *ip-address* | Specifies the IPv6 address of an NMS. | The value is a 32-digit hexadecimal number, in the format of x:x:x:x:x. |



Views
-----

Alarm management view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If a network or device is working unstably, the device generates many alarms and sends them to an NMS, which deteriorates NMS performance after the NMS receives the alarms. To suppress correlative alarms to be sent to the NMS, run the alarm correlation-suppress enable target-host command to enable NMS-based correlative alarm suppression.PrerequisiteThe **correlation-analyze enable** command has been used in the alarm view to enable alarm correlation analysis.

**Prerequisites**

The **correlation-analyze enable** command has been used in the alarm view to enable alarm correlation analysis.


Example
-------

# Disable correlative alarm suppression for an NMS named aaa123 with IP address 192.168.3.1.
```
<HUAWEI> system-view
[~HUAWEI] alarm
[~HUAWEI-alarm] correlation-analyze enable
[*HUAWEI-alarm] undo alarm correlation-suppress enable target-host 192.168.3.1 securityname aaa123

```