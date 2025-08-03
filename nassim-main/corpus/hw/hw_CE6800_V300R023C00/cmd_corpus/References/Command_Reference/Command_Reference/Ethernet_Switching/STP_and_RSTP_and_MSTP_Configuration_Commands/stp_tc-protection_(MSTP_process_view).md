stp tc-protection (MSTP process view)
=====================================

stp tc-protection (MSTP process view)

Function
--------



The **stp tc-protection** command enables the topology change bridge protocol data unit (TC BPDU) protection function for a Multiple Spanning Tree Protocol (MSTP) process.

The **undo stp tc-protection** command disables the TC BPDU protection function of the MSTP process.



By default, the TC BPDU protection function of an MSTP process is disabled. That is, each time when an MSTP process receives a TC BPDU, the MSTP process updates the forwarding entries. The time for a device to process the maximum number of TC BPDUs is the Hello time. A device processes one TC BPDU within a specified period.

The Hello time is the value of the Hello timer and specifies the interval at which the device sends BPDUs. You can configure the Hello time using the stp timer hello command.




Format
------

**stp tc-protection** [ **threshold** *threshold* | **interval** *interval-value* ]

**undo stp tc-protection** [ **threshold** | **interval** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **threshold** *threshold* | Specifies the maximum number of TC BPDUs that a device processes within a specified period. | The value is an integer ranging from 1 to 255. |
| **interval** *interval-value* | Specifies the time for a device to process the maximum number of TC BPDUs. | The value is an integer ranging from 1 to 600, in seconds. |



Views
-----

MSTP process view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a Layer 2 network running STP, a device that receives TC BPDUs will delete its MAC and ARP entries. Frequent deletion operations lead to high CPU usage. In this case, run the **stp tc-protection** command to enable the TC BPDU protection function.After the TC BPDU protection function is enabled using the **stp tc-protection** command, you can run the **stp tc-protection interval** command to set the time for a device to process the maximum number of TC BPDUs specified by the **stp tc-protection threshold** command. If the number of received TC BPDUs exceeds the maximum number, the device processes the excess TC BPDUs after the time specified by the **stp tc-protection interval** command expires. For example, if the time is set to 10 seconds and the maximum number is set to 5, when a device receives TC BPDUs, the device processes only the first 5 TC BPDUs within 10 seconds and processes the other TC BPDUs after the time expires. In this way, the device does not frequently update its MAC and ARP entries, reducing CPU usage.



**Prerequisites**



The TC BPDU protection function has been enabled using the **stp tc-protection** command.



**Configuration Impact**



The device processes only the maximum number of TC BPDUs specified by the **stp tc-protection threshold** command within the time specified by the **stp tc-protection interval** command. Other TC BPDUs are delayed processing, which may slow down spanning tree convergence.



**Follow-up Procedure**



Run the **stp tc-protection threshold** command to set the maximum number of TC BPDUs that the device processes within a specified time.Run the **stp tc-protection interval** command to set the time for a device to process the maximum number of TC BPDUs.




Example
-------

# Set the time for a device to process the maximum number of TC BPDUs in MSTP 1 to 10 seconds.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] stp tc-protection
[*HUAWEI-mst-process-1] stp tc-protection interval 10

```

# Configure a device to process a maximum of 5 TC BPDUs in MSTP process 1 within a specified period.
```
<HUAWEI> system-view
[~HUAWEI] stp process 1
[*HUAWEI-mst-process-1] stp tc-protection
[*HUAWEI-mst-process-1] stp tc-protection threshold 5

```

# Enable the TC BPDU protection function for MSTP processes 0 and 1.
```
<HUAWEI> system-view
[~HUAWEI] stp tc-protection
[*HUAWEI] stp process 1
[*HUAWEI-mst-process-1] stp tc-protection

```