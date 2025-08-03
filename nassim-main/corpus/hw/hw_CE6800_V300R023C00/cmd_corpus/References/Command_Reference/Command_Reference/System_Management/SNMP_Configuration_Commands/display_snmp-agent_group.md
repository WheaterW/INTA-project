display snmp-agent group
========================

display snmp-agent group

Function
--------



The **display snmp-agent group** command displays information about an SNMP agent group.




Format
------

**display snmp-agent group** [ *group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **group** *group-name* | Displays the name of an SNMP agent group.  This parameter is specified using the snmp-agent group command. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When you configure a management object based on the SNMPv3 group information, to view information about the SNMP agent group, run the **display snmp-agent group** command.If no parameter is specified in the command, information about all groups is displayed, such as the group name, security model, and storage type.

**Prerequisites**

The SNMP agent group has been created using the **snmp-agent group** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the name and security model of an SNMP agent group.
```
<HUAWEI> display snmp-agent group
   Group name: mygroup
       Security model: USM noAuthNoPriv
       Readview: ViewDefault
       Writeview: <no specified>
       Notifyview: <no specified>
       Storage-type: nonVolatile
       Acl: 2000

```

**Table 1** Description of the **display snmp-agent group** command output
| Item | Description |
| --- | --- |
| Group name | Name of an SNMP agent group. |
| Security model | Security model of the group. |
| Readview | Read-only MIB of the group view. |
| Writeview | Read-write MIB of the group view. |
| Notifyview | Notify MIB of the group view. |
| Storage-type | Storage mode, that is, the standard mode that specifies how rows are stored in the memory. Currently, only nonVolatile is supported.   * other: other types. * volatile: If a storage-type object is set to this value, the corresponding row is stored in the volatile memory and will be lost after the device is restarted. If the storage type of a row is set to volatile, you cannot change it to permanent or readOnly. * nonVolatile: Rows are stored in non-volatile memory (such as NVRAM). The row can be restored after the device is restarted. If the storage type of a row is set to nonVolatile, you cannot change it to permanent or readOnly. * permanent: Permanent rows are stored in non-volatile memory (such as ROM). You can change this line, but you cannot delete it. If the storage type of a row is permanent, you cannot change it to other storage types. * readOnly: A read-only row is stored in non-volatile memory (such as ROM). It cannot be modified or deleted. In addition, you cannot delete the row. |
| Acl | Either ACL name or number. |