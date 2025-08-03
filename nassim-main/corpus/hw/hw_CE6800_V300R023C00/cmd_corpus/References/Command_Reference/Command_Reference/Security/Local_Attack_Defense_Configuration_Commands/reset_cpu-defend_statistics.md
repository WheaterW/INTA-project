reset cpu-defend statistics
===========================

reset cpu-defend statistics

Function
--------



The **reset cpu-defend statistics** command clears statistics on packets sent to the CPU.




Format
------

**reset cpu-defend statistics** [ **packet-type** *packet-type* ] { **all** | **slot** *slot-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet-type** *packet-type* | Specifies the protocol type of packets. packet-type specifies the packet type.   * If packet-type packet-type is specified, the statistics on the specified type of protocol packets are cleared. * If packet-type packet-type is not specified, the statistics on all protocol packets are cleared. | The packet type information displayed on the device prevails. You can run the display cpu-defend configuration command to check the supported packet types and rate limit. |
| **all** | Specifies all cards. | - |
| **slot** *slot-id* | Specifies the slot ID. | The value must be set according to the device configuration. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view statistics on the packets sent to the CPU in a specified period, run the **reset cpu-defend statistics** command to clear existing statistics and run the display cpu-defend statistics command.

**Precautions**

The deleted packet statistics cannot be restored.


Example
-------

# Clear FTP packet statistics for a slot.
```
<HUAWEI> reset cpu-defend statistics packet-type ftp slot 1

```