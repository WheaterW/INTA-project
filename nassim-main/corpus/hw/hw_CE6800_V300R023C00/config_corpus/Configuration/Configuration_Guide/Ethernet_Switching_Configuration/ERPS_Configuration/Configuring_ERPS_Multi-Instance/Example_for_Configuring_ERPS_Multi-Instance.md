Example for Configuring ERPS Multi-Instance
===========================================

Example for Configuring ERPS Multi-Instance

#### Networking Requirements

On an ERPS network, a physical ring can be configured with only one ERPS ring and only one blocked port can be specified. When the ERPS ring is complete, the blocked port prevents all user packets from passing through. As a result, all user packets are transmitted over only one path on the ERPS ring, and the link on the other side of the blocked port becomes idle, wasting bandwidth resources.

In [Figure 1](#EN-US_TASK_0000001142718098__fig8777358165819), two ERPS instances, ERPS ring 1 and ERPS ring 2, are configured on DeviceA through DeviceD. P1 on DeviceB is a blocked port on ERPS ring 1, and P2 on DeviceA is a blocked port on ERPS ring 2, implementing load balancing and link backup.

**Figure 1** ERPS single-ring multi-instance networking![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001188758123.png)
#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set the link type of all ports to be added to an ERPS ring to trunk.
2. Create ERPS rings and configure control VLANs and ERP instances.
3. Add Layer 2 ports to ERPS rings and configure port roles.
4. Configure the Guard timer and WTR timer for ERPS rings.
5. Configure the Layer 2 forwarding function on DeviceA through DeviceD.

#### Procedure

1. Set the link type of all ports to be added to an ERPS ring to trunk.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [~HUAWEI] commit
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA-100GE1/0/2] commit
   ```
2. Create ERPS ring 1 and ERPS ring 2 and configure ERP instances for the two rings. Set the control VLAN ID of ERPS ring 1 to 10 and the control VLAN ID of ERPS ring 2 to 20. Enable ERPS ring 1 to transmit data packets from VLANs 100 to 200 and ERPS ring 2 to transmit data packets from VLANs 300 to 400.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] erps ring 1
   [*DeviceA-erps-ring1] control-vlan 10
   [*DeviceA-erps-ring1] protected-instance 1
   [*DeviceA-erps-ring1] quit
   [*DeviceA] stp region-configuration
   [*DeviceA-mst-region] instance 1 vlan 10 100 to 200
   [*DeviceA-mst-region] quit
   [*DeviceA] erps ring 2
   [*DeviceA-erps-ring2] control-vlan 20
   [*DeviceA-erps-ring2] protected-instance 2
   [*DeviceA-erps-ring2] quit
   [*DeviceA] stp region-configuration
   [*DeviceA-mst-region] instance 2 vlan 20 300 to 400
   [*DeviceA-mst-region] quit
   [*DeviceA-mst-region] commit
   ```
3. Add Layer 2 ports to ERPS rings and configure port roles. Configure 100GE1/0/1 on DeviceA and 100GE1/0/2 on DeviceB as their respective RPL owner ports.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] stp disable
   [*DeviceA-100GE1/0/1] erps ring 1
   [*DeviceA-100GE1/0/1] erps ring 2 rpl owner
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] stp disable
   [*DeviceA-100GE1/0/2] erps ring 1
   [*DeviceA-100GE1/0/2] erps ring 2
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   # Configure DeviceB.
   ```
   [~DeviceB] interface 100ge 1/0/1
   [*DeviceB-100GE1/0/1] stp disable
   [*DeviceB-100GE1/0/1] erps ring 1
   [*DeviceB-100GE1/0/1] erps ring 2
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] interface 100ge 1/0/2
   [*DeviceB-100GE1/0/2] stp disable
   [*DeviceB-100GE1/0/2] erps ring 1 rpl owner
   [*DeviceB-100GE1/0/2] erps ring 2
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] commit
   ```
   
   # Configure DeviceC. The configuration of DeviceD is similar to that of DeviceC. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceC] interface 100ge 1/0/1
   [*DeviceC-100GE1/0/1] stp disable
   [*DeviceC-100GE1/0/1] erps ring 1
   [*DeviceC-100GE1/0/1] erps ring 2
   [*DeviceC-100GE1/0/1] quit
   [*DeviceC] interface 100ge 1/0/2
   [*DeviceC-100GE1/0/2] stp disable
   [*DeviceC-100GE1/0/2] erps ring 1
   [*DeviceC-100GE1/0/2] erps ring 2
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] commit
   ```
4. Configure the Guard timer and WTR timer for ERPS rings.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] erps ring 1
   [~DeviceA-erps-ring1] wtr-timer 6
   [*DeviceA-erps-ring1] guard-timer 100
   [*DeviceA-erps-ring1] quit
   [*DeviceA] erps ring 2
   [*DeviceA-erps-ring2] wtr-timer 6
   [*DeviceA-erps-ring2] guard-timer 100
   [*DeviceA-erps-ring2] quit
   [*DeviceA] commit
   ```
5. Configure the Layer 2 forwarding function on DeviceA through DeviceD.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] vlan batch 100 to 200 300 to 400
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo port trunk allow-pass vlan 1
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 100 to 200 300 to 400
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo port trunk allow-pass vlan 1
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 100 to 200 300 to 400
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
6. Verify the configuration.
   
   
   
   # After the network becomes stable, run the [**display erps**](cmdqueryname=display+erps) command to check brief information about the ERPS ring and ports added to the ERPS ring. The following example uses the command output on DeviceB.
   
   ```
   [~DeviceB] display erps
   D : Discarding
   F : Forwarding
   R : RPL Owner
   N  : RPL Neighbour
   FS : Forced Device
   MS : Manual Device
   Total number of rings configured = 2
   Ring  Control  WTR Timer  Guard Timer  Port 1              Port 2
   ID    VLAN     (min)      (csec)
   --------------------------------------------------------------------------------
      1       10          6          100  (F)100GE1/0/1          (D,R)100GE1/0/2
      2       20          6          100  (F)100GE1/0/1          (F)100GE1/0/2
   --------------------------------------------------------------------------------
   
   ```
   
   # Run the [**display erps verbose**](cmdqueryname=display+erps+verbose) command to check detailed information about the ERPS ring and ports added to the ERPS ring. The following example uses the command output on DeviceB.
   
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
   Version                             : 1
   Sub-ring                            : No
   Forced Device Port                  : -
   Manual Device Port                  : -
   TC-Notify                           : -
   Time since last topology change     : 0 days 0h:35m:5s
    
   --------------------------------------------------------------------------------
   Port                Port Role     Port Status     Signal Status
   --------------------------------------------------------------------------------
   100GE1/0/1             Common        Forwarding      Non-failed
   100GE1/0/2             RPL Owner     Discarding      Non-failed
   
   Ring ID                             : 2
   Description                         : Ring 2
   Control Vlan                        : 20
   Protected Instance                  : 2
   Service Vlan                        : 300 to 400
   WTR Timer Setting (min)             : 6      Running (s)           : 0
   Guard Timer Setting (csec)          : 100    Running (csec)        : 0
   Holdoff Timer Setting (deciseconds) : 0      Running (deciseconds) : 0
   WTB Timer Running (csec)            : 0
   Ring State                          : Idle
   RAPS_MEL                            : 7
   Revertive Mode                      : Revertive
   R-APS Channel Mode                  : -
   Version                             : 1
   Sub-ring                            : No 
   Forced Device Port                  : -
   Manual Device Port                  : -
   TC-Notify                           : -
   Time since last topology change     : 0 days 0h:35m:30s
   --------------------------------------------------------------------------------
   Port                Port Role     Port Status     Signal Status
   --------------------------------------------------------------------------------
   100GE1/0/1             Common        Forwarding      Non-failed
   100GE1/0/2             Common        Forwarding      Non-failed
   ```

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  vlan batch 10 20 100 to 200 300 to 400
  #
  stp region-configuration
   instance 1 vlan 10 100 to 200
   instance 2 vlan 20 300 to 400
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   wtr-timer 6
   guard-timer 100
  erps ring 2
   control-vlan 20
   protected-instance 2
   wtr-timer 6
   guard-timer 100
  #
  interface 100ge 1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20 100 to 200 300 to 400
   stp disable
   erps ring 1
   erps ring 2 rpl owner
  #
  interface 100ge 1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20 100 to 200 300 to 400
   stp disable
   erps ring 1
   erps ring 2
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  vlan batch 10 20 100 to 200 300 to 400
  #
  stp region-configuration
   instance 1 vlan 10 100 to 200
   instance 2 vlan 20 300 to 400
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   wtr-timer 6
   guard-timer 100
  erps ring 2
   control-vlan 20
   protected-instance 2
   wtr-timer 6
   guard-timer 100
  #
  interface 100ge 1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20 100 to 200 300 to 400
   stp disable
   erps ring 1
   erps ring 2
  #
  interface 100ge 1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20 100 to 200 300 to 400
   stp disable
   erps ring 1 rpl owner
   erps ring 2
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  vlan batch 10 20 100 to 200 300 to 400
  #
  stp region-configuration
   instance 1 vlan 10 100 to 200
   instance 2 vlan 20 300 to 400
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   wtr-timer 6
   guard-timer 100
  erps ring 2
   control-vlan 20
   protected-instance 2
   wtr-timer 6
   guard-timer 100
  #
  interface 100ge 1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20 100 to 200 300 to 400
   stp disable
   erps ring 1
   erps ring 2
  #
  interface 100ge 1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20 100 to 200 300 to 400
   stp disable
   erps ring 1
   erps ring 2
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  vlan batch 10 20 100 to 200 300 to 400
  #
  stp region-configuration
   instance 1 vlan 10 100 to 200
   instance 2 vlan 20 300 to 400
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   wtr-timer 6
   guard-timer 100
  erps ring 2
   control-vlan 20
   protected-instance 2
   wtr-timer 6
   guard-timer 100
  #
  interface 100ge 1/0/1
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20 100 to 200 300 to 400
   stp disable
   erps ring 1
   erps ring 2
  #
  interface 100ge 1/0/2
   port link-type trunk
   undo port trunk allow-pass vlan 1
   port trunk allow-pass vlan 10 20 100 to 200 300 to 400
   stp disable
   erps ring 1
   erps ring 2
  #
  return
  ```