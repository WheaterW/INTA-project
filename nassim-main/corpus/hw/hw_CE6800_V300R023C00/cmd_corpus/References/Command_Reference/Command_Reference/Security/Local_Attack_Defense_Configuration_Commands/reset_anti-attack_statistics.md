reset anti-attack statistics
============================

reset anti-attack statistics

Function
--------



The **reset anti-attack statistics** command clears statistics about attack defense.




Format
------

**reset anti-attack statistics** [ **abnormal** | **fragment** | **tcp-syn** | **udp-flood** | **icmp-flood** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **abnormal** | Indicates the statistics about defense against malformed packets. | - |
| **fragment** | Indicates the statistics about defense against packet fragments. | - |
| **tcp-syn** | Indicates the statistics about defense against TCP SYN flood. | - |
| **udp-flood** | Indicates the statistics about defense against UDP flood. | - |
| **icmp-flood** | Indicates the statistics about defense against ICMP flood. | - |



Views
-----

All views


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If attack defense type is not specified, statistics about all types of attack defense are cleared.

**Precautions**

Statistics cannot be restored after being cleared. Exercise caution when running this command.


Example
-------

# Clear statistics about defense against malformed packets.
```
<HUAWEI> system-view
[~HUAWEI] reset anti-attack statistics abnormal

```