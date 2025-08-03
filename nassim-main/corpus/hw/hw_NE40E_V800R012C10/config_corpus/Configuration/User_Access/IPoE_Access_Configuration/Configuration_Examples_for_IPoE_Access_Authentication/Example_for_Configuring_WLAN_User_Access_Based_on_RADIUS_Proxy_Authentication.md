Example for Configuring WLAN User Access Based on RADIUS Proxy Authentication
=============================================================================

This section provides an example for configuring WLAN user access based on RADIUS proxy authentication.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172374060__fig_dc_ne_cfg_bras_001001), to allow WLAN users to access the network, RADIUS authentication needs to be performed on the AC through the EAP authentication mode, and RADIUS accounting needs to be performed through the Router. The user access process is as follows:

1. A WLAN user sends an EAP packet to the AC. The AC terminates the EAP packet and sends a RADIUS packet to the Router.
2. The Router functions as a RADIUS proxy to listen to and forward authentication packets sent by the AC to the RADIUS server, as well as authentication response packets sent in reply by the RADIUS server to the AC. During this process, the Router saves the authorization information delivered by the RADIUS server to the account.
3. After the authentication is successful, the user sends DHCP messages to the Router to obtain an IP address. The Router uses the user's MAC address to query the authorization information saved for the user account in the proxy process. If the user account's authorization information exists, the Router assigns an idle IP address to the user and uses the saved authorization information to authorize the user. The Router also sends an Accounting Start packet to the RADIUS server for user accounting.
4. The device responds to the accounting packets sent by the AC, without sending them to the RADIUS server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a large number of ACs or APs are connected to a BRAS, RADIUS proxy authentication is used to prevent these ACs or APs from sending authentication packets to the RADIUS server. RADIUS proxy authentication reduces the number of RADIUS clients that need to be managed by the RADIUS server. The BRAS transparently transmits RADIUS packets of specified RADIUS clients to the RADIUS server, records authorization information delivered by the RADIUS server, and transparently transmits authentication response packets to the RADIUS server.

**Figure 1** Networking for configuring WLAN user access based on RADIUS proxy authentication![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000002132051718.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure address pools.
2. Configure a RADIUS server group.
3. Configure AAA schemes.
4. Configure an AAA domain.
5. Configure an IP address for AC access on the interface.
6. Configure RADIUS proxy.
7. Configure RADIUS proxy for avalanche prevention.
8. Configure a DUID for the device.
9. Configure BAS access on an interface.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address of the RADIUS authentication server
* IP address of the RADIUS accounting server
* Interface IP address for the AC to send RADIUS packets

#### Procedure

1. Configure address pools.
   
   
   
   # Configure a local IPv4 address pool.
   
   ```
   [~HUAWEI] ip pool wifi1x bas local
   [*HUAWEI-ip-pool-wifi1x] gateway 172.30.0.1 24
   [*HUAWEI-ip-pool-wifi1x] commit
   [~HUAWEI-ip-pool-wifi1x] section 0 172.30.0.2 172.30.0.254
   [~HUAWEI-ip-pool-wifi1x] quit
   ```
   
   
   
   # Configure a local IPv6 prefix pool.
   
   ```
   [~HUAWEI] ipv6 prefix wifi local
   [*HUAWEI-ipv6-prefix-wifi] prefix 2001:db8:3::/48
   [*HUAWEI-ipv6-prefix-wifi] commit
   [~HUAWEI-ipv6-prefix-wifi] quit
   ```
   
   # Configure a local IPv6 address pool, and bind the prefix pool to this address pool.
   
   ```
   [~HUAWEI] ipv6 pool wifi bas local
   [*HUAWEI-ipv6-pool-wifi] prefix wifi
   [*HUAWEI-ipv6-pool-wifi] commit
   [~HUAWEI-ipv6-pool-wifi] quit
   ```
2. Configure a RADIUS server group.
   
   
   ```
   [~HUAWEI] radius-server group shiva
   [*HUAWEI-radius-shiva] radius-server shared-key-cipher YsHsjx_202206
   [*HUAWEI-radius-shiva] radius-server authentication 10.1.123.151 1812
   [*HUAWEI-radius-shiva] radius-server accounting 10.1.123.151 1813
   [*HUAWEI-radius-shiva] commit
   [~HUAWEI-radius-shiva] quit
   ```
3. Configure AAA schemes.
   
   
   
   # Configure a password for an IPoE user.
   
   ```
   [~HUAWEI] aaa
   [~HUAWEI-aaa] default-password cipher YsHsjx_202207
   [*HUAWEI-aaa] commit
   ```
   
   
   
   # Configure the pure username generation mode for the IPoE user.
   
   ```
   [~HUAWEI-aaa] default-user-name include mac-address -
   [*HUAWEI-aaa] commit
   ```
   
   # Configure an authentication scheme and set the authentication mode to RADIUS proxy authentication.
   
   ```
   [~HUAWEI-aaa] authentication-scheme rdp
   [*HUAWEI-aaa-authen-rdp] authentication-mode radius-proxy
   [*HUAWEI-aaa-authen-rdp] commit
   [~HUAWEI-aaa-authen-rdp] quit
   ```
   
   
   
   # Configure an accounting scheme named **rds**, with RADIUS accounting specified.
   
   ```
   [~HUAWEI-aaa] accounting-scheme rds
   [*HUAWEI-aaa-accounting-rds] accounting-mode radius
   [*HUAWEI-aaa-accounting-rds] commit
   [~HUAWEI-aaa-accounting-rds] quit
   ```
4. Configure an AAA domain and apply the authentication scheme **rdp**, accounting scheme **rds**, and RADIUS server group **shiva** to the domain.
   
   
   ```
   [~HUAWEI-aaa] domain radiusproxy
   [*HUAWEI-aaa-domain-radiusproxy] authentication-scheme rdp
   [*HUAWEI-aaa-domain-radiusproxy] accounting-scheme rds
   [*HUAWEI-aaa-domain-radiusproxy] radius-server group shiva
   [*HUAWEI-aaa-domain-radiusproxy] commit
   [~HUAWEI-aaa-domain-radiusproxy] ip-pool wifi1x
   [~HUAWEI-aaa-domain-radiusproxy] ipv6-pool wifi
   [~HUAWEI-aaa-domain-radiusproxy] quit
   [~HUAWEI-aaa] quit
   ```
5. Configure an IP address for AC access.
   
   
   ```
   [~HUAWEI] interface gigabitethernet 0/1/2
   [*HUAWEI-GigabitEthernet0/1/2] ip address 10.1.0.197 8
   [*HUAWEI-GigabitEthernet0/1/2] commit
   [~HUAWEI-GigabitEthernet0/1/2] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This IP address is used for AC access. RADIUS authentication packets sent by the AC must be sent to this address. If the device has another IP address for communication with the AC, this configuration is not needed.
6. Configure RADIUS proxy.
   
   
   
   # Configure the RADIUS client.
   
   
   
   ```
   [~HUAWEI] radius-client 10.1.0.201 server-group shiva shared-key-cipher YsHsjx_202208
   [*HUAWEI] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The IP address configured after [**radius-client**](cmdqueryname=radius-client) is the interface IP address to which the AC sends RADIUS packets. In this example, the RADIUS server group bound to the domain is the same as that for RADIUS proxy. In practice, the RADIUS server group bound to a domain may be different from that for RADIUS proxy.
   
   # Configure the local IP address used by the RADIUS server to create UDP sockets with local ports 1645, 1646, and 3799.
   
   ```
   [~HUAWEI] radius local-ip 10.1.0.197
   [*HUAWEI] commit
   ```
   
   # (Optional) Configure a DSCP value for RADIUS packets sent from the BRAS to the AC.
   
   To prevent RADIUS packets from being discarded due to network congestion, run the following commands to increase the DSCP value of RADIUS packets sent from the BRAS to a RADIUS proxy.
   
   ```
   [~HUAWEI] radius-client packet dscp 48
   [*HUAWEI] commit
   ```
7. (Optional) Configure RADIUS proxy for avalanche prevention.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To view RADIUS proxy statistics, run the [**display radius-client statistics global**](cmdqueryname=display+radius-client+statistics+global) command. If the RADIUS proxy continuously discards a large number of packets, you need to decrease the first packet processing rate of the RADIUS proxy, increase the suppression and recovery thresholds for the number of active RADIUS sessions, and increase the CPCAR and total CAR bandwidth for the RADIUS whitelist based on the processing capability of the BRAS.
   
   # Set the first packet processing rate of the RADIUS proxy.
   
   ```
   [~HUAWEI] radius-client first-packet rate 100
   [*HUAWEI] commit
   ```
   
   # Configure the suppression and recovery thresholds for the number of active sessions on the RADIUS proxy.
   
   ```
   [~HUAWEI] aaa
   [*HUAWEI-aaa] access-speed adjustment system-state radius-proxy active-session threshold restrain 200 resume 70
   [*HUAWEI-aaa] commit
   [~HUAWEI-aaa] quit
   ```
   
   # Configure CPCAR for the RADIUS whitelist.
   
   ```
   [~HUAWEI] cpu-defend policy 6
   [*HUAWEI-cpu-defend-policy-6] car whitelist radius cir 4000 cbs 1024000
   [*HUAWEI-cpu-defend-policy-6] commit
   [~HUAWEI-cpu-defend-policy-6] quit
   [~HUAWEI]slot 1
   [~HUAWEI-slot-1] cpu-defend-policy 6
   [*HUAWEI-slot-1] commit
   [~HUAWEI-slot-1] quit
   ```
   
   # Set the total rate for sending packets to the CPU.
   
   ```
   [~HUAWEI] cpu-defend policy 6
   [*HUAWEI-cpu-defend-policy-6] car total-packet high
   [*HUAWEI-cpu-defend-policy-6] commit
   [~HUAWEI-cpu-defend-policy-6] quit
   [~HUAWEI] slot 1
   [~HUAWEI-slot-1] cpu-defend-policy 6
   [*HUAWEI-slot-1] commit
   [~HUAWEI-slot-1] quit
   ```
8. Configure a DUID for the device.
   
   
   ```
   [~HUAWEI] dhcpv6 duid llt
   [*HUAWEI] commit
   ```
9. Configure BAS access on an interface.
   
   
   
   # Configure a sub-interface and a user-side VLAN.
   
   
   
   ```
   [~HUAWEI] interface gigabitethernet 0/1/1.1
   [*HUAWEI-GigabitEthernet0/1/1.1] commit
   [~HUAWEI-GigabitEthernet0/1/1.1] user-vlan 3000 3799 qinq 2700 2955
   [~HUAWEI-GigabitEthernet0/1/1.1-vlan-3000-3799-QinQ-2700-2955] quit
   ```
   
   # Enable IPv6 and configure stateful address autoconfiguration on the interface.
   
   ```
   [~HUAWEI-GigabitEthernet0/1/1.1] ipv6 enable
   [*HUAWEI-GigabitEthernet0/1/1.1] ipv6 address auto link-local
   [*HUAWEI-GigabitEthernet0/1/1.1] ipv6 nd autoconfig managed-address-flag 
   [*HUAWEI-GigabitEthernet0/1/1.1] commit
   ```
   
   # Configure BAS access on the interface.
   
   ```
   [~HUAWEI-GigabitEthernet0/1/1.1] bas
   [~HUAWEI-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication radiusproxy
   [*HUAWEI-GigabitEthernet0/1/1.1-bas] authentication-method bind
   [*HUAWEI-GigabitEthernet0/1/1.1-bas] authentication-method-ipv6 bind
   [*HUAWEI-GigabitEthernet0/1/1.1-bas] commit
   [~HUAWEI-GigabitEthernet0/1/1.1-bas] quit
   [~HUAWEI-GigabitEthernet0/1/1.1] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The BAS access configuration on an interface in RADIUS proxy scenarios is the same as that in IPoE access scenarios. RADIUS proxy applies only to IPoE users, not PPPoE users.
10. Verify the configuration.
    
    
    
    Run the [**display radius-server configuration group shiva**](cmdqueryname=display+radius-server+configuration+group+shiva) command on the device to view RADIUS server group configurations.
    
    ```
    [~HUAWEI] display radius-server configuration group shiva
      -------------------------------------------------------
    -------------------------------------------------------
      Server-group-name    :  shiva
      Authentication-server:  IP:10.1.123.151 Port:1812 Weight[0] [UP] [MASTER] 
                              Vpn: -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Authentication-server:  -
      Accounting-server    :  IP:10.1.123.151 Port:1813 Weight[0] [UP] [MASTER] 
                              Vpn: -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Accounting-server    :  -
      Protocol-version     :  radius
      Shared-secret-key    :  ******
      Retransmission       :  3
      Timeout-interval(s)  :  5
      Acct-Start-Packet Resend  :  NO
      Acct-Start-Packet Resend-Times  :  0
      Acct-Stop-Packet Resend  :  NO
      Acct-Stop-Packet Resend-Times  :  0
      Traffic-unit         :  B
      ClassAsCar           :  NO
      User-name-format     :  Domain-included
      Option82 parse mode  :  -
      Attribute-translation:  NO
      Packet send algorithm:  Master-Backup
      Tunnel password      :  cipher
      Attribute decode-error-policy list: -
      Trust server username:  NO
      Attach username in ACK:  -
      Qos-profile no-exist-policy  :  Offline
      Policy-name no-exist-policy  :  Offline
      Hw-domain-name block policy  :  Online
      Accounting-merge max-length  :  --
      Radius-attribute include agent-circuit-id value-added-service  :  FALSE
      Radius-attribute include agent-remote-id value-added-service  :  FALSE
      Radius-attribute include hw-avpair nat:nat-vpn :  FALSE
      Radius-attribute include hw-avpair nat:nat-export :  FALSE
      Radius-attribute include hw-avpair subscriber:fq :  FALSE
      Radius-attribute include class edsg :  FALSE
      Radius-attribute include class daa :  FALSE
      Radius-attribute include hw-acct-terminate-subcause :  FALSE
      Radius-attribute include hw-acct-terminate-subcause edsg :  FALSE
      Radius-attribute include hw-avpair subscriber:vpnid :  FALSE
      Radius-attribute include replymessage :  FALSE
      Acct-Interim-Packet Resend  :  NO
      Acct-Interim-Packet Resend-Times  :  0
      Nasport Bypass enable  :  0
      NAS-IP-Address using remote-ip: NO
      NAS-PORT using user-id: NO
      Radius-server alarm enable :  YES
    ```
    
    Run the [**display domain**](cmdqueryname=display+domain) command on the device to view domain configurations.
    
    ```
    [~HUAWEI] display domain radiusproxy
      ------------------------------------------------------------------------------
      Domain-name                     : radiusproxy                     
      Domain-state                    : Active
      Authentication-scheme-name      : rdp
      Accounting-scheme-name          : rds
      Authorization-scheme-name       : -
      Primary-DNS-IP-address          : -
      Second-DNS-IP-address           : -
      Primary-DNS-IPV6-address        : -
      Second-DNS-IPV6-address         : -
      Web-server-URL-parameter        : No
      Portal-server-URL-parameter     : No
      Primary-NBNS-IP-address         : -
      Second-NBNS-IP-address          : -
      Time-range                      : Disable
      Idle-cut direction              : Both
      Idle-data-attribute (time,flow) : 0, 60
      User detect interval            : 0s
      User detect retransmit times    : 0
      Install-BOD-Count               : 0
      Report-VSM-User-Count           : 0
      Value-added-service             : default
      User-access-limit               : 246272
      Online-number                   : 0
      Web-IP-address                  : -
      Web-IPv6-address                : -
      Dns-redirect-IP-address         : -
      Web-URL                         : -
      Web-auth-server                 : -
      Web-auth-state                  : -
      Web-server-mode                 : get
      Slave Web-IP-address            : -
      Slave Web-IPv6-address          : -
      Slave Web-URL                   : -
      Slave Web-auth-server           : -
      Slave Web-auth-state            : -
      Web-server identical-url        : Disable
      Portal-server-IP                : -
      Portal-URL                      : -
      Portal-force-times              : 2
      Portal-server identical-url     : Disable 
      Service-policy(Portal)          : - 
      Ds-lite IPv4 portal             : Disable
      PPPoE-user-URL                  : Disable
      AdminUser-priority              : 16
      IPUser-ReAuth-Time              : 300s
      mscg-name-portal-key            : -
      Portal-user-first-url-key       : -
      User-session-limit              : 4294967295
      Ancp auto qos adapt             : Disable
      L2TP-group-name                 : -
      User-lease-time-no-response     : 0s
      RADIUS-server-template          : shiva
      Two-acct-template               : -
      RADIUS-server-pre-template      : -
                                        -
                                        -
      RADIUS-server-llid-first-template: -
      HWTACACS-server-template        : -
      Bill Flow                       : Disable
      Tunnel-acct-2867                : Disable
      Qos-profile-name inbound        : -
      Qos-profile-name outbound       : -
     
      Flow Statistic:
      Flow-Statistic-Up               : Yes
      Flow-Statistic-Down             : Yes
      Source-IP-route                 : Disable
      IP-warning-threshold            : -
      IP-warning-threshold(Low)       : -
      IPv6-warning-threshold          : -
      IPv6-warning-threshold(Low)     : -
      Multicast Forwarding            : Yes
      Multicast Virtual               : No
      Max-multilist num               : 4
      Multicast-profile               : -
      Multicast-profile ipv6          : - 
      Multicast-policy                : - 
      Multicast-bandwidth             : - 
      Multicast-bandwidth-level-1     : -
      IP-address-pool-name            : wifi1x
      IPv6-Pool-name                  : wifi
      Quota-out                       : Offline
      Service-type                    : -
      User-basic-service-ip-type      : -/-/-
      PPP-ipv6-address-protocol       : Ndra
      IPv6-information-protocol       : Stateless dhcpv6
      IPv6-PPP-assign-interfaceid     : Disable
      IPv6-PPP-NDRA-halt              : Disable
      IPv6-PPP-NDRA-unicast           : Disable
      Trigger-packet-wait-delay       : 60s
      Peer-backup                     : Enable
      Reallocate-ip-address           : Disable
      Cui  enable                     : Disable 
      Igmp enable                     : Enable 
      CPE IP address                  : -
      Pim snooping enable             : Enable
      L2tp-user radius-force          : Disable
      Accounting dual-stack           : Separate
      Radius server domain-annex      : -
      Dhcp-option64-service           : Disable
      Parse-separator                 : -
      Parse-segment-value             : -
      Dhcp-receive-server-packet      : -
      Http-hostcar                    : Disable
      Public-address assign-first     : Disable 
      Public-address nat              : Enable
      Dhcp-user auto-save             : Disable
      IP-pool usage-status threshold  : 255 , 255 
      Select-Pool-Rule                : gateway + local priority 
      AFTR name                       : - 
      Traffic-rate-mode               : Separate 
      Traffic-statistic-mode          : Separate 
      Rate-limit-mode-inbound         : Car 
      Rate-limit-mode-outbound        : Car 
      Service-change-mode             : Stop-start 
      DAA Direction                   : both 
      Session Volumequota apply direction: both
      Nas logic-sysname               : -
      Accounting exclude-type vlan    : -/-
      Framed-ip urpf                  : Enable
      RA link-prefix                  : Disable 
      Dslam connect speed             : Disable 
      Local backup                    : Enable 
      DAA start accounting merge      : disable 
      DAA stop accounting merge       : disable 
      DAA interim accounting merge    : disable 
      DAA merged interim accounting interval(minute) : -- 
      DAA merged interim accounting hash  : disable 
      EDSG stop accounting merge      : disable 
      EDSG interim accounting merge   : disable 
      EDSG merged interim accounting interval(minute): -- 
      EDSG merged interim accounting hash : disable 
      Stop dropped flow direction     : - 
      Interval dropped flow direction : - 
      Edsg family-schedule inbound    : Disable 
      Edsg family-schedule outbound   : Disable 
      Layer2 IPoE ip-pool select-mode : Local 
      Layer2 PPPoE ip-pool select-mode: Local
      access-trigger loose time(minute)   : 0
      access-trigger loose infinite-lease : Disable
      IPv6 address assignment mode    : - 
      LNS Tcp-Ack Priority-Car        : Disable 
      EDSG Tcp-Ack Priority-Car       : Disable 
      Include LNS-IPv6                : Disable
      Map priority                    : MAP-E
      Coa-zero-lease Dual-cut         : Disable
      COA lease zero policy           : -
      Authentication fail online domain : -
      ipv6-address authorization      : Enable
      Traffic-policy ucl upstream match-source-ip : Disable
      ------------------------------------------------------------------------------
    ```
    
    Run the [**display radius-client configuration**](cmdqueryname=display+radius-client+configuration) command on the device to view RADIUS proxy configurations.
    
    ```
    [~HUAWEI] display radius-client configuration
      Radius-client packet dscp value: 48
      Radius-client first packet rate (unit: pps): 100
      Radius-client nas-ip-address from packet : SOURCE_IP
      -----------------------------------------------------------------------------
      IP-Address       Mask             VPN-instance          Group
      Domain-authorization   Roam-domain      Trigger-web
      -----------------------------------------------------------------------------
      10.1.0.201       255.255.255.255  --                    shiva           
      NO                     --               ACCT_TRIGGER
     
      -----------------------------------------------------------------------------
      1 Radius client(s) in total  
    ```

#### Configuration Files

```
#
sysname HUAWEI
#
cpu-defend policy 6
 car whitelist radius cir 4000 cbs 1024000
 car total-packet high
#
slot 1
 cpu-defend-policy 6
#
radius-server group shiva
 radius-server shared-key-cipher %+%##!!!!!!!!!"!!!!'!!!!(!!!!*j}18H7WTV^zEAUblld-@40X-I[F@/Qly@ALX^F%2jp5!!!!!!A!!!!B9yVKme:499+wNV>.W7>+-!GWwqyaJ%6B3,=e~rO%+%#
 radius-server authentication 10.1.123.151 1812 weight 0
 radius-server accounting 10.1.123.151 1813 weight 0
#
radius local-ip 10.1.0.197
#
ip pool wifi1x bas local
 gateway 172.30.0.1 255.255.255.0
 section 0 172.30.0.2 172.30.0.254
#
ipv6 prefix wifi local
 prefix 2001:DB8:3::/48
#
ipv6 pool wifi bas local
 prefix wifi
#
dhcpv6 duid 000100012ba5fc198038bc19704d
#
aaa
 default-password cipher %@%##!!!!!!!!!"!!!!'!!!!(!!!!*j}18H7WTVZ&V`0v5PlMaY,<~8'a+L*fILUqdM,22jp5!!!!!!A!!!!0+1,B8UxW(2M8i$X1T_,iL*C%Yu=jLP9vH2v&q|;%@%#
 default-user-name include mac-address -
 access-speed adjustment system-state radius-proxy active-session threshold restrain 200 resume 70
 #
 authentication-scheme rdp
  authentication-mode radius-proxy
 #
 accounting-scheme rds
 #
 domain radiusproxy
  authentication-scheme rdp
  accounting-scheme rds
  radius-server group shiva 
  ip-pool wifi1x
  ipv6-pool wifi
#
radius-client packet dscp 48
radius-client first-packet rate 100
radius-client 10.1.0.201 mask 255.255.255.255 shared-key-cipher %^%#}v{/ZA}>yTiC'[0bvy'X"N[+,uj*U)L0^5;4Jtf6%^%# server-group shiva
#
license
 active bas slot 1
#
interface GigabitEthernet 0/1/1.1
 ipv6 enable
 ipv6 address auto link-local
 statistic enable
 user-vlan 3000 3799 qinq 2700 2955
 ipv6 nd autoconfig managed-address-flag
 bas
 #
  access-type layer2-subscriber default-domain authentication radiusproxy
  authentication-method bind
  authentication-method-ipv6 bind
 #
#
interface GigabitEthernet 0/1/2
 undo shutdown
 ip address 10.1.0.197 255.0.0.0
#
return
```