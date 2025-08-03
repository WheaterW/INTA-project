Example for Configuring a Basic ACL to Manage Device Access Rights
==================================================================

This section provides an example for configuring a basic ACL to manage device access rights.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172364648__fig_dc_vrp_acl4_cfg_007501), the PE is a device in the HR department and two VPN instances VPN-A and VPN-B are created on the PE. CE1 is a device in Department A and belongs to VPN-A that uses 111:1 as the VPN-target. CE2 is a device in Department B and belongs to VPN-B that uses 222:2 as the VPN-target. To allow the user (CE1) in VPN-A to log in to the PE by Telnet and prevent the user (CE2) in VPN-B from logging in to the PE, configure a basic ACL on the PE so that devices in Department A are allowed to access the devices in the HR department, whereas devices in Department B are not allowed to access the devices in the HR department, and devices in Department A and Department B cannot access each other.

**Figure 1** Configuring a basic ACL to manage device access rights![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_acl4_cfg_007501.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure VPN instances on different devices.
2. Define ACL rules to configure rights for different VPN users to access the PE.
3. Apply the ACL to allow different VPN users to have different rights to access the PE.

#### Data Preparation

To complete the configuration, you need the following data:

* ACL number
* VPN instance names

#### Procedure

1. Configure VPN instances on the PE.
   
   
   
   # Configure VPN-A.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE] ip vpn-instance vpna
   ```
   ```
   [*PE-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE-vpn-instance-vpna-af-ipv4] commit
   ```
   ```
   [~PE-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [~PE-vpn-instance-vpna] quit
   ```
   ```
   [~PE] interface gigabitethernet 0/1/0
   ```
   ```
   [~PE-GigabitEthernet0/1/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE-GigabitEthernet0/1/0] ip address 10.1.1.1 24
   ```
   ```
   [*PE-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE-GigabitEthernet0/1/0] quit
   ```
   
   # Configure VPN-B.
   
   ```
   [~PE] ip vpn-instance vpnb
   ```
   ```
   [*PE-vpn-instance-vpnb] ipv4-family
   ```
   ```
   [*PE-vpn-instance-vpnb-af-ipv4] route-distinguisher 100:2
   ```
   ```
   [*PE-vpn-instance-vpnb-af-ipv4] vpn-target 222:2 both
   ```
   ```
   [*PE-vpn-instance-vpnb-af-ipv4] commit
   ```
   ```
   [~PE-vpn-instance-vpnb-af-ipv4] quit
   ```
   ```
   [~PE-vpn-instance-vpnb] quit
   ```
   ```
   [~PE] interface gigabitethernet 0/2/0
   ```
   ```
   [~PE-GigabitEthernet0/2/0] ip binding vpn-instance vpnb
   ```
   ```
   [*PE-GigabitEthernet0/2/0] ip address 10.2.1.1 24
   ```
   ```
   [*PE-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE-GigabitEthernet0/2/0] quit
   ```
2. Create a basic ACL and configure ACL rules on the PE to allow the user (CE1) in VPN-A to log in to PE by Telnet and prevent the user (CE2) in VPN-B from logging in to the PE. 
   
   
   ```
   [~PE] acl number 2001
   ```
   ```
   [*PE-acl4-basic-2001] rule permit vpn-instance vpna
   ```
   ```
   [*PE-acl4-basic-2001] rule deny vpn-instance vpnb
   ```
   ```
   [*PE-acl4-basic-2001] commit
   ```
   ```
   [~PE-acl4-basic-2001] quit
   ```
3. Apply the ACL in Telnet services on the PE. 
   
   
   ```
   [~PE] user-interface vty 0 4
   ```
   ```
   [~PE-ui-vty0-4] authentication-mode password
   ```
   ```
   [*PE-ui-vty0-4] set authentication password
   ```
   ```
   Please configure the login password (8-16)
   Enter Password:
   Confirm Password:
   ```
   ```
   [*PE-ui-vty0-4] acl 2001 inbound
   ```
   ```
   [*PE-ui-vty0-4] commit
   ```
4. Configure IP addresses for CE1 and CE2 as shown in [Figure 1](#EN-US_TASK_0172364648__fig_dc_vrp_acl4_cfg_007501). For configuration details, see [Configuration Files](#EN-US_TASK_0172364648__example518361630214033) in this section.
5. Verify the configuration. 
   
   
   
   # Log in to the PE from CE1 by Telnet. The command output shows that CE1 can log in to the PE by Telnet.
   
   ```
   <CE1> telnet vpn-instance vpna 10.1.1.1
   ```
   ```
   Trying 10.1.1.1 ...                                                             
   Press CTRL+K to abort                                                           
   Connected to 10.1.1.1 ...                                                       
   Info: The max number of VTY users is 10, and the number                         
         of current VTY users on line is 1.  
   <PE>
   ```
   
   The command output shows that CE1 can log in to the PE by Telnet.
   
   # Log in to the PE from CE2 by Telnet.
   
   ```
   <CE2> telnet vpn-instance vpnb 10.2.1.1
   ```
   ```
   Trying 10.2.1.1 ...
   Press CTRL+K to abort
   Error: Failed to connect to the remote host.Press CTRL+K to abort
   ```
   
   The command output shows that CE2 cannot log in to the PE by Telnet.
   
   # Log in to CE2 from CE1 by Telnet.
   
   ```
   <CE1> telnet vpn-instance vpnb 10.2.1.2
   ```
   ```
   Trying 10.2.1.2 ...
   Press CTRL+K to abort
   Error: Failed to connect to the remote host.Press CTRL+K to abort
   ```
   
   The command output shows that CE1 cannot log in to CE2 by Telnet.

#### Configuration Files

* PE configuration file
  
  ```
  #
   sysname PE
  #
  ip vpn-instance vpna
   ipv4 family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  ip vpn-instance vpnb
   ipv4 family
    route-distinguisher 100:2
    apply-label per-instance
    vpn-target 222:2 export-extcommunity
    vpn-target 222:2 import-extcommunity
  #
  acl number 2001
   rule 5 permit vpn-instance vpna
   rule 10 deny vpn-instance vpnb
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpnb                        
   ip address 10.2.1.1 255.255.255.0 
  #    
  user-interface con 0
  user-interface vty 0 4
   acl 2001 inbound
   authentication-mode password
   user privilege level 15
   set authentication password cipher $1c$`g=H/qo%;7$b6Za%2'[D!0blsOXF=.3QCNC-f)co,[aeE.`e`-<$
  user-interface vty 16 20
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
   sysname CE1
  #
  ip vpn-instance vpna
   route-distinguisher 100:1
   apply-label per-instance
   vpn-target 111:1 export-extcommunity
   vpn-target 111:1 import-extcommunity
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
  #
  user-interface con 0
  user-interface vty 0 4
  user-interface vty 16 20
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
   sysname CE2
  #
  ip vpn-instance vpnb
   route-distinguisher 100:2
   apply-label per-instance
   vpn-target 222:2 export-extcommunity
   vpn-target 222:2 import-extcommunity
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpnb
   ip address 10.2.1.2 255.255.255.0
  #
  user-interface con 0
  user-interface vty 0 4
  user-interface vty 16 20
  #
  return
  ```