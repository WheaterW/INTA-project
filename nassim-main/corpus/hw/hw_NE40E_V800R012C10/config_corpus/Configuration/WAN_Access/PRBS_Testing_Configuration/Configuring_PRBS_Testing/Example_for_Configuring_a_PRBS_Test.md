Example for Configuring a PRBS Test
===================================

This section provides an example on how to configure a PRBS test to check device connectivity when two devices are connected to each other through E1 interfaces.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172364447__fig_dc_vrp_mp_cfg_000701), Device A and Device B connect to each other through E1 interfaces. A PRBS test needs to be performed to check the connectivity between the two devices.

**Figure 1** Networking diagram for configuring a PRBS test![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent E1 0/1/0 and E1 0/2/0, respectively.


  
![](images/fig_dc_ne_prbs_cfg_000701.png "Click to enlarge")  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a synchronous serial interface on Device A and Device B.
2. Configure remote loopback on the E1 interface of Device B.
3. Perform a PRBS test on Device A.
4. Check the PRBS test result on Device A.
5. After the PRBS test is completed, cancel the remote loopback configuration on the E1 interface of Device B.


#### Data Preparation

To complete the configuration, you need the following data:

* E1 interface number of Device A
* E1 interface number of Device B

#### Procedure

1. Create a synchronous serial interface on Device A and Device B.
   
   
   
   # Configure the E1 interface on Device A as a synchronous serial interface.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] controller e1 0/1/0
   [~DeviceA-E1 0/1/0] channel-set 1 timeslot-list 1-31
   [*DeviceA-E1 0/1/0] commit
   [~DeviceA-E1 0/1/0] quit
   ```
   
   
   
   # Configure the E1 interface on Device B as a synchronous serial interface.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] controller e1 0/2/0
   [~DeviceB-E1 0/2/0] channel-set 1 timeslot-list 1-31
   [*DeviceB-E1 0/2/0] commit
   [~DeviceB-E1 0/2/0] quit
   ```
2. Configure remote loopback on the E1 interface of Device B.
   
   
   ```
   [~DeviceB] controller e1 0/2/0
   [~DeviceB-E1 0/2/0] loopback remote
   [*DeviceB-E1 0/2/0] commit
   [~DeviceB-E1 0/2/0] quit
   ```
3. Perform a PRBS test on Device A.
   
   
   ```
   [~DeviceA] interface serial 0/1/0:1
   [~DeviceA-Serial0/1/0:1] link-protocol tdm
   [*DeviceA-Serial0/1/0:1] commit
   [~DeviceA-Serial0/1/0:1] quit
   [~DeviceA] test connectivity interface Serial0/1/0:1 uni-direction pattern prbs15 interval second 20 interval-repeat 5
   ```
4. Check the PRBS test result on Device A.
   
   
   ```
   [~DeviceA] display connectivity-test interface serial 0/1/0:1
   Summary:
   Start time           Side  Pattern  Phy-port   Total time (Interval*Round)
   2018-08-10 16:12:46  UNI   PRBS15   E1 0/1/0   00:01:40 (20s*5)
   Total bits     Error bits     BER   LOS      Test progress
   198400000      0              0e-0  0s       100%(00:01:40)finished
   Details:
   Round  Total bits   Error bits   BER   LOS     ES      EFS     SES     UAS
   1      39680000     0            0e-0  0s      0s      20s     0s      0s
   2      39680000     0            0e-0  0s      0s      20s     0s      0s
   3      39680000     0            0e-0  0s      0s      20s     0s      0s
   4      39680000     0            0e-0  0s      0s      20s     0s      0s
   5      39680000     0            0e-0  0s      0s      20s     0s      0s
   Error Bits Insert Record (Latest 10):
   Start time           Type        BER   Duration  Insert in round
   
   ```
5. After the PRBS test is completed, cancel the remote loopback configuration on the E1 interface of Device B.
   
   
   ```
   [~DeviceB] controller e1 0/2/0
   [~DeviceB-E1 0/2/0] undo loopback
   [*DeviceB-E1 0/2/0] commit
   [~DeviceB-E1 0/2/0] quit
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  controller E1 0/1/0
   channel-set 1 timeslot-list 1-31
  #
  interface Serial0/1/0:1
   link-protocol tdm
  #
   test connectivity interface Serial0/1/0:1 uni-direction pattern prbs15 interval second 20 interval-repeat 5
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  controller E1 0/2/0
   channel-set 1 timeslot-list 1-31
   loopback remote
   undo loopback
  #
  return
  ```