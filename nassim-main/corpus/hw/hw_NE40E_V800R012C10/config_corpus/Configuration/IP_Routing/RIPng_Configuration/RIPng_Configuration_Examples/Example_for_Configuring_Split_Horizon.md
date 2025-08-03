Example for Configuring Split Horizon
=====================================

This section describes how to configure split horizon to prevent routing loops.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365934__fig_dc_vrp_ripng_cfg_002801), IP addresses have been configured for interfaces on all Routers, RIPng has been configured on each Router, and RIPng services are running properly. Split horizon needs to be re-configured on DeviceA and DeviceC.

**Figure 1** Network diagram of split horizon![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and Interface 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_ripng_cfg_002801.png)

#### Precautions

During the configuration, note the following:

When the split horizon and poison reverse are configured together, only poison reverse takes effect.

To improve security, you are advised to deploy IPsec authentication for RIPng. For details, see Configuring IPsec Authentication for RIPng. The following uses IPSec authentication in a RIPng process as an example. For details, see Example for Configuring Basic RIPng Functions.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable split horizon.

#### Data Preparation

To complete the configuration, you need the following data:

* RIPng network segments of DeviceA: 2001:db8:3::1/96, 2001:db8:4::1/96, and 2001:db8:5::1/96
* RIPng network segments of DeviceB: 2001:db8:1::2/64 and 2001:db8:2::2/64
* RIPng network segments of DeviceC: 2001:db8:7::1/96, 2001:db8:8::1/96, and 2001:db8:9::1/96
* IPv6 address of each interface

#### Procedure

1. Configure split horizon.
   
   
   
   Configure split horizon on the RIPng interfaces of all Routers. The configuration of DeviceC is the same as the configuration of DeviceA and DeviceB, and is not mentioned here.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ripng split-horizon
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ripng split-horizon
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ripng split-horizon
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet0/1/3
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] ripng split-horizon
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceA] commit
   ```
2. Verify the configuration.
   
   
   
   # Run the [**display ripng 1 interface verbose**](cmdqueryname=display+ripng+1+interface+verbose) command on DeviceA and DeviceC to check the split horizon configuration. Use the command output on DeviceA as an example. If the displayed Split-Horizon field is Enabled, split horizon has been enabled.
   
   ```
   [~DeviceA] display ripng 1 interface verbose
   ```
   ```
    GigabitEthernet0/1/0
       FE80::A0A:200:1
       State : UP, Protocol : RIPNG, MTU : 1440
       Metricin : 0 , Metricout : 1
       Default Route : Disabled
       Poison Reverse : Disabled
       Split Horizon : Enabled  
    GigabitEthernet0/1/1(10.1.1.1)
       FE80::A0A:200:1
       State : UP, Protocol : RIPNG, MTU : 1440
       Metricin : 0 , Metricout : 1
       Default Route : Disabled
       Poison Reverse : Disabled
       Split Horizon : Enabled  
    GigabitEthernet0/1/2
       FE80::A0A:200:1
       State : UP, Protocol : RIPNG, MTU : 1440
       Metricin : 0 , Metricout : 1
       Default Route : Disabled
       Poison Reverse : Disabled
       Split Horizon : Enabled  
    GigabitEthernet0/1/3
       FE80::A0A:200:1
       State : UP, Protocol : RIPNG, MTU : 1440
       Metricin : 0 , Metricout : 1
       Default Route : Disabled
       Poison Reverse : Disabled
       Split Horizon : Enabled  
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1::1/64
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:3::1/96
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.2.1.1 255.255.0.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/3
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:5::1/96
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  ripng 1
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:1::2/64
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:2::2/64
  ```
  ```
   ripng 1 enable
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:2::1/64
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:7::1/96
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:8::1/96
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/3
  ```
  ```
   undo shutdown
  ```
  ```
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:9::1/96
  ```
  ```
   ripng 1 enable
  ```
  ```
  #
  ```
  ```
  ripng 1
  ```
  ```
  #
  ```
  ```
  return
  ```