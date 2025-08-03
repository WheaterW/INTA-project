display qos micro-burst statistics interface
============================================

display qos micro-burst statistics interface

Function
--------



The **display qos micro-burst statistics interface** command displays statistics about microburst detection on an interface.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display qos micro-burst statistics interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | The value is a string case-sensitive characters, spaces not supported. |
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

**Usage Scenario**

In default microburst detection mode, the packet sampling interval is 5 ms. In enhanced microburst detection mode, the packet sampling interval is 1 ms.The microburst detection period is 5 minutes. That is, key performance indicators of an interface are collected every 5 minutes and related entries are generated. You can run the **display qos micro-burst statistics interface interface-type interface-number** command to view statistics collected within 300 minutes after microburst detection is enabled on an interface, including the average rate of burst traffic, maximum rate of burst traffic, number of discarded packets, average buffer usage on the interface, peak buffer usage on the interface, and entry generation time.

**Prerequisites**

1. The microburst detection function has been enabled on the device using the **qos micro-burst detection** [ **enhanced** ] **enable** command in the system view.
2. The microburst detection function has been enabled on an interface using the **qos micro-burst detection enable** command in the interface view.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# In default microburst detection mode, display microburst detection statistics on 10GE1/0/1.
```
<HUAWEI> display qos micro-burst statistics interface 10GE 1/0/1
-----------------------------------------------------------------------------------------------------                               
A-Rate            P-Rate           Discard         A-Buffer         P-Buffer                 DateTime                               
(bps)              (bps)           Packets             (B)             (B)                                                        
-----------------------------------------------------------------------------------------------------
84038560        84571200           2995675             2503             2507      2021-06-02 14:54:43
84056160        84571200           1352434             2503             2507      2021-06-02 14:49:43
-----------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display qos micro-burst statistics interface** command output
| Item | Description |
| --- | --- |
| A-Rate | Average rate of packets forwarded to an interface from any other interfaces on the same device, in bit/s. |
| P-Rate | Peak rate of packets forwarded to an interface from any other interfaces on the same device, in bit/s. |
| Discard Packets | Number of discarded packets. |
| A-Buffer | Average buffer usage, in bytes. |
| P-Buffer | Peak buffer usage, in bytes. |
| DateTime | Time when an entry is generated. |