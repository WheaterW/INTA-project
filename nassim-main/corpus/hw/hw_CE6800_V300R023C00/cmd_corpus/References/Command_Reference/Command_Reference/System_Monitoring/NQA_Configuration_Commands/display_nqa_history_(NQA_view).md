display nqa history (NQA view)
==============================

display nqa history (NQA view)

Function
--------



The **display nqa history** command displays history records of an NQA test instance.




Format
------

**display nqa history** [ **this** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **this** | Display history records of the current instance. | - |



Views
-----

NQA view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

NQA test instances can detect network operation conditions, output statistics, and effectively cut costs. NQA measures the performance of different protocols on the network, which allows carriers to collect the operation indicator of networks in real time.To query the history statistics on NQA tests, run the display nqa history [ this ] command. You can view information about each test packet, including the status and round trip delay. This allows you to learn about network running status.

**Prerequisites**

NQA test instances are configured.

**Configuration Impact**

History records of a failed jitter test instance will not be recorded.

**Precautions**

This command is run in an NQA test instance view, and the command only displays the history statistics on the test instance.The **display nqa history** command displays history statistics on all NQA test instances.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display history statistics on the NQA test instance admin icmp.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance admin icmp
[*HUAWEI-nqa-admin-icmp] test-type icmp
[*HUAWEI-nqa-admin-icmp] display nqa history this
T/H/P = Test ID/Hop ID/Probe ID
NQA entry(admin,icmp) history:
--------------------------------------------------------------------------------
Index   T/H/P     Response(ms) Status       Address         Time
--------------------------------------------------------------------------------
 1      1/1/1        32  success      1.1.1.1         2012-11-27 10:12:38.511
 2      1/1/2        47  success      1.1.1.1         2012-11-27 10:12:42.520
 3      1/1/3        46  success      1.1.1.1         2012-11-27 10:12:46.531
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display nqa history (NQA view)** command output
| Item | Description |
| --- | --- |
| NQA entry(admin,icmp) history | NQA test entry information:   * admin: administrator of an NQA test instance. * icmp: name of an NQA test instance. |
| Index | Index of a history record. |
| T/H/P | Number of times a test packet will be sent/Number of hops a test packet will pass through/Number of sent test packets. |
| T/H/P = Test ID/Hop ID/Probe ID | T: the number of times an NQA test instance is performed.  H: the number of current hops.  P: the number of the current probe times during an NQA test instance. |
| Response | Value of the Round-Trip Time (RTT). |
| Status | Status of an NQA test packet:   * timeout: The response packet times out, and the test fails. * success: The test is successful. * drop: Sending packets fails due to incorrect configuration of the test instance. In this case, the test fails. |
| Address | Destination IP address. |
| Time | Date and time when a test packet was received. |