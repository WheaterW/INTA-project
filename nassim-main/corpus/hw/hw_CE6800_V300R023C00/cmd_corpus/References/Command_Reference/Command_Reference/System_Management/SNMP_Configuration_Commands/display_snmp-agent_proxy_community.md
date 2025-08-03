display snmp-agent proxy community
==================================

display snmp-agent proxy community

Function
--------



The **display snmp-agent proxy community** command displays SNMP proxy community information.




Format
------

**display snmp-agent proxy community** *community-name*

**display snmp-agent proxy community cipher** *cipher-name*

**display snmp-agent proxy community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cipher** *community-name* | Specifies the name of an SNMP proxy community. | The value is a string of case-sensitive characters, spaces not supported. The length range depends on whether the complexity check of community names is enabled:   * If it is enabled, the length ranges from 8 to 32. * If it is disabled, the length ranges from 1 to 32.   When quotation marks are used around the string, spaces are allowed in the string. |
| **cipher** *cipher-name* | Specifies the name of an SNMP proxy community to be stored in ciphertext.The cipher-name value is displayed in ciphertext, no matter whether you specify it in ciphertext or simple text. | The value is a string of 1 to 168 consecutive characters, spaces not supported. Ciphertext passwords with various lengths configured in an earlier version are also supported in the existing version. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view SNMP proxy community information, run the display **snmp-agent proxy community** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display SNMP proxy community information.
```
<HUAWEI> display snmp-agent proxy community
Proxy Community name : %@%@,WEuC<6\a2;[T0X.K_hOK":RcIt}j>-WBo5aGpD$(E)D4:Rf"LNQ/O$q,%(8A-[T0X.K_hOK":RcIt}j>-WBo5aGpD$(E)D4:Rf"LNQ/O$q,%(8A-<:YaMw5Ro":%@%@
       Remote engine ID : 800007DB03360607111100 active
       Alias name:huawei
       Acl              : 2000
       Storage-type     : nonVolatile

   Proxy Community name : %#%#qTp*MccD#Z[sHw4"pbzVHzAfO]gWN;h#30K=)%}X1jIHNF<QdMskYG$9xj:9k\EZN6Mi!Hrt@\Oa8tqP%#%#
       Remote engine ID : 800007DB01192168001100 active
       Storage-type     : nonVolatile

```

**Table 1** Description of the **display snmp-agent proxy community** command output
| Item | Description |
| --- | --- |
| Proxy Community name | SNMP proxy community name.  You can run the snmp-agent proxy community command to create an SNMP proxy community name. |
| Remote engine ID | Engine ID of a managed device.  active indicates that an SNMP proxy community is in the active state. |
| Alias name | Community alias.  You can run the snmp-agent proxy community command to configure an SNMPv1/SNMPv2c community alias. |
| Acl | ACL corresponding to an SNMP proxy community name.  If you do not configure an ACL when you run the snmp-agent proxy community command, the Acl field is not displayed. |
| Storage-type | Storage type of a row in the memory:   * volatile: The row is lost after the system restarts. A row with Storage-type of volatile cannot have its storage type changed to permanent or readOnly. * nonVolatile: The row is not lost after the system restarts. A row with Storage-type of nonVolatile cannot have its storage type changed to permanent or readOnly. * permanent: The row is not lost after the system restarts. A row with Storage-type of permanent can be modified, but cannot be deleted. * readOnly: The row is not lost after the system restarts. A row with Storage-type of readOnly cannot be modified or deleted. * other: The row has other storage types.   At present, the storage type of a row can only be nonVolatile. |