display dcb
===========

display dcb

Function
--------



The **display dcb** command displays the DCB configuration and negotiation status.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dcb** [ **interface** { *interface-name* | *interface-type* *interface-num* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-num* | Displays the DCB configuration on a specified interface.   * interface-type specifies the type of an interface. * interface-num specifies the number of an interface.   If this parameter is not specified, the system displays the DCB configuration on all interfaces. | - |
| **interface** *interface-name* | Displays the DCB configuration on a specified interface.   * interface-name specifies the name of an interface.   If this parameter is not specified, DCB configurations on all interfaces are displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After configuring DCB on interfaces, you can run the **display dcb** command to check the DCB configuration and negotiation status on the interfaces.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the DCB configuration and negotiation status on all interfaces.
```
<HUAWEI> display dcb
M:Manual;    A:Auto                                                             
------------------------------------------------------------------------------- 
Interface         PFC Name     PFC Status  ETS Name    ETS Status App-Profile   
------------------------------------------------------------------------------- 
25GE1/0/1         default      ENABLE(M)   default     ENABLE     -             
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display dcb** command output
| Item | Description |
| --- | --- |
| Interface | Name of an interface. |
| PFC Name | Name of a PFC profile.  "-" indicates that no PFC template is applied to the interface. |
| PFC Status | Indicates the negotiation status of the PFC function. In the preceding information:  -SUCCEED: indicates that the PFC negotiation is successful.  -FAILED: indicates that the PFC negotiation fails.  -ENABLE: indicates that the PFC works in forcible mode and no negotiation is required.  "-": indicates that PFC is disabled on the interface.  PFC working mode. In the preceding information:  -A: indicates the negotiation mode.  -M: forcible mode. |
| ETS Name | Indicates the name of an ETS profile.  "-" indicates that no ETS profile is applied to the interface. |
| ETS Status | Indicates the negotiation status of the ETS function. In the preceding information:  -SUCCEED: indicates that the ETS negotiation is successful.  -FAILED: indicates that the ETS negotiation fails.  -ENABLE: indicates that the ETS working mode is forcible and no negotiation is required.  "-": indicates that the ETS function is disabled on the interface. |
| App-Profile | App template name.  "-" indicates that no APP template is applied to the interface. |