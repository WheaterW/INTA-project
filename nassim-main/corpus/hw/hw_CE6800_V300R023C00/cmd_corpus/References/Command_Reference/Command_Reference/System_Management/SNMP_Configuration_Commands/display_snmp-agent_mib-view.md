display snmp-agent mib-view
===========================

display snmp-agent mib-view

Function
--------



The **display snmp-agent mib-view** command displays the existing MIB view.




Format
------

**display snmp-agent mib-view** [ [ **exclude** | **include** ] | **viewname** *view-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **exclude** | Excludes the displayed and configured attributes of an SNMP MIB view. | - |
| **include** | Includes the displayed and configured attributes of an SNMP MIB view. | - |
| **viewname** *view-name* | Specifies a view to be displayed. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



To view the default and configured MIB view, run the **display snmp-agent mib-view** command.



**Prerequisites**



The SNMP agent function has been enabled using the **snmp-agent** command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the existing MIB view.
```
<HUAWEI> display snmp-agent mib-view
View name: ViewDefault
       MIB Subtree: internet
       Subtree mask: F0(Hex)
       Storage type: nonVolatile
       View Type: included
       View status: active

   View name: ViewDefault
       MIB Subtree: snmpCommunityMIB
       Subtree mask: FE(Hex)
       Storage type: nonVolatile
       View Type: excluded
       View status: active

   View name: ViewDefault
       MIB Subtree: snmpUsmMIB
       Subtree mask: FE(Hex)
       Storage type: nonVolatile
       View Type: excluded
       View status: active

   View name: ViewDefault
       MIB Subtree: snmpVacmMIB
       Subtree mask: FE(Hex)
       Storage type: nonVolatile
       View Type: excluded
       View status: active

```

**Table 1** Description of the **display snmp-agent mib-view** command output
| Item | Description |
| --- | --- |
| View name | View name. |
| View Type | Whether access to a MIB object is permitted or denied. |
| View status | Status of the MIB view. |
| MIB Subtree | MIB subtree. |
| Subtree mask | Subtree mask. |
| Storage type | Storage mode, that is, the standard mode that specifies how rows are stored in the memory. Currently, only nonVolatile is supported.   * other: other types. * volatile: If a storage-type object is set to this value, the corresponding row is stored in the volatile memory and will be lost after the device is restarted. If the storage type of a row is set to volatile, you cannot change it to permanent or readOnly. * nonVolatile: Rows are stored in non-volatile memory (such as NVRAM). The row can be restored after the device is restarted. If the storage type of a row is set to nonVolatile, you cannot change it to permanent or readOnly. * permanent: Permanent rows are stored in non-volatile memory (such as ROM). You can change this line, but you cannot delete it. If the storage type of a row is permanent, you cannot change it to other storage types. * readOnly: A read-only row is stored in non-volatile memory (such as ROM). It cannot be modified or deleted. In addition, you cannot delete the row. |