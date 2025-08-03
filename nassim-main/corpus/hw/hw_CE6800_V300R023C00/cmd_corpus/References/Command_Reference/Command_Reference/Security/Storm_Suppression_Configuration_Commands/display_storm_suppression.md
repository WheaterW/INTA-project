display storm suppression
=========================

display storm suppression

Function
--------



The **display storm suppression** command displays the configured and effective broadcast,unknown-multicast,unknown-unicast traffic suppression thresholds on an interface.




Format
------

**display storm suppression** { **broadcast** | **unknown-unicast** | **multicast** } [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **broadcast** | Configures broadcast packet suppression. | - |
| **unknown-unicast** | Configures unknown-unicast packet suppression. | - |
| **multicast** | Configures unknown multicast packet suppression. | - |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The broadcast, unknown multicast, and unknown unicast traffic suppression thresholds configured on the device may be different from those that take effect on the interface. You can run this command to view detailed information about the two thresholds.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configured and effective broadcast traffic suppression thresholds on the interface.
```
<HUAWEI> display storm suppression broadcast interface 100ge 1/0/1
------------------------------------------------------------------------------------------------------                              
                                 Configured                                 Current                                                 
interface        percent(%) cir(kbps) cbs(bytes)        pps percent(%) cir(kbps) cbs(bytes)        pps                              
------------------------------------------------------------------------------------------------------                              
100GE1/0/1               10        --         --         --        10        --         --         --                              
------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display storm suppression** command output
| Item | Description |
| --- | --- |
| interface | Name of an interface. |
| Configured | The threshold for configuring broadcast,unknown-multicast,unknown-unicast traffic suppression on the interface. |
| Current | Threshold for the actual suppression of broadcast,unknown-multicast,unknown-unicast traffic. |
| percent(%) | The percentage value is the ratio of the packet rate to the interface rate. |
| cir(kbps) | Specify the Committed Information Rate (CIR), that is, the rate that can be passed. The unit is kbit/s. |
| cbs(bytes) | Specify Committed Burst Size (CBS), that is, the committed traffic that can pass in an instant. The unit is bytes. |