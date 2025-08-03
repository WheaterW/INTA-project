Example for Configuring Clock Synchronization on a Ring Network
===============================================================

Example for Configuring Clock Synchronization on a Ring Network

#### Networking Requirements

[Figure 1](#EN-US_TASK_0000001825840949__fig_dc_ne_clock_cfg_501501) shows a ring network. To ensure the reliability of the entire clock synchronization network, DeviceA and DeviceC are connected to external BITSs to import clock signals. During network deployment, each device automatically selects a clock source based on the clock signals transmitted from DeviceA and DeviceC.

**Figure 1** Network diagram of configuring clock synchronization on a ring network![](../../../../public_sys-resources/note_3.0-en-us.png) 

The configuration in this example is performed on DeviceA, DeviceB, DeviceC, and DeviceD.

In this example, interface1 and interface2 represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001778921638.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a clock synchronization mode and enable the devices to select clock sources based on SSM levels.
2. Configure clock sources.

#### Data Preparation

To complete the configuration, plan the clock source priority of each Router, as listed in [Table 1](#EN-US_TASK_0000001825840949__tab_dc_ne_clock_cfg_501501).

**Table 1** Clock source priority of each Router
| Router | Clock Source in Use | Priority |
| --- | --- | --- |
| DeviceA | BITS0 | 10 |
| GE0/1/0 | 20 |
| GE0/2/0 | - |
| DeviceB | GE0/1/0 | 10 |
| GE0/2/0 | 20 |
| DeviceC | BITS0 | 10 |
| GE0/1/0 | - |
| GE0/2/0 | 30 |
| DeviceD | GE0/1/0 | 10 |
| GE0/2/0 | 20 |


#### Procedure

1. Enable the devices to select clock sources based on SSM levels.
   
   
   
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
   [~DeviceA] clock ssm-control on
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure other devices by using the same method for configuring DeviceA.
2. Configure clock sources.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] clock bits-type bits0 2mbps
   ```
   ```
   [*DeviceA] clock source bits0 synchronization enable
   ```
   ```
   [*DeviceA] clock source bits0 priority 10
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] clock synchronization enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] clock priority 20
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] clock synchronization enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] clock synchronization enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] clock priority 10
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] clock synchronization enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] clock priority 20
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] commit
   ```
   
   # Configure DeviceD by using the same method for configuring DeviceB.
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] clock bits-type bits0 2mbps
   ```
   ```
   [*DeviceC] clock source bits0 synchronization enable
   ```
   ```
   [*DeviceC] clock source bits0 priority 10
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] clock synchronization enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] clock synchronization enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] clock priority 30
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
3. Verify the configuration.
   
   
   
   Run the [**display clock source**](cmdqueryname=display+clock+source) command on DeviceA, DeviceB, DeviceC, and DeviceD to check the clock synchronization configurations and clock source information.
   
   # Verify the configuration on DeviceA.
   
   ```
   <DeviceA> display clock source
   System trace source State:    lock mode
                                 into pull-in range
    Current system trace source: bits0
    Current 2M-1 trace source:   system PLL
    Frequency lock success:      yes
   
    Master board
    Source        Pri(sys/2m-1)   In-SSM     Out-SSM    State      Ref-Source
    --------------------------------------------------------------------------
    bits0     10/---          prc        --        normal     yes
    GE0/1/0         20/---          dnu        prc       normal     yes
    GE0/2/0         ---/---         prc        prc       normal     yes
    
   ```
   
   # Verify the configuration on DeviceB.
   
   ```
   <DeviceB> display clock source
   System trace source State:    lock mode
                                 into pull-in range
    Current system trace source: GigabitEthernet0/1/0
    Current 2M-1 trace source:   system PLL
    Frequency lock success:      yes
   
    Master board
    Source        Pri(sys/2m-1)   In-SSM     Out-SSM    State      Ref-Source
    --------------------------------------------------------------------------
    GE0/1/0          10/---         prc        dnu       normal     yes
    GE0/2/0          20/---         dnu        prc       normal     yes
    
   ```
   
   # Verify the configuration on DeviceC.
   
   ```
   <DeviceC> display clock source
   System trace source State:    lock mode
                                 into pull-in range
    Current system trace source: GigabitEthernet0/2/0
    Current 2M-1 trace source:   system PLL
    Frequency lock success:      yes
   
    Master board
    Source        Pri(sys/2m-1)   In-SSM     Out-SSM    State      Ref-Source
    --------------------------------------------------------------------------
    bits0     10/---         ssub        --        normal     yes
    GE0/1/0         ---/---        dnu         prc       normal     yes
    GE0/2/0         30/---         prc         dnu       normal     yes
    
   ```
   
   # Verify the configuration on DeviceD.
   
   ```
   <DeviceD> display clock source
   System trace source State:    lock mode
                                 into pull-in range
    Current system trace source: GigabitEthernet0/1/0
    Current 2M-1 trace source:   system PLL
    Frequency lock success:      yes
   
    Master board
    Source        Pri(sys/2m-1)   In-SSM     Out-SSM    State      Ref-Source
    --------------------------------------------------------------------------
    GE0/1/0          10/---         prc        dnu       normal     yes
    GE0/2/0          20/---         prc        prc       normal      yes
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceA
  ```
  ```
  #
  ```
  ```
  clock ssm-control on
  ```
  ```
  clock bits-type bits0 2mbps 
  ```
  ```
  clock source bits0 synchronization enable 
  ```
  ```
  clock source bits0 priority 10 
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   clock synchronization enable
  ```
  ```
   clock priority 20
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   clock synchronization enable
  ```
  ```
  #
  ```
  ```
  return 
  ```
* DeviceB configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  clock ssm-control on
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   clock synchronization enable
  ```
  ```
   clock priority 10
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   clock synchronization enable
  ```
  ```
   clock priority 20
  ```
  ```
  #
  ```
  ```
  return 
  ```
* DeviceC configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  ```
  ```
  clock ssm-control on
  ```
  ```
  clock bits-type bits0 2mbps 
  ```
  ```
  clock source bits0 synchronization enable 
  ```
  ```
  clock source bits0 priority 10 
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   clock synchronization enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   clock synchronization enable
  ```
  ```
   clock priority 30
  ```
  ```
  #
  ```
  ```
  return 
  ```
* DeviceD configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
  ```
  ```
  #
  ```
  ```
  clock ssm-control on
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   clock synchronization enable
  ```
  ```
   clock priority 10
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   clock synchronization enable
  ```
  ```
   clock priority 20
  ```
  ```
  #
  ```
  ```
  return 
  ```