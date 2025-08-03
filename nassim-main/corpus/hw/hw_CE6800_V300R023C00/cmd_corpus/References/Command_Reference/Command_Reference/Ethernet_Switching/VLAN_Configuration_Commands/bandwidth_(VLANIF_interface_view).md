bandwidth (VLANIF interface view)
=================================

bandwidth (VLANIF interface view)

Function
--------



The **bandwidth** command sets the bandwidth of a VLANIF interface.

The **undo bandwidth** command deletes the configured bandwidth of a VLANIF interface.



By default, the bandwidth of a VLANIF interface is 1000 Mbits/s.


Format
------

**bandwidth** *bandwidth*

**undo bandwidth**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bandwidth* | Specifies the bandwidth of a VLANIF interface. | The value ranges from 1 to 1000000, in Mbits/s. |



Views
-----

VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The bandwidth command mainly ensures that the network management station (NMS) can acquire the bandwidth of the VLANIF interface. The NMS can check the interface bandwidth through the two objects ifSpeed and ifHighSpeed in IF-MIB.

* If the configured bandwidth is smaller than 4000 Mbit/s, ifSpeed and ifHighSpeed are respectively displayed as bandwidth x 1000 x 1000 and bandwidth.
* If the configured bandwidth is equal to or larger than 4000 Mbit/s, ifSpeed and ifHighSpeed are respectively displayed as 4294967295 (0XFFFFFFFF) and bandwidth.


Example
-------

# Set the bandwidth of VLANIF 2 to 10000 Mbits/s.
```
<HUAWEI> system-view
[~HUAWEI] vlan 2
[*HUAWEI-vlan2] quit
[*HUAWEI] interface vlanif 2
[*HUAWEI-Vlanif2] bandwidth 10000

```