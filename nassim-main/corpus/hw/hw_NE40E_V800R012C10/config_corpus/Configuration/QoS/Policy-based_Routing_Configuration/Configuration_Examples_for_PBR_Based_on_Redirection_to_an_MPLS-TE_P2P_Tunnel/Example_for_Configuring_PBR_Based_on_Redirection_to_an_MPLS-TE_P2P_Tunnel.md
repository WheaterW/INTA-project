Example for Configuring PBR Based on Redirection to an MPLS-TE P2P Tunnel
=========================================================================

This section provides an example for configuring policy-based routing (PBR) based on redirection to an MPLS-TE P2P tunnel.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172371377__fig_dc_ne_qos_cfg_701001), a PBR policy named **aaa** needs to be configured on Device A. After the PBR policy is configured, if receiving packets from GE 0/1/0, Device A forwards all the packets with the source address of 10.100.0.11/24 to Tunnel30; if receiving packets from GE 0/2/0, Device A forwards all the packets with the source address of 10.110.0.11/24 to Tunnel 40. Device A is directly connected to Device B and Device C.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and Interface 2 in this example are GE 0/1/0 and GE 0/2/0, respectively.


**Figure 1** Configuring PBR based on redirection to an MPLS-TE P2P tunnel  
![](images/fig_dc_ne_qos_cfg_701001.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces on Device A, Device B, Device C, and Device D.
2. Configure routes from Device B and Device C to Device D.
3. Define ACLs.
4. Configure rules and the action for PBR and apply PBR to an interface.

#### Data Preparation

To complete the configuration, you need the following data:

* ACL numbers and rules
* Name of a PBR policy
* Outbound interface or next hop address to which packets are redirected

#### Procedure

1. Configure IP addresses for interfaces on Device A, Device B, Device C, and Device D.
2. Configure routes from Device B and Device C to Device D.
3. Define an ACL on Device A.
   
   
   
   # Define ACL 3001 to match the packets with the source address of **10.100.0.11/24** and ACL 3002 to match the packets with the source address of **10.110.0.11/24**.
   
   ```
   [~DeviceA] acl number 3001
   ```
   ```
   [*DeviceA-acl4-advance-3001] rule 5 permit ip source 10.100.0.11 0.0.0.255
   ```
   ```
   [*DeviceA-acl4-advance-3001] commit
   ```
   ```
   [~DeviceA-acl4-advance-3001] quit
   ```
   ```
   [~DeviceA]  acl number 3002
   ```
   ```
   [*DeviceA-acl4-advance-3002] rule 5 permit ip source 10.110.0.11 0.0.0.255
   ```
   ```
   [*DeviceA-acl4-advance-3002] commit
   ```
   ```
   [~DeviceA-acl4-advance-3002] quit
   ```
4. Configure rules and the action for PBR and apply PBR to an interface of Device A.
   
   
   
   # Configure node 5 to forward packets with the source address of **10.100.0.11/24** to **Tunnel 30**.
   
   ```
   [~DeviceA] interface Tunnel30
   ```
   ```
   [*DeviceA] quit
   ```
   ```
   [*DeviceA] policy-based-route aaa permit node 5
   ```
   ```
   [*DeviceA-policy-based-route-aaa-5] if-match acl name a3001
   ```
   ```
   [*DeviceA-policy-based-route-aaa-5] apply output-interface Tunnel30
   ```
   ```
   [*DeviceA-policy-based-route-aaa-5] commit
   ```
   ```
   [~DeviceA-policy-based-route-aaa-5] quit
   ```
   
   # Configure node 10 to forward packets with the source address of **10.110.0.11/24** to **Tunnel 40**.
   
   ```
   [~DeviceA] interface Tunnel40
   ```
   ```
   [*DeviceA] quit
   ```
   ```
   [*DeviceA] policy-based-route aaa permit node 10
   ```
   ```
   [*DeviceA-policy-based-route-aaa-10] if-match acl name a3002
   ```
   ```
   [*DeviceA-policy-based-route-aaa-10] apply output-interface Tunnel40
   ```
   ```
   [*DeviceA-policy-based-route-aaa-10] commit
   ```
   ```
   [~DeviceA-policy-based-route-aaa-10] quit
   ```
   
   # Apply the PBR policy named **aaa** to GE 0/1/0.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ip address 10.100.0.10 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip policy-based-route aaa
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
   ```
   
   # Apply the PBR policy named **aaa** to GE 0/2/0.
   
   ```
   [~DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] ip address 10.110.0.10 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ip policy-based-route aaa
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [~DeviceA] quit
   ```
5. Verify the configuration.
   
   
   
   Run the [**display ip policy-based-route**](cmdqueryname=display+ip+policy-based-route) command. The command output shows the enabled PBR policies.
   
   ```
   <DeviceA> display ip policy-based-route
   ```
   ```
   policy Name                     Interface
   ```
   ```
   aaa                          GigabitEthernet0/1/0
   ```
   ```
   aaa                          GigabitEthernet0/2/0
   ```
   
   Run the [**display policy-based-route**](cmdqueryname=display+policy-based-route) command. The command output shows the created policy content.
   
   ```
   <DeviceA> display policy-based-route
   ```
   ```
   -----------------------------------------------------
   ```
   ```
     User Defined policy-based-route Policy Information:
   ```
   ```
   -----------------------------------------------------
   ```
   ```
       Total: 100  Used: 1  Free: 99
   ```
   ```
       Policy: aaa
   ```
   ```
           Node: 5     MapInstance: 5
   ```
   ```
                 if-match acl name a3001
   ```
   ```
                 apply output-interface Tunnel30
   ```
   ```
           Node: 10    MapInstance: 10
   ```
   ```
                 if-match acl name a3002
   ```
   ```
                 apply output-interface Tunnel40
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceA
  ```
  ```
  #
  ```
  ```
  acl number 3001
  ```
  ```
   rule 5 permit ip source 10.100.0.11 0.0.0.255
  ```
  ```
  acl number 3002
  ```
  ```
   rule 5 permit ip source 10.110.0.11 0.0.0.255
  ```
  ```
  #
  ```
  ```
  interface Tunnel30
  ```
  ```
  #
  ```
  ```
  interface Tunnel40
  ```
  ```
  #
  ```
  ```
   policy-based-route aaa permit node 5 map-instance 5
  ```
  ```
    if-match acl name a3001
  ```
  ```
    apply output-interface Tunnel30
  ```
  ```
   policy-based-route aaa permit node 10 map-instance 10
  ```
  ```
    if-match acl name a3002
  ```
  ```
    apply output-interface Tunnel40
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.100.0.10 255.255.255.0
  ```
  ```
   ip policy-based-route aaa
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.0.10 255.255.255.0
  ```
  ```
   ip policy-based-route aaa
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device B configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.100.0.11 255.255.255.0
  ```
  ```
  #
  ```
  ```
   ip route-static 10.1.3.0 255.255.255.0 10.100.0.10
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device C configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.110.0.11 255.255.255.0
  ```
  ```
  #
  ```
  ```
   ip route-static 10.1.2.0 255.255.255.0 10.110.0.10
  ```
  ```
  #
  ```
  ```
  return
  ```