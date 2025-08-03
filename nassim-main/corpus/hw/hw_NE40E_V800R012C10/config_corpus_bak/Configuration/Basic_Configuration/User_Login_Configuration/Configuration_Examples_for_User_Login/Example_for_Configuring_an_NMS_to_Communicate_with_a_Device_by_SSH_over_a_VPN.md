Example for Configuring an NMS to Communicate with a Device by SSH over a VPN
=============================================================================

This section provides an example for configuring an NMS to communicate with a device by SSH over a VPN.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172359871__fig_dc_vrp_ssh_cfg_0138), an NMS, device, and AAA server are connected over a VPN. The NMS is integrated with the SSH client and SFTP server functions. The SSH client uses SSH to log in to and communicate with the device. The SFTP server uses SFTP for file transfer with the device functioning as an SFTP client.

**Figure 1** Networking diagram for configuring an NMS to communicate with a device by SSH over a VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 stands for GE 0/1/0, interface 2 stands for GE 0/2/0, and interface 3 stands for GE 0/3/0. The interfaces are bound to the same VPN instance.


  
![](images/fig_dc_vrp_ssh_cfg_0138.png)  


#### Precautions

Ensure that the route between the device and NMS is reachable.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a VPN instance.
2. Bind the interfaces connecting the device to the NMS and HWTACACS server to the VPN instance.
3. Configure a default VPN instance used by the NMS to manage the device.
4. Configure an HWTACACS server.
5. Create a local AAA user, and set the access type to SSH and authentication mode to HWTACACS for the user.
6. Configure an SSH user and set its authentication and service modes.
7. Configure an SNMPv3 USM user to allow the NMS to access the device.
8. Configure an SFTP client to use SFTP for file transfer.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

After the default VPN instance is configured for the NMS to manage the device, the HWTACACS server, TFTP client, FTP client, SFTP client, SCP client, SNMP module, Info Center module, IP FPM module, and PM module on the device all belong to the default VPN if other VPN instances are not configured. If other VPN instances are configured, the VPN instance configured for each feature is preferentially selected. To access the public network, you must set the **public-net** parameter.



#### Data Preparation

To complete the configuration, you need the following data:

* Name of a VPN instance
* SNMP version
* SNMPv3 USM username and password
* Authentication mode, username, service type, and server authentication mode of the local user: AAA, **sshuser001**, SSH, and HWTACACS, respectively

#### Procedure

1. Configure a VPN instance.
   
   
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
   [~DeviceA] ip vpn-instance vrf1
   ```
   ```
   [*DeviceA-vpn-instance-vrf1] ipv4-family
   ```
   ```
   [*DeviceA-vpn-instance-vrf1-af-ipv4] route-distinguisher 22:1
   ```
   ```
   [*DeviceA-vpn-instance-vrf1-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*DeviceA-vpn-instance-vrf1-af-ipv4] quit
   ```
   ```
   [*DeviceA-vpn-instance-vrf1] quit
   ```
   ```
   [*DeviceA] commit
   ```
2. # Bind interfaces to the VPN instance.
   
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip binding vpn-instance vrf1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ip-address 10.1.1.2 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/2/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ip binding vpn-instance vrf1
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ip-address 10.2.1.2 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/3/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] undo shutdown
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] ip binding vpn-instance vrf1
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] ip-address 10.3.1.1 255.255.255.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/3/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
3. Configure a default VPN instance used by the NMS to manage the device.
   
   
   ```
   [~DeviceA] set net-manager vpn-instance vrf1
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The VPN configured using this command affects the following service modules on the device: TFTP client, FTP client, SFTP client, SCP client, Info Center, SNMP, PM, IP FPM, and TACACS. To access the public network, you must set the **public-net** parameter.
   
   ```
   [*DeviceA] commit
   ```
4. Configure an HWTACACS server.
   
   
   
   # Enable the HWTACACS function and configure an HWTACACS server template named **ht**.
   
   ```
   [~DeviceA] hwtacacs enable
   ```
   ```
   [*DeviceA] hwtacacs-server template ht
   ```
   
   # Configure an IP address and port number for the primary HWTACACS authentication and authorization server.
   
   ```
   [*DeviceA-hwtacacs-ht] hwtacacs-server authentication 10.2.1.1 49
   ```
   ```
   [*DeviceA-hwtacacs-ht] hwtacacs-server authorization 10.2.1.1 49
   ```
   
   # Configure a key for the HWTACACS server.
   
   ```
   [*DeviceA-hwtacacs-ht] hwtacacs-server shared-key cipher it-is-my-secret123
   ```
   ```
   [*DeviceA-hwtacacs-ht] commit
   ```
   ```
   [~DeviceA-hwtacacs-ht] quit
   ```
   
   # Enter the AAA view.
   
   ```
   [~DeviceA] aaa
   ```
   
   # Configure an authentication scheme named **scheme1** and set the authentication mode to HWTACACS authentication.
   
   ```
   [~DeviceA-aaa] authentication-scheme scheme1
   ```
   ```
   [*DeviceA-aaa-authen-scheme1] authentication-mode hwtacacs
   ```
   ```
   [*DeviceA-aaa-authen-scheme1] commit
   ```
   ```
   [~DeviceA-aaa-authen-scheme1] quit
   ```
   
   # Configure an authorization scheme named **scheme2** and set the authorization mode to HWTACACS authorization.
   
   ```
   [~DeviceA-aaa] authorization-scheme scheme2
   ```
   ```
   [*DeviceA-aaa-author-scheme2] authorization-mode hwtacacs
   ```
   ```
   [*DeviceA-aaa-author-scheme2] commit
   ```
   ```
   [~DeviceA-aaa-author-scheme2] quit
   ```
   
   # Configure the **huawei** domain. Use the **scheme1** authentication scheme, **scheme2** authorization scheme, and **ht** template in the domain.
   
   ```
   [~DeviceA-aaa] domain huawei
   ```
   ```
   [*DeviceA-aaa-domain-huawei] authentication-scheme scheme1
   ```
   ```
   [*DeviceA-aaa-domain-huawei] authorization-scheme scheme2
   ```
   ```
   [*DeviceA-aaa-domain-huawei] hwtacacs-server ht
   ```
   ```
   [*DeviceA-aaa-domain-huawei] commit
   ```
   ```
   [~DeviceA-aaa-domain-huawei] quit
   ```
5. Create a local AAA user named **sshuser001**, and set the access type to SSH and authentication mode to HWTACACS for the user.
   
   
   
   # Configure a local user named sshuser001 in the **huawei** domain. After the configuration is complete, the sshuser001 user uses the authentication and authorization modes in the **huawei** domain.
   
   ```
   [~DeviceA-aaa] local-user sshuser001@huawei password
   Please configure the password (8-128)
   Enter Password:                                                                 
   Confirm Password:
   ```
   ```
   [*DeviceA-aaa] local-user sshuser001@huawei service-type ssh
   ```
   ```
   [*DeviceA-aaa] commit
   ```
   ```
   [~DeviceA-aaa] quit
   ```
6. Configure authentication and service modes for the SSH user.
   
   
   ```
   [*DeviceA] ssh authentication-type default password
   ```
   ```
   [*DeviceA] ssh user sshuser001 service-type stelnet snetconf
   ```
   ```
   [*DeviceA] commit
   ```
7. Enable STelnet on the SSH server.
   
   
   ```
   [~DeviceA] stelnet server enable
   ```
   ```
   [*DeviceA] ssh server-source -i gigabitethernet 0/3/0
   ```
   ```
   [*DeviceA] commit
   ```
8. Configure an SNMPv3 USM user to allow the NMS to access the device.
   
   
   
   # Enable the SNMP agent function.
   
   ```
   [*DeviceA] snmp-agent
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Set the SNMP version to SNMPv3.
   
   ```
   [~DeviceA] snmp-agent sys-info version v3
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure a MIB view.
   
   ```
   [~DeviceA] snmp-agent mib-view included iso iso
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure a user group and users in the group, and authenticate and encrypt user data.
   
   ```
   [~DeviceA] snmp-agent group v3 admin privacy write-view iso notify-view iso read-view iso
   [*DeviceA] snmp-agent usm-user v3 nms-admin group admin
   [*DeviceA] snmp-agent usm-user v3 nms-admin authentication-mode sha
   Please configure the authentication password (10-255)
   Enter Password:
   Confirm Password:   
   [*DeviceA] snmp-agent usm-user v3 nms-admin privacy-mode aes128
   Please configure the privacy password (10-255)
   Enter Password:
   Confirm Password:
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure the alarm function.
   
   ```
   [~DeviceA] snmp-agent target-host trap address udp-domain 10.1.1.1 vpn-instance vrf1 params securityname nms-admin v3 privacy
   [*DeviceA] snmp-agent trap enable
   ```
   ```
   [*DeviceA] commit
   ```
9. Enable the device functioning as an SFTP client to transfer files with the NMS functioning as an SFTP server over the VPN.
   
   For details about how to configure the NMS to function as an SFTP server, see the NMS server configuration guide. The username and password used for file transfer between the device and NMS must be the same as those configured on the SFTP server.
   ```
   [~DeviceA] ssh client first-time enable
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] sftp client-transfile get -a 10.1.1.2 host-ip 10.1.1.1 username sshuser002 password YsHsjx_202206 sourcefile aaa.txt
   ```
10. Verify the configuration.
    
    
    
    After completing the configuration, perform the following operations to check whether the configuration takes effect.
    
    # Display the SNMP version.
    
    ```
    <DeviceA> display snmp-agent sys-info version
    ```
    ```
       The contact person for this managed node:
               R&D Beijing, Huawei Technologies co.,Ltd.
    
       The physical location of this node:
               Beijing China
    
       SNMP version running in the system:
               SNMPv3
    ```
    
    # Display local user information.
    
    ```
    <DeviceA> display snmp-agent usm-user
    ```
    ```
       User name: nms-admin,
           Engine ID: 800007DB0300259E0370C3 active
           Authentication Protocol: sha
           Privacy Protocol: aes128
           Group-name: admin
           State: Active
    ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  hwtacacs enable
  #
  ip vpn-instance vrf1
   ipv4-family
    route-distinguisher 22:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  hwtacacs-server template ht
   hwtacacs-server authentication 10.2.1.1 vpn-instance vrf1
   hwtacacs-server authorization 10.2.1.1 vpn-instance vrf1
   hwtacacs-server shared-key cipher %^%#x@ZaCImt|X79[^A&]DEYC6[>U]OD(8n&BVHvsu2R{=zVSySB'|H[;I`|ef#%^%#
  #
  aaa
   local-user sshuser001@huawei password irreversible-cipher $1c$\h[;D"`M79$GN]A=y;*4EFG%t>vIJI=rJvxWe/V%Xbd;(J+AzC+$
   local-user sshuser001@huawei service-type ssh
   #
   authentication-scheme scheme1
    authentication-mode hwtacacs
   #
   authorization-scheme scheme2
    authorization-mode hwtacacs
   #
   accounting-scheme default0
   #
   accounting-scheme default1
   #
   domain huawei
    authentication-scheme scheme1
    authorization-scheme scheme2
    hwtacacs-server ht
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vrf1
   ip-address 10.1.1.2 255.255.255.0
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vrf1
   ip-address 10.2.1.2 255.255.255.0
  interface GigabitEthernet0/3/0
   undo shutdown
   ip binding vpn-instance vrf1
   ip-address 10.3.1.1 255.255.255.0
  #
  snmp-agent
  snmp-agent local-engineid 800007DB0300313D6A1FA0
  #
  snmp-agent sys-info version v3
  snmp-agent group v3 admin privacy write-view iso notify-view iso read-view iso
  snmp-agent target-host trap address udp-domain 10.1.1.1 vpn-instance vrf1 params securityname nms-admin v3 privacy
  #
  snmp-agent mib-view included iso iso
  snmp-agent usm-user v3 nms-admin group admin
  snmp-agent usm-user v3 nms-admin authentication-mode sha %#%##/L&Fd]S.!i*S7<\jCh2DkfkE4+:<%Wap|8zZWwPL+[a>h$wy>VJsp9(L{%B%#%#
  snmp-agent usm-user v3 nms-admin privacy-mode aes128 %#%#CM-]HDuhH6VX)**J<186nf({M823f(0Z73++7(A#%,1jODj}D>_HS>W,'Ss=%#%#
  #
  stelnet server enable
  ssh server-source -i gigabitethernet 0/3/0
  ssh user sshuser001
  ssh authorization-type default password
  ssh user sshuser001 service-type stelnet snetconf
  #
  ssh client first-time enable
  #
  return
  ```