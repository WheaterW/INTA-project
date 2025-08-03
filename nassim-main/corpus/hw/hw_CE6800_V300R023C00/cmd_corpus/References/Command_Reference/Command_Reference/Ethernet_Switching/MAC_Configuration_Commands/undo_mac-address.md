undo mac-address
================

undo mac-address

Function
--------



The **undo mac-address** command deletes a MAC address entry.




Format
------

**undo mac-address** { { **static** [ *interface-type* *interface-number* | *interface-name* ] } | { **blackhole** [ *mac-address* ] } | *mac-address* }

**undo mac-address** { *interface-type* *interface-number* | *interface-name* }

**undo mac-address all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **static** | Deletes a static MAC address. | - |
| *interface-type* | Specifies the interface type. | - |
| *interface-number* | Specifies the interface number. | - |
| *interface-name* | Specifies the interface name. | - |
| **blackhole** | Number of blackhole MAC address entries. | - |
| *mac-address* | Specifies a MAC address. | The value is a hexadecimal number in the format of H-H-H. H is a 4-bit hexadecimal number, such as 00e0 or fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. |
| **all** | Specifies all MAC entries. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



This command is used to delete a manually configured MAC address entry.




Example
-------

# Deletes all configured MAC entries.
```
<HUAWEI> system-view
[~HUAWEI] undo mac-address all

```