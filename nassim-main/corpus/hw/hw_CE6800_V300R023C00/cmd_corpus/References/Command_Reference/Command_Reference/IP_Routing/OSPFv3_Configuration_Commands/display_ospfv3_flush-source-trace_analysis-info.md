display ospfv3 flush-source-trace analysis-info
===============================================

display ospfv3 flush-source-trace analysis-info

Function
--------



The **display ospfv3 flush-source-trace analysis-info** command displays information about definitely and possibly faulty nodes identified by OSPFv3 flush LSA source tracing.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] [ **area** { *area-id-integer* | *area-id-ipv4* } ] **flush-source-trace** **analysis-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPFv3 process. | The value is an integer ranging from 1 to 4294967295. |
| **area** *area-id-integer* | Specifies an area ID in the format of a decimal integer. | The value is an integer ranging from 0 to 4294967295. |
| **area** *area-id-ipv4* | Specifies an area ID in the IP address format. | The value is in dotted decimal notation. |



Views
-----

All views,Privilege view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about definitely and possibly faulty nodes identified by OSPFv3 flush LSA source tracing, run the display ospfv3 flush-source-trace analysis-info command. The identified definitely and possibly faulty nodes are prioritized in descending order in the command output, which helps maintenance personnel locate the faulty nodes and isolate them in time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about definitely and possibly faulty nodes identified by OSPFv3 flush LSA source tracing.
```
<HUAWEI> display ospfv3 1 flush-source-trace analysis-info
Flush Source Analysis Information for OSPFv3(1)
             ------------------------------------------------
                   
                    Area(0.0.0.1)Analysis Information

Exactly Flush Source :1        Possible  Flush Source :1  
Maybe Flush Source   :1        Not Flush Source       :0 
Total                :3 
Router Id            Ip Address                    FlushType     Host Name     
1.1.1.1              2001:db8:1::1                 Yes           RTA           
2.2.2.2              2001:db8:1::2                 Maybe         RTB           
3.3.3.3              2001:db8:1::3                 No            RTC

```

**Table 1** Description of the **display ospfv3 flush-source-trace analysis-info** command output
| Item | Description |
| --- | --- |
| Exactly Flush Source | Number of determined flush sources. |
| Possible Flush Source | Number of devices that possibly flushed LSAs. |
| Maybe Flush Source | Number of devices that may have flushed LSAs. |
| Not Flush Source | Number of confirmed devices that did not flush LSAs. |
| Total | Total number of devices. |
| Router Id | Router ID. |
| Ip Address | IPv6 address. |
| FlushType | Whether the device flushed LSAs:   * Yes: The device definitely flushed LSAs. * Maybe: The device may have flushed LSAs. * Possible: The device possibly flushed LSAs. * No: The device did not flush LSAs. |
| Host Name | Dynamic hostname. |