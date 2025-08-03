display radius-server item
==========================

display radius-server item

Function
--------



The **display radius-server item** command displays the RADIUS server configuration.




Format
------

**display radius-server item** { **ip-address** *ip-address* { **accounting** | **authentication** } | **template** *template-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** *ip-address* | Specifies the IP address of the RADIUS server. | The value is in dotted decimal notation. |
| **accounting** | Indicates the RADIUS accounting server. | - |
| **authentication** | Indicates the RADIUS authentication server. | - |
| **template** *template-name* | Displays the RADIUS server template name. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

The command shows the RADIUS server configuration.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of RADIUS server template rds.
```
<HUAWEI> display radius-server item template rds
 ------------------------------------------------------------------------------ 
  STState    = STState-up 
  STChgTime  = -
  Type       = auth-server                                                      
  State      = state-up                                                         
  AlarmFlag  = false                                                            
  STUseNum   = 1 
  IPAddress  = 192.168.30.1 
  AlarmTimer = 0xffffffff 
  Head       = 1057 
  Tail       = 1311
  ProbeID    = 255
  Type       = acct-server 
  State      = state-up 
  AlarmFlag  = false 
  STUseNum   = 1                                                                
  IPAddress  = 192.168.30.1                                                     
  AlarmTimer = 0xffffffff                                                       
  Head       = 1057                                                             
  Tail       = 1311                                                             
  ProbeID    = 255                                                              
 ------------------------------------------------------------------------------

```

**Table 1** Description of the **display radius-server item** command output
| Item | Description |
| --- | --- |
| STState | Status of the RADIUS server template.  STState-up: indicates that the RADIUS server template is in up state.  STState-down: indicates that the RADIUS server template is in down state. |
| STChgTime | Time when the RADIUS server template status changes. |
| Type | RADIUS server type:  auth-server: authentication server.  acct-server: accounting server. |
| State | RADIUS server status.  state-up: indicates that the RADIUS server is in up state.  state-down: indicates that the RADIUS server is in down state.  state-probe: indicates that the RADIUS server is in detection state. |
| AlarmFlag | Alarm flag.  true: indicates that an alarm about status change has been sent.  false: indicates that an alarm about status change is not sent. |
| STUseNum | RADIUS server template ID. |
| IPAddress | RADIUS server IP address. |
| AlarmTimer | ID of the alarm timer. |
| Head | Head pointer used to allocate the ID to RADIUS packets. |
| Tail | Tail pointer used to allocate the ID to RADIUS packets. |
| ProbeID | ID of probe packets. |