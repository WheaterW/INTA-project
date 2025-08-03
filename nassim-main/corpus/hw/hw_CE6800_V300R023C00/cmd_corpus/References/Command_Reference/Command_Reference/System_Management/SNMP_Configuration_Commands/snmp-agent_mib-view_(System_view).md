snmp-agent mib-view (System view)
=================================

snmp-agent mib-view (System view)

Function
--------



The **snmp-agent mib-view** command creates or updates a MIB view.

The **undo snmp-agent mib-view** command restores the default information about a view.



By default, the view name is ViewDefault and the MIB subtrees are internet, snmpVacmMIB, snmpUsmMIB and snmpCommunityMIB.


Format
------

**snmp-agent mib-view** *type* *view-name* *oid-tree*

**undo snmp-agent mib-view** [ *type* ] *view-name* [ *oid-tree* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *type* | Type of operation. | * excluded: Excludes the MIB subtree. * included: Includes the MIB subtree. |
| *view-name* | Specifies the view name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| *oid-tree* | Specifies the OID for the MIB subtree. oid-tree can be the OID (such as 1.4.5.3.1) or the name (such as system) of the subtree. | The value is a string of 1 to 255 case-sensitive characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

Most SNMP configuration commands contain the parameter view-name. The **snmp-agent mib-view** command is used to create or update a view. You cannot modify or delete the default ViewDefault MIB view.In the **snmp-agent mib-view** command, the view-name parameter can be displayed as an OID or an object name.

* snmp-agent mib-view included myview 1.3.6.1.2.1: displays the view-name parameter as an OID.
* snmp-agent mib-view excluded myview system.7: displays the view-name parameter as an object name.Note:To uniquely identify object identifiers in SNMP messages, SNMP uses a hierarchical naming structure to distinguish object identifiers from one another. This is a tree-shaped structure, with the nodes (such as {1.3.6.1.2.1}) representing object identifiers.Only nodes can be filtered. Instances of nodes cannot be filtered. For example, {1.3.6.1.2.1} indicates a node. An index is added to the OID of the node. For example, {1.3.6.1.2.1.0} indicates an instance of the node.

**Precautions**

If a MIB view is referenced by a community name or SNMP group, the view can be deleted using the **undo snmp-agent mib-view** command only after you delete the view reference relationship.


Example
-------

# Create a view that includes all objects in the MIB-II subtree, with the name of the view of mib2view and the OID subtree of 1.3.6.1.2.1.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent mib-view included mib2view 1.3.6.1.2.1

```