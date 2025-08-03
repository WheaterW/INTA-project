Example for Configuring ERPSv1
==============================

Example for Configuring ERPSv1

#### Networking Requirements

Redundant links are usually used on an Ethernet switched network to provide link backup and improve network reliability. The use of redundant links, however, may cause loops on the switched network, leading to broadcast storms and unstable MAC address entries. As a result, the communication quality deteriorates, and communication services may even be interrupted. ERPS can be configured on devices on a ring network to prevent loops caused by redundant links. As a Layer 2 loop prevention protocol defined by the ITU-T, ERPS provides fast convergence that can meet carrier-class reliability requirements.

In [Figure 1](#EN-US_TASK_0000001188671261__fig7895317249), DeviceA, DeviceB, DeviceC, and DeviceD constitute an ERPS ring.

**Figure 1** ERPS single-ring networking![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE1/0/1 and 100GE1/0/2, respectively.


  
![](figure/en-us_image_0000001142631330.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set the link type of all ports to be added to an ERPS ring to trunk.
2. Create an ERPS ring and configure a control VLAN and an ERP instance.
3. Add Layer 2 ports to the ERPS ring and configure port roles.
4. Configure the Guard timer and WTR timer for the ERPS ring.
5. Configure the Layer 2 forwarding function on DeviceA through DeviceD.

#### Procedure

1. Set the link type of all ports to be added to an ERPS ring to trunk.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA-100GE1/0/2] commit
   ```
2. Create ERPS ring 1 and configure an ERP instance. Set the control VLAN ID of the ERPS ring to 10 and configure ERPS ring 1 to transmit data packets from VLANs 100 to 200.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] stp region-configuration
   [*DeviceA-mst-region] instance 1 vlan 10 100 to 200
   [*DeviceA-mst-region] quit
   [*DeviceA] erps ring 1
   [*DeviceA-erps-ring1] control-vlan 10
   [*DeviceA-erps-ring1] protected-instance 1
   [*DeviceA-erps-ring1] quit
   [*DeviceA-erps-ring1] commit
   ```
3. Add Layer 2 ports to the ERPS ring and configure port roles. Configure 100GE1/0/1 on DeviceB as the RPL owner port.
   
   
   
   # Configure DeviceA. The configurations of DeviceC and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] stp disable
   [*DeviceA-100GE1/0/1] erps ring 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] stp disable
   [*DeviceA-100GE1/0/2] erps ring 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA-100GE1/0/2] commit
   ```
   
   # Configure DeviceB.
   
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
4. Configure the Guard timer and WTR timer for the ERPS ring.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] erps ring 1
   [*DeviceA-erps-ring1] wtr-timer 6
   [*DeviceA-erps-ring1] guard-timer 100
   [*DeviceA-erps-ring1] quit
   [*DeviceA-erps-ring1] commit
   ```
5. Configure the Layer 2 forwarding function on DeviceA through DeviceD.
   
   
   
   # Configure DeviceA. The configurations of DeviceB, DeviceC, and DeviceD are similar to the configuration of DeviceA. For detailed configurations, see Configuration Scripts.
   
   ```
   [~DeviceA] vlan batch 100 to 200
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] undo port trunk allow-pass vlan 1
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 100 to 200
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] undo port trunk allow-pass vlan 1
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 100 to 200 
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA-100GE1/0/2] commit
   ```
6. Verify the configuration.
   
   
   
   # After the network becomes stable, run the [**display erps**](cmdqueryname=display+erps) command to check brief information about the ERPS ring and ports added to the ERPS ring. The following example uses the command output on DeviceB.
   
   ```
   [~DeviceB] display erps
   D  : Discarding
   F  : Forwarding
   R  : RPL Owner
   N  : RPL Neighbour
   FS : Forced 
   MS : Manual Switch
   Total number of rings configured = 1
   Ring  Control  WTR Timer  Guard Timer  Port 1               Port 2
   ID    VLAN     (min)      (csec)
   --------------------------------------------------------------------------------
      1       10          6          100  (D,R)100GE1/0/1         (F)100GE1/0/2
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
   Forced Switch Port                  : -
   Manual Switch Port                  : -
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
   instance 1 vlan 10 100 to 200
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   wtr-timer 6
   guard-timer 100
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
   erps ring 1 rpl owner
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
   instance 1 vlan 10 100 to 200
  #
  erps ring 1
   control-vlan 10
   protected-instance 1
   wtr-timer 6
   guard-timer 100
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