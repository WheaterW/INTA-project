rmon statistics
===============

rmon statistics

Function
--------

The **rmon statistics** command configures RMON Ethernet statistics function.

The **undo rmon statistics** command disables the RMON Ethernet statistics function.

By default, the RMON Ethernet statistics function is disabled.



Format
------

**rmon statistics** *entry-number* [ **owner** *owner-name* ]

**undo rmon statistics** *entry-number*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *entry-number* | Specifies the index number of a MIB entry mapped to an Ethernet statistics object. | The value is an integer ranging from 1 to 65535. |
| **owner** *owner-name* | Specifies an owner that creates the Ethernet statistics function. | The value is a string of 1 to 127 case-sensitive characters, spaces not supported. |




Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

The RMON Ethernet statistics function is used to monitor the Ethernet interfaces and collect statistics of errors on the interfaces, to check and handle problems timely. The statistics includes the service collision, number of CRC errors, undersize or oversize packets, data timeout transmission, fragments, broadcast packets, multicast packets, and unicast packets.

**Prerequisites**

The Ethernet statistics function has been enabled using the **rmon-statistics enable** command.



Example
-------

# Configure the Ethernet statistics function on the specified interface.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] rmon statistics 20 owner creater

```