display nqa results collection
==============================

display nqa results collection

Function
--------



The **display nqa results collection** command displays accumulated result records of an NQA test instance.




Format
------

**display nqa results collection** [ **test-instance** *adminName* *testName* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **test-instance** *adminName* | Specifies the name of the administrator for an NQA test instance. | The name is a string of 1 to 32 characters.  If spaces are used, the string must start and end with double quotation marks ("). |
| *testName* | Specifies the name of an NQA test instance. | The name is a string of 1 to 32 characters.  If spaces are used, the string must start and end with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

NQA test instances monitor the network operating status, output statistics, and effectively help reduce costs. NQA measures performance of various protocols on the network, which allows carriers to collect network operation indexes in real time.The NQA test result cannot be displayed automatically on the terminal. To view the NQA test result, run the **display nqa results** command.To view all accumulated statistics, run the display nqa results collection command.

**Precautions**

If no optional parameter is specified, the displaynqaresultscollection command displays the results of all NQA test instances.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display accumulative statistics on jitter NQA tests.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance admin jitter
[*HUAWEI-nqa-admin-jitter] test-type jitter
[*HUAWEI-nqa-admin-jitter] commit
[~HUAWEI-nqa-admin-jitter] display nqa results collection test-instance admin jitter
NQA entry(admin, jitter): test type is JITTER
    1 . Test 1 collect result
   SendProbe: 60                           ResponseProbe: 60                      
   Completion: 1                           RTD over thresholds number: 0           
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

**Table 1** Description of the **display nqa results collection** command output
| Item | Description |
| --- | --- |
| NQA entry(admin, jitter) | NQA test entry information:   * admin: administrator of an NQA test instance. * jitter: name of an NQA test instance. |
| RTD over thresholds number | Number of times the RTD exceeds the specified threshold. |
| OWD over thresholds SD number | Number of times that the one-way transmission (from the source to the destination) delay exceeds the threshold. |
| OWD over thresholds DS number | Number of times that the one-way transmission (from the destination to the source) delay exceeds the threshold. |
| OWD SD sum | Sum of one-way delays from the source to the destination. |
| OWD DS sum | Sum of one-way delays from the destination to the source. |
| Min/Max/Avg/Sum RTT | Minimum, maximum, average, or sum of the RTT. |
| RTT square sum | Square sum of the RTT. |
| RTT stats errors number | Number of RTT status errors. |
| Num of RTT | Number of RTTs. |
| Drop operation number | Number of system resource allocation failures. |
| Operation sequence errors number | Sequence number of the error packets received by the client. |
| Operation timeout number | Operation timeout number. |
| System busy operation number | Number of test conflicts. |
| Min positive SD | Minimum positive jitter from the source to the destination. |
| Min positive DS | Minimum positive jitter from the destination to the source. |
| Min negative SD | Minimum negative jitter from the source to the destination. |
| Min negative DS | Minimum negative jitter from the destination to the source. |
| Min delay SD | Minimum delay from the source to the destination. |
| Min delay DS | Minimum delay from the destination to the source. |
| Max positive SD | Maximum positive jitter from the source to the destination. |
| Max positive DS | Maximum positive jitter from the destination to the source. |
| Max negative SD | Maximum negative jitter from the source to the destination. |
| Max negative DS | Maximum negative jitter from the destination to the source. |
| Max delay SD | Maximum delay from the source to the destination. |
| Max delay DS | Maximum delay from the destination to the source. |
| Positive SD number | Number of positive jitters from the source to the destination. |
| Positive DS number | Number of positive jitters from the destination to the source. |
| Positive SD sum | Sum of positive jitters from the source to the destination. |
| Positive DS sum | Sum of positive jitters from the destination to the source. |
| Positive SD square sum | Square sum of positive jitters from the source to the destination. |
| Positive DS square sum | Square sum of positive jitters from the destination to the source. |
| Negative SD number | Number of negative jitters from the source to the destination. |
| Negative DS number | Number of negative jitters from the destination to the source. |
| Negative SD sum | Sum of negative jitters from the source to the destination. |
| Negative DS sum | Sum of negative jitters from the destination to the source. |
| Negative SD square sum | Square sum of negative jitters from the source to the destination. |
| Negative DS square sum | Square sum of negative jitters from the destination to the source. |
| Avg delay SD | Average delay from the source to the destination. |
| Avg delay DS | Average delay from the destination to the source. |
| Delay SD square sum | Square sum of the delay jitter from the source to the destination. |
| Delay DS square sum | Square sum of the delay jitter from the destination to the source. |
| Packet loss SD | Maximum number of dropped packets from the source to the destination. |
| Packet loss DS | Maximum number of dropped packets from the destination to the source. |
| Packet loss unknown | Number of packets dropped in the unknown direction. |
| Packet loss ratio | Test packet loss ratio. |
| Average of jitter | Average jitter. |
| Average of jitter SD | Average jitter from the source to the destination. |
| Average of jitter DS | Average jitter from the destination to the source. |
| Jitter out value | Jitter in packet sending. |
| Jitter in value | Jitter in packet receiving. |
| Number of OWD | Number of one-way delay packets. |
| ICPIF value | Advantage factor. |
| MOS-CQ value | Mean Opinion Score (MOS) of VoIP performance. |
| TimeStamp unit | TimeStamp unit. |
| SendProbe | Number of sent probes. |
| ResponseProbe | Number of received response probes. |
| Completion | Completion states. |