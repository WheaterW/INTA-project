Example for Configuring DCN Traversal over a Third-Party Layer 2 Network
========================================================================

This section provides an example for configuring DCN traversal over a third-party Layer 2 network. This function enables NEs on target networks to learn the DCN VLAN ID sent by a GNE and establish DCN connections with the GNE.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172361428__fig_dc_vrp_dcn_cfg_002301), a DCN VLAN group is configured on the GNE, and the GNE sends DCN negotiation packets carrying the IDs of VLANs in the DCN VLAN group to a third-party network. On the third-party network, DCN packets carrying different VLAN IDs are forwarded to leaf nodes through different virtual leased lines (VLLs). The NE devices learn the DCN VLAN packets sent from the GNE and establish DCN connections with the GNE.

**Figure 1** Configuring DCN traversal over a third-party Layer 2 network![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Interface1 in this example is GE 0/1/0.


  
![](images/fig_dc_vrp_dcn_cfg_002301.png "Click to enlarge")

#### Precautions

This function applies only to the router mode.

If an Ethernet sub-interface is configured as a Dot1q termination sub-interface, the VLAN ID of the sub-interface can be the same as the DCN VLAN ID of the main interface.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable global DCN on the GNE, NE1, NE2, and NE3.
2. Enable interface-specific DCN on the interfaces connecting the GNE, NE1, NE2, and NE3 to the third-party network.
3. Configure a DCN VLAN group on the GNE, with VLAN IDs in the group being the same as the service VLAN IDs configured for involved sub-interfaces on the GNE.
4. Configure the automatic NE report function on the GNE.
5. Configure the NEID and NEIP for the GNE.

#### Data Preparation

To complete the configuration, you need the following data:

* DCN VLAN ID

#### Procedure

1. Enable the DCN feature globally.
   
   
   
   # Enable the DCN feature globally. In this example, a GNE is used. Then, use the same method to enable DCN feature globally for NE1, NE2, and NE3.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] dcn
   ```
   ```
   [~HUAWEI-dcn] quit
   ```
2. Enable interface-specific DCN.
   
   
   
   # Enable interface-specific DCN. For example, enable DCN on GE0/1/0 of the GNE. Then, use the same method to enable interface-specific DCN for NE1, NE2, and NE3.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] interface gigabitethernet 0/1/0
   [~HUAWEI-GigabitEthernet0/1/0] dcn
   ```
3. Configure the DCN VLAN group on the GNE.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/0
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] dcn
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] dcn vlan 1 to 3
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0] quit
   ```
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/0.1
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1] vlan-type dot1q 1 default
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.1] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/0.2
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.2] vlan-type dot1q 2 default
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.2] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.2] quit
   ```
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/0.3
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.3] vlan-type dot1q 3 default
   ```
   ```
   [*HUAWEI-GigabitEthernet0/1/0.3] commit
   ```
   ```
   [~HUAWEI-GigabitEthernet0/1/0.3] quit
   ```
4. Configure the automatic NE report function on the GNE.
   
   
   ```
   [~HUAWEI] dcn
   ```
   ```
   [*HUAWEI-dcn] auto-report
   ```
   ```
   [*HUAWEI-dcn] commit
   ```
5. Configure NEID and NEIP on the GNE.
   
   
   ```
   [~HUAWEI] set neid 111111
   ```
   ```
   [*HUAWEI] dcn
   ```
   ```
   [*HUAWEI-dcn] ne-ip 10.1.1.2 255.255.0.0
   ```
   ```
   [*HUAWEI-dcn] commit
   ```
6. Verify the configuration.
   
   
   
   # Run the [**display dcn interface**](cmdqueryname=display+dcn+interface) command on the GNE to check DCN interface information.
   
   ```
   <HUAWEI> display dcn interface
   total 4 DCN physical interface
   -----------------------------------------------------------------------------------------------------------------
   interface                          Vid     state         logical-if                       
   -----------------------------------------------------------------------------------------------------------------
   GE0/1/1                              0     up (Ready)    DCN-Serial0/1/1:0 (Ready)
   GE0/1/0                             1     up (Ready)    DCN-Serial0/1/0:0 (Ready)
                                        2     up (Ready)    DCN-Serial0/1/0:1 (Ready)  
                                        3     up (Ready)    DCN-Serial0/1/0:2 (Ready)  
   -----------------------------------------------------------------------------------------------------------------
   
   ```

#### Configuration Files

* Configuration file of the GNE
  
  ```
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   dcn                                                                            
   dcn vlan 1 to 3                                           
  #                                                                               
  interface GigabitEthernet0/1/0.1
   vlan-type dot1q 1                                    
  #                                                                               
  interface GigabitEthernet0/1/0.2
   vlan-type dot1q 2 default                                   
  #
  interface GigabitEthernet0/1/0.3
   vlan-type dot1q 3 default                                   
  #                                                                               
  !The DCN function implements the capability of plug-and-play for this device.
  !A NE IP address based on the unique NE ID is automatically generated in VPN
  !of DCN. It is recommended that the NE IP address be changed to the planned 
  !one by running the ne-ip X.X.X.X <MASK> command after the device being online.
  
  dcn                                                                             
   auto-report                                                                    
   ne-ip 10.1.1.2 255.255.0.0
  #                                                                               
  return 
  ```

* NE1 configuration file, which is the same as NE2/NE3 configuration file
  
  ```
  #                                                                               
  interface GigabitEthernet0/1/0                                                  
   undo shutdown                                                                  
   dcn                                                                            
  #                                                                               
  !The DCN function implements the capability of plug-and-play for this device.
  !A NE IP address based on the unique NE ID is automatically generated in VPN
  !of DCN. It is recommended that the NE IP address be changed to the planned 
  !one by running the ne-ip X.X.X.X <MASK> command after the device being online.
  
  dcn                                                                             
  #                                                                               
  return 
  ```