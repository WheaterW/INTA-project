Example for Configuring EFM OAM
===============================

This configuration example describes basic applications of EFM OAM.

#### Networking Requirements

To ensure the reliability and stability of connections between a user network and a carrier network and to improve link manageability and maintainability, configure EFM OAM for link detection, fault detection, and packet loss ratio testing. In addition, associate EFM OAM with an interface to perform link switchovers when a fault occurs.

**Figure 1** EFM OAM![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/1 and GE 0/2/1, respectively.


  
![](images/fig_dc_vrp_efm_cfg_202801.png)  


#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure EFM OAM on the CE, PE1, and PE2, and configure an interface on the CE to work in passive mode.
2. Configure remote loopback on PE1 to test the packet loss ratio before the link is used.
3. Configure link monitoring on PE1.
4. Associate EFM OAM with an interface on the CE.


#### Data Preparation

To complete the configuration, you need the following data:

* Interval at which errored frames are checked on GE 0/2/1 on PEs and threshold for the number of detected errored frames
* Interval at which errored codes are checked on GE 0/2/1 on PEs and threshold for the number of detected errored codes
* Interval at which errored frame seconds are checked on GE 0/2/1 on PEs and threshold for the number of detected errored frame seconds


#### Procedure

1. Configure basic EFM OAM functions.
   
   
   
   # Enable EFM OAM globally on the CE.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE
   ```
   ```
   [*HUAWEI] commit 
   ```
   ```
   [~CE] efm enable
   ```
   ```
   [*CE] commit
   ```
   
   # Enable EFM OAM globally on PE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit 
   ```
   ```
   [~PE1] efm enable
   ```
   ```
   [*PE1] commit
   ```
   
   # Enable EFM OAM globally on PE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] efm enable
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure GE 0/1/1 on the CE to work in passive mode.
   
   ```
   [~CE] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE-GigabitEthernet0/1/1] efm mode passive
   ```
   ```
   [*CE-GigabitEthernet0/1/1] commit
   ```
   
   # Enable EFM OAM on GE 0/1/1 on the CE.
   
   ```
   [~CE-GigabitEthernet0/1/1] efm enable
   ```
   ```
   [*CE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE] commit
   ```
   
   # Enable EFM OAM on GE 0/2/1 on the CE.
   
   ```
   [~CE] interface gigabitethernet 0/2/1
   ```
   ```
   [~CE-GigabitEthernet0/2/1] efm enable
   ```
   ```
   [*CE-GigabitEthernet0/2/1] quit
   ```
   ```
   [*CE] commit
   ```
   
   # Enable EFM OAM on GE 0/2/1 on PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/2/1
   ```
   ```
   [~PE1-GigabitEthernet0/2/1] efm enable
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Enable EFM OAM on GE 0/2/1 on PE2.
   
   ```
   [~PE2] interface gigabitethernet 0/2/1
   ```
   ```
   [~PE2-GigabitEthernet0/2/1] efm enable
   ```
   ```
   [*PE2-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Verify the configuration.
   
   If EFM OAM configurations on PE1 and the CE are correct, GE 0/1/1 and GE 0/2/1 enter the Detect state after EFM session negotiation succeeds. Run the [**display efm session**](cmdqueryname=display+efm+session) { **all** | **interface** *interface-type* *interface-num* } command on the CE or PE1. The command output shows that the EFM OAM status of GE 0/1/1 or GE 0/2/1 is **detect**. The following example uses the command output on the CE.
   
   ```
   [~CE] display efm session all
   ```
   ```
     Interface                 EFM State                   Loopback Timeout
     ----------------------------------------------------------------------
     GigabitEthernet0/1/1           detect                      --
     GigabitEthernet0/2/1           detect                      --
   ```
2. Configure remote loopback.
   
   
   
   # Configure remote loopback on PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/2/1
   ```
   ```
   [~PE1-GigabitEthernet0/2/1] efm loopback start
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] quit
   ```
   
   Verify the configuration.
   
   After remote loopback is configured, run the [**display efm session**](cmdqueryname=display+efm+session) { **all** | **interface** *interface-type* *interface-num* } command on PE1. The command output shows that the EFM OAM status of GE 0/2/1 is **Loopback(control)**, which indicates that GE 0/2/1 initiates remote loopback.
   
   ```
   [~PE1] display efm session interface gigabitethernet 0/2/1
   ```
   ```
     Interface                 EFM State                   Loopback Timeout
     ----------------------------------------------------------------------
     GigabitEthernet0/2/1           loopback (control)          19
   ```
   
   After remote loopback is configured, run the [**display efm session**](cmdqueryname=display+efm+session) { **all** | **interface** *interface-type* *interface-num* } command on the CE. The command output shows that the EFM OAM status of GE 0/1/1 is **Loopback(be controlled)**, which indicates that GE 0/1/1 responds to remote loopback.
   
   ```
     Interface                 EFM State                   Loopback Timeout
     ----------------------------------------------------------------------
     Gigabitethernet0/1/1           loopback (be controlled)    --
   ```
3. Configure PE1 to send testing packets to the CE.
   
   
   ```
   [~PE1] test-packet start interface gigabitethernet 0/2/1
   ```
4. Check statistics about testing packets on PE1.
   
   
   ```
   [~PE1] display test-packet result
   ```
   ```
    TestResult         Value
   --------------------------------------------------------
     PacketsSend    :   5
     PacketsReceive :   5
     PacketsLost    :   0
     BytesSend      :   320
     BytesReceive   :   320
     BytesLost      :   0
     StartTime      :   Feb  8 2014 16:08:00
     EndTime        :   Feb  8 2014 16:08:00    
   ```
   
   Based on the preceding data, you can calculate the packet loss ratio of the link.
5. Disable remote loopback.
   
   
   ```
   [~PE1] interface gigabitethernet 0/2/1
   ```
   ```
   [~PE1-GigabitEthernet0/2/1] efm loopback stop
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To disable remote loopback before a timeout period elapses, perform this step.
6. Verify the configuration.
   
   
   
   After remote loopback is disabled, run the [**display efm session**](cmdqueryname=display+efm+session) { **all** | **interface** *interface-type* *interface-num* } command on PE1 or the CE. The command output shows that the EFM OAM status of interfaces at both ends of the link is **Detect** or **Discovery**. That is, the two interfaces are in the Detect or Discovery state. For example:
   
   ```
   [*PE1] display efm session interface gigabitethernet0/2/1
   ```
   
   If remote loopback detects that the link works properly, perform the following configurations to monitor link connectivity and faults in real time.
7. Configure GE 0/2/1 on PE1 to check errored codes, errored frames, and errored frame seconds.
   
   
   
   # Configure GE 0/2/1 on PE1 to check errored frames.
   
   ```
   [~PE1] interface gigabitethernet 0/2/1
   ```
   ```
   [~PE1-GigabitEthernet0/2/1] efm error-frame period 5
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] efm error-frame threshold 5
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] efm error-frame notification enable
   ```
   
   # Configure GE 0/2/1 on PE1 to check errored codes.
   
   ```
   [*PE1-GigabitEthernet0/2/1] efm error-code period 5
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] efm error-code threshold 5
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] efm error-code notification enable
   ```
   
   # Configure GE 0/2/1 on PE1 to check errored frame seconds.
   
   ```
   [*PE1-GigabitEthernet0/2/1] efm error-frame-second period 120
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] efm error-frame-second threshold 5
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] efm error-frame-second notification enable
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] quit
   ```
   ```
   [*PE1] commit
   ```
8. Verify the configuration.
   
   
   
   After the configurations are complete, GE 0/1/1 on the CE and GE 0/2/1 on PE1 enter the Detect state after EFM session negotiation succeeds. Run the [**display efm session**](cmdqueryname=display+efm+session) { **all** | **interface** *interface-type* *interface-num* } command on the CE or PE1. The command output shows that the EFM OAM status of GE 0/1/1 or GE 0/2/1 is **detect**.
   
   The following example uses the command output on the CE.
   
   ```
   [~CE] display efm session interface gigabitethernet 0/1/1
   ```
   ```
     Interface                 EFM State                   Loopback Timeout
     ----------------------------------------------------------------------
     GigabitEthernet0/1/1           detect                      --
     GigabitEthernet0/2/1           detect                      --
   ```
   
   Run the [**display efm**](cmdqueryname=display+efm) { **all** | **interface** *interface-type* *interface-number* } command on PE1 to view EFM OAM configurations.
   
   ```
   [~PE1] display efm interface gigabitethernet 0/2/1
   ```
   ```
     Item                           Value
     ----------------------------------------------------
     Interface:                     GigabitEthernet0/2/1
     EFM Enable Flag:               enable  
     Mode:                          active
     Loopback IgnoreRequest:        no
     OAMPDU MaxSize:                128
     OAMPDU Interval:               1000
     OAMPDU Timeout:                5000
     ErrCodeNotification:           enable
     ErrCodePeriod:                 5
     ErrCodeThreshold:              5
     ErrFrameNotification:          enable
     ErrFramePeriod:                5
     ErrFrameThreshold:             5
     ErrFrameSecondNotification:    enable
     ErrFrameSecondPeriod:          120
     ErrFrameSecondThreshold:       5
     Hold Up Time:                  0 
     TriggerIfDown:                 disable
     TriggerMacRenew:               disable
     Remote MAC:                    --
     Remote EFM Enable Flag:        --
     Remote Mode:                   --
     Remote MaxSize:                --
     Remote Loopback IgnoreRequest: --
     Remote Parser:                 --
     Remote Multiplexer:            --  ErrFramePeriodNotification:    disable
     ErrFramePeriodPeriod:          200000
     ErrFramePeriodThreshold:       1
   ```
9. Associate EFM OAM with an interface on the CE.
   
   
   ```
   [~CE] interface gigabitethernet 0/1/1
   ```
   ```
   [~CE-GigabitEthernet0/1/1] efm trigger if-down
   ```
   ```
   [*CE-GigabitEthernet0/1/1] efm holdup-timer 20
   ```
   ```
   [*CE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE] commit
   ```
10. Verify the configuration.
    
    
    
    After the configuration is complete, run the [**display efm**](cmdqueryname=display+efm) { **all** | **interface** *interface-type* *interface-number* command on the CE. The command output shows that **TriggerIfDown** is **enable**.
    
    ```
    [~CE] display efm all
    ```
    ```
      Item                           Value
      ----------------------------------------------------
      Interface:                     GigabitEthernet0/1/1
      EFM Enable Flag:               enable  
      Mode:                          passive
      OAMPDU MaxSize:                128
      OAMPDU Interval:               1000
      OAMPDU Timeout:                5000
      ErrCodeNotification:           disable
      ErrCodePeriod:                 1
      ErrCodeThreshold:              1
      ErrFrameNotification:          disable
      ErrFramePeriod:                1
      ErrFrameThreshold:             1
      ErrFrameSecondNotification:    disable
      ErrFrameSecondPeriod:          60
      ErrFrameSecondThreshold:       1
      Hold Up Time:                  20
      TriggerIfDown:                 enable
      Remote MAC:                    00e0-fc12-7880
      Remote EFM Enable Flag:        enable
      Remote Mode:                   active
      Remote MaxSize:                128
      Remote Loopback IgnoreRequest: --
      Remote Parser:                 --
      Remote Multiplexer:            --
      ----------------------------------------------------
      Interface:                     GigabitEthernet0/2/1
      EFM Enable Flag:               enable  
      Mode:                          active
      OAMPDU MaxSize:                128
      OAMPDU Interval:               1000
      OAMPDU Timeout:                5000
      ErrCodeNotification:           disable
      ErrCodePeriod:                 1
      ErrCodeThreshold:              1
      ErrFrameNotification:          disable
      ErrFramePeriod:                1
      ErrFrameThreshold:             1
      ErrFrameSecondNotification:    disable
      ErrFrameSecondPeriod:          60
      ErrFrameSecondThreshold:       1
      Hold Up Time:                  20
      TriggerIfDown:                 enable
      Remote MAC:                    00e0-fc12-7890
      Remote EFM Enable Flag:        enable
      Remote Mode:                   active
      Remote MaxSize:                128
      Remote Loopback IgnoreRequest: --
      Remote Parser:                 --
      Remote Multiplexer:            --
    ```

#### Configuration Files

* CE configuration file
  
  ```
  #
  ```
  ```
  sysname CE
  ```
  ```
  #
  efm enable
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   efm enable
   efm mode passive
   efm trigger if-down
   efm holdup-timer 20
  #
  interface Gigabitethernet0/2/1
   undo shutdown
   efm enable
   efm trigger if-down
   efm holdup-timer 20
  #
  ```
  ```
  return
  ```
* PE1 configuration file
  
  ```
  #
  ```
  ```
  sysname PE1
  ```
  ```
  #
  ```
  ```
  efm enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/1
  ```
  ```
   undo shutdown
  ```
  ```
   efm enable
  ```
  ```
   efm loopback start
  ```
  ```
   test-packet start interface gigabitethernet 0/2/1
  ```
  ```
   efm loopback stop
  ```
  ```
   efm error-frame period 5
  ```
  ```
   efm error-frame threshold 5
  ```
  ```
   efm error-frame notification enable
  ```
  ```
   efm error-frame-second period 120
  ```
  ```
   efm error-frame-second threshold 5
  ```
  ```
   efm error-frame-second notification enable
  ```
  ```
   efm error-code period 5
  ```
  ```
   efm error-code threshold 5
  ```
  ```
   efm error-code notification enable
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE2 configuration file
  
  ```
  #
  ```
  ```
  sysname PE2
  ```
  ```
  #
  ```
  ```
  efm enable
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/1
  ```
  ```
   undo shutdown
  ```
  ```
   efm enable
  ```
  ```
  #
  ```
  ```
  return
  ```