Example for Configuring Basic LLDP Functions
============================================

This section provides an example to describe how to configure basic LLDP functions to help the NMS obtain information about network topology.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000002107746089__fig103091844183012), DeviceA and DeviceB are directly connected, the NMS has reachable routes to DeviceA and DeviceB, and SNMP is configured on the devices and NMS.

A network administrator wants to obtain link communication information between DeviceA and DeviceB, and alarms of device function changes to learn details about the network topology and configuration conflicts.

**Figure 1** Figure Networking diagram for configuring basic LLDP functions  
![](figure/en-us_image_0000002108334053.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, each LLDP interface represents GigabitEthernet 0/1/1.



#### Configuration Roadmap

To obtain the link communication information between DeviceA and DeviceB from the NMS, configure LLDP on the devices. The configuration roadmap is as follows:

1. Enable LLDP globally on DeviceA and DeviceB.
2. Configure management IP addresses for DeviceA and DeviceB.


#### Procedure

1. Configure IP addresses and routing protocols for interfaces, as shown in [Figure 1](#EN-US_TASK_0000002107746089__fig103091844183012). For details, see Configuration Scripts.
2. Enable LLDP globally on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] lldp enable
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] lldp enable
   ```
   ```
   [*DeviceB] commit
   ```
3. Configure management IP addresses for DeviceA and DeviceB.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The IP address specified in the [**lldp management-address**](cmdqueryname=lldp+management-address) command is the IP address of the LLDP interface. For details about how to configure an IP address for an LLDP interface, see Configuration Scripts.
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] lldp management-address 10.10.10.1
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] lldp management-address 10.10.10.2
   ```
   ```
   [*DeviceB] commit
   ```
4. (Optional) Configure LLDP parameters for DeviceA and DeviceB. These parameters include the interval and delay for sending LLDP packets.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] lldp message-transmission interval 60
   ```
   ```
   [*DeviceA] lldp message-transmission delay 9
   ```
   ```
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to that of DeviceA. For details, see Configuration Scripts.
5. (Optional) Enable the LLDP trap function for DeviceA and DeviceB and configure a delay for the devices to send LLDP traps.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] snmp-agent trap enable feature-name lldp
   ```
   ```
   [*DeviceA] lldp trap-interval 10
   ```
   ```
   [*DeviceA] commit
   ```
   
   The configuration of DeviceB is similar to that of DeviceA. For details, see Configuration Scripts.
6. Verify the configuration.
   
   
   
   # Check whether the LLDP function is enabled, whether an LLDP management address is configured, whether the LLDP alarm function is enabled, and whether values of LLDP attributes are the same as values configured for DeviceA.
   
   * Display the local LLDP information of DeviceA.
     ```
     <DeviceA> display lldp local
     System information
     --------------------------------------------------------------------------
     Chassis type                       :macAddress
     Chassis ID                         :00e0-fc21-1220
     System name                        :DeviceA                        
     System description                 :Huawei Versatile Routing Platform Software
     VRP (R) software, Version 8.230 (NE40E V800R023C00SPC500)
     Copyright (C) 2012-2023 Huawei Technologies Co., Ltd.
     HUAWEI NE40E-M2K
     
     System capabilities supported      :bridge router
     System capabilities enabled        :bridge router
     LLDP Up time                       :2022/02/26 15:08:28
     
     System configuration
     --------------------------------------------------------------------------
     LLDP Status                        :enabled              (default is disabled)         
     LLDP Message Tx Interval           :60                   (default is 30s)              
     LLDP Message Tx Hold Multiplier    :4                   (default is 4)                
     LLDP Refresh Delay                 :2                   (default is 2s)               
     LLDP Tx Delay                      :9                   (default is 2s)               
     LLDP Notification Interval         :10                  (default is 5s)               
     LLDP Notification Enable           :enabled             (default is disabled)
     Management Address                 :ipv4: 10.10.10.1                               
     LLDP Fast Message Count            :4                   (default is 4)               
     Remote Table Statistics:
     --------------------------------------------------------------------------
     Remote Table Last Change Time      :0 days,0 hours, 11 minutes,49 seconds
     Remote Neighbors Added             :0
     Remote Neighbors Deleted           :0
     Remote Neighbors Dropped           :0
     Remote Neighbors Aged              :0
     Total Neighbors                    :2
     
     Port information:
     --------------------------------------------------------------------------
     Interface Gigabitethernet 0/1/1:
     LLDP Enable Status                 :txAndRx             (default is disabled)         
     Total Neighbors                    :2
     
     Port ID subtype                    :interfaceName
     Port ID                            :Gigabitethernet 0/1/1                 
     Port description                   :
     
     Port and Protocol VLAN ID(PPVID)   :unsupported 
     Port VLAN ID(PVID)                 :0
     VLAN name of VLAN                  :--
     Protocol identity                  :
     Auto-negotiation supported         :Yes
     Auto-negotiation enabled           :No
     OperMau                            :speed (10000) /duplex (Full)
     Link aggregation supported         :Yes
     Link aggregation enabled           :No
     Aggregation port ID                :0
     Maximum frame Size                 :9216
     ```
   * Display the LLDP information about neighbors connected to DeviceA.
     ```
     <DeviceA> display lldp neighbor interface gigabitethernet 0/1/1
     GigabitEthernet 0/1/1 has 1 neighbor(s):
     
     Neighbor index                     :1
     Chassis type                       :macAddress
     Chassis ID                         :00e0-fc11-1220                
     Port ID type                       :interfaceName
     Port ID                            :GigabitEthernet 0/1/1                               
     Port description                   :--
     System name                        :DeviceB                     
     System description                 :Huawei Versatile Routing Platform Software
     VRP (R) software, Version 8.230 (NE40E V800R023C00SPC500)
     Copyright (C) 2012-2023 Huawei Technologies Co., Ltd.
     HUAWEI NE40E-M2K
     
     System capabilities supported      :bridge router
     System capabilities enabled        :bridge router
     Management address type            :ipv4
     Management address                 :10.10.10.2
     Expired time                       :104 (s)
     
     Port VLAN ID(PVID)                 :0 
     Port And Protocol VLAN ID(PPVID)   :unsupported
     VLAN name of VLAN 1                :--
     Protocol identity                  :--
     Auto-negotiation supported         :Yes
     Auto-negotiation enabled           :No
     OperMau                            :speed (10000) /duplex (Full)
     Link aggregation supported         :Yes
     Link aggregation enabled           :No
     Aggregation port ID                :0
     Maximum frame Size                 :0
     Discovered time                    :2022-02-21 11:09:15
     ```
   
   # Check lldp information of DeviceB. For details, see the procedures for DeviceA.

#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  lldp enable
  lldp transmit interval 60
  lldp transmit delay 9
  #
  interface GigabitEthernet 0/1/1
    ip address 10.10.10.1 255.255.255.0
  #
  lldp management-address  10.10.10.1
  snmp-agent trap enable feature-name lldp
  lldp trap-interval 10
  #
  return
  ```
* DeviceB
  
  ```
  #
   sysname DeviceB
  #
  lldp enable
  lldp transmit interval 60
  lldp transmit delay 9
  #
  interface GigabitEthernet 0/1/1
   ip address 10.10.10.2 255.255.255.0
  #
  lldp management-address  10.10.10.2
  snmp-agent trap enable feature-name lldp
  lldp trap-interval 10
  #
  return
  ```