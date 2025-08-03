display snmp-agent community
============================

display snmp-agent community

Function
--------



The **display snmp-agent community** command displays the configured community information.




Format
------

**display snmp-agent community** [ **read** | **write** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **read** | Displays the name, group name, and storage type of a read-only community. The parameter is specified using the snmp-agent community command. | - |
| **write** | Displays the name, group name, and storage type of a read-write community. The parameter is specified using the snmp-agent community command. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To display information about an existing agent community, run the **display snmp-agent community** command. The command output contains the following information:

* Community name: encrypted text
* Group name: encrypted text
* Storage type
* ACL

**Prerequisites**

A community name has been configured using the **snmp-agent community** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configured community name.
```
<HUAWEI> display snmp-agent community
   Community name: %#%#SW5+R]B`!*8kRB23VfV-S%d;$N]\GS/1~$,EjcbP_#ZS~jw2:#Q7i"5@_;_Bu=L&Y|dnMCvIY>2jy4BH%#%#
       Group name: %#%#SW5+R]B`!*8kRB23VfV-S%d;$N]\GS/1~$,EjcbP_#ZS~jw2:#Q7i"5@_;_Bu=L&Y|dnMCvIY>2jy4BH%#%#
       Alias name: huawei
       Acl: 2000
       Storage-type: nonVolatile

```

**Table 1** Description of the **display snmp-agent community** command output
| Item | Description |
| --- | --- |
| Community name | Encrypted community name. |
| Group name | Name of a group. |
| Alias name | Community alias.  You can run the snmp-agent community command to configure an SNMPv1/SNMPv2c community alias. |
| Acl | ACL number or name. |
| Storage-type | Storage mode, that is, the standard mode that specifies how rows are stored in the memory. Currently, only nonVolatile is supported.   * other: other types. * volatile: If a storage-type object is set to this value, the corresponding row is stored in the volatile memory and will be lost after the device is restarted. If the storage type of a row is set to volatile, you cannot change it to permanent or readOnly. * nonVolatile: Rows are stored in non-volatile memory (such as NVRAM). The row can be restored after the device is restarted. If the storage type of a row is set to nonVolatile, you cannot change it to permanent or readOnly. * permanent: Permanent rows are stored in non-volatile memory (such as ROM). You can change this line, but you cannot delete it. If the storage type of a row is permanent, you cannot change it to other storage types. * readOnly: A read-only row is stored in non-volatile memory (such as ROM). It cannot be modified or deleted. In addition, you cannot delete the row. |