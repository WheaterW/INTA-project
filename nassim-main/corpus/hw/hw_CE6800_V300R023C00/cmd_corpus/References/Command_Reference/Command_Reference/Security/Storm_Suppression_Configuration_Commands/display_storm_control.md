display storm control
=====================

display storm control

Function
--------



The **display storm control** command displays the storm control information on an interface.




Format
------

**display storm control** [ **interface** { *interface-name* | *interface-type* *interface-number* } [ **verbose** ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the type and number of an interface. | - |
| **interface** *interface-name* | Specifies an interface name. | - |
| **verbose** | Displays the detailed information about storm control. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to view information about storm control on broadcast, unknown multicast, and unknown unicast packets on an interface, including the packet mode, storm control action, and packet status on the interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about storm control on the interface.
```
<HUAWEI> display storm control interface 10ge 1/0/1
--------------------------------------------------------------------------------                                                    
NOTE:                                                                                                                               
BC = Broadcast; MC = Unknown Multicast; UUC = Unknown Unicast                                                                 
Int = Interval value (unit: seconds)                                                                                                
--------------------------------------------------------------------------------                                                    
PortName     Type   MaxRate Mode Action    Punish-   Trap Log  Int Last                                                             
                                           Status                  Punish-Time                                                      
--------------------------------------------------------------------------------                                                    
10GE1/0/1    BC        2000 Pps  ErrorDown Normal    Off  On    90 --                                                               
10GE1/0/1    MC        2000 Pps  ErrorDown Normal    Off  On    90 --                                                               
10GE1/0/1    UUC       2000 Pps  ErrorDown Normal    Off  On    90 --

```

# Display information about storm control on the interface.
```
<HUAWEI> display storm control interface 10ge 1/0/1 verbose
Port Name         : 10GE1/0/1
 Type             : Unknown Unicast
 Minimum Rate     : 22(Pps)
 Maximum Rate     : 33(Pps)
 Action           : None
 Punish Status    : Normal
 Trap             : Off
 Log              : Off
 Interval         : 5(s)
 Last Punish Time : --

```

**Table 1** Description of the **display storm control** command output
| Item | Description |
| --- | --- |
| Int | The detection interval of storm control in seconds. The default value is 5 seconds. |
| Interval | Strom control detection interval, in seconds, configured by running the storm control interval command. |
| PortName | Name of an interface. |
| Type | Packet type.  BC: Broadcast.  MC: Unknown Multicast.  UUC: Unknown Unicast. |
| MaxRate | Maximum threshold, configured by running the storm control command. |
| Mode | Storm control message mode, including:  Kbps: byte mode.  Pps: packet mode.  %: percentage mode. |
| Action | Storm control actions include:  None: No action is configured.  Errordown: Shut down the interface.  Block: Block the packet.  Suppress: Suppress packet. |
| Trap | Alarm function status, including:  on.  off. |
| Log | Log function status, including:  on.  off. |
| Last Punish-Time | The last time the storm control penalty was implemented. |
| Last Punish Time | The last time the storm control penalty was implemented. |
| Port Name | Name of an interface. |
| Minimum Rate | Minimum threshold, configured by running the storm control command. |
| Maximum Rate | Maximum threshold, configured by running the storm control command. |
| Punish Status | Packet status of the current interface:  ErrorDown: When the rate is greater than MaxRate and the storm control action is to shut down the interface, the status is shut down.  Normal: Normal forwarding.  Block: When the rate is greater than MaxRate and the storm control action is blocked, the status is blocked interface packets.  Suppress: When the rate is greater than MaxRate and the storm control action is to suppress packets, the status is to suppress interface packets, that is, packets exceeding the rate are discarded. |
| Punish-Status | Packet status of the current interface:  ErrorDown: When the rate is greater than MaxRate and the storm control action is to shut down the interface, the status is shut down.  Normal: Normal forwarding.  Block: When the rate is greater than MaxRate and the storm control action is blocked, the status is blocked interface packets.  Suppress: When the rate is greater than MaxRate and the storm control action is to suppress packets, the status is to suppress interface packets, that is, packets exceeding the rate are discarded. |
| NOTE | Description. |