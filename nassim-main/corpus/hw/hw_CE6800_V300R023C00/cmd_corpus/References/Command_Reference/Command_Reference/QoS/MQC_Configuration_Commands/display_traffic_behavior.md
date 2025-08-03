display traffic behavior
========================

display traffic behavior

Function
--------



The **display traffic behavior** command displays the traffic behavior configuration on the device.




Format
------

**display traffic behavior** [ *behavior-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *behavior-name* | Displays the configuration of a specified traffic behavior. If the name of a traffic behavior is not specified, the configuration of all traffic behaviors is displayed. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display traffic behavior command displays the configuration of a specified traffic behavior or all traffic behaviors. The command output helps you check the traffic behavior configuration and locate faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display configurations of all traffic behaviors on the device.
```
<HUAWEI> display traffic behavior
  Traffic Behavior Information:               
    Behavior: b1                             
      Committed Access Rate:                         
        CIR 200000 (Kbps), PIR 250000 (Kbps), CBS 25000000 (Bytes), PBS 31250000 (Bytes)
        Color Mode: color blind                
        Conform Action: pass                           
        Yellow  Action: pass       
        Exceed  Action: discard                  
      Statistics: enable              
      Remark:                                    
        Remark dscp af11                                  
Total behavior number is 1

```

**Table 1** Description of the **display traffic behavior** command output
| Item | Description |
| --- | --- |
| Behavior | Traffic behavior name. To create a traffic behavior, run the traffic behavior command. |
| Committed Access Rate | CAR. To configure an action taken for packets whose rate exceeds the CAR, run the car (traffic behavior view) command. |
| CIR | Committed information rate (CIR). To set the CIR, run the car (traffic behavior view) command. |
| PIR | Peak information rate (PIR). To set the PIR, run the car (traffic behavior view) command. |
| CBS | Committed burst size (CBS). To set the CBS, run the car (traffic behavior view) command. |
| PBS | Peak burst size (PBS). To set the PBS, run the car (traffic behavior view) command. |
| Color Mode | Color mode, which can be color-aware or color-blind. To set the color mode, run the car (traffic behavior view) command. |
| Conform Action | Action taken for packets whose rate is within the CIR. To configure an action taken for packets whose rate is within the CIR, run the car (traffic behavior view) command. |
| Yellow Action | Action taken for yellow packets. To configure an action taken for yellow packets, run the car (traffic behavior view) command. |
| Exceed Action | Action taken for packets whose rate exceeds the CIR. To configure an action taken for packets whose rate exceeds the CIR, run the car (traffic behavior view) command. |
| Remark | Re-marking action. To configure re-marking, run the remark command. |
| Total behavior number is 1 | Total number of created traffic behaviors. |
| Statistics | Whether the traffic statistics function is enabled. To enable the traffic statistics function, run the statistics enable (traffic behavior view) command. |