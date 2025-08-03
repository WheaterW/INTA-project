Example for Configuring Atom GNSS Timing
========================================

Example_for_Configuring_Atom_GNSS_Timing

#### Networking Requirements

On the IP RAN shown in [Figure 1](#EN-US_TASK_0000001778922026__fig_dc_ne_atom-gnss_cfg_901701), clock synchronization and time synchronization need to be performed between gNodeBs. In this case, you can deploy the Atom GNSS timing solution as follows: Insert an Atom GNSS module into an access aggregation node ASG. The Atom GNSS module functions as a lightweight BITS to provide GNSS access for the transport network. The Atom GNSS module can receive clock and time signals from the GNSS. The clock and time signals are converted into SyncE and 1588v2 signals, respectively, and then output to the ASG. The ASG transmits the clock/time signals to downstream devices which then transmit the signals to gNodeBs, achieving network-wide clock and time synchronization.

**Figure 1** Atom GNSS timing  
![](figure/en-us_image_0000001778922046.png)

#### Configuration Roadmap

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section describes Atom GNSS timing configuration only on ASGs. For details about how to configure SyncE to implement clock synchronization for downstream devices of ASGs, see [Clock Synchronization Configuration](dc_ne_clock_cfg_0001.html). For details about how to configure 1588v2 to implement time synchronization for downstream devices of ASGs, see [1588v2 Configuration](dc_ne_1588v2_cfg_5000.html).

The configuration roadmap is as follows:

1. Configure SyncE.
2. Configure time synchronization.

#### Data Preparation

To complete the configuration, you need the following data:

* Information about the optical interface to which the Atom GNSS module is inserted
* Priority of the clock source

#### Procedure

1. Configure SyncE on ASG1 and ASG2.
   
   
   
   ASG1 configuration is similar to ASG2 configuration. ASG1 configuration is used as an example.
   
   1. Configure SyncE on the Atom GNSS module.![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The SyncE function has been enabled on the Atom GNSS module by default, with no need for manual configuration.
   2. Configure SyncE on ASG1 where the Atom GNSS module resides.
      
      # Configure clock source selection based on SSM levels.
      ```
      <ASG1> system-view
      ```
      ```
      [~ASG1] clock ssm-control on
      ```
      ```
      [*ASG1] commit
      ```
      
      # Enable SyncE and configure priorities for interfaces.
      ```
      [~ASG1] interface gigabitethernet 0/1/0
      ```
      ```
      [~ASG1-GigabitEthernet0/1/0] clock synchronization enable
      ```
      ```
      [*ASG1-GigabitEthernet0/1/0] clock priority 10
      ```
      ```
      [*ASG1-GigabitEthernet0/1/0] commit
      ```
      ```
      [~ASG1-GigabitEthernet0/1/0] quit
      ```
2. Configure time synchronization on ASG1 and ASG2.
   
   
   
   ASG1 configuration is similar to ASG2 configuration. ASG1 configuration is used as an example.
   
   1. Configure time synchronization on the Atom GNSS module.
      ```
      [~ASG1] interface gigabitethernet 0/1/0
      ```
      ```
      [~ASG1-GigabitEthernet0/1/0] smart clock gnss-model gps glonass
      ```
      ```
      [*ASG1-GigabitEthernet0/1/0] smart-clock cable-delay 60
      ```
      ```
      [*ASG1-GigabitEthernet0/1/0] commit
      ```
      ```
      [~ASG1-GigabitEthernet0/1/0] quit
      ```
   2. Configure time synchronization on ASG1 where the Atom GNSS module resides.
      
      # Configure 1588v2 globally.
      ```
      [*ASG1] ptp enable
      ```
      ```
      [*ASG1] ptp device-type bc
      ```
      ```
      [*ASG1] commit
      ```
      
      # Configure 1588v2 on the involved interface.
      ```
      [~ASG1] interface gigabitethernet 0/1/0
      ```
      ```
      [*ASG1-GigabitEthernet0/1/0] ptp enable
      ```
      ```
      [*ASG1-GigabitEthernet0/1/0] commit
      ```
      ```
      [~ASG1-GigabitEthernet0/1/0] quit
      ```
3. Verify the configuration.
   
   
   
   Run the [**display clock source**](cmdqueryname=display+clock+source) command to check the status information about all clock sources or the clock source being tracked.
   
   ```
   <HUAWEI> display clock source
    System trace source State:   lock mode
                                 into pull-in range
    Current system trace source: GE0/1/0
    Current 2M-1 trace source:   system PLL
    Frequency lock success:      yes
   
    Master board
    Source        Pri(sys/2m-1)   In-SSM     Out-SSM    State      Ref
    --------------------------------------------------------------------------
    GE0/1/0         10 /---         prc        dnu       normal     yes
    GE0/2/0         ---/---         dnu        prc       initial    no
    
   ```
   
   Run the **display ptp all** command to check whether BITS information has been successfully input.
   
   ```
   <HUAWEI> display ptp all
   Device config info
     ------------------------------------------------------------------------------
     PTP state         :enabled              Domain  value      :0
     Slave only        :no                   Device type        :BC
     Set port state    :no                   Local clock ID     :0aa1c6fffe699700
     Acl               :no                   Virtual clock ID   :no
     Acr               :no                   Time lock success  :yes
     Asymmetry measure :disable              Passive measure    :enabled
     Send GM WTR       :no
   
     BMC run info
     ------------------------------------------------------------------------------
     Grand clock ID    :0a05d7fffe341500               
     Receive number    :GigabitEthernet0/1/0           
     Parent clock ID   :0a05d7fffe341500               
     Parent portnumber :35585                          
     Priority1         :128                 Priority2           :128               
     Step removed      :0                   Clock accuracy      :0x21              
     Clock class       :6                   Time Source         :0x20              
     UTC Offset        :37                  UTC Offset Valid    :True             
     Timescale         :PTP                 Time traceable      :True          
     Leap              :None                Frequency traceable :True          
     Offset scaled     :0xffff              Sync uncertain      :False           
   
     Port info
     Name                        State        Delay-mech Ann-timeout Type   Domain 
     ------------------------------------------------------------------------------
     GigabitEthernet0/1/0        slave        delay      3           BC     0
   
     Time Performance Statistics(ns): Slot X  Card X  Port X  
     ------------------------------------------------------------------------------
     Realtime(T2-T1)   :8                Pathdelay     :0 
     Max(T2-T1)        :8
     Min(T2-T1)        :2
   
     Clock source info
     Clock     Pri1 Pri2 Accuracy Class TimeSrc  Signal Switch Direction In-Status
     ------------------------------------------------------------------------------
     local     128  128  0x31     187   0xa0     -      -      -         -
     bits1/11  128  128  0x20     6     0x20     1pps   off    in/-      abnormal
     bits1/12  128  128  0x20     6     0x20     1pps   off    in/-      abnormal
   ```

#### Configuration Files

* ASG1 configuration file
  
  ```
  #
  sysname ASG1
  #
  clock ssm-control on
  #
  ptp enable
  ptp device-type bc
  #
  interface gigabitEthernet 0/1/0 
   clock synchronization enable 
   clock priority 10
   smart clock gnss-model gps glonass
   smart-clock cable-delay 60
   ptp enable
  #
  return
  ```
* ASG2 configuration file
  
  ```
  #
  sysname ASG2
  #
  clock ssm-control on
  #
  ptp enable
  ptp device-type bc
  #
  interface gigabitEthernet 0/1/0 
   clock synchronization enable 
   clock priority 10
   smart clock gnss-model gps glonass
   smart-clock cable-delay 60
   ptp enable
  #
  return
  ```