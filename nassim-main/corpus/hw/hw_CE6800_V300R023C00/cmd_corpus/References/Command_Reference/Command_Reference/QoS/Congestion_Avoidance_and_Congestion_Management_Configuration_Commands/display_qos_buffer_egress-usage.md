display qos buffer egress-usage
===============================

display qos buffer egress-usage

Function
--------



The **display qos buffer egress-usage** command displays the buffer usage for outbound queues on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display qos buffer egress-usage** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | The value is a string case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | The value is a string case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display qos buffer egress-usage command displays the buffer usage for outbound queues on an interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the buffer usage for outbound queues on 100GE1/0/1.
```
<HUAWEI> display qos buffer egress-usage interface 100GE 1/0/1
Total indicates the queue buffer threshold of the WRED profile. 
If ECN is enabled and the ECN threshold is greater than the WRED threshold, current may be greater than total.                                                    
Egress Buffer Usage (KBytes) on single queue: (Current/Total)                                                                       
*: Dynamic threshold                                                                                                                
-------------------------------------------------                                                                                   
Interface       Queue   Type               Shared                                                                                   
                                                                                                                                    
-------------------------------------------------                                                                                   
100GE1/0/1          0   Lossy              0/5*                                                                                     
                    1   Lossy              0/5*                                                                                     
                    2   Lossy              0/5*                                                                                     
                    3   Lossy              0/5*                                                                                     
                    4   Lossy              0/5*                                                                                     
                    5   Lossy              0/5*                                                                                     
                    6   Lossy              0/5*                                                                                     
                    7   Lossy              0/5*

```
```
<HUAWEI> display qos buffer egress-usage interface 100GE 1/0/1
Egress buffer usage (KBytes) of each queue: (Current/Total)                                                                   
*: Dynamic threshold                                                                                                                
-------------------------------------------------                                                                                   
Interface       Queue   Type               Shared                                                                                   
                                                                                                                                    
-------------------------------------------------                                                                                   
100GE1/0/1          0   Lossy              0/5*                                                                                     
                    1   Lossy              0/5*                                                                                     
                    2   Lossy              0/5*                                                                                     
                    3   Lossy              0/5*                                                                                     
                    4   Lossy              0/5*                                                                                     
                    5   Lossy              0/5*                                                                                     
                    6   Lossy              0/5*                                                                                     
                    7   Lossy              0/5*

```

**Table 1** Description of the **display qos buffer egress-usage** command output
| Item | Description |
| --- | --- |
| Total | Total buffer. |
| Egress Buffer Usage (KBytes) on single queue | Buffer usage for outbound queues on an interface. |
| Interface | Type and number of the interface. |
| Queue | Queue index. |
| Type | Queue type.   * Lossless. * Lossy. |
| Shared | Shared buffer. If the value is followed by the asterisk (\*), the value is the dynamic threshold. Otherwise, the value is the static threshold. |
| Current | Used buffer. |