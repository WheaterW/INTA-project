display dcb app-profile
=======================

display dcb app-profile

Function
--------



The **display dcb app-profile** command displays the APP profile configuration.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dcb app-profile** [ *profilename* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profilename* | Displays the configuration of a specified APP profile.  If this parameter is not specified, the configurations of all APP profiles are displayed. | The value is a string of 1 to 31 case-sensitive characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After the APP profile configuration is complete, run the display dcb app-profile command to view the APP profile configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all APP profiles.
```
<HUAWEI> display dcb app-profile
APP-Profile Maximum: 8                                                          
Total: 1                                                                        
------------------------------------------------------------------------------- 
APP Profile: myapp                                                              
------------------------------------------------------------------------------- 
Application                           Priority                                  
------------------------------------------------------------------------------- 
FCoE                                         3                                         
FIP                                          4                                         
ISCSI                                        5                                         
Ethtype:0xa3                                 6                                         
TCPPort:45                                   0                                         
UDPPort:56                                   1                                         
Port:23                                      7
-------------------------------------------------------------------------------

```

**Table 1** Description of the **display dcb app-profile** command output
| Item | Description |
| --- | --- |
| APP-Profile Maximum | Maximum number of APP profiles can be configured. |
| APP Profile | APP profile name. |
| Application | Type of the service. |
| Priority | Service priority. |
| Total | Total number of APP profiles. |