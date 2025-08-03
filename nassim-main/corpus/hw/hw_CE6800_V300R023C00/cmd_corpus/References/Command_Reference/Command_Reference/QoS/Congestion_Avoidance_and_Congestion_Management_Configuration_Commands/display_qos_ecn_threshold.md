display qos ecn threshold
=========================

display qos ecn threshold

Function
--------



The **display qos ecn threshold** command displays information about the ECN threshold.




Format
------

**display qos ecn threshold** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


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

You can run the display qos ecn threshold command to display the ECN threshold of each queue.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the ECN threshold of a specified interface.
```
<HUAWEI> display qos ecn threshold interface 100GE 1/0/1
* : indicates AI ECN                                                       
[] : indicates the upper ECN threshold
Interface       Queue     Min     Max  Probability  Queue Size                  
                         (KB)    (KB)          (%)        (KB)                  
--------------------------------------------------------------                  
100GE1/0/1          0    2048    2048          100           0
                    1       0       0            0           0
                    2       0       0            0           0
                    3       0       0            0           0
                    4       0       0            0           0
                    5       0       0            0           0
                    6       0       0            0           0
                    7       0       0            0           0

```
```
<HUAWEI> display qos ecn threshold interface 100GE 1/0/1
* : indicates AI ECN                                                       
[] : indicates the upper ECN threshold
Interface       Queue     Min     Max  Probability  Queue Size                  
                         (KB)    (KB)          (%)        (KB)                  
--------------------------------------------------------------                  
100GE1/0/1          0    2048    2048          100           0
                    1       0       0            0           0
                    2       0       0            0           0
                    3       0       0            0           0
                    4       0       0            0           0
                    5       0       0            0           0

```

**Table 1** Description of the **display qos ecn threshold** command output
| Item | Description |
| --- | --- |
| Interface | Type and number of the interface. |
| Queue | Queue index. If the value follows an asterisk (\*), the AI ECN threshold is enabled for the queue. Otherwise, the AI ECN threshold is disabled. |
| Queue Size | Service buffer usage. |
| Min | Lower ECN threshold. If the value is placed in brackets ([]), the lower ECN threshold of the queue is the maximum buffer size. If the AI ECN threshold is enabled for a queue, the actual value is displayed only when traffic passes through the queue. |
| Max | Upper ECN threshold. If the value is placed in brackets ([]), the upper ECN threshold of the queue is the maximum buffer size. If the AI ECN threshold is enabled for a queue, the actual value is displayed only when traffic passes through the queue. |
| Probability | Maximum marking probability of ECN. For queues enabled with AI ECN, the value takes effect only after traffic passes through the queues. |