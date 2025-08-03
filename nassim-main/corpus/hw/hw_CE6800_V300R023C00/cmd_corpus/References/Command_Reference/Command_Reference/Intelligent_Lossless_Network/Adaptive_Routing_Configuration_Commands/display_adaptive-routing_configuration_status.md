display adaptive-routing configuration status
=============================================

display adaptive-routing configuration status

Function
--------



The **display adaptive-routing configuration status** command displays the configuration delivery status of adaptive routing.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display adaptive-routing configuration status** [ **interface** { *interface-name* | *interface-type* *interface-num* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies an interface name. | - |
| **interface** *interface-type* *interface-num* | Specifies the type and number of an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the adaptive routing function is enabled on a device, you can run this command to check the delivery status of the adaptive routing configuration on an interface enabled with the adaptive routing function.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the delivery status of adaptive routing configurations on a specified interface. (CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM)
```
<HUAWEI> display adaptive-routing configuration status interface 100GE 1/0/1
Global Status: Enable 
Dragonfly Info:  
  ----------------------------------------------------------------- 
  Interface    Role    Profile  Adaptive-Routing   ABS-PFC   Adjust 
  ----------------------------------------------------------------- 
  100GE1/0/1   Global  default  Normal             Normal    Normal 
  -----------------------------------------------------------------

```

# Display the delivery status of adaptive routing configurations on a specified interface. (CE8855 and CE8851-32CQ4BQ)
```
<HUAWEI> display adaptive-routing configuration status interface 100GE 1/0/1
Global Status: Enable 
Dragonfly Info:  
  --------------------------------------------------------- 
  Interface    Role    Profile  Adaptive-Routing     Adjust 
  --------------------------------------------------------- 
  100GE1/0/1   Global  default  Normal               Normal 
  ---------------------------------------------------------

```

**Table 1** Description of the **display adaptive-routing configuration status** command output
| Item | Description |
| --- | --- |
| Global Status | Whether the global adaptive route function is enabled.   * Enable: The function is enabled. * Disable: The function is disabled. |
| Dragonfly Info | Delivery status of the direct topology configuration. |
| Interface | Name of an interface. |
| Role | Interface role.   * Global: global role. * Local: local role. |
| Profile | Direct topology configuration profile. |
| Adaptive-Routing | Configuration delivery status of adaptive routing.   * Normal. * Abnormal. * --: not configured. |
| ABS-PFC | Configuration delivery status of dragonfly antilocking PFC.   * Normal. * Abnormal. * --: not configured. |
| Adjust | Configuration delivery status of dragonfly deadlock prevention.   * Normal. * Abnormal. * --: not configured. |