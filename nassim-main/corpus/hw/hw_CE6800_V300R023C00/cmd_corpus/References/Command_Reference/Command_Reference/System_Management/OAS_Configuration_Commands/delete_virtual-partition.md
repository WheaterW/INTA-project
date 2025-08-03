delete virtual-partition
========================

delete virtual-partition

Function
--------



The **delete virtual-partition** command deletes a virtual partition from an open application system.




Format
------

**delete virtual-partition type image**

**delete virtual-partition type rootfs slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **type** | Specifies the partition type. | - |
| **rootfs** | Virtual partition of the root path. | - |
| **slot** *slot-id* | Specifies the slot ID of a board. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **image** | Image virtual partition. | - |



Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

* If type image is specified in the command, the image storage partition will be deleted.
* If the type rootfs parameter is specified in the command, the root path partition used for running application is deleted.

Example
-------

# Delete the image storage partition.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] delete virtual-partition type image
Warning: The virtual partition will be deleted. Continue? [Y/N]:y
Info: Virtual partition is deleted successfully.

```

# Delete the root directory partition for running applications.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] delete virtual-partition type rootfs slot 1
Warning:The virtual partition will be deleted. Continue? [Y/N]:y
Info: Virtual partition is deleted successfully.

```