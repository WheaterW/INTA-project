Example for Configuring ERPSv2
==============================

Example for Configuring ERPSv2

#### Networking Requirements

Redundant links are usually used on an Ethernet switched network to provide link backup and improve network reliability. The use of redundant links, however, may cause loops on the switched network, leading to broadcast storms and unstable MAC address entries. As a result, the communication quality deteriorates, and communication services may even be interrupted. ERPS can be configured on devices on a ring network to prevent loops caused by redundant links. As a Layer 2 loop prevention protocol defined by the ITU-T, ERPS provides fast convergence that can meet carrier-class reliability requirements. In addition to loop prevention, ERPSv2 supports functions including multi-ring networking and setting the revertive switching mode. It is applicable to more networking scenarios when improving network reliability.

In [Figure 1](#EN-US_TASK_0000001188455753__fig985443212816), DeviceA, DeviceB, DeviceC, and DeviceD constitute a major ring, and DeviceA, LSW1, LSW2, LSW3, and DeviceD constitute a sub-ring.

**Figure 1** ERPS multi-ring networking![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001188865361.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set the link type of all ports to be added to an ERPS ring to trunk.
2. Create ERPS rings and configure control VLANs and ERP instances.
3. Configure the ERPS version and configure an ERPS ring as a sub-ring.
4. Add Layer 2 ports to ERPS rings and configure port roles.
5. Configure the topology change notification and topology change protection functions.
6. Configure the Guard timer and WTR timer for ERPS rings.
7. Configure the Layer 2 forwarding function on DeviceA through DeviceD and LSW1 through LSW3.

#### Procedure

1. Set the link type of all ports to be added to an ERPS ring to trunk.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, DeviceD, LSW1, LSW2, and LSW3 are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA-100GE1/0/3] commit
   ```
2. Create ERPS ring 1 and ERPS ring 2 and configure ERP instances for the two rings. Set the control VLAN ID of ERPS ring 1 to 10 and the control VLAN ID of ERPS ring 2 to 20. Enable ERPS rings 1 and 2 to transmit data packets from VLANs 100 to 200.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, DeviceD, LSW1, LSW2, and LSW3 are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] stp region-configuration
   [*DeviceA-mst-region] instance 1 vlan 10 20 100 to 200
   [*DeviceA-mst-region] quit
   [*DeviceA] erps ring 1
   [*DeviceA-erps-ring1] control-vlan 10
   [*DeviceA-erps-ring1] protected-instance 1
   [*DeviceA-erps-ring1] quit
   [*DeviceA] erps ring 2
   [*DeviceA-erps-ring2] control-vlan 20
   [*DeviceA-erps-ring2] protected-instance 1
   [*DeviceA-erps-ring2] quit
   [*DeviceA-erps-ring2] commit
   ```
3. Configure ERPSv2 and configure ERPS ring 2 as a sub-ring.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, DeviceD, LSW1, LSW2, and LSW3 are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] erps ring 1
   [*DeviceA-erps-ring1] version v2
   [*DeviceA-erps-ring1] quit
   [*DeviceA] erps ring 2
   [*DeviceA-erps-ring2] version v2
   [*DeviceA-erps-ring2] sub-ring
   [*DeviceA-erps-ring2] quit
   [*DeviceA-erps-ring2] commit
   ```
4. Add Layer 2 ports to ERPS rings and configure port roles. Configure 100GE1/0/1 on DeviceB and 100GE1/0/2 on LSW3 as their respective RPL owner ports.
   
   
   
   # Configure DeviceA. The configurations of DeviceC, DeviceD, LSW1, and LSW2 are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] stp disable
   [*DeviceA-100GE1/0/1] erps ring 2
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] stp disable
   [*DeviceA-100GE1/0/2] erps ring 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] stp disable
   [*DeviceA-100GE1/0/3] erps ring 1
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA-100GE1/0/3] commit
   ```
   
   # Configure DeviceB. The configuration of LSW3 is similar to that of DeviceB. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] stp disable
   [*DeviceB-100GE1/0/1] erps ring 1 rpl owner
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] stp disable
   [*DeviceB-100GE1/0/2] erps ring 1
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB-100GE1/0/2] commit
   ```
5. Configure the topology change notification and topology change protection functions on interconnected nodes DeviceA and DeviceD.
   
   
   
   # Configure DeviceA. The configuration of DeviceD is similar to that of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] erps ring 1
   [*DeviceA-erps-ring1] tc-protection interval 200
   [*DeviceA-erps-ring1] tc-protection threshold 60
   [*DeviceA-erps-ring1] quit
   [*DeviceA] erps ring 2
   [*DeviceA-erps-ring2] tc-notify erps ring 1
   [*DeviceA-erps-ring2] quit
   [*DeviceA-erps-ring2] commit
   ```
6. Configure the Guard timer and WTR timer for ERPS rings.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, DeviceD, LSW1, LSW2, and LSW3 are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] erps ring 1
   [~DeviceA-erps-ring1] wtr-timer 6
   [*DeviceA-erps-ring1] guard-timer 100
   [*DeviceA-erps-ring1] quit
   [*DeviceA] erps ring 2
   [*DeviceA-erps-ring2] wtr-timer 6
   [*DeviceA-erps-ring2] guard-timer 100
   [*DeviceA-erps-ring2] quit
   [*DeviceA-erps-ring2] commit
   ```
7. Configure the Layer 2 forwarding function on DeviceA through DeviceD and LSW1 through LSW3.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, DeviceD, LSW1, LSW2, and LSW3 are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] vlan batch 100 to 200
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo port trunk allow-pass vlan 1
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 100 to 200
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo port trunk allow-pass vlan 1
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 100 to 200 
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] undo port trunk allow-pass vlan 1
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 100 to 200
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA-100GE1/0/3] commit
   ```
8. Verify the configuration.
   
   
   
   # After the network becomes stable, run the [**display erps**](cmdqueryname=display+erps) command to check brief information about the ERPS ring and ports added to the ERPS ring. The following example uses the command output on DeviceB.
   
   ```
   [~DeviceB] display erps
   D  : Discarding
   F  : Forwarding
   R  : RPL Owner
   N  : RPL Neighbour
   FS : Forced Device
   MS : Manual Device
   Total number of rings configured = 1
   Ring  Control  WTR Timer  Guard Timer  Port 1               Port 2
   ID    VLAN     (min)      (csec)
   --------------------------------------------------------------------------------
      1       10          6          100  (D,R)100GE1/0/1         (F)100GE1/0/2
   --------------------------------------------------------------------------------
   ```
   
   
   
   # Run the [**display erps verbose**](cmdqueryname=display+erps+verbose) command to check detailed information about the ERPS ring and ports added to the ERPS ring.
   
   ```
   [~DeviceB] display erps verbose
   Ring ID                             : 1
   Description                         : Ring 1
   Control Vlan                        : 10
   Protected Instance                  : 1 
   Service Vlan                        : 100 to 200
   WTR Timer Setting (min)             : 6      Running (s)           : 0  
   Guard Timer Setting (csec)          : 100    Running (csec)        : 0  
   Holdoff Timer Setting (deciseconds) : 0      Running (deciseconds) : 0  
   WTB Timer Running (csec)            : 0  
   Ring State                          : Idle
   RAPS_MEL                            : 7
   Revertive Mode                      : Revertive
   R-APS Channel Mode                  : -
   Version                             : 2
   Sub-ring                            : No 
   Forced Device Port                  : -
   Manual Device Port                  : -
   TC-Notify                           : -
   Time since last topology change     : 0 days 4h:12m:20s
    
   --------------------------------------------------------------------------------
   Port                Port Role     Port Status     Signal Status
   --------------------------------------------------------------------------------
   100GE1/0/1             RPL Owner     Discarding      Non-failed      
   100GE1/0/2             Common        Forwarding      Non-failed
   ```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 100 to 200
  #
  stp region-configuration
   instance 1 vlan 10 20 100 to 200
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   wtr-timer 6
   guard-timer 100
   version v2
   tc-protection interval 200
   tc-protection threshold 60
  erps ring 2
   control-vlan 20
   protected-instance 1
   wtr-timer 6
   guard-timer 100
   version v2
   sub-ring
   tc-notify erps ring 1
  #
  interface 100ge 1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 100 to 200
   stp disable
   erps ring 2
  #
  interface 100ge 1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1
  #
  interface 100ge 1/0/3
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 100 to 200
  #
  stp region-configuration
   instance 1 vlan 10 100 to 200
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   wtr-timer 6
   guard-timer 100
   version v2
  #
  interface 100ge 1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1 rpl owner
  #
  interface 100ge 1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 100 to 200
  #
  stp region-configuration
   instance 1 vlan 10 100 to 200
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   wtr-timer 6
   guard-timer 100
   version v2
  #
  interface 100ge 1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1
  #
  interface 100ge 1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  vlan batch 100 to 200
  #
  stp region-configuration
   instance 1 vlan 10 20 100 to 200
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   wtr-timer 6
   guard-timer 100
   version v2
   tc-protection interval 200
   tc-protection threshold 60
  erps ring 2
   control-vlan 20
   protected-instance 1
   wtr-timer 6
   guard-timer 100
   version v2
   sub-ring
   tc-notify erps ring 1
  #
  interface 100ge 1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 100 to 200
   stp disable
   erps ring 2
  #
  interface 100ge 1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1
  #
  interface 100ge 1/0/3
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 100 to 200
   stp disable
   erps ring 1
  #
  return
  ```
* LSW1
  
  ```
  #
  sysname LSW1
  #
  vlan batch 100 to 200
  #
  stp region-configuration
   instance 1 vlan 20 100 to 200
  #
  erps ring 2
   control-vlan 20
   protected-instance 1
   wtr-timer 6
   guard-timer 100
   version v2
   sub-ring
  #
  interface 100ge 1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 100 to 200
   stp disable
   erps ring 2
  #
  interface 100ge 1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 100 to 200
   stp disable
   erps ring 2
  #
  return
  ```
* LSW2
  
  ```
  #
  sysname LSW2
  #
  vlan batch 100 to 200
  #
  stp region-configuration
   instance 1 vlan 20 100 to 200
  #
  erps ring 2
   control-vlan 20
   protected-instance 1
   wtr-timer 6
   guard-timer 100
   version v2
   sub-ring
  #
  interface 100ge 1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 100 to 200
   stp disable
   erps ring 2
  #
  interface 100ge 1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 100 to 200
   stp disable
   erps ring 2
  #
  return
  ```
* LSW3
  
  ```
  #
  sysname LSW3
  #
  vlan batch 100 to 200
  #
  stp region-configuration
   instance 1 vlan 20 100 to 200
  #
  erps ring 2
   control-vlan 20
   protected-instance 1
   wtr-timer 6
   guard-timer 100
   version v2
   sub-ring
  #
  interface 100ge 1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 100 to 200
   stp disable
   erps ring 2
  #
  interface 100ge 1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 20 100 to 200
   stp disable
   erps ring 2 rpl owner
  #
  return
  ```