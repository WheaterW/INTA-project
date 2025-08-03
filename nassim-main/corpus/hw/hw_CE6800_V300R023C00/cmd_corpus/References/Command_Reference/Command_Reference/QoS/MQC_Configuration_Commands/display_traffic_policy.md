display traffic policy
======================

display traffic policy

Function
--------



The **display traffic policy** command displays the traffic policy configuration on the device.




Format
------

**display traffic policy** [ *policy-name* [ **classifier** *classifier-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of a traffic policy. If this parameter is not specified, the configuration of all traffic policies is displayed. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **classifier** *classifier-name* | Specifies the name of a traffic classifier. If the name of a traffic policy is specified but this parameter is not specified, only the traffic policy configuration is displayed. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display traffic policy command displays the configuration of a specified traffic policy or all traffic policies. The command output helps you check the traffic policy configuration and locate faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of all traffic policies.
```
<HUAWEI> display traffic policy
  Traffic Policy Information:  
    Policy: p1
      Classifier: c1
        Type: OR
      Behavior: b1
        Statistics: enable
        Committed Access Rate:
          CIR 1000 (Kbps), PIR 2000 (Kbps), CBS 125000 (Bytes), PBS 250000 (Bytes)
          Color Mode: color Blind
          Conform Action: pass
          Yellow  Action: pass
          Exceed  Action: discard
      Classifier: c2
        Type: OR
      Behavior: b2
        Deny

Total policy number is 1

```

**Table 1** Description of the **display traffic policy** command output
| Item | Description |
| --- | --- |
| Traffic Policy Information | Traffic Policy Information. |
| Policy | Traffic policy name. To configure a traffic policy, run the traffic policy command. |
| Committed Access Rate | CAR. To configure CAR, run the car (traffic behavior view) command. |
| CIR 1000 (Kbps), PIR 2000 (Kbps), CBS 125000 (Bytes), PBS 250000 (Bytes) | CAR parameters, including the CIR, PIR, CBS, and PBS. To configure the parameters, run the car (traffic behavior view) command. |
| Color Mode | Color mode, which can be color-aware or color-blind. To configure a color mode, run the car (traffic behavior view) command. |
| Conform Action | Action taken for packets whose rate is within the CIR. To configure an action taken for packets whose rate is within the CIR, run the car (traffic behavior view) command. |
| Yellow Action | Action taken for yellow packets. To configure an action taken for yellow packets, run the car (traffic behavior view) command. |
| Exceed Action | Action taken for packets whose rate exceeds the CIR. To configure an action taken for packets whose rate exceeds the CIR, run the car (traffic behavior view) command. |
| Deny | Deny action. To configure the deny action, run the deny | permit command. |
| Total policy number is 1 | Total number of created traffic policies. |
| Classifier | Traffic classifier in a traffic policy. To create a traffic classifier, run the traffic classifier command. |
| Type | Relationship between rules in the traffic classifier. To configure the relationship between rules in a traffic classifier, run the traffic classifier command. |
| Behavior | Traffic behavior bound to the traffic classifier. To create a traffic behavior, run the traffic behavior command. |
| Statistics | Whether the traffic statistics function is enabled. To enable the traffic statistics function, run the statistics enable (traffic behavior view) command. |