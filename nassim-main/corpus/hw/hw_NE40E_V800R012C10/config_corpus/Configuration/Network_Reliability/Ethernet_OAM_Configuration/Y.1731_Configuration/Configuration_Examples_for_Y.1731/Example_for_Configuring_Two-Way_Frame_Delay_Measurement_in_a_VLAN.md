Example for Configuring Two-Way Frame Delay Measurement in a VLAN
=================================================================

This example describes how to configure two-way frame delay measurement in a virtual local area network (VLAN) on an E2E network.

#### Networking Requirements

As networks continue to develop and diversify, various value-added services such as IPTV, video conferencing, and Voice over Internet Protocol (VoIP) are becoming increasingly popular. The performance monitoring function can be used to check the performance of links that transmit services.

On the network shown in [Figure 1](#EN-US_TASK_0172362175__fig_dc_vrp_cfg_01154301), CFM is configured to monitor the connectivity of links between CEs. To provide high-quality video services, a carrier expects to monitor the bidirectional delay on mobile transport links in real time while monitoring link connectivity so that they can promptly respond to video service quality deterioration.

**Figure 1** Networking diagram for configuring Y.1731 function on a VLAN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example are GE 0/1/1, GE 0/1/2 respectively.


  
![](images/fig_dc_vrp_cfg_01154001.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure on-demand two-way frame delay measurement between CEs.
2. Configure proactive two-way frame delay measurement between CEs.


#### Data Preparation

To complete the configuration, you need the following data:

* ID of a VLAN to which CE interfaces belong
* Names of the MD and MA on CE1 and CE2
* Interval between DMMs and number of detection times in on-demand OAM mode

#### Procedure

1. Configure on-demand two-way frame delay measurement for links between CEs.
   
   
   1. Configure basic Ethernet CFM functions, including outward-facing MEPs.
      
      On each CE, configure IEEE Std 802.1ag-2007 CFM, create an MD named **md3** and an MA named **ma3**, and bind the MA to a VLAN.
      
      # Configure CE1.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname CE1
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~CE1] vlan 2
      ```
      ```
      [~CE1] interface gigabitethernet0/1/1
      ```
      ```
      [~CE1-GigabitEthernet0/1/1] portswitch
      ```
      ```
      [*CE1-GigabitEthernet0/1/1] port link-type trunk
      ```
      ```
      [*CE1-GigabitEthernet0/1/1] port trunk allow-pass vlan 2
      ```
      ```
      [*CE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*CE1] cfm enable
      ```
      ```
      [*CE1] cfm md md3
      ```
      ```
      [*CE1-md-md3] ma ma3
      ```
      ```
      [*CE1-md-md3-ma-ma3] map vlan 2
      ```
      ```
      [*CE1-md-md3-ma-ma3] mep mep-id 3 interface gigabitethernet0/1/1 outward
      ```
      ```
      [*CE1-md-md3-ma-ma3] mep ccm-send mep-id 3 enable
      ```
      ```
      [*CE1-md-md3-ma-ma3] remote-mep mep-id 4
      ```
      ```
      [*CE1-md-md3-ma-ma3] remote-mep ccm-receive mep-id 4 enable
      ```
      ```
      [*CE1-md-md3-ma-ma3] test-id 1 mep 3 remote-mep 4
      ```
      ```
      [*CE1] commit
      ```
      
      # Configure CE2.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~HUAWEI] sysname CE2
      ```
      ```
      [*HUAWEI] commit
      ```
      ```
      [~CE2] vlan 2
      ```
      ```
      [~CE2] interface gigabitethernet0/1/1
      ```
      ```
      [~CE2-GigabitEthernet0/1/1]portswitch
      ```
      ```
      [~CE2-GigabitEthernet0/1/1]port link-type trunk
      ```
      ```
      [*CE2-GigabitEthernet0/1/1]port trunk allow-pass vlan 2
      ```
      ```
      [*CE2-GigabitEthernet0/1/1]quit
      ```
      ```
      [*CE2] cfm enable
      ```
      ```
      [*CE2] cfm md md3
      ```
      ```
      [*CE2-md-md3] ma ma3
      ```
      ```
      [*CE2-md-md3-ma-ma3] map vlan 2
      ```
      ```
      [*CE2-md-md3-ma-ma3] mep mep-id 4 interface gigabitethernet0/1/1 outward
      ```
      ```
      [*CE2-md-md3-ma-ma3] mep ccm-send mep-id 4 enable
      ```
      ```
      [*CE2-md-md3-ma-ma3] remote-mep mep-id 3
      ```
      ```
      [*CE2-md-md3-ma-ma3] remote-mep ccm-receive mep-id 3 enable
      ```
      ```
      [*CE2-md-md3-ma-ma3] test-id 1 mep 4
      ```
      ```
      [*CE2] commit
      ```
   2. Enable CE2 to receive DMMs.
      
      # Configure CE2.
      
      ```
      [~CE2] cfm md md3
      ```
      ```
      [*CE2-md-md3] ma ma3
      ```
      ```
      [*CE2-md-md3-ma-ma3] delay-measure two-way receive test-id 1
      ```
      ```
      [*CE2-md-md3-ma-ma3] quit
      ```
      ```
      [*CE2-md-md3] quit
      ```
      ```
      [*CE2] commit
      ```
   3. Enable on-demand two-way frame delay measurement.
      
      # Configure CE1.
      
      ```
      [~CE1] cfm md md3
      ```
      ```
      [*CE1-md-md3] ma ma3
      ```
      ```
      [*CE1-md-md3-ma-ma3] delay-measure two-way send test-id 1 interval 1000 count 20
      ```
      ```
      [*CE1-md-md3-ma-ma3] quit
      ```
      ```
      [*CE1-md-md3] quit
      ```
      ```
      [*CE1] commit
      ```
   4. Verify the configuration.
      
      # After completing the configuration, run the **display y1731 statistic-type twoway-delay** command to view actual on-demand two-way frame delay measurements on CE1.
      
      ```
      <CE1> display y1731 statistic-type twoway-delay
      Latest two-way delay statistics of test-id 1:
      --------------------------------------------------------------------------------
      Index    Delay(usec)    Delay variation(usec)
      --------------------------------------------------------------------------------
          1            422                        -
          2            320                      102
          3            467                      147
          4            309                      158
          5            328                       19
          6            316                       12
          7            336                       20
          8            282                       54
          9            421                      139
         10            287                      134
         11            322                       35
         12            446                      124
         13            275                      171
         14            291                       16
         15            341                       50
      --------------------------------------------------------------------------------
      Average delay(usec) :        344    Average delay variation(usec) :         84
      Maximum delay(usec) :        467    Maximum delay variation(usec) :        171
      Minimum delay(usec) :        275    Minimum delay variation(usec) :         12
      
      ```
2. Configure proactive two-way frame delay measurement for links between CEs.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Proactive two-way frame delay measurement within a specified VLAN allows you to collect link measurement statistics continuously over a long term.
   
   1. Disable CE2 from receiving DMMs.
      
      # Configure CE2.
      
      ```
      [~CE2] cfm md md3
      ```
      ```
      [*CE2-md-md3] ma ma3
      ```
      ```
      [*CE2-md-md3-ma-ma3] test-id 2 mep 4 remote-mep 3
      ```
      ```
      [*CE2-md-md3-ma-ma3] quit
      ```
      ```
      [*CE2-md-md3] quit
      ```
      ```
      [*CE2] commit
      ```
   2. Enable CE1 to receive DM messages.
      
      # Configure CE1.
      
      ```
      [~CE1] cfm md md3
      ```
      ```
      [*CE1-md-md3] ma ma3
      ```
      ```
      [*CE1-md-md3] test-id 2 mep 3
      ```
      ```
      [*CE1-md-md3-ma-ma3] delay-measure two-way receive test-id 2
      ```
      ```
      [*CE1-md-md3-ma-ma3] quit
      ```
      ```
      [*CE1-md-md3] quit
      ```
      ```
      [*CE1] commit
      ```
   3. Enable proactive two-way frame delay measurement.
      
      # Configure CE2.
      
      ```
      [~CE2] cfm md md3
      ```
      ```
      [*CE2-md-md3] ma ma3
      ```
      ```
      [*CE2-md-md3-ma-ma3] delay-measure two-way continual send test-id 2 interval 1000
      ```
      ```
      [*CE2-md-md3-ma-ma3] quit
      ```
      ```
      [*CE2-md-md3] quit
      ```
      ```
      [*CE2] commit
      ```
   4. Verify the configuration.
      
      # After completing the configuration, run the **display y1731 statistic-type twoway-delay** command to view statistics about two-way frame delay measurements on CE1.
      
      ```
      <CE1> display y1731 statistic-type twoway-delay
      Latest two-way delay statistics of test-id 2:
      --------------------------------------------------------------------------------
      Index    Delay(usec)    Delay variation(usec)
      --------------------------------------------------------------------------------
          1            181                        -
          2            356                      175
          3            166                      190
          4            180                       14
          5            162                       18
          6            160                        2
          7            177                       17
          8            149                       28
          9            190                       41
         10            185                        5
         11            230                       45
         12            221                        9
         13            184                       37
         14            415                      231
         15            187                      228
         16            235                       48
         17            184                       51
         18            184                        0
         19            168                       16
         20            185                       17
      --------------------------------------------------------------------------------
      Average delay(usec) :         204    Average delay variation(usec) :         61
      Maximum delay(usec) :         415    Maximum delay variation(usec) :        231
      Minimum delay(usec) :         149    Minimum delay variation(usec) :          0
      
      
      ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
   sysname CE1
  #
   vlan batch 2
  #
   cfm version standard
   cfm enable
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
  #
   cfm md md3
    ma ma3
     map vlan 2
     mep mep-id 3 interface GigabitEthernet0/1/1 outward
     mep ccm-send mep-id 3 enable
     remote-mep mep-id 4
     remote-mep ccm-receive mep-id 4 enable
     test-id 1 mep 3 remote-mep 4
     test-id 2 mep 3
     delay-measure two-way receive test-id 2
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
   sysname CE2
  #
   vlan 2
  #
   cfm version standard
   cfm enable
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 2
  #
   cfm md md3
    ma ma3
     map vlan 2
     mep mep-id 4 interface GigabitEthernet0/1/1 outward
     mep ccm-send mep-id 4 enable
     remote-mep mep-id 3
     remote-mep ccm-receive mep-id 3 enable
     test-id 1 mep 4
     delay-measure two-way receive test-id 1
     test-id 2 mep 4 remote-mep 3
     delay-measure two-way continual send test-id 2 interval 1000
  #
  return
  ```