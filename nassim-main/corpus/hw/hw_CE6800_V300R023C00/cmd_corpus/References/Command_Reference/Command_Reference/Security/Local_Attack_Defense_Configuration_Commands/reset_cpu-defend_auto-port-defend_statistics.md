reset cpu-defend auto-port-defend statistics
============================================

reset cpu-defend auto-port-defend statistics

Function
--------



The **reset cpu-defend auto-port-defend statistics** command deletes packet statistics on port attack defense.




Format
------

**reset cpu-defend auto-port-defend statistics** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
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

Before viewing packet statistics of port attack defense in a certain period, delete existing packet statistics, and then run the **display auto-port-defend statistics** command to collect the latest statistics.

**Precautions**

The deleted packet statistics cannot be restored.


Example
-------

# Delete packet statistics on the interfaces of the device.
```
<HUAWEI> reset cpu-defend auto-port-defend statistics

```