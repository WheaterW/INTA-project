stp vlan timer max-age
======================

stp vlan timer max-age

Function
--------



The **stp vlan timer max-age** command sets the Max Age of a device, that is, the BPDU aging time on a port of the device.

The **undo stp vlan timer max-age** command restores the default setting.



By default, the Max Age of a device is 2000 centiseconds (20 seconds).


Format
------

**stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **timer** **max-age** *time-value*

**undo stp vlan** *vlan-id* [ **to** *vlan-id* ] [ *vlan-id* [ **to** *vlan-id* ] ] &<1-9> **timer** **max-age** [ *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *vlan-id* | Specifies one or more VLANs in which the Max Age value is set. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| *time-value* | Specifies the BPDU aging time on a port of the device. | The value is an integer that ranges from 600 to 4000, in centiseconds, and the step is 100. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a network where a spanning tree protocol is enabled, a device checks whether the BPDUs received from an upstream device time out based on the set Max Age value. If the received BPDUs time out, the device ages the BPDUs and blocks the port that receives the BPDUs. Then, the device sends the BPDUs with the device as the root bridge. This aging mechanism effectively controls the diameter of the spanning tree. After the stp vlan timer max-age command is run, the Max Age value is set to control the timeout period of received BPDUs.

**Configuration Impact**

The value of the Max Age set on the root bridge is advertised to other devices of the same spanning tree using BPDUs. Then it becomes the Max Age value of all devices in the spanning tree.

**Precautions**

The relationships between the Hello Time, Forward Delay, and Max Age are as follows. The spanning tree functions properly only if the relationships are correctly established. Otherwise, frequent network flapping occurs.

* 2 x (Forward Delay - 1.0 second) >= Max Age
* Max Age >= 2 x (Hello Time + 1.0 second)Running the **stp vlan bridge-diameter** command to set the network diameter is recommended. After the **stp vlan bridge-diameter** command is run, the switching device sets optimum values for the three parameters, Hello Time, Forward Delay, and Max Age.

Example
-------

# Set the Max Age to 1000 centiseconds (10 seconds) for VLAN 10 when VBST is running.
```
<HUAWEI> system-view
[~HUAWEI] stp vlan 10 timer max-age 1000

```