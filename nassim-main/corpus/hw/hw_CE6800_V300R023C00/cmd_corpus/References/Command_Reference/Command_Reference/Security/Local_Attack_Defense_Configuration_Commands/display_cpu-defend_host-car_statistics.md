display cpu-defend host-car statistics
======================================

display cpu-defend host-car statistics

Function
--------



The **display cpu-defend host-car statistics** command displays the number of packets discarded in user-level rate limiting.




Format
------

**display cpu-defend host-car** [ **mac-address** *mac-address* ] **statistics** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mac-address** *mac-address* | Indicates the number of discarded packets from the specified MAC address. | The value is in the format of H-H-H. |
| **slot** *slot-id* | Indicates the number of packets discarded by the specified card. | The value is a string of 1 to 31 case-sensitive characters without spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To view the number of packets discarded in the user-level rate limiting, run this command.

**Precautions**

* Before using this command, run the **cpu-defend host-car enable** command to enable user-level rate limiting.
* If the number of discarded packets is 0, the index is not displayed.

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the number of packets discarded in the user-level rate limiting.
```
<HUAWEI> display cpu-defend host-car statistics
slot 1                                                                                                                             
car-id                              car-drop                                                                                        
--------------------------------------------                                                                                        
3192                                  740385                                                                                        
3347                                       7                                                                                        
4133                                  529474                                                                                        
4471                                  529477                                                                                        
5075                                  529476                                                                                        
5836                                  529474                                                                                        
6046                                 1001218

```

**Table 1** Description of the **display cpu-defend host-car statistics** command output
| Item | Description |
| --- | --- |
| slot | Slot ID. |
| car-id | Bucket ID for rate limiting. |
| car-drop | Number of dropped packets whose rate exceeds the CAR. To configure the CAR value, run the cpu-defend host-car [ mac-address mac-address | car-id car-id ] pps pps-value command. |