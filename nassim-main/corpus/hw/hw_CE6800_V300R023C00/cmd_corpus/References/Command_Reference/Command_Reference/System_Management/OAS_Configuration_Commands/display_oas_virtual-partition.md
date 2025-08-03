display oas virtual-partition
=============================

display oas virtual-partition

Function
--------



The **display oas virtual-partition** command displays information about created virtual partitions.




Format
------

**display oas virtual-partition**


Parameters
----------

None

Views
-----

OAS view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After OAS is enabled, you can run this command to query information about created virtual partitions.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Query information about the created virtual partition.
```
<HUAWEI> system-view
[~HUAWEI] oas
[~HUAWEI-oas] display oas virtual-partition
---------------------------------------------------------------------------------------------------
Partition Path    Slot ID  Total Size(M)  Used Size(M) Free Size(M)
---------------------------------------------------------------------------------------------------
flash:/oas/images 1/5      2048           218          1830
flash:/oas/images 1/6      2048           218          1830
---------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display oas virtual-partition** command output
| Item | Description |
| --- | --- |
| Partition Path | Path address of the created partition. |
| Slot ID | Slot ID. |
| Total Size(M) | Total size of a partition, in MB. |
| Used Size(M) | Size of the used partition space, in MB. |
| Free Size(M) | Size of the remaining space of the partition, in MB. |