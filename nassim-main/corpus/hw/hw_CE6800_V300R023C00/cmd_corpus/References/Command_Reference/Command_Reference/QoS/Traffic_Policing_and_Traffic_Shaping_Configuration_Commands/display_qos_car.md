display qos car
===============

display qos car

Function
--------



The **display qos car** command displays the QoS CAR profile configuration.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display qos car** [ *car-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *car-name* | Displays the configuration of a specified QoS CAR profile.  If this parameter is not specified, the configurations of all QoS CAR profiles are displayed. | The value must be the name of an existing CAR profile on the device. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The **display qos car** command displays the configurations of all QoS CAR profiles or a specified QoS CAR profile. The command output helps you check the QoS CAR profile configuration and locate QoS faults.

**Precautions**

If you do not use the **qos car** command to create a QoS CAR profile, no information is displayed after the **display qos car** command is executed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configurations of all QoS CAR profiles.
```
<HUAWEI> display qos car
   ----------------------------------------------------------------
   CAR Name     : qoscar1
   CAR Index    : 0
    car cir 8000 Kbps pir 10000 Kbps cbs 1000000 Bytes pbs 1250000 Bytes
   Applied number on behavior  : 0
   Applied number on interface inbound  : 0
   Applied number on Eth-Trunk inbound  : 0
   Applied number on interface outbound  : 0                                                                                        
   Applied number on Eth-Trunk outbound  : 0
  ----------------------------------------------------------------
   CAR Name     : qoscar2
   CAR Index    : 1
    car cir 5000 Kbps pir 8000 Kbps cbs 625000 Bytes pbs 1000000 Bytes
   Applied number on behavior  : 0
   Applied number on interface inbound  : 0
   Applied number on Eth-Trunk inbound  : 0
   Applied number on interface outbound  : 0                                                                   
   Applied number on Eth-Trunk outbound  : 0

```

**Table 1** Description of the **display qos car** command output
| Item | Description |
| --- | --- |
| car cir 8000 Kbps pir 10000 Kbps cbs 1000000 Bytes pbs 1250000 Bytes | Parameters of the QoS CAR profile, including the CIR, PIR, CBS, and PBS. To set parameters in a QoS CAR profile, run the qos car command. |
| CAR Name | QoS CAR profile name. To configure a QoS CAR profile, run the qos car command. |
| CAR Index | Index of the QoS CAR profile. |
| Applied number on behavior | Number of traffic behaviors to which the QoS CAR profile is applied. |
| Applied number on interface inbound | Number of inbound interfaces to which the QoS CAR profile is applied. |
| Applied number on Eth-Trunk inbound | Number of inbound Eth-Trunk interfaces to which the QoS CAR profile is applied. |
| Applied number on interface outbound | Number of inbound interfaces to which the QoS CAR profile is applied. |
| Applied number on Eth-Trunk outbound | Number of outbound Eth-Trunk interfaces to which the QoS CAR profile is applied. |