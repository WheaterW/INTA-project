Example for Configuring Layer 2-to-Layer 3 Mode Switching on Ethernet Interfaces
================================================================================

Example for Configuring Layer 2-to-Layer 3 Mode Switching on Ethernet Interfaces

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001606889297__fig_dc_cfg_int_005701), PC1, PC2, PC3, and PC4 each are on a different network segment, and DeviceB, DeviceC, DeviceD, and DeviceE are access devices for the four network segments, respectively. It is required that four physical Ethernet interfaces on DeviceA be configured as gateway interfaces for the four network segments.

**Figure 1** Network diagram of configuring Layer 2/Layer 3 mode switching![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001556210158.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

* Switch the interface working mode to Layer 3.
* Configure the IP addresses of Layer 3 Ethernet interfaces as gateway addresses.


#### Procedure

1. Switch the interface working mode to Layer 3.
   
   
   * Switch a single interface to Layer 3 mode.
     ```
     <HUAWEI> system-view
     [HUAWEI] sysname DeviceA
     [DeviceA] interface 100ge 1/0/1
     [DeviceA-100GE1/0/1] undo portswitch
     [DeviceA-100GE1/0/1] quit
     ```
   
   
   * Switch Ethernet interfaces to Layer 3 mode in batches.
     ```
     [DeviceA] undo portswitch batch 100ge 1/0/2 to 1/0/4
     ```
2. Configure the IP addresses of Layer 3 Ethernet interfaces as gateway addresses.
   
   
   
   # Configure the IP address of 100GE1/0/1 as a gateway address. The configurations of 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4 are similar to the configuration of 100GE1/0/1. For details, see Configuration Scripts.
   
   ```
   [DeviceA] interface 100ge 1/0/1
   [DeviceA-100GE1/0/1] ip address 10.10.1.1 24
   [DeviceA-100GE1/0/1] quit
   ```

#### Verifying the Configuration

Run the **display interface 100GE 1/0/1** command in any view to check the current working mode of the interface.

```
[DeviceA] display interface 100ge 1/0/1
...
Description:
Route Port,The Maximum Frame Length is 9216
Internet Address is 10.10.1.1/24
...
```

If **Switch Port** is displayed, the interface works in Layer 2 mode. If **Route Port** is displayed, the interface works in Layer 3 mode. The preceding command output shows that the interface works in Layer 3 mode.


#### Configuring Scripts

```
#
sysname DeviceA
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.10.1.1 255.255.255.0
#
interface 100GE1/0/2
 undo portswitch
 ip address 10.10.2.1 255.255.255.0
#
interface 100GE1/0/3
 undo portswitch
 ip address 10.10.3.1 255.255.255.0
#
interface 100GE1/0/4
 undo portswitch
 ip address 10.10.4.1 255.255.255.0
#
return
```