Example for Configuring User Access (Web+MAC Authentication) in a Dual-Device Hot Backup Scenario
=================================================================================================

This section provides an example for configuring user access (web+MAC authentication) in a dual-device hot backup scenario, so that users can access the network again without re-entering usernames and passwords within a specified period after their first login. A networking diagram is provided to help you understand the configuration scenario and procedure.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374423__fig_dc_ne_cfg_rui_003101), users access BRAS1 and BRAS2 through SW1. When a user accesses the Internet for the first time, the user is required to enter the username and password on the portal page. The RADIUS server automatically records the MAC address of the user terminal and associates the MAC address with the username. Later, the user can access the network again without re-entering the username and password within a specified period after the first login.

In dual-device hot backup scenarios, the networking planning for web+MAC authentication is as follows:

* RADIUS authentication and accounting are used.
* The RADIUS server address is 192.168.7.249. The authentication and accounting port numbers are 1812 and 1813, respectively. The standard RADIUS protocol is adopted, and the key is **YsHsjx\_202206**.
* The IP address of the DNS server is 192.168.9.111.
* The IP address of the web server is 192.168.8.251.

**Figure 1** User access (web+MAC authentication) in a dual-device hot backup scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/3/1, GE0/3/6, and GE0/3/2, respectively.

![](figure/en-us_image_0000001769883254.png)

| **Device** | **Interface** | **IP Address** | **Function** |
| --- | --- | --- | --- |
| BRAS1 | GE0/3/1 | 10.32.1.1/24 | BRAS1's interface for establishing an RBS channel |
| BRAS1 | GE0/3/6.1 | 10.24.0.1/24 | Interface running VRRP |
| BRAS1 | Loopback1 | 10.1.1.1/32 | Protection tunnel interface |
| BRAS2 | GE0/3/2 | 10.32.1.2/24 | BRAS2's interface for establishing an RBS channel |
| BRAS2 | GE0/3/6.1 | 10.24.0.2/24 | Interface running VRRP |
| BRAS2 | Loopback1 | 10.1.1.2/32 | Protection tunnel interface |




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic user access functions and ensure that the two devices for backup have the same configuration.
2. Configure VRRP on the access side of the master and backup BRASs. BRAS1 is the master, and BRAS2 is the backup.
3. Configure a remote backup service (RBS) and a remote backup profile (RBP) for backing up BRAS user information.
4. Configure Layer 2 IPoE access (web+MAC authentication).
5. Specify the source IP address of portal packets to be sent to the web authentication server.

#### Data Preparation

To complete the configuration, you need the following data:

* VRRP parameters (such as the VRRP ID and preemption delay)
* IP address of each interface on BRAS1 and BRAS2
* Backup ID, which works together with an RBS to identify an RBP to which users belong

#### Procedure

1. Configure VRRP on the access side of the master and backup BRASs. BRAS1 is the master, and BRAS2 is the backup.
   
   
   
   The configurations on BRAS1 are as follows:
   
   # Configure a VRRP group on an interface (GE0/3/6.1 is used as an example).
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS1
   [*BRAS1] commit
   [~BRAS1] interface GigabitEthernet 0/3/6.1               
   [*BRAS1-GigabitEthernet0/3/6.1] vlan-type dot1q 400                           
   [*BRAS1-GigabitEthernet0/3/6.1] ip address 10.24.0.1 255.255.255.0            
   [*BRAS1-GigabitEthernet0/3/6.1] vrrp vrid 1 virtual-ip 10.24.0.100            
   [*BRAS1-GigabitEthernet0/3/6.1] admin-vrrp vrid 1                             
   [*BRAS1-GigabitEthernet0/3/6.1] vrrp vrid 1 priority 120                      
   [*BRAS1-GigabitEthernet0/3/6.1] commit
   [~BRAS1-GigabitEthernet0/3/6.1] quit
   ```
   
   The configurations on BRAS2 are as follows:
   
   # Configure a VRRP group on an interface (GE0/3/6.1 is used as an example).
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname BRAS2
   [*BRAS2] commit
   [~BRAS2] interface GigabitEthernet 0/3/6.1               
   [*BRAS2-GigabitEthernet0/3/6.1] vlan-type dot1q 400                           
   [*BRAS2-GigabitEthernet0/3/6.1] ip address 10.24.0.2 255.255.255.0            
   [*BRAS2-GigabitEthernet0/3/6.1] vrrp vrid 1 virtual-ip 10.24.0.100            
   [*BRAS2-GigabitEthernet0/3/6.1] admin-vrrp vrid 1                             
   [*BRAS2-GigabitEthernet0/3/6.1] vrrp vrid 1 priority 110                      
   [*BRAS2-GigabitEthernet0/3/6.1] commit
   [~BRAS2-GigabitEthernet0/3/6.1] quit
   ```
2. Configure an RBS and an RBP.
   
   
   
   The configurations on BRAS1 are as follows:
   
   # Configure an IP address for the protection tunnel.
   
   ```
   [~BRAS1] interface loopback1
   [*BRAS1-loopback1] ip address 10.1.1.1 32
   [*BRAS1-loopback1] commit
   [~BRAS1-loopback1] quit
   ```
   
   # Configure an RBS interface.
   
   ```
   [~BRAS1] interface gigabitethernet 0/3/1
   [*BRAS1-GigabitEthernet0/3/1] undo shutdown
   [*BRAS1-GigabitEthernet0/3/1] ip address 10.32.1.1 24
   [*BRAS1-GigabitEthernet0/3/1] mpls
   [*BRAS1-GigabitEthernet0/3/1] mpls ldp
   [*BRAS1-GigabitEthernet0/3/1] commit
   [~BRAS1-GigabitEthernet0/3/1] quit
   ```
   
   # Configure an RBS.
   
   ```
   [~BRAS1] remote-backup-service s1
   [*BRAS1-rm-backup-srv-s1] peer 10.32.1.2 source 10.32.1.1 port 11000
   [*BRAS1-rm-backup-srv-s1] protect lsp-tunnel for-all-instance peer-ip 10.1.1.2
   [*BRAS1-rm-backup-srv-s1] commit
   [~BRAS1-rm-backup-srv-s1] quit
   ```
   
   # Configure an RBP.
   
   ```
   [~BRAS1] remote-backup-profile p1
   [*BRAS1-rm-backup-prf-p1] service-type bras
   [*BRAS1-rm-backup-prf-p1] backup-id 1 remote-backup-service s1
   [*BRAS1-rm-backup-prf-p1] peer-backup hot
   [*BRAS1-rm-backup-prf-p1] vrrp-id 1 interface gigabitethernet 0/3/6.1
   [*BRAS1-rm-backup-prf-p1] commit
   [~BRAS1-rm-backup-prf-p1] quit
   ```
   
   # Bind the RBP to the interface through which users go online.
   
   ```
   [~BRAS1] interface gigabitethernet 0/3/6.2
   [*BRAS1-GigabitEthernet0/3/6.2] remote-backup-profile p1
   [*BRAS1-GigabitEthernet0/3/6.2] commit
   [~BRAS1-GigabitEthernet0/3/6.2] quit
   [~BRAS1] quit
   ```
   
   The configurations on BRAS2 are as follows:
   
   # Configure an IP address for the protection tunnel.
   
   ```
   [~BRAS2] interface loopback1
   [*BRAS2-loopback1] ip address 10.1.1.2 32
   [*BRAS2-loopback1] commit
   [~BRAS2-loopback1] quit
   ```
   
   # Configure an RBS interface.
   
   ```
   [~BRAS2] interface gigabitethernet 0/3/2
   [*BRAS2-GigabitEthernet0/3/2] undo shutdown
   [*BRAS2-GigabitEthernet0/3/2] ip address 10.32.1.2 24
   [*BRAS2-GigabitEthernet0/3/2] mpls
   [*BRAS2-GigabitEthernet0/3/2] mpls ldp
   [*BRAS2-GigabitEthernet0/3/2] commit
   [~BRAS2-GigabitEthernet0/3/2] quit
   ```
   
   # Configure an RBS.
   
   ```
   [~BRAS2] remote-backup-service s1
   [*BRAS2-rm-backup-srv-s1] peer 10.32.1.1 source 10.32.1.2 port 11000
   [*BRAS2-rm-backup-srv-s1] protect lsp-tunnel for-all-instance peer-ip 10.1.1.1
   [*BRAS2-rm-backup-srv-s1] ip-pool pool2
   [*BRAS2-rm-backup-srv-s1] commit
   [~BRAS2-rm-backup-srv-s1] quit
   ```
   
   # Configure an RBP.
   
   ```
   [~BRAS2] remote-backup-profile p1
   [*BRAS2-rm-backup-prf-p1] service-type bras
   [*BRAS2-rm-backup-prf-p1] backup-id 1 remote-backup-service s1
   [*BRAS2-rm-backup-prf-p1] peer-backup hot
   [*BRAS2-rm-backup-prf-p1] vrrp-id 1 interface gigabitethernet 0/3/6.1
   [*BRAS2-rm-backup-prf-p1] commit
   [~BRAS2-rm-backup-prf-p1] quit
   ```
   
   # Bind the RBP to the interface through which users go online.
   
   ```
   [~BRAS2] interface gigabitethernet 0/3/6.2
   [*BRAS2-GigabitEthernet0/3/6.2] remote-backup-profile p1
   [*BRAS2-GigabitEthernet0/3/6.2] commit
   [~BRAS2-GigabitEthernet0/3/6.2] quit
   [~BRAS2] quit
   ```
3. Configure MPLS.
   
   
   
   The configurations on BRAS1 are as follows:
   
   ```
   [~BRAS1] mpls lsr-id 10.1.1.1
   [~BRAS1] mpls
   [*BRAS1-mpls] commit
   [~BRAS1-mpls] mpls ldp
   [*BRAS1-mpls-ldp] commit
   [~BRAS1-mpls] quit
   ```
   
   The configurations on BRAS2 are as follows:
   
   ```
   [~BRAS2] mpls lsr-id 10.1.1.2
   [~BRAS2] mpls
   [*BRAS2-mpls] commit
   [~BRAS2-mpls] mpls ldp
   [*BRAS2-mpls-ldp] commit
   [~BRAS2-mpls] quit
   ```
4. Configure OSPF.
   
   
   
   The configurations on BRAS1 are as follows:
   
   ```
   [~BRAS1] ospf 1
   [*BRAS1-ospf-1] default cost inherit-metric
   [*BRAS1-ospf-1] import-route unr
   [*BRAS1-ospf-1] area 0
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.1.1.1 0.0.0.0
   [*BRAS1-ospf-1-area-0.0.0.0] network 10.32.1.1 0.0.0.255
   [*BRAS1-ospf-1-area-0.0.0.0] commit
   [~BRAS1-ospf-1-area-0.0.0.0] quit
   [~BRAS1-ospf-1] quit
   ```
   
   The configurations on BRAS2 are as follows:
   
   ```
   [~BRAS2] ospf 1
   [*BRAS2-ospf-1] default cost inherit-metric
   [*BRAS2-ospf-1] import-route unr
   [*BRAS2-ospf-1] area 0
   [*BRAS2-ospf-1-area-0.0.0.0] network 10.1.1.2 0.0.0.0
   [*BRAS2-ospf-1-area-0.0.0.0] network 10.32.1.2 0.0.0.255
   [*BRAS2-ospf-1-area-0.0.0.0] commit
   [~BRAS2-ospf-1-area-0.0.0.0] quit
   [~BRAS2-ospf-1] quit
   ```
5. Configure Layer 2 IPoE access (web+MAC authentication).
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration on BRAS2 is similar to the configuration on BRAS1. The configuration on BRAS1 is used in this example. For details about the configuration on BRAS2, see the BRAS2 configuration file.
   
   1. Create a MAC authentication domain named **mac-auth**, a web authentication domain named **web-auth**, and a post-authentication domain named **after-auth**.
      
      ```
      <HUAWEI> system-view
      ```
      ```
      [~BRAS1] aaa
      ```
      ```
      [*BRAS1-aaa] domain mac-auth
      ```
      ```
      [*BRAS1-aaa-domain-mac-auth] commit
      ```
      ```
      [~BRAS1-aaa-domain-mac-auth] quit
      ```
      ```
      [~BRAS1-aaa] domain web-auth
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] commit
      ```
      ```
      [~BRAS1-aaa-domain-web-auth] quit
      ```
      ```
      [~BRAS1-aaa] domain after-auth
      ```
      ```
      [*BRAS1-aaa-domain-after-auth] commit
      ```
      ```
      [~BRAS1-aaa-domain-after-auth] quit
      ```
      ```
      [~BRAS1-aaa] quit
      ```
   2. Configure AAA schemes and a RADIUS server group.
      
      # Create a RADIUS server group named **rd1**. In the RADIUS server group view, configure the BRAS to carry the Hw-Auth-Type attribute in authentication request packets.
      
      ```
      [~BRAS1] radius-server group rd1
      ```
      ```
      [*BRAS1-radius-rd1] radius-server authentication 192.168.7.249 1812 weight 0
      ```
      ```
      [*BRAS1-radius-rd1] radius-server accounting 192.168.7.249 1813 weight 0
      ```
      ```
      [*BRAS1-radius-rd1] radius-server type standard
      ```
      ```
      [*BRAS1-radius-rd1] radius-server shared-key-cipher YsHsjx_202206
      ```
      ```
      [*BRAS1-radius-rd1] radius-server attribute translate
      ```
      ```
      [*BRAS1-radius-rd1] radius-attribute include HW-Auth-Type
      ```
      ```
      [*BRAS1-radius-rd1] commit
      ```
      ```
      [~BRAS1-radius-rd1] quit
      ```
      
      # Configure a RADIUS server group named **rd2**.
      
      ```
      [~BRAS1] radius-server group rd2
      ```
      ```
      [*BRAS1-radius-rd2] radius-server authentication 192.168.8.249 1812 weight 0
      ```
      ```
      [*BRAS1-radius-rd2] radius-server accounting 192.168.8.249 1813 weight 0
      ```
      ```
      [*BRAS1-radius-rd2] radius-server type standard
      ```
      ```
      [*BRAS1-radius-rd2] radius-server shared-key-cipher YsHsjx_202206
      ```
      ```
      [*BRAS1-radius-rd2] commit
      ```
      ```
      [~BRAS1-radius-rd2] quit
      ```
      
      # Create an authentication scheme named **mac-auth**, and configure the device to redirect the user to the web authentication domain **web-auth** when authentication fails.
      
      ```
      [~BRAS1] aaa
      ```
      ```
      [~BRAS1-aaa] authentication-scheme mac-auth
      ```
      ```
      [*BRAS1-aaa-authen-mac-auth] authening authen-fail online authen-domain web-auth
      ```
      ```
      [*BRAS1-aaa-authen-mac-auth] commit
      ```
      ```
      [~BRAS1-aaa-authen-mac-auth] quit
      ```
      
      # Set the authentication mode of the authentication scheme **auth2** to RADIUS authentication so that the authentication scheme can be bound to the authentication domain **after-auth** for user authentication.
      
      ```
      [~BRAS1] aaa
      ```
      ```
      [~BRAS1-aaa] authentication-scheme auth2
      ```
      ```
      [*BRAS1-aaa-authen-auth2] authentication-mode radius
      ```
      ```
      [*BRAS1-aaa-authen-auth2] commit
      ```
      ```
      [~BRAS1-aaa-authen-auth2] quit
      ```
      
      # Set the accounting mode of the accounting scheme **acct2** to RADIUS accounting so that the accounting scheme can be bound to the authentication domain **after-auth** for user accounting.
      
      ```
      [~BRAS1-aaa] accounting-scheme acct2
      ```
      ```
      [*BRAS1-aaa-accounting-acct2] accounting-mode radius
      ```
      ```
      [*BRAS1-aaa-accounting-acct2] commit
      ```
      ```
      [~BRAS1-aaa-accounting-acct2] quit
      ```
      ```
      [~BRAS1-aaa] quit
      ```
      
      # Set the authentication mode of the authentication scheme **auth3** to none authentication so that the authentication scheme can be bound to the web pre-authentication domain **web-auth**. Users in this domain can access only the web authentication page. In insecure network environments, you are advised to use a secure password authentication mode, encryption authentication algorithm, and protocol. For examples of secure authentication, see RADIUS authentication of the authentication scheme **auth2** in this example.
      
      ```
      [~BRAS1] aaa
      ```
      ```
      [*BRAS1-aaa] authentication-scheme auth3
      ```
      ```
      [*BRAS1-aaa-authen-auth3] authentication-mode none
      ```
      ```
      [*BRAS1-aaa-authen-auth3] commit
      ```
      ```
      [~BRAS1-aaa-authen-auth3] quit
      ```
      
      # Set the accounting mode of the accounting scheme **acct3** to none accounting so that the accounting scheme can be bound to the web pre-authentication domain **web-auth**. No accounting is performed for users in this domain.
      
      ```
      [~BRAS1-aaa] accounting-scheme acct3
      ```
      ```
      [*BRAS1-aaa-accounting-acct3] accounting-mode none
      ```
      ```
      [*BRAS1-aaa-accounting-acct3] commit
      ```
      ```
      [~BRAS1-aaa-accounting-acct3] quit
      ```
      ```
      [~BRAS1-aaa] quit
      ```
   3. Configure address pools.
      
      ```
      [~BRAS1] ip pool pool2 bas local
      ```
      ```
      [*BRAS1-ip-pool-pool2] gateway 172.16.1.1 255.255.255.0
      ```
      ```
      [*BRAS1-ip-pool-pool2] commit
      ```
      ```
      [~BRAS1-ip-pool-pool2] section 0 172.16.1.2 172.16.1.200
      ```
      ```
      [*BRAS1-ip-pool-pool2] dns-server 192.168.9.111
      ```
      ```
      [*BRAS1-ip-pool-pool2] commit
      ```
      ```
      [~BRAS1-ip-pool-pool2] quit
      ```
   4. Enable MAC authentication in the MAC authentication domain **mac-auth**, and bind the RADIUS server group **rd1** and authentication scheme **mac-auth** to the domain.
      
      ```
      [~BRAS1-aaa] domain mac-auth
      ```
      ```
      [*BRAS1-aaa-domain-mac-auth] radius-server group rd1
      ```
      ```
      [*BRAS1-aaa-domain-mac-auth] authentication-scheme mac-auth
      ```
      ```
      [*BRAS1-aaa-domain-mac-auth] accounting-scheme acct2
      ```
      ```
      [*BRAS1-aaa-domain-mac-auth] ip-pool pool2
      ```
      ```
      [*BRAS1-aaa-domain-mac-auth] mac-authentication enable
      ```
      ```
      [*BRAS1-aaa-domain-mac-auth] commit
      ```
      ```
      [~BRAS1-aaa-domain-mac-auth] quit
      ```
   5. Configure a web pre-authentication domain named **web-auth** to allow users in this domain to access only the web authentication page. Then, bind the authentication scheme **auth3** (none authentication) and accounting scheme **acct3** (none accounting) to this domain.
      
      # Configure a web pre-authentication domain named **web-auth**.
      
      ```
      [~BRAS1] user-group web-before
      ```
      ```
      [~BRAS1] aaa
      ```
      ```
      [~BRAS1-aaa] domain web-auth
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] authentication-scheme auth3
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] accounting-scheme acct3
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] ip-pool pool2
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] user-group web-before
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] web-server 192.168.8.251
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] web-server url http://192.168.8.251
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] commit
      ```
      
      # Configure the keyword of the customized Portal attribute.
      
      ```
      [~BRAS1-aaa-domain-web-auth] web-server redirect-key mscg-ip mscgip
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] web-server redirect-key mscg-name mscgname
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] web-server redirect-key user-ip-address userip
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] web-server redirect-key nas-logic-sysname nasname
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] web-server redirect-key user-mac-address usermac
      ```
      ```
      [*BRAS1-aaa-domain-web-auth] web-server redirect-key ssid wlan
      ```
      ```
      [*BRAS1-aaa-domain-web-auth]commit
      ```
      ```
      [~BRAS1-aaa-domain-web-auth]quit
      ```
      ```
      [~BRAS1-aaa] quit
      ```
      
      # Configure a web authentication server.
      
      ```
      [~BRAS1] web-auth-server 192.168.8.251 key cipher YsHsjx_202206
      ```
   6. Configure an authentication domain named **after-auth**.
      
      ```
      [~BRAS1-aaa] domain after-auth
      ```
      ```
      [*BRAS1-aaa-domain-after-auth] authentication-scheme auth2
      ```
      ```
      [*BRAS1-aaa-domain-after-auth] accounting-scheme acct2
      ```
      ```
      [*BRAS1-aaa-domain-after-auth] radius-server group rd2
      ```
      ```
      [*BRAS1-aaa-domain-after-auth] commit
      ```
      ```
      [~BRAS1-aaa-domain-after-auth] quit
      ```
      ```
      [~BRAS1-aaa] quit
      ```
   7. Configure ACL rules.
      
      # Configure an ACL numbered 6004 and create ACL rules to deny the traffic originating from the user group **web-before**.
      
      ```
      [~BRAS1] acl number 6004
      ```
      ```
      [*BRAS1-acl-ucl-6004] rule 3 permit ip source user-group web-before destination user-group web-before
      ```
      ```
      [*BRAS1-acl-ucl-6004] rule 5 permit ip source user-group web-before destination ip-address any
      ```
      ```
      [~BRAS1-acl-ucl-6004] quit
      ```
      
      # Configure an ACL numbered 6005 and create ACL rules to permit the traffic between the user group **web-before** and the web authentication server and between the user group **web-before** and the DNS server.
      
      ```
      [~BRAS1] acl number 6005
      ```
      ```
      [*BRAS1-acl-ucl-6005] rule 5 permit ip source user-group web-before destination ip-address 192.168.8.251 0
      ```
      ```
      [*BRAS1-acl-ucl-6005] rule 15 permit ip source user-group web-before destination ip-address 192.168.9.111 0
      ```
      ```
      [~BRAS1-acl-ucl-6005] quit
      ```
      
      # Configure an ACL numbered 6008 and create ACL rules to allow HTTP redirection for the TCP packets originating from user group **web-before** and carrying destination port www or 8080.
      
      ```
      [~BRAS1] acl number 6008
      ```
      ```
      [*BRAS1-acl-ucl-6008] rule 5 permit tcp source user-group web-before destination-port eq www
      ```
      ```
      [*BRAS1-acl-ucl-6008] rule 10 permit tcp source user-group web-before destination-port eq 8080
      ```
      ```
      [*BRAS1-acl-ucl-6008] commit
      ```
      ```
      [~BRAS1-acl-ucl-6008] quit
      ```
   8. Configure traffic classifiers.
      
      ```
      [~BRAS1] traffic classifier web-be-permit
      ```
      ```
      [*BRAS1-classifier-web-be-permit] if-match acl 6005
      ```
      ```
      [*BRAS1-classifier-web-be-permit] quit
      ```
      ```
      [*BRAS1] traffic classifier web-be-deny
      ```
      ```
      [*BRAS1-classifier-web-be-deny] if-match acl 6004
      ```
      ```
      [*BRAS1-classifier-web-be-deny] quit
      ```
      ```
      [*BRAS1] traffic classifier redirect
      ```
      ```
      [*BRAS1-classifier-redirect] if-match acl 6008
      ```
      ```
      [*BRAS1-classifier-redirect] commit
      ```
      ```
      [~BRAS1-classifier-redirect] quit
      ```
   9. ```
      [*BRAS1] traffic behavior perm1
      ```
      ```
      [*BRAS1-behavior-perm1] permit
      ```
      ```
      [*BRAS1-behavior-perm1] quit
      ```
      ```
      [*BRAS1] traffic behavior deny1
      ```
      ```
      [*BRAS1-behavior-deny1] deny
      ```
      ```
      [*BRAS1-behavior-deny1] commit
      ```
      ```
      [~BRAS1-behavior-deny1] quit
      ```
      ```
      [*BRAS1] traffic behavior redirect
      ```
      ```
      [*BRAS1-behavior-redirect] http-redirect plus
      ```
      ```
      [*BRAS1-behavior-redirect] commit
      ```
      ```
      [~BRAS1-behavior-redirect] quit
      ```
   10. Configure and apply a traffic policy.
       
       # Configure a traffic policy.
       
       ```
       [*BRAS1] traffic policy web
       ```
       ```
       [*BRAS1-policy-web] share-mode
       ```
       ```
       [*BRAS1-policy-web] classifier web-be-permit behavior perm1
       ```
       ```
       [*BRAS1-policy-web] classifier redirect behavior redirect
       ```
       ```
       [*BRAS1-policy-web] classifier web-be-deny behavior deny1
       ```
       ```
       [*BRAS1-policy-web] commit
       ```
       ```
       [~BRAS1-policy-web] quit
       ```
       
       # Apply the traffic policy in the system view.
       
       ```
       [~BRAS1] traffic-policy web inbound
       ```
   11. In the AAA view, configure the MAC address carried in user access request packets as the pure username.
       
       ```
       [~BRAS1-aaa] default-user-name include mac-address
       ```
       ```
       [*BRAS1-aaa] default-password cipher YsHsjx_202206
       ```
       ```
       [*BRAS1-aaa] commit
       ```
       ```
       [~BRAS1-aaa] quit
       ```
   12. Configure the access type of the BAS interface.
       
       ```
       [~BRAS1] license
       ```
       ```
       [*BRAS1-license] active bas slot 1
       ```
       ```
       [*BRAS1-license] commit
       ```
       ```
       [~BRAS1-license] quit
       ```
       ```
       [~BRAS1] interface GigabitEthernet0/3/6.2
       ```
       ```
       [~BRAS1-GigabitEthernet0/3/6.2] bas
       ```
       ```
       [*BRAS1-GigabitEthernet0/3/6.2-bas] access-type layer2-subscriber default-domain pre-authentication mac-auth authentication after-auth
       ```
       ```
       [*BRAS1-GigabitEthernet0/3/6.2-bas] authentication-method web
       ```
       ```
       [*BRAS1-GigabitEthernet0/3/6.2-bas] commit
       ```
       ```
       [~BRAS1-GigabitEthernet0/3/6.2-bas] quit
       ```
6. Specify the source IP address of portal packets to be sent to the web authentication server.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration on BRAS2 is similar to the configuration on BRAS1. The configuration on BRAS1 is used in this example. For details about the configuration on BRAS2, see the BRAS2 configuration file.
   
   # Configure the source IP address of portal packets sent by the device to the web authentication server to 192.168.8.252 in the remote backup service **s1**.
   
   ```
   [~BRAS1] remote-backup-service s1
   [*BRAS1-rm-backup-srv-s1] web-auth-server source 192.168.8.252
   [*BRAS1-rm-backup-srv-s1] commit
   [~BRAS1-rm-backup-srv-s1] quit
   ```
7. Verify the configuration. 
   
   
   
   # Check the RBS configuration on BRAS1. The command output shows that the TCP connection state (**TCP-State**) of the RBS is **Connected**.
   
   ```
   <BRAS1> display remote-backup-service s1
   ```
   ```
   ----------------------------------------------------------
    Service-Index    : 1
    Service-Name     : s1
    TCP-State        : Connected
    Peer-ip          : 10.32.1.2
    Source-ip        : 10.32.1.1
    TCP-Port         : 11000
    Track-BFD        : -
    SSL-Policy-Name  : --
    SSL-State        : --
    Last up time     : 2019-03-06 09:03:59
    Last down time   : 2019-03-06 06:28:37
    Last down reason : TCP closed for echo time out
    Uplink state     : 2 (1:DOWN 2:UP)
    Domain-map-list  : --
   ----------------------------------------------------------
    ip pool:  
    ipv6 pool:  
    NULL0 Static route tag:
    Failure ratio    : 100%
    Failure duration : 0 min
   ----------------------------------------------------------
    Rbs-ID         : 0
    Peer-ip        : 10.1.1.2
    Vrfid          : 0
    Tunnel-state   : UP
    Tunnel-OperFlag: NORMAL
    Spec-interface : Null
    Total users    : 1
    Path 1:
        Tunnel-index   : 0x4c4b42
        Tunnel-index-v6: 0x4c4b42
        Out-interface  : GigabitEthernet0/3/1
        Vc-lable       : 48210
        Vc-lable-v6    : 48211
        User-number    : --
        Public-Lsp-Load: TRUE
   ----------------------------------------------------------
    Rbs-ID         : 0
    Protect-type   : public(LSP)
    Peer-ip        : 10.1.1.2
    Vrfid          : 4294967295
    Tunnel-state   : UP
    Tunnel-OperFlag: NORMAL
    Spec-interface : Null
    Total users    : 0
    Path 1:
        Tunnel-index   : 0x4c4b42
        Tunnel-index-v6: 0x0
        Out-interface  : GigabitEthernet0/3/1
        Vc-lable       : 4294967295
        Vc-lable-v6    : 4294967295
        User-number    : --
        Public-Lsp-Load: TRUE
   ```
   
   # Check the RBP configuration on BRAS1. The command output shows that the state of the local end is **Master** and that of the peer end is **Slave**.
   
   ```
   <BRAS1> display remote-backup-profile p1
   ```
   ```
   ----------------------------------------------------------
    Profile-Index        : 0x1000
    Profile-Name         : p1
    Service              : bras 
    Remote-backup-service: s1
    Backup-ID            : 1
    track protocol       : VRRP
    VRRP-ID              : 1
    VRRP-Interface       : GigabitEthernet0/3/6.1
    Access-Control       : --
    State                : Master
    Peer State           : Slave
    Interface            :
                           GigabitEthernet0/3/6.2
    Backup mode          : hot
    Slot-Number          : 3
    Card-Number          : 0
    Port-Number          : 6
    Traffic threshold       : 50(MB)
    Traffic interval       : 10(minutes)
    Forwarding Configured: Slave Forwarding 
   ```

#### Configuration Files

* BRAS1 configuration file
  
  ```
  #
  sysname BRAS1
  #
  license
   active bas slot 1
  #
  vlan batch 5 400
  #
  user-group web-before
  #
  radius-server group rd2
   radius-server shared-key-cipher %^%#0Iy%9Gu1),kLlP/jw;X-AOiZD%{YoCH<RC(P*>^5%^%#    
   radius-server authentication 192.168.8.249 1812 weight 0
   radius-server accounting 192.168.8.249 1813 weight 0
  #               
  radius-server group rd1
   radius-server shared-key-cipher %^%#)';d7xr::-'Nq3)5BO|-:WVZ7$|Tt,7rbP&tz\()%^%#    
   radius-server authentication 192.168.7.249 1812 weight 0
   radius-server accounting 192.168.7.249 1813 weight 0
   radius-server attribute translate
   radius-attribute include HW-Auth-Type
  #
  soc
  #
  ip dcn vpn-instance __dcn_vpn__
   ipv4-family
  #
  mpls lsr-id 10.1.1.1
  #
  mpls
  #
  mpls ldp
  #
  ipv4-family
  #               
  ip pool pool2 bas local
   gateway 172.16.1.1 255.255.255.0
   section 0 172.16.1.2 172.16.1.200
   dns-server 192.168.9.111
  #
  remote-backup-service s1
   peer 10.32.1.2 source 10.32.1.1 port 11000
   protect lsp-tunnel for-all-instance peer-ip 10.1.1.2
   web-auth-server source 192.168.8.252
  #
  remote-backup-profile p1
   service-type bras
   backup-id 1 remote-backup-service s1
   peer-backup hot
   vrrp-id 1 interface GigabitEthernet0/3/6.1
  #
  acl number 6004
   rule 3 permit ip source user-group web-before destination user-group web-before
   rule 5 permit ip source user-group web-before destination ip-address any
  #
  acl number 6005
   rule 5 permit ip source user-group web-before destination ip-address 192.168.8.251 0
   rule 15 permit ip source user-group web-before destination ip-address 192.168.9.111 0
  #
  acl number 6008
   rule 5 permit tcp source user-group web-before destination-port eq www
   rule 10 permit tcp source user-group web-before destination-port eq 8080
  #
  traffic classifier redirect operator or
   if-match acl 6008
  #
  traffic classifier web-be-deny operator or
   if-match acl 6004
  #
  traffic classifier web-be-permit operator or
   if-match acl 6005
  #
  traffic behavior deny1
   deny
  #
  traffic behavior perm1
  #
  traffic behavior redirect
   http-redirect plus
  #               
  traffic policy web
   share-mode
   classifier web-be-permit behavior perm1 precedence 1
   classifier redirect behavior redirect precedence 2
   classifier web-be-deny behavior deny1 precedence 4
  #
  aaa
   default-user-name include mac-address 
   default-password cipher @%@%UyQs4,KTtSwJo(4QmW#K,LC:@%@% 
   #
   authentication-scheme mac-auth
    authening authen-fail online authen-domain web-auth
   #
   authentication-scheme auth2
   #
   authentication-scheme auth3
    authentication-mode none
   #
   accounting-scheme acct2
   #
   accounting-scheme acct3
    accounting-mode none
   #
   domain mac-auth
    authentication-scheme mac-auth
    accounting-scheme acct2
    radius-server group rd1
    ip-pool pool2
    mac-authentication enable
   #
   domain web-auth
    authentication-scheme auth3
    accounting-scheme acct3
    ip-pool pool2 
    user-group web-before
    web-server 192.168.8.251
    web-server url http://192.168.8.251
    web-server redirect-key mscg-ip mscgip
    web-server redirect-key mscg-name mscgname
    web-server redirect-key user-ip-address userip
    web-server redirect-key nas-logic-sysname nasname
    web-server redirect-key user-mac-address usermac
    web-server redirect-key ssid wlan
   #
   domain after-auth
    authentication-scheme auth2
    accounting-scheme acct2
    radius-server group rd2
  #
  interface GigabitEthernet0/3/6.1
   vlan-type dot1q 400
   ip address 10.24.0.1 255.255.255.0
   vrrp vrid 1 virtual-ip 10.24.0.100
   admin-vrrp vrid 1
   vrrp vrid 1 priority 120
  #               
  interface GigabitEthernet0/3/6.2
   statistic enable
   user-vlan 5
   remote-backup-profile p1
   bas
   #
    access-type layer2-subscriber default-domain pre-authentication mac-auth authentication after-auth
    authentication-method web
   #
  #
  interface GigabitEthernet0/3/1
   undo shutdown
   ip address 10.32.1.1 255.255.255.0
   mpls
   mpls ldp
   dcn
  #
  interface LoopBack1
   ip address 10.1.1.1 255.255.255.255
  #
  ospf 1
   default cost inherit-metric
   import-route unr
   area 0.0.0.0
    network 10.1.1.1 0.0.0.0
    network 10.32.1.1 0.0.0.255
  #
  ospf 65534 vpn-instance __dcn_vpn__
   description DCN ospf create by default
   opaque-capability enable
   hostname
   vpn-instance-capability simple
   area 0.0.0.0
    network 0.0.0.0 255.255.255.255
  #
  ip ip-prefix 192 index 10 permit 192.168.1.0 24
  #
  route-policy rui permit node 1
   if-match ip-prefix 192
   apply cost 10
  #
  traffic-policy web inbound
  #
  return
  ```
* BRAS2 configuration file
  
  ```
  #
  license
   active bas slot 1
  #
  sysname BRAS2
  #
  vlan batch 5 400
  #
  user-group web-before
  #
  radius-server group rd2
   radius-server shared-key-cipher %^%#EQ0X4:387-4{QP9I,j.Dbx1rRedx2PO.j]HJZW1Y%^%#    
   radius-server authentication 192.168.8.249 1812 weight 0
   radius-server accounting 192.168.8.249 1813 weight 0
  #               
  radius-server group rd1
   radius-server shared-key-cipher %^%#3~8T2}\sbBuWA|)^$>07yX78&.Q(W3DG$p"|h`NH%^%#    
   radius-server authentication 192.168.7.249 1812 weight 0
   radius-server accounting 192.168.7.249 1813 weight 0
   radius-server attribute translate
   radius-attribute include HW-Auth-Type
  #
  soc
  #
  ip dcn vpn-instance __dcn_vpn__
   ipv4-family
  #
  mpls lsr-id 10.1.1.2
  #
  mpls
  #
  mpls ldp
  #
  ipv4-family
  #
  ip pool pool2 bas local rui-slave
   gateway 172.16.1.1 255.255.255.0
   # LOCAL        
    section 0 172.16.1.2 172.16.1.200 
    dns-server 192.168.9.111
   # REMOTE 
  #
  remote-backup-service s1
   peer 10.32.1.1 source 10.32.1.2 port 11000
   protect lsp-tunnel for-all-instance peer-ip 10.1.1.1
   web-auth-server source 192.168.8.252
  #
  remote-backup-profile p1
   service-type bras
   backup-id 1 remote-backup-service s1
   peer-backup hot
   vrrp-id 1 interface GigabitEthernet0/3/6.1
  #
  acl number 6004
   rule 3 permit ip source user-group web-before destination user-group web-before
   rule 5 permit ip source user-group web-before destination ip-address any
  #
  acl number 6005
   rule 5 permit ip source user-group web-before destination ip-address 192.168.8.251 0
   rule 15 permit ip source user-group web-before destination ip-address 192.168.9.111 0
  #
  acl number 6008
   rule 5 permit tcp source user-group web-before destination-port eq www
   rule 10 permit tcp source user-group web-before destination-port eq 8080
  #
  traffic classifier redirect operator or
   if-match acl 6008
  #
  traffic classifier web-be-deny operator or
   if-match acl 6004
  #
  traffic classifier web-be-permit operator or
   if-match acl 6005
  #
  traffic behavior deny1
   deny
  #
  traffic behavior perm1
  #
  traffic behavior redirect
   http-redirect plus
  #
  traffic policy web
   share-mode
   classifier web-be-permit behavior perm1 precedence 1
   classifier redirect behavior redirect precedence 2
   classifier web-be-deny behavior deny1 precedence 4
  #
  aaa
   default-user-name include mac-address 
   default-password cipher @%@%UyQs4,KTtSwJo(4QmW#K,LC:@%@% 
   #
   authentication-scheme auth2
   #
   authentication-scheme auth3
    authentication-mode none
   #
   authentication-scheme mac-auth
    authening authen-fail online authen-domain web-auth
   #
   accounting-scheme acct2
   #
   accounting-scheme acct3
    accounting-mode none
   #
   domain mac-auth
    authentication-scheme mac-auth
    accounting-scheme acct2
    radius-server group rd1
    ip-pool pool2
    mac-authentication enable
   #
   domain web-auth
    authentication-scheme auth3
    accounting-scheme acct3
    ip-pool pool2
    user-group web-before
    web-server 192.168.8.251
    web-server url http://192.168.8.251
    web-server redirect-key mscg-ip mscgip
    web-server redirect-key mscg-name mscgname
    web-server redirect-key user-ip-address userip
    web-server redirect-key nas-logic-sysname nasname
    web-server redirect-key user-mac-address usermac
    web-server redirect-key ssid wlan
   #
   domain after-auth
    authentication-scheme auth2
    accounting-scheme acct2
    radius-server group rd2
  #
  interface LoopBack1
   ip address 10.1.1.2 255.255.255.255
  #
  #
  interface GigabitEthernet0/3/2
   undo shutdown  
   ip address 10.32.1.2 255.255.255.0
   mpls
   mpls ldp
   dcn
  #
  interface GigabitEthernet0/3/6.1
   vlan-type dot1q 400
   ip address 10.24.0.2 255.255.255.0
   vrrp vrid 1 virtual-ip 10.24.0.100
   admin-vrrp vrid 1
   vrrp vrid 1 priority 110
  #
  interface GigabitEthernet0/3/6.2
   statistic enable
   user-vlan 5
   remote-backup-profile p1
   bas
   #
    access-type layer2-subscriber default-domain pre-authentication mac-auth authentication after-auth
    authentication-method web
   #
  #
  ospf 1
   default cost inherit-metric
   import-route unr
   area 0.0.0.0
    network 10.1.1.2 0.0.0.0
    network 10.32.1.2 0.0.0.255
  #
  ospf 65534 vpn-instance __dcn_vpn__
   description DCN ospf create by default
   opaque-capability enable
   hostname
   vpn-instance-capability simple
   area 0.0.0.0
    network 0.0.0.0 255.255.255.255
  #
  ip ip-prefix 192 index 10 permit 192.168.1.0 24
  #
  web-auth-server 192.168.8.251 port 50100 key cipher %^%#aQL6,Ua<|@sxPQK/1f'4/GBJ6,6)q>$Z^7*,!2yR%^%# 
  #
  traffic-policy web inbound
  #
  return
  ```