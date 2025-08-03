Example for Configuring Split Horizon
=====================================

Example for Configuring Split Horizon

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001176744241__fig117811933131614), IP addresses are assigned to interfaces on all devices, RIPng is configured on each device, and RIPng services are running properly. Split horizon must be configured on DeviceA and DeviceC.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, and interface 4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


**Figure 1** Network diagram of configuring routing loop prevention  
![](figure/en-us_image_0000001130784604.png)

#### Precautions

During the configuration, note the following:

If both split horizon and poison reverse are configured, only poison reverse takes effect.


#### Configuration Roadmap

To complete the configuration, you need the following data:

* RIPng network segments of DeviceA: 2001:db8:3::1/96, 2001:db8:4::1/96, and 2001:db8:5::1/96
* RIPng network segments of DeviceB: 2001:db8:1::2/64 and 2001:db8:2::2/64
* RIPng network segments of DeviceC: 2001:db8:7::1/96, 2001:db8:8::1/96, and 2001:db8:9::1/96
* IPv6 address of each interface

#### Procedure

1. Assign an IPv6 address to each interface.
2. Configure split horizon.
   
   
   
   On all devices, configure split horizon on the interfaces running RIPng. The configurations of DeviceB and DeviceC are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge1/0/1
   [*DeviceA-100GE1/0/1] ripng split-horizon
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge1/0/2
   [*DeviceA-100GE1/0/2] ripng split-horizon
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge1/0/3
   [*DeviceA-100GE1/0/3] ripng split-horizon
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge1/0/4
   [*DeviceA-100GE1/0/4] ripng split-horizon
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the [**display ripng 1 interface verbose**](cmdqueryname=display+ripng+1+interface+verbose) command on DeviceA and DeviceC to check whether split horizon has been enabled. The following example uses the command output on DeviceA. If **Split-Horizon** is displayed as **Enabled**, split horizon has been enabled.

```
[~DeviceA] display ripng 1 interface verbose
 100GE1/0/1
    FE80::A0A:200:1
    State : UP, Protocol : RIPNG, MTU : 1440
    Metricin : 0 , Metricout : 1
    Default Route : Disabled
    Poison Reverse : Disabled
    Split Horizon : Enabled  
 
    FE80::A0A:200:1
    State : UP, Protocol : RIPNG, MTU : 1440
    Metricin : 0 , Metricout : 1
    Default Route : Disabled
    Poison Reverse : Disabled
    Split Horizon : Enabled  
 100GE1/0/3
    FE80::A0A:200:1
    State : UP, Protocol : RIPNG, MTU : 1440
    Metricin : 0 , Metricout : 1
    Default Route : Disabled
    Poison Reverse : Disabled
    Split Horizon : Enabled  
 100GE1/0/4
    FE80::A0A:200:1
    State : UP, Protocol : RIPNG, MTU : 1440
    Metricin : 0 , Metricout : 1
    Default Route : Disabled
    Poison Reverse : Disabled
    Split Horizon : Enabled 
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   ripng 1 enable
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/96
   ripng 1 enable
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::1/96
   ripng 1 enable
  #
  interface 100GE1/0/4
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:5::1/96
   ripng 1 enable
  #
  ripng 1
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   ripng 1 enable
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   ripng 1 enable
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   ripng 1 enable
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:7::1/96
   ripng 1 enable
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:8::1/96
   ripng 1 enable
  #
  interface 100GE1/0/4
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:9::1/96
   ripng 1 enable
  #
  ripng 1
  #
  return
  ```