Example for Configuring Synchronous Ethernet on a Ring Network
==============================================================

Example for Configuring Synchronous Ethernet on a Ring Network

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513039850__fig1495210207529), network devices are connected over a ring clock synchronization network. To ensure reliability of the clock synchronization network, DeviceA and DeviceC are each connected to an external clock source to import clock signals. During network deployment, all devices preferentially synchronize with the line clock signals transmitted from DeviceA. If the external clock source connected to DeviceA becomes faulty, the entire network switches to synchronize with the line clock signals transmitted from DeviceC.

To enable the devices to synchronize with the highest-quality clock signals, enable clock source selection based on SSM quality levels on each device.

**Figure 1** Network diagram of configuring SyncE![](public_sys-resources/note_3.0-en-us.png) 

In this figure, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001513039906.png)
#### Configuration Roadmap

1. Configure a clock source.
2. Configure the automatic clock source selection mode, and enable clock source selection based on SSM quality levels.


#### Procedure

1. Configure a clock source.
   
   # Configure DeviceA.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface 100GE 1/0/1
   ```
   ```
   [~DeviceA-100GE1/0/1] clock synchronization enable
   ```
   ```
   [*DeviceA-100GE1/0/1] clock priority 2
   ```
   ```
   [*DeviceA-100GE1/0/1] commit
   ```
   ```
   [~DeviceA-100GE1/0/1] quit
   ```
   ```
   [~DeviceA] interface 100GE 1/0/2
   ```
   ```
   [~DeviceA-100GE1/0/2] clock synchronization enable
   ```
   ```
   [*DeviceA-100GE1/0/2] commit
   ```
   ```
   [~DeviceA-100GE1/0/2] quit
   ```
   ```
   [~DeviceA] interface 100GE 1/0/3
   ```
   ```
   [~DeviceA-100GE1/0/3] clock synchronization enable
   ```
   ```
   [~DeviceA-100GE1/0/3] clock ssm ssua
   ```
   ```
   [*DeviceA-100GE1/0/3] clock priority 1
   ```
   ```
   [*DeviceA-100GE1/0/3] commit
   ```
   ```
   [~DeviceA-100GE1/0/3] quit
   ```
   
   # Configure DeviceB. The configuration of DeviceD is similar to the configuration of DeviceB. For detailed configurations, see Configuration Scripts.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface 100GE 1/0/1
   ```
   ```
   [~DeviceB-100GE1/0/1] clock synchronization enable
   ```
   ```
   [*DeviceB-100GE1/0/1] clock priority 1
   ```
   ```
   [*DeviceB-100GE1/0/1] commit
   ```
   ```
   [~DeviceB-100GE1/0/1] quit
   ```
   ```
   [~DeviceB] interface 100GE 1/0/2
   ```
   ```
   [~DeviceB-100GE1/0/2] clock synchronization enable
   ```
   ```
   [*DeviceB-100GE1/0/2] clock priority 2
   ```
   ```
   [*DeviceB-100GE1/0/2] commit
   ```
   ```
   [~DeviceB-100GE1/0/2] quit
   ```
   
   # Configure DeviceC.
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceC
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceC] interface 100GE 1/0/1
   ```
   ```
   [~DeviceC-100GE1/0/1] clock synchronization enable
   ```
   ```
   [*DeviceC-100GE1/0/1] commit
   ```
   ```
   [~DeviceC-100GE1/0/1] quit
   ```
   ```
   [~DeviceC] interface 100GE 1/0/2
   ```
   ```
   [~DeviceC-100GE1/0/2] clock synchronization enable
   ```
   ```
   [*DeviceC-100GE1/0/2] clock priority 3
   ```
   ```
   [*DeviceC-100GE1/0/2] commit
   ```
   ```
   [~DeviceC-100GE1/0/2] quit
   ```
   ```
   [~DeviceC] interface 100GE 1/0/3
   ```
   ```
   [~DeviceC-100GE1/0/3] clock synchronization enable
   ```
   ```
   [*DeviceC-100GE1/0/3] clock ssm ssub
   ```
   ```
   [*DeviceC-100GE1/0/3] clock priority 1
   ```
   ```
   [*DeviceC-100GE1/0/3] commit
   ```
   ```
   [~DeviceC-100GE1/0/3] quit
   ```
2. Configure the automatic clock source selection mode, and enable clock source selection based on SSM quality levels.
   
   
   
   # Configure DeviceA. The configurations of other devices are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] clock clear         //If manual or forcible clock source selection has been performed, run this command to restore the automatic clock source selection mode. Otherwise, skip this step.
   ```
   ```
   [~DeviceA] clock ssm-control on
   ```
   ```
   [*DeviceA] clock run-mode normal
   ```
   ```
   [*DeviceA] commit
   ```
3. Verify the configuration.
   
   
   
   Run the [**display clock source**](cmdqueryname=display+clock+source) command on DeviceA, DeviceB, DeviceC, and DeviceD to check information about the clock source they each synchronize with.
   
   # Check the clock source information on DeviceA.
   
   ```
   [~DeviceA] display clock source
     System trace source State:   lock mode            
                                  into pull-in range   
     Current system trace source: 100GE1/0/3            
     Frequency lock success:      yes                  
   
     Master board
     Source        Pri(sys)   In-SSM   Out-SSM   State          Ref-Source
     ------------------------------------------------------------------------------
     100GE1/0/1     2          dnu      ssua      normal         yes
     100GE1/0/3     1          ssua     --        normal         yes
   ```
   
   # Check the clock source information on DeviceB.
   
   ```
   [~DeviceB] display clock source
     System trace source State:   lock mode            
                                  into pull-in range   
     Current system trace source: 100GE1/0/1            
     Frequency lock success:      yes                  
   
     Master board
     Source        Pri(sys)   In-SSM   Out-SSM   State          Ref-Source
     ------------------------------------------------------------------------------
     100GE1/0/1     1          ssua     dnu       normal         yes
     100GE1/0/2     2          dnu      ssua      normal         yes
   ```
   
   # Check the clock source information on DeviceC.
   
   ```
   [~DeviceC] display clock source
     System trace source State:   lock mode            
                                  into pull-in range   
     Current system trace source: 100GE1/0/2            
     Frequency lock success:      yes                  
   
     Master board
     Source        Pri(sys)   In-SSM   Out-SSM   State          Ref-Source
     ------------------------------------------------------------------------------
     100GE1/0/1     ---        dnu      ssua      normal         no 
     100GE1/0/2     3          ssua     dnu       normal         yes
     100GE1/0/3     1          ssub     ssua      normal         yes
   ```
   
   # Check the clock source information on DeviceD.
   
   ```
   [~DeviceD] display clock source
     System trace source State:   lock mode            
                                  into pull-in range   
     Current system trace source: 100GE1/0/1            
     Frequency lock success:      yes                  
   
     Master board
     Source        Pri(sys)   In-SSM   Out-SSM   State          Ref-Source
     ------------------------------------------------------------------------------
     100GE1/0/1     1          ssua     dnu       normal         yes
     100GE1/0/2     2          dnu      ssua      normal         yes
   ```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  clock ssm-control on
  #
  interface 100GE1/0/1
   clock synchronization enable
   clock priority 2
  #
  interface 100GE1/0/2
   clock synchronization enable
  #
  interface 100GE1/0/3
   clock synchronization enable 
   clock priority 1
   clock ssm ssua
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  clock ssm-control on
  #
  interface 100GE1/0/1
   clock synchronization enable
   clock priority 1
  #
  interface 100GE1/0/2
   clock synchronization enable
   clock priority 2
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  clock ssm-control on
  #
  interface 100GE1/0/1
   clock synchronization enable
  #
  interface 100GE1/0/2
   clock synchronization enable
   clock priority 3
  interface 100GE1/0/3
   clock synchronization enable 
   clock priority 1 
   clock ssm ssub
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  clock ssm-control on
  #
  interface 100GE1/0/1
   clock synchronization enable
   clock priority 1
  #
  interface 100GE1/0/2
   clock synchronization enable
   clock priority 2
  #
  return
  ```