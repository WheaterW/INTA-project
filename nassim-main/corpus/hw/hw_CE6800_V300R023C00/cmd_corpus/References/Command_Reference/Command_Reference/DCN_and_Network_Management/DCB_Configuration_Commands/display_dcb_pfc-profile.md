display dcb pfc-profile
=======================

display dcb pfc-profile

Function
--------



The **display dcb pfc-profile** command displays the PFC profile configuration.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dcb pfc-profile** [ *profilename* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profilename* | Displays the configuration of a specified PFC profile.  If this parameter is not specified, the configurations of all PFC profiles are displayed. | The PFC profile must already exist. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After configuring a PFC profile, you can run this command to check the PFC profile configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all PFC profiles.
```
<HUAWEI> display dcb pfc-profile
PFC-Profile Maximum: 2                                                          
Total: 2                                                                        
------------------------------------------------------------------------------- 
PFC-profile Name                      Priority                                  
------------------------------------------------------------------------------- 
default                               3                                         
------------------------------------------------------------------------------- 
mypfc                                 4                                    
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display dcb pfc-profile** command output
| Item | Description |
| --- | --- |
| PFC-Profile Maximum | Maximum number of PFC profiles that can be configured. |
| PFC-profile Name | PFC profile name. |
| Priority | Priority of a queue for which PFC is enabled. |
| Total | Total number of PFC profiles. |