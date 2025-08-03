display snmp-agent usm-user
===========================

display snmp-agent usm-user

Function
--------



The **display snmp-agent usm-user** command displays information about an SNMP user.




Format
------

**display snmp-agent usm-user** [ **engineid** *engineid* | **username** *user-name* | **group** *group-name* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **engineid** *engineid* | Displays information about an SNMPv3 user with a specified engine ID. | The value is a string of 10 to 64 case-sensitive characters, spaces not supported. |
| **username** *user-name* | Displays information about a specified SNMPv3 user. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| **group** *group-name* | Displays the SNMPv3 user belonging to a specified group. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view the SNMP user information configured, run the **display snmp-agent usm-user** command. The SNMP user is a remote user that carries out SNMP management.The command output contains the following information:

* User name.
* Local engine ID of the user. The SNMP engine ID uniquely identifies an SNMP agent in a management domain. The SNMP engine ID is an important component of the SNMP agent. It helps schedule and process SNMP messages and implement security authentication and access control.

**Precautions**

The **display snmp-agent usm-user** command is applicable only to SNMPv3 users.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all SNMP users.
```
<HUAWEI> display snmp-agent usm-user
   User name: test
       Engine ID: 800007DB0338BA83002F01 active
       Authentication Protocol: sha2-256
       Privacy Protocol: aes128
       Group name: gtest
       State: Active

```

**Table 1** Description of the **display snmp-agent usm-user** command output
| Item | Description |
| --- | --- |
| User name | Name of an SNMP user. |
| Engine ID | Engine ID of an SNMP-enabled device. |
| Authentication Protocol | Type of an authentication protocol. |
| Privacy Protocol | Encryption mode. |
| Group name | User group to which the user belongs. |
| State | Status of an SNMP user. |