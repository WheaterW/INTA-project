display nqa results
===================

display nqa results

Function
--------



The **display nqa results** command displays result records of an NQA test instance.




Format
------

**display nqa results** [ **test-instance** *adminName* *testName* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **test-instance** *adminName* | Specifies the name of the administrator for an NQA test instance. | It is a string of 1 to 32 characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
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

NQA test instances monitor the network operating status, output statistics, and effectively help reduce costs. NQA measures performance of various protocols on the network, which allows carriers to collect network operation indexes in real time.The NQA test result cannot be displayed automatically on the terminal. To view the NQA test result, run the **display nqa results** command.The command output helps you understand the operation of the specified test instance.The **display nqa results** command output contains two parts:

* General results: identical for all test types.
* Detailed results: vary according to test types.

**Configuration Impact**

The **display nqa results** command displays the test results of only the running or the complete test instances.

**Precautions**

If no optional parameter is specified, the **display nqa results** command displays the results of all NQA test instances.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the result of a jitter test instance.
```
<HUAWEI> display nqa results test-instance admin jitter
NQA entry(admin, jitter): test flag is active, test type is JITTER
  1 . Test 1 result   The test is finished
   SendProbe: 60                           ResponseProbe: 60                      
   Completion: success                     RTD over thresholds number: 0           
   OWD over thresholds SD number: 0        OWD over thresholds DS number: 0        
   Min/Max/Avg/Sum RTT: 1/132/8/491        RTT square sum: 41843                  
   Num of RTT: 60                          Drop operation number: 0               
   Operation sequence errors number: 0     RTT stats errors number: 0             
   System busy operation number: 0         Operation timeout number: 0            
   Min positive SD: 0                      Min positive DS: 8                     
   Max positive SD: 0                      Max positive DS: 24                    
   Positive SD number: 0                   Positive DS number: 54                 
   Positive SD sum: 0                      Positive DS sum: 1153                  
   Positive SD square sum: 0               Positive DS square sum: 24847          
   Min negative SD: 20                     Min negative DS: 2                     
   Max negative SD: 23                     Max negative DS: 3                     
   Negative SD number: 59                  Negative DS number: 5                  
   Negative SD sum: 1273                   Negative DS sum: 12                    
   Negative SD square sum: 27491           Negative DS square sum: 30             
   Min delay SD: 1                         Min delay DS: 0                        
   Avg delay SD: 7                         Avg delay DS: 0                        
   Max delay SD: 132                       Max delay DS: 0                        
   Delay SD square sum: 41825              Delay DS square sum: 0                 
   Packet loss SD: 0                       Packet loss DS: 0                      
   Packet loss unknown: 0                  Average of jitter: 20                  
   Average of jitter SD: 21                Average of jitter DS: 19               
   Jitter out value: 15.9377600            Jitter in value: 14.1930380            
   Number of OWD: 60                       Packet loss ratio: 0 %                 
   OWD SD sum: 473                         OWD DS sum: 0                          
   ICPIF value: 0                          MOS-CQ value: 0                        
   TimeStamp unit: ms

```

# Display the result of an ICMP test instance.
```
<HUAWEI> display nqa results test-instance admin icmp
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

**Table 1** Description of the **display nqa results** command output
| Item | Description |
| --- | --- |
| NQA entry(admin, icmp): test flag is inactive, test type is ICMP | NQA test items:admin:   * administrator of an NQA test instance. * icmp: name of an NQA test instance. |
| 1 . Test 1 result | Sequence number of the test result, which is labeled based on the end time of the test instance. |
| Test 1 result The test is finished | The test is complete. |
| The test is finished | Test status:   * finished: The test is complete. * running: The test is running. |
| RTD OverThresholds number | Number of times the RTD threshold is exceeded. |
| RTD over thresholds number | Number of times the RTD threshold is exceeded. |
| OWD OverThresholds SD number | Number of times that the one-way transmission (from the source to the destination) delay exceeds the threshold. |
| OWD over thresholds SD number | Number of times that the one-way transmission (from the source to the destination) delay exceeds the threshold. |
| OWD OverThresholds DS number | Number of times that the one-way transmission (from the destination to the source) delay exceeds the threshold. |
| OWD over thresholds DS number | Number of times that the one-way transmission (from the destination to the source) delay exceeds the threshold. |
| OWD SD sum | Sum of one-way delays from the source to the destination. |
| OWD DS sum | Sum of one-way delays from the destination to the source. |
| Min/Max/Avg/Sum RTT | Minimum, maximum, average, or sum of the RTT. |
| RTT Stats errors number | Number of RTT status errors. |
| RTT stats errors number | Number of RTT status errors. |
| RTT Square Sum | Square sum of the RTT. |
| RTT square sum | Square sum of the RTT. |
| Drop operation number | Number of system resource allocation failures. |
| Operation timeout number | Number of timeouts during a test. |
| Operation sequence errors number | Number of received out-of-order packets. |
| System busy operation number | Number of test conflicts. |
| Min positive SD | Minimum positive jitter from the source to the destination. |
| Min positive DS | Minimum positive jitter from the destination to the source. |
| Min negative SD | Minimum negative jitter from the source to the destination. |
| Min negative DS | Minimum negative jitter from the destination to the source. |
| Min delay SD | Minimum delay from the source to the destination. |
| Min delay DS | Minimum delay from the destination to the source. |
| Positive SD number | Number of positive jitters from the source to the destination. |
| Positive DS number | Number of positive jitters from the destination to the source. |
| Positive SD sum | Sum of positive jitters from the source to the destination. |
| Positive DS sum | Sum of positive jitters from the destination to the source. |
| Positive SD square sum | Square sum of positive jitters from the source to the destination. |
| Positive DS square sum | Square sum of positive jitters from the destination to the source. |
| Max positive SD | Maximum positive jitter from the source to the destination. |
| Max positive DS | Maximum positive jitter from the destination to the source. |
| Max negative SD | Maximum negative jitter from the source to the destination. |
| Max negative DS | Maximum negative jitter from the destination to the source. |
| Max delay SD | Maximum delay from the source to the destination. |
| Max delay DS | Maximum delay from the destination to the source. |
| Negative SD number | Number of negative jitters from the source to the destination. |
| Negative DS number | Number of negative jitters from the destination to the source. |
| Negative SD sum | Sum of negative jitters from the source to the destination. |
| Negative DS sum | Sum of negative jitters from the destination to the source. |
| Negative SD square sum | Square sum of negative jitters from the source to the destination. |
| Negative DS square sum | Square sum of negative jitters from the destination to the source. |
| Delay SD square sum | Square sum of delay jitters from the source to the destination. |
| Delay DS square sum | Square sum of delay jitters from the destination to the source. |
| Avg delay SD | Average delay from the source to the destination. |
| Avg delay DS | Average delay from the destination to the source. |
| Packet loss SD | Maximum number of dropped packets from the source to the destination. |
| Packet loss DS | Maximum number of dropped packets from the destination to the source. |
| Packet loss unknown | Number of packets dropped in the unknown direction. |
| Packet loss ratio | Packet loss rate. |
| Average of jitter | Average jitter. |
| Average of jitter SD | Average jitter from the source to the destination. |
| Average of jitter DS | Average jitter from the destination to the source. |
| Jitter out value | Jitter in packet sending. |
| Jitter in value | Jitter in packet receiving. |
| ICPIF value | Compensation factor. |
| MOS-CQ value | Mean Opinion Score (MOS) of VoIP performance. |
| TimeStamp unit | Timestamp unit. |
| Num of RTT | Number of RTTs. |
| Number of OWD | Number of one-way delay packets. |
| Send operation times | Number of sent packets. |
| Receive response times | Number of response packets received. |
| Attempts number | Number of times a test instance is performed. |
| Disconnect operation number | Number of times the peer tears down the connection. |
| Connection fail number | Number of connection failures. |
| Destination ip address | Destination IP address of a test. |
| Destination IP address | Destination IP address of a test. |
| Min/Max/Average Completion Time | Minimum, maximum, or average completion time of a test instance, in milliseconds. |
| Min/Max/Average completion time | Minimum, maximum, or average completion time of a test instance, in milliseconds. |
| Completion | Test completion status. When a static route is bound to an NQA test instance, the routing policy is determined based on the test instance result.   * success: The test succeeds. * no result: The test is running and no result is obtained. * failed: The test fails. |
| Sum/Square-Sum completion time | Sum and square sum of the completion time of a test instance, in milliseconds. |
| Last Good Probe Time | Date and time when the last probe was complete. |
| Last response packet receiving time | Date and time when the last probe was complete. |
| Lost packet ratio | Packet loss rate. |
| SendProbe | Number of sent probes. |
| ResponseProbe | Number of received response probes. |
| NumOfRTT | Number of RTTs. |