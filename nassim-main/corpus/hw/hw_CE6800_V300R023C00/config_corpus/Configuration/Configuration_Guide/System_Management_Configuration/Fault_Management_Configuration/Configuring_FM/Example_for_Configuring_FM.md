Example for Configuring FM
==========================

Example for Configuring FM

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001513165074__fig11497111211507), there are reachable routes between the user and DeviceA. You can configure FM to help the user learn about the alarms generated on DeviceA in a timely manner and locate faults.

**Figure 1** Networking diagram for configuring FM  
![](figure/en-us_image_0000001512845550.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an alarm severity.
2. Configure delayed alarm reporting.
3. Disable alarm correlation suppression.


#### Procedure

1. Set the APPDATA\_NOT\_SYN alarm severity to critical.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] alarm
   [*DeviceA-alarm] alarm APPDATA_NOT_SYN severity critical
   [*DeviceA-alarm] commit
   ```
2. Configure delayed alarm reporting.
   
   
   
   # Enable delayed alarm reporting and set the delay for reporting active alarms to 5 seconds and the delay for reporting clear alarms to 15 seconds.
   
   ```
   [~DeviceA-alarm] delay-suppression enable
   [*DeviceA-alarm] suppression alarm APPDATA_NOT_SYN cause-period 5
   [*DeviceA-alarm] suppression alarm APPDATA_NOT_SYN clear-period 15
   [*DeviceA-alarm] commit
   ```
3. Disable alarm correlation suppression for the NMS host whose IP address is 192.168.3.1 and username is **aaa123**.
   
   
   ```
   [~DeviceA-alarm] correlation-analyze enable
   [*DeviceA-alarm] undo alarm correlation-suppress enable target-host 192.168.3.1 securityname aaa123
   [*DeviceA-alarm] commit
   ```

#### Verifying the Configuration

Run the [**display alarm information**](cmdqueryname=display+alarm+information) command to check whether the configuration is correct.

```
<DeviceA> display alarm information name APPDATA_NOT_SYN
--------------------------------------------------------------------------------
Feature             : CONFIGURATION
AlarmName           : APPDATA_NOT_SYN
AlarmId             : 0x8152022
Severity            : Critical
Cause Suppress Time : 5
Clear Suppress Time : 15    
--------------------------------------------------------------------------------
```

#### Configuration Scripts

```
#
 sysname DeviceA
#
alarm
 correlation-analyze enable
 alarm APPDATA_NOT_SYN severity critical
 suppression alarm APPDATA_NOT_SYN cause-period 5
 suppression alarm APPDATA_NOT_SYN clear-period 15
 undo alarm correlation-suppress enable target-host 192.168.3.1 securityname cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!M'QCMk|;n!+ttaFN:B%L)q5F9-.u.Bc4Pd;!!!!!!!!!!!!!!!7!!!!:kiHA*OO]%"x:zHit670|z&=~0qG"G!!!!!!!!!!%+%#
#
return  
```