display ospf flush-source-trace analysis-info
=============================================

display ospf flush-source-trace analysis-info

Function
--------



The **display ospf flush-source-trace analysis-info** command displays information about definitely and possibly faulty nodes identified by OSPF flush LSA source tracing.




Format
------

**display ospf** [ *process-id* ] [ **area** { *area-id-integer* | *area-id-ipv4* } ] **flush-source-trace** **analysis-info**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| *area-id-integer* | Specifies an area ID. | The value is an integer ranging from 0 to 4294967295. |
| *area-id-ipv4* | Specifies an area ID. | The value is an IP address ranging from 0.0.0.0 to 255.255.255.255. |



Views
-----

All views,Privilege view


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To check information about definitely and possibly faulty nodes identified by OSPF flush LSA source tracing, run the display ospf flush-source-trace analysis-info command. The identified definitely and possibly faulty nodes are prioritized in descending order in the command output, which helps maintenance personnel locate the faulty nodes and isolate them in time.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about definitely and possibly faulty nodes identified by OSPF flush LSA source tracing.
```
<HUAWEI> display ospf 1 flush-source-trace analysis-info
Flush Source Analysis Information for OSPF(1)
             ------------------------------------------------

                    Area(0.0.0.0)Analysis Information

Exactly Flush Source :1        Possible  Flush Source :1  
Maybe Flush Source   :1        Not Flush Source       :0 
Total                :3 
Router Id            Ip Address           FlushType      Host Name      
1.1.1.1              10.100.100.100      Yes            RTA            
2.2.2.2              10.100.200.200      Possible       RTB            
3.3.3.3              10.100.210.210      Maybe          RTC

```

**Table 1** Description of the **display ospf flush-source-trace analysis-info** command output
| Item | Description |
| --- | --- |
| Exactly Flush Source | Number of devices that definitely flushed LSAs. |
| Possible Flush Source | Number of devices that possibly flushed LSAs. |
| Maybe Flush Source | Number of devices that may have flushed LSAs. |
| Not Flush Source | Number of confirmed devices that did not flush LSAs. |
| Total | Total number of devices. |
| Router Id | Router ID. |
| Ip Address | IP address. |
| FlushType | Whether the device flushed LSAs:   * Yes: The device definitely flushed LSAs. * Maybe: The device may have flushed LSAs. * Possible: The device possibly flushed LSAs. * No: The device did not flush LSAs. |
| Host Name | Dynamic hostname. |