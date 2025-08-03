rmon history
============

rmon history

Function
--------

The **rmon history** command configures the RMON historical sampling function.

The **undo rmon history** command disables the RMON historical sampling function.

By default, no object is configured with the RMON historical sampling function.



Format
------

**rmon history** *entry-number* **buckets** *number* **interval** *sampling-interval* [ **owner** *owner-name* ]

**undo rmon history** *entry-number*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *entry-number* | Specifies the index number of a history control table MIB entry mapped to a historical sampling object. | The value is an integer ranging from 1 to 65535. |
| **buckets** *number* | Specifies the capacity of the history table mapped to the historical control table entry, specifically, the maximum number of records in the history table. | The value is an integer ranging from 1 to 10. |
| **interval** *sampling-interval* | Specifies the sampling interval. | The value is an integer ranging from 5 to 3600, in seconds. |
| **owner** *owner-name* | Specifies an owner that creates the historical sampling function. | The value is a string of 1 to 127 case-sensitive characters, spaces not supported. |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

If you want the system regularly collects data about a specified interface and stores these data for future use, the rmon history command can be used to configure the RMON historical sampling function.

**Precautions**

The number of collected data that can be stored is determined by buckets number. When the capacity of the history table reaches the maximum, the system will delete the earliest records and store new statistics at the same time. Statistics includes the total number of packets, broadcast packets, and multicast packets received by an interface in a sampling period. You can view the historical sampling result using the **display rmon history** command.



Example
-------

# Create a history control table entry with the index number as 1, table capacity as 10, sampling interval as 5 seconds, and owner as user1 to enable the historical sampling function on an interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] rmon history 1 buckets 10 interval 5 owner user1

```