display disk partition
======================

display disk partition

Function
--------



The **display disk partition** command is used to view information about disk partition .




Format
------

**display disk partition** *partitionName* [ **slot** *slotId* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *partitionName* | Specifies the name of a disk partition. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **slot** *slotId* | Specifies an available slot ID. | The value is a string of 1 to 49 characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Run the display disk partition command to view disk partition related information.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display common information about the home partition.
```
<HUAWEI> display disk partition home
Slot: 1
-------------------------------------------------------------------
Partition   Total(Mbytes)   Used(Mbytes)   Usage(%)   Threshold(%)
-------------------------------------------------------------------
home                  985            818         84             90

```

**Table 1** Description of the **display disk partition** command output
| Item | Description |
| --- | --- |
| Partition | Partition name. |
| Slot | Slot number. |
| Total | Total size of disk partition(Mbytes). |
| Used | Used of disk partition(Mbytes). |
| Usage | Percentage of disk partition using(%). |
| Threshold | Overload threshold of disk partition(%). |