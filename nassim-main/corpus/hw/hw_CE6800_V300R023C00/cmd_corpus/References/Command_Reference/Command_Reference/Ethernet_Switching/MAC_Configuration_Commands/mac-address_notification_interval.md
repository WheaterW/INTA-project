mac-address notification interval
=================================

mac-address notification interval

Function
--------



The **mac-address notification interval** command sets the interval at which the device checks MAC address learning or aging.

The **undo mac-address notification interval** command restores the default interval at which the device checks MAC address learning or aging.



By default, the device checks MAC address learning or aging at intervals of 10s.


Format
------

**mac-address notification interval** *interval-time*

**undo mac-address notification interval** [ *interval-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval-time* | Specifies the interval at which the device checks MAC address learning or aging. | The value is an integer that ranges from 10 to 600. The default value is 10. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the **mac-address notification** command is used to enable the trap function when the device learns MAC addresses or MAC addresses are aged, the device periodically checks whether MAC addresses are learned or aged. You can run the **mac-address notification interval** command to set the interval.


Example
-------

# Set the interval at which the device checks MAC address learning or aging to 20s.
```
<HUAWEI> system-view
[~HUAWEI] mac-address notification interval 20

```