display qos buffer ingress-usage
================================

display qos buffer ingress-usage

Function
--------



The **display qos buffer ingress-usage** command displays the buffer usage for inbound queues on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display qos buffer ingress-usage** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


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

The display qos buffer ingress-usage command displays the buffer usage for inbound queues on an interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the buffer configuration and usage in the inbound direction of 100GE1/0/1.
```
<HUAWEI> display qos buffer ingress-usage interface 100GE 1/0/1
Ingress Buffer Usage (KBytes) on lossless priority: (Current/Total)                                                                 
*: Dynamic threshold                                                                                                                
----------------------------------------                                                                                            
Interface       Priority        PFC-Xoff                                                                                            
                                                                                                                                    
----------------------------------------                                                                                            
100GE1/0/1             3           0/4*

```
```
<HUAWEI> display qos buffer ingress-usage interface 100GE 1/0/1
Ingress Buffer Usage (KBytes) on lossless priority: (Current/Total)
*: Dynamic threshold
--------------------------------------------------------------------------
Interface       Priority        Guaranteed        PFC-Xoff        Headroom

--------------------------------------------------------------------------
100GE1/0/1             3               0/2            0/5*         0/20

```

**Table 1** Description of the **display qos buffer ingress-usage** command output
| Item | Description |
| --- | --- |
| Ingress Buffer Usage (KBytes) on lossless priority | Buffer usage for inbound queues on an interface. |
| Interface | Type and number of the interface. |
| Priority | Priority of lossless services. |
| PFC-Xoff | Threshold for triggering PFC frames. If the value is followed by the asterisk (\*), the value is the dynamic threshold. Otherwise, the value is the static threshold. |
| Guaranteed | Guaranteed buffer. |
| Headroom | Headroom buffer. |
| Current | Used buffer. |
| Total | Total buffer. |