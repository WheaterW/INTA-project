display inof configuration status
=================================

display inof configuration status

Function
--------



The **display inof configuration status** command displays the configuration status on the iNOF network.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display inof configuration status**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run this command to check configuration status of the iNOF network.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# You can run this command to check configuration status of the iNOF network.
```
<HUAWEI> display inof configuration status
Role: Reflector
IPv4 Info:
Reflector1: Local
Reflector2: 1.1.1.2
---------------------------------------------------------------
Item          Reflector1 Status  Reflector2 Status  iNOF Status
---------------------------------------------------------------
Default Zone  Enable             Disable            Enable     
Hard Zoning   Enable             Disable            Enable     
BFD           Enable             Disable            Enable         
---------------------------------------------------------------
IPv6 Info:
Reflector1: Local
Reflector2: 2001:DB8:1::2
---------------------------------------------------------------
Item          Reflector1 Status  Reflector2 Status  iNOF Status
---------------------------------------------------------------
Default Zone  Enable             Disable            Enable     
Hard Zoning   Enable             Disable            Enable     
BFD           Enable             Disable            Enable       
---------------------------------------------------------------

```

**Table 1** Description of the **display inof configuration status** command output
| Item | Description |
| --- | --- |
| IPv4 Info | IPv4 information. |
| Item | Configuration item. The options are as follows:   * Default Zone: function of automatically adding hosts to the iNOF default zone. * Hard Zoning: iNOF zone isolation. * BFD: BFD for iNOF. |
| Reflector1 Status | Configuration status on reflector 1, the value can be either of the following:   * If Disable is displayed, it means iNOF configuration status is disabled; * If Enable is displayed, it means iNOF configuration status is enabled. |
| Reflector1 | IP address of reflector 1:   * Displays the IP address of reflector 1. * If Local is displayed, the current device is a reflector. |
| Reflector2 Status | Configuration status on reflector 2, the value can be either of the following:   * If Disable is displayed, it means iNOF configuration status is disabled; * If Enable is displayed, it means iNOF configuration status is enabled. |
| Reflector2 | IP address of reflector 2:   * Displays the IP address of reflector 2. |
| iNOF Status | iNOF Configuration status, the value can be either of the following:   * If Disable is displayed, it means iNOF configuration status is disabled; * If Enable is displayed, it means iNOF configuration status is enabled. |
| IPv6 Info | IPv6 information. |
| Role | Role:   * Reflect-client; * Reflector; * Standalone. |