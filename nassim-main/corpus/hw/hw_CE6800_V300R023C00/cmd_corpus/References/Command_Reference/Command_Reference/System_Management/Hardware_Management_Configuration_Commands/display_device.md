display device
==============

display device

Function
--------



The **display device** command displays the type and status of components on a device.




Format
------

**display device** [ **slot** *slotid* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slotid* | Displays the type and status of components on the device. If slot-id is specified, interface information on the device is displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can use this command to check the working status of components on a device and check whether the device is working normally.

**Precautions**

After an alarm is generated, you can clear the hardware alarm record to change the running status of the component to normal, but the alarm indicator does not recover.When a hardware alarm such as CPU registration failure is generated on a device, the alarm status in the display device command output is abnormal.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display component information of the board in a specified slot.
```
<HUAWEI> display device slot 1
CE6866's Device status:
--------------------------------------------------------------------------------
Slot  Card   Type                     Online   Power Register     Alarm     Primary        
--------------------------------------------------------------------------------
1     -      CE6866-48S8CQ-P          Present  On    Registered   Normal    Master         
--------------------------------------------------------------------------------
  Part  Number      :   
  Board Type        : CE6866-48S8CQ-P
  Board Description : 48-Port 25GE SFP28,8*100GE QSFP28,
                      Without Fan and Power Module
------------------------------------------------------------------------------

-------------------------------------------------------------------------------
Interface          Port     Optic   MDI    Speed  Duplex Input   Output  Port  
                   Type     Status         (Mbps)        Flow-   Flow-   Status
                                                         control control       
-------------------------------------------------------------------------------
100GE1/0/1         Fiber    Present --     100000 Full   Disable Disable Up    
100GE1/0/2         Fiber    Present --     40000  Full   Disable Disable Up    
100GE1/0/3         Fiber    Present --     100000 Full   Disable Disable Up    
100GE1/0/4         Fiber    Absent  --     AUTO   Full   Disable Disable *Down 
100GE1/0/5         Fiber    Absent  --     AUTO   Full   Disable Disable *Down    
... 
-------------------------------------------------------------------------------

```

# Display component information about the device.
```
<HUAWEI> display device
CE8851-32CQ8DQ-K's Device status:                                               
--------------------------------------------------------------------------------
Slot  Card   Type                     Online   Power Register     Alarm     Prim
ary                                                                             
--------------------------------------------------------------------------------
1     -      CE8851-32CQ8DQ-K         Present  On    Registered   Normal    Mast
er                                                                              
      FAN1   FAN                      Present  On    Registered   Normal    NA  
                                                                                
      FAN2   FAN                      Present  On    Registered   Normal    NA  
                                                                                
      FAN3   FAN                      Present  On    Registered   Normal    NA  
                                                                                
      FAN4   FAN                      Present  On    Registered   Normal    NA  
                                                                                
      FAN5   FAN                      Present  On    Registered   Normal    NA  
                                                                                
      FAN6   FAN                      Present  On    Registered   Normal    NA  
                                                                                
      PWR1   PAC1K2S12-CB             Present  On    Registered   Abnormal  NA  
                                                                                
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display device** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID of a board. |
| Card | Subcard number. |
| Type | Type of a component. |
| Online | Indicates whether a component is running properly.   * Present: The board is properly installed. * Offline: The board is not installed or is isolated. |
| Power | Whether the component is powered on:   * On: The board is powered on. * Off: The board is not powered on.   If this field displays -, the power-on status of the component cannot be obtained. The status probably is caused by the following situations:   * The component is not registered or fails to be registered. If the component is not registered, check again after the component is registered. If the registration fails, rectify the fault according to the troubleshooting manual. * The component is just registered, and the power-on status is not reported. Wait a moment and check again. |
| Register | Whether a component is registered:   * Registered: The component has been registered. * Unregistered: The component is not registered. |
| Alarm | Running status of a component:   * Abnormal: The slot corresponding to the component has a major or critical hardware alarm. You can run the display device alarm hardware command to view hardware alarms. * Normal: The component is running properly. * WrongType: The model of the inserted component conflicts with the pre-configured model. * -: The system cannot obtain the component running status. |
| Part Number | Part number. |
| Board Type | Board type. |
| Board Description | Board description. |
| Interface | Interface number. |
| MDI | MDI type of an interface. This field displays Auto for an electrical interface and -- for an optical interface or a management interface. |
| Duplex | Duplex mode of the interface:   * Half: indicates the half-duplex mode. * Full: indicates the full-duplex mode. |
| Primary | Active/standby status of the device. The value is Master for the active device, Slave for the standby device, and NA for other devices. |