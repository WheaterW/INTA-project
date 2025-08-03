Example for Configuring MAC Address Flapping Detection
======================================================

Example for Configuring MAC Address Flapping Detection

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001130624934__fig_dc_cfg_mac_003801), a network loop occurs because DeviceB and DeviceC are mistakenly connected using a network cable. Consequently, this causes MAC address flapping on DeviceA.

To quickly detect the loop, configure MAC address flapping detection on DeviceA. After this function is enabled, DeviceA checks whether MAC address flapping occurs between interfaces to determine the presence of a loop, and then carries out troubleshooting.

**Figure 1** Networking for configuring MAC address flapping detection![](public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001176664495.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable MAC address flapping detection.
2. Set an aging time for flapping MAC addresses.
3. Configure an action against MAC address flapping on the interfaces to eliminate the loop.

#### Procedure

1. Enable MAC address flapping detection.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] mac-address flapping detection
   [*DeviceA] commit
   ```
2. Set an aging time for flapping MAC addresses.
   
   
   ```
   [~DeviceA] mac-address flapping aging-time 500
   [*DeviceA] commit
   ```
3. Set the action against MAC address flapping to **error-down** on 100GE 1/0/1 and 100GE 1/0/2.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] mac-address flapping trigger error-down
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] mac-address flapping trigger error-down
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
4. Enable the error-down interfaces to recover after a specified delay.
   
   
   ```
   [~DeviceA] error-down auto-recovery cause mac-address-flapping interval 500
   [*DeviceA] commit
   ```

#### Verifying the Configuration

Run the **display mac-address flapping** command to check the MAC address flapping configuration.

```
[~DeviceA] [display mac-address flapping](cmdqueryname=display+mac-address+flapping)
MAC Address Flapping Configurations :
-------------------------------------------------------------------------
  Flapping detection          : Enable
  Aging  time(s)              : 500
  Quit-VLAN Recover time(m)   : --
  Exclude VLAN-list           : --
  Security level              : Middle
  Exclude BD-list             : --
-------------------------------------------------------------------------
```

#### Configuration Scripts

```
#
sysname DeviceA
#
mac-address flapping aging-time 500
#                                                                                
error-down auto-recovery cause mac-address-flapping interval 500 
#
interface 100GE1/0/1
 mac-address flapping trigger error-down    
#
interface 100GE1/0/2
 mac-address flapping trigger error-down    
#
return
```