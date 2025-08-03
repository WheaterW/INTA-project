display cpu-defend policy
=========================

display cpu-defend policy

Function
--------



The **display cpu-defend policy** command displays the attack defense policy configuration.




Format
------

**display cpu-defend policy** [ *policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Displays the configuration of a specified attack defense policy.  If policy-name is specified, information about the specified attack defense policy is displayed.  If policy-name is not specified, information about all attack defense policies is displayed. | The attack defense policy must already exist. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After an attack defense policy is created, you can run the **display cpu-defend policy** command to view the slot ID that the attack defense policy is applied to and configurations of the attack defense policy.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all attack defense policies.
```
<HUAWEI> display cpu-defend policy test1
==============================================
Policy name: test1          
Policy applies on slot: 1   
 Car packet-type bfd(pps) : 128      
==============================================

```

**Table 1** Description of the **display cpu-defend policy** command output
| Item | Description |
| --- | --- |
| Policy name | Name of an attack defense policy. To configure an attack defense policy, run the cpu-defend policy command. |
| Policy applies on slot | Slot that an attack defense policy is applied to. |
| Car packet-type bfd(pps) | CPCAR value of BFD packets. To set the CAR value for BFD packets, run the car command in the attack defense policy view. |