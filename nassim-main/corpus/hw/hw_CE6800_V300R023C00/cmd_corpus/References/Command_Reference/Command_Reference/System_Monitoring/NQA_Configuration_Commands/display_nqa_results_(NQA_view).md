display nqa results (NQA view)
==============================

display nqa results (NQA view)

Function
--------



The **display nqa results** this command displays NQA test result statistics in a specified NQA test instance view.




Format
------

**display nqa results** [ **this** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **this** | Display result statistics of the current instance. | - |



Views
-----

NQA view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

NQA test instances monitor the network operating status, output statistics, and effectively help reduce costs. NQA measures performance of various protocols on the network, which allows carriers to collect network operation indexes in real time.The **display nqa results this** command can be used to query the test result of a specified NQA test instance in the corresponding test view. This allows you to learn information the test instance more comprehensively.The display nqa results collection this command displays accumulative test statistics.

**Prerequisites**

NQA test instances are configured.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on ICMP NQA tests.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance admin icmp
[*HUAWEI-nqa-admin-icmp] test-type icmp
[*HUAWEI-nqa-admin-icmp] commit
[~HUAWEI-nqa-admin-icmp] display nqa results this
NQA entry(admin, icmp): test flag is inactive, test type is ICMP
1 . Test 1 result The test is finished
    Send operation times: 3               Receive response times: 3 
    Completion: success                   RTD over thresholds number: 0
    Attempts number: 1                    Drop operation number: 0
    Disconnect operation number: 0        Operation timeout number: 0
    System busy operation number: 0       Connection fail number: 0
    Operation sequence errors number: 0   RTT stats errors number: 0
    Destination IP address: 10.1.1.2
    Min/Max/Average completion time: 31/46/36
    Sum/Square-Sum completion time: 108/4038
    Last response packet receiving time: 2006-8-2 10:7:11.4
    Lost packet ratio: 0 %

```

**Table 1** Description of the **display nqa results (NQA view)** command output
| Item | Description |
| --- | --- |
| NQA entry(admin, icmp) | NQA test entry information:   * admin: administrator of an NQA test instance. * icmp: name of an NQA test instance. |
| The test is finished | Test status:   * finished: The test is complete. * running: The test is running. |
| Send operation times | Number of sent packets. |
| Receive response times | Number of received packets. |
| RTD over thresholds number | Number of times the RTD threshold is exceeded. |
| Attempts number | Number of times a test instance is performed. |
| Drop operation number | Number of system resource allocation failures. |
| Disconnect operation number | Number of forcible disconnections. |
| Operation timeout number | Number of timeouts during a test. |
| Operation sequence errors number | Number of received out-of-order packets. |
| System busy operation number | Number of test conflicts. |
| Connection fail number | Number of connection failures. |
| RTT stats errors number | Number of RTT status errors. |
| Destination IP address | Destination IP address of a test. |
| Min/Max/Average completion time | Minimum, maximum, or average completion time of a test instance. |
| Sum/Square-Sum completion time | Sum and square sum of the completion time of a test instance. |
| Last response packet receiving time | Date and time when the last probe was complete. |
| Lost packet ratio | Test packet loss ratio. |
| Completion | Status of a test instance:   * success: The test instance is successful. * no result: The test is running, and no result is obtained. * failed: The test instance fails. |