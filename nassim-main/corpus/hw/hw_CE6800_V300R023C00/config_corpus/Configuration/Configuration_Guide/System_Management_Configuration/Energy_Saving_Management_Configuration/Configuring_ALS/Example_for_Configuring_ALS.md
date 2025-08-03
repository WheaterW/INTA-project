Example for Configuring ALS
===========================

Example for Configuring ALS

#### Networking Requirements

If an optical fiber link is faulty, to save energy, the lasers on the optical modules are required to automatically stop emitting pulses and only resume after the link recovers.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


**Figure 1** Networking diagram for configuring ALS  
![](figure/en-us_image_0000001512688742.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable ALS on the interfaces so that the lasers automatically stop emitting pulses if a link is faulty.
2. Set the restart mode of the lasers to the automatic restart mode so that the lasers resume emitting pulses after the link recovers.

#### Procedure

1. Configure ALS on the interfaces and set a restart mode of the lasers.# Enable ALS on 100GE1/0/1 of DeviceA and set the restart mode of the laser to **automatic**.
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname DeviceA 
   [*HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1 
   [~DeviceA-100GE1/0/1] als enable 
   [*DeviceA-100GE1/0/1] als restart mode automatic 
   [*DeviceA-100GE1/0/1] commit
   [~DeviceA-100GE1/0/1] quit
   ```
   
   # Enable ALS on 100GE1/0/1 of DeviceB and set the restart mode of the laser to **automatic**.
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname DeviceB 
   [*HUAWEI] commit
   [~DeviceB] interface 100ge 1/0/1 
   [~DeviceB-100GE1/0/1] als enable 
   [*DeviceB-100GE1/0/1] als restart mode automatic 
   [*DeviceB-100GE1/0/1] commit
   [*DeviceB-100GE1/0/1] quit
   ```

#### Verifying the Configuration

* Check the ALS configuration on the interface of DeviceA.
  ```
  <DeviceA> display als interface 100ge 1/0/1 
  -------------------------------------------------------------------------------------- 
  Interface          ALS Status   Laser Status   Restart Mode   Interval(s)   Width(s) 
  -------------------------------------------------------------------------------------- 
  100GE1/0/1          Enable       On             Auto           100           2    
  -------------------------------------------------------------------------------------- 
  ```
* Check the ALS configuration on the interface of DeviceB.
  ```
  <DeviceB> display als interface 100ge 1/0/1 
  -------------------------------------------------------------------------------------- 
  Interface          ALS Status   Laser Status   Restart Mode   Interval(s)   Width(s) 
  -------------------------------------------------------------------------------------- 
  100GE1/0/1          Enable       On             Auto           100           2    
  --------------------------------------------------------------------------------------
  ```

#### Configuration Scripts

* DeviceA
  ```
  # 
  sysname DeviceA 
  # 
  interface 100GE1/0/1  
   als enable 
  # 
  return  
  ```
* DeviceB
  ```
  # 
  sysname DeviceB 
  # 
  interface 100GE1/0/1  
   als enable 
  # 
  return  
  ```