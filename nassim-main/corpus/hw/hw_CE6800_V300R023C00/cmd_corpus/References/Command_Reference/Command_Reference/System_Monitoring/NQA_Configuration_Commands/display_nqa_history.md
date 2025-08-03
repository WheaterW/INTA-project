display nqa history
===================

display nqa history

Function
--------



The **display nqa history** command displays history records of an NQA test instance.




Format
------

**display nqa history** [ **test-instance** *adminName* *testName* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **test-instance** *adminName* | Specifies the administrator of an NQA test instance. | It is a string of 1 to 32 characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| *testName* | Specifies the name of an NQA test instance. | It is a string of 1 to 32 characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

NQA test instances can detect network operation conditions, output statistics, and effectively cut costs. NQA measures the performance of different protocols on the network, which allows carriers to collect the operation indicator of networks in real time.To obtain history records of an NQA test instance, you can run the **display nqa history** command.The **display nqa history** command helps you understand the network status by displaying the operation statistics about each test packet, including the status and round-trip delay.

**Configuration Impact**



History records of a failed jitter test instance will not be recorded.



**Precautions**



If no parameter is specified, history records of all NQA test instance are displayed.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display history records of a test instance named admin icmp.
```
<HUAWEI> display nqa history test-instance admin icmp
T/H/P = Test ID/Hop ID/Probe ID
NQA entry(admin,icmp) history:
- -------------------------------------------------------------------------------
Index   T/H/P     Response(ms) Status       Address         Time
- -------------------------------------------------------------------------------
 1      1/1/1        32      success      1.1.1.1         2015-11-27 10:12:38.511
 2      1/1/2        47      success      1.1.1.1         2015-11-27 10:12:42.520
 3      1/1/3        46      success      1.1.1.1         2015-11-27 10:12:46.531
- -------------------------------------------------------------------------------

```

**Table 1** Description of the **display nqa history** command output
| Item | Description |
| --- | --- |
| NQA entry(admin,icmp) history | NQA test entry information:   * admin: administrator of an NQA test instance. * icmp: name of an NQA test instance. |
| Index | Index of a history record. |
| Status | Status of an NQA test packet:   * timeout: The response packet times out, and the test fails. * success: The test is successful. * busy: Sending packets fails due to insufficient system resources. In this case, the test fails. * drop: Sending packets fails due to incorrect configuration of the test instance. In this case, the test fails. |
| Address | Destination IP address. |
| Time | Date and time when a test packet was received. |
| Response | Value of the round-trip time (RTT), in millisecond seconds. |
| T | Number of times of a test packet will be sent. |
| H | Number of hops a test packet will pass through. |
| P | Number of sent test packets. |