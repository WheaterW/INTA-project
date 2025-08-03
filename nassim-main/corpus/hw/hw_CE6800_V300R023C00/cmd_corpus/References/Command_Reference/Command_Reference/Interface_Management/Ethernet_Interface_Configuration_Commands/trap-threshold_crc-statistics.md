trap-threshold crc-statistics
=============================

trap-threshold crc-statistics

Function
--------



The **trap-threshold crc-statistics** command sets the alarm threshold for CRC error packets and the interval for collecting statistics on CRC error packets.

The **undo trap-threshold crc-statistics** command restores the default alarm threshold for CRC error packets and the default interval for collecting statistics on CRC error packets.



By default, the alarm threshold for CRC error packets is 3, and the interval for collecting statistics on CRC error packets is 10 seconds.


Format
------

**trap-threshold crc-statistics** *threshold-value* **interval** *interval-value*

**undo trap-threshold crc-statistics** [ *threshold-value* **interval** *interval-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *threshold-value* | Specifies the alarm threshold for CRC error packets. | The value is an integer ranging from 1 to 65535. |
| **interval** *interval-value* | Specifies the interval for collecting statistics on CRC error packets. | The value is an integer ranging from 10 to 65535, in seconds. |



Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The system generates a CRC error alarm when both of the following conditions are met:

* When the alarm threshold for CRC error packets is smaller than 3, the interface receives CRC error packets at least 1s within the specified interval. When the alarm threshold for CRC error packets is greater than or equal to 3, the interface receives CRC error packets at least three 1s within the specified interval.
* The total number of CRC error packets received by the interface within the specified interval is greater than the alarm threshold for CRC error packets.

The conditions for the system to clear the CRC error alarm are as follows:

* The number of CRC error packets received by the interface within the alarm interval is 0.

Example
-------

# Set the alarm threshold for CRC error packets on 100GE1/0/1 to 10 and the alarm interval to 30 seconds.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] trap-threshold crc-statistics 10 interval 30

```