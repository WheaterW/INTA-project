isis link-group
===============

isis link-group

Function
--------



The **isis link-group** command binds an IS-IS interface to an existing link group.

The **undo isis link-group** command unbinds an IS-IS interface from a link group.



By default, an IS-IS interface is not bound to any link group.


Format
------

**isis link-group** *group-name* [ **level-1** | **level-2** ]

**undo isis link-group** [ *group-name* ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a link group. | The value is a string of 1 to 32 case-sensitive characters. When quotation marks are used around the string, spaces are allowed in the string. |
| **level-1** | Binds a Level-1 interface to the link group. | - |
| **level-2** | Binds a Level-2 interface to the link group.  If neither level-1 nor level-2 is specified in the command, both Level-1 and Level-2 interfaces are bound to the link group. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After a link group is created in the IS-IS view, run the **isis link-group** or **isis ipv6 link-group** command to bind a specified interface to the link group for the link group to take effect.


Example
-------

# Bind 100GE1/0/1 to the link group named link-a.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] link-group link-a
[*HUAWEI-isis-1-link-group-link-a] quit
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-isis-100GE1/0/1] undo portswitch
[*HUAWEI-isis-100GE1/0/1] isis enable
[*HUAWEI-isis-100GE1/0/1] isis link-group link-a

```