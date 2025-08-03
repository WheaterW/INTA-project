Example for Configuring FM
==========================

This section describes how to configure FM.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172361249__fig_dc_vrp_fm_cfg_001801), log in to the Device as a user.

**Figure 1** Configuring FM  
![](images/fig_dc_vrp_fm_cfg_001801.png)  

To help rapidly locate and rectify the faults on the Device, configure FM.


#### Configuration Roadmap

The configuration roadmap is as follows:

* Configure a suppression period for an alarm
* Edit and applying an alarm masking table

#### Data Preparation

To complete the configuration, you need the following data:

* Alarm name
* Alarm suppression period
* Name of the alarm masking table
* Alarm severity
* Name of the NMS host

#### Procedure

1. Enter the alarm management view.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname Device
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~Device] alarm
   ```
2. Configure the severity and suppression period of the alarm named hwBTBChassisRunningModeConflict.
   
   
   
   # Set the severity of the alarm named hwBTBChassisRunningModeConflict to Critical.
   
   ```
   [~Device-alarm] alarm-name hwBTBChassisRunningModeConflict severity critical
   ```
   
   # Set the suppression period for reporting the alarm hwBTBChassisRunningModeConflict to 5s and the suppression period for clearing the alarm to 15s.
   
   ```
   [*Device-alarm] suppression alarm-name hwBTBChassisRunningModeConflict cause-period 5
   [*Device-alarm] suppression alarm-name hwBTBChassisRunningModeConflict clear-period 15
   ```
   ```
   [*Device-alarm] commit
   ```
   
   After the configuration is complete, run the [**display alarm information name hwBTBChassisRunningModeConflict**](cmdqueryname=display+alarm+information+name+hwBTBChassisRunningModeConflict) command to verify the configuration.
   
   ```
   [~Device-alarm] display alarm information name hwBTBChassisRunningModeConflict
   --------------------------------------------------------------------------------
   Feature             : DEVM
   AlarmName           : hwBTBChassisRunningModeConflict
   AlarmId             : 0x801002B
   Severity            : Critical
   Cause Suppress Time : 5
   Clear Suppress Time : 15                                                          
   --------------------------------------------------------------------------------
   ```
3. Edit the alarm masking table.
   
   
   
   # Create an alarm masking table named mask1 and enter the mask1 view.
   
   ```
   [~Device-alarm] mask name mask1
   ```
   
   # Configure masking rules.
   
   ```
   [*Device-alarm-mask1] mask feature-name PMSERVER
   ```
   ```
   [*Device-alarm-mask1] mask severity Minor
   ```
   ```
   [*Device-alarm-mask1] mask severity Warning
   ```
   ```
   [*Device-alarm-mask1] commit
   ```
   
   # After the configuration is complete, run the [**display this**](cmdqueryname=display+this) command in the mask1 view to verify the configuration.
   
   ```
   [~Device-alarm-mask1] display this
     mask severity Minor                                                           
     mask severity Warning                                                         
     mask alarm-name PmThresholdAlarm                                              
   ```
4. Apply the alarm masking table.
   
   
   
   # Configure the NMS host named target-host1 to use the alarm masking table named mask1.
   
   ```
   [~Device-alarm-mask1] quit
   ```
   ```
   [~Device-alarm] snmp target-host target-host1 mask name mask1
   ```
   ```
   [*Device-alarm] commit
   ```
   
   # After the configuration is complete, run the [**display this**](cmdqueryname=display+this) command in the alarm management view to verify the configuration.
   
   ```
   [~Device-alarm] display this
    snmp target-host target-host1 mask name mask1
   ```
5. (Optional) Configure correlative alarm suppression to prevent the system from sending hwBTBChassisRunningModeConflict's correlative alarms to an NMS named **aaa123** with IP address **192.168.3.1**.
   
   
   ```
   [~Device-alarm] correlation-analyze enable
   ```
   ```
   [*Device-alarm] alarm correlation-suppress enable target-host 192.168.3.1 securityname aaa123
   ```

#### Example

```
#
sysname Device
#                                                                               
alarm                                                                           
 suppression alarm-name hwBTBChassisRunningModeConflict cause-period 5                            
 suppression alarm-name hwBTBChassisRunningModeConflict clear-period 15                           
 alarm-name hwBTBChassisRunningModeConflict severity Critical                               
 snmp target-host target-host1 mask name mask1                                  
 #                                                                              
 mask name mask1                                                                
  mask severity Minor                                                           
  mask severity Warning                                                         
  mask alarm-name PmThresholdAlarm                                              
#                                                                           
return                                                                          
```