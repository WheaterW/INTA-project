Example for Configuring User-Side Multicast for IPoE Access Users
=================================================================

This section provides an example for configuring user-side multicast service for Internet Protocol over Ethernet (IPoE) access users.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367670__fig_dc_vrp_bras-multicast_cfg_000901), users (with PC1 and PC2) are IPoE access users, and they want to join multicast programs. Configure user-side multicast to implement user-based on-demand multicast data forwarding.

**Figure 1** Configuring user-side multicast for IPoE access users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and interface 2 in this example stand for GE 0/1/0 and GE 0/1/1.1, respectively.


  
![](images/fig_dc_vrp_bras-multicast_cfg_000801.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IPv4 address pool.
2. Configure Authentication, Authorization and Accounting (AAA) schemes.
3. Configure a domain.
4. Configure the IPoE access mode:
   
   1. Configure an authentication scheme.
   2. Bind a sub-interface to a VLAN.
   3. Configure a BAS interface and specify a user access type for the interface. (The BAS interface can be a main interface, a common sub-interface, or a QinQ sub-interface. A common sub-interface is used in the example.)
5. Enable multicast traffic replication by session on the BAS interface.
6. Configure basic multicast functions:
   
   1. Enable multicast routing.
   2. Enable Protocol Independent Multicast-Sparse Mode (PIM-SM) on all BRAS interfaces.
   3. Enable IGMP on the BRAS interface connected to users.

#### Data Preparation

* IPv4 address pool
* Authentication and accounting schemes (user authentication on the BRAS through RADIUS)
* User domain
* BAS interface parameters

#### Procedure

1. Configure an IPv4 address pool.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [HUAWEI] sysname BRAS
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS] ip pool huawei bas local
   ```
   ```
   [*BRAS-ip-pool-huawei] gateway 172.16.0.1 255.255.0.0
   ```
   ```
   [*BRAS-ip-pool-huawei] commit
   ```
   ```
   [~BRAS-ip-pool-huawei] section 1 172.16.0.1 172.16.255.255
   ```
   ```
   [*BRAS-ip-pool-huawei] quit
   ```
   ```
   [*BRAS] commit
   ```
2. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   [~BRAS] aaa
   ```
   ```
   [*BRAS-aaa] authentication-scheme radius
   ```
   ```
   [*BRAS-aaa-authen-radius] authentication-mode radius
   ```
   ```
   [*BRAS-aaa-authen-radius] quit
   ```
   ```
   [*BRAS-aaa] commit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~BRAS-aaa] accounting-scheme none
   ```
   ```
   [*BRAS-aaa-accounting-none] accounting-mode none
   ```
   ```
   [*BRAS-aaa-accounting-none] quit
   ```
   ```
   [*BRAS-aaa] quit
   ```
   ```
   [*BRAS] commit
   ```
3. Configure a RADIUS server group.
   
   
   
   # Configure a RADIUS server group named **shiva**.
   
   ```
   [~BRAS] radius-server group shiva
   ```
   
   # Configure an IP address and port numbers for the primary RADIUS authentication and accounting server.
   
   ```
   [*BRAS-radius-shiva] radius-server authentication 10.7.66.66 1812
   ```
   ```
   [*BRAS-radius-shiva] radius-server accounting 10.7.66.66 1813
   ```
   
   # Configure a shared key and the number of retransmissions for the RADIUS server.
   
   ```
   [*BRAS-radius-shiva] radius-server shared-key-cipher YsHsjx_202206
   ```
   ```
   [*BRAS-radius-shiva] radius-server retransmit 2
   ```
   ```
   [*BRAS-radius-shiva] commit
   ```
   ```
   [~BRAS-radius-shiva] quit
   ```
4. Configure a domain.
   
   
   ```
   [~BRAS] aaa
   ```
   ```
   [*BRAS-aaa] domain ipv4
   ```
   ```
   [*BRAS-aaa-domain-ipv4] authentication-scheme radius
   ```
   ```
   [*BRAS-aaa-domain-ipv4] accounting-scheme none
   ```
   ```
   [*BRAS-aaa-domain-ipv4] radius-server group shiva
   ```
   ```
   [*BRAS-aaa-domain-ipv4] ip-pool huawei
   ```
   ```
   [*BRAS-aaa-domain-ipv4] quit
   ```
   ```
   [*BRAS-aaa] quit
   ```
   ```
   [*BRAS] commit
   ```
5. Bind a sub-interface to a VLAN.
   
   
   ```
   [~BRAS] interface gigabitethernet 0/1/1.1
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] user-vlan 2
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-vlan-2-2] quit
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] commit
   ```
6. Configure a BAS interface, specify a user access type for the interface, and configure an authentication scheme.
   
   
   ```
   [~BRAS-GigabitEthernet0/1/1.1] bas
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication ipv4
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] authentication-method bind
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] quit
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] commit
   ```
   # Run the **display access-user domain ipv4** command to display online user information. The command output shows that users with ID 352 and 353 accessed the Internet through IPoE.
   ```
   [~BRAS] display access-user domain ipv4
     ------------------------------------------------------------------------------
     UserID  Username                Interface      IP address       MAC
             Vlan          IPv6 address             Access type
     ------------------------------------------------------------------------------
     352     BRAS-01008000100000...  GE0/1/1.1      172.16.1.2          00-e0-fc-12-34-561
             1/-           -                        IPOE
     353     BRAS-01008000300002...  GE0/1/1.1      172.16.1.3          00-e0-fc-22-34-56
             3/2           -                        IPOE
     ------------------------------------------------------------------------------
     Normal users                       : 2
     RUI Local users                    : 0
     RUI Remote users                   : 0
     Total users                        : 2
   
   ```
7. Enable multicast traffic replication by session on the BAS interface.
   
   
   ```
   [~BRAS-GigabitEthernet0/1/1.1] bas
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] multicast copy by-session
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] quit
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*BRAS] commit
   ```
8. Configure basic multicast functions.
   
   
   ```
   [~BRAS] multicast routing-enable
   ```
   ```
   [*BRAS] interface gigabitethernet 0/1/0
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] quit
   ```
   ```
   [*BRAS] commit
   ```
   ```
   [~BRAS] interface gigabitethernet 0/1/1.1
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] pim sm
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] igmp enable
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*BRAS] commit
   ```
9. Verify the configuration.
   
   # Run the **display multicast group-ip** command to display information about users of a specified multicast group. The command output shows that users with ID 352 and 353 joined multicast programs whose group address is 225.0.0.1.
   ```
   [~BRAS] display multicast group-ip 225.0.0.1 out-interface GigabitEthernet 0/1/1.1
     User ID    User IP                     User type    Interface
   
     352        172.16.1.2                     Local        GigabitEthernet0/1/1.1
     353        172.16.1.3                     Local        GigabitEthernet0/1/1.1
   
     Local user number :2
     Remote user number:0
     Total user number :2     
   ```
   
   # Run the **display multicast user-id** command to check the multicast programs that a specified user joined on a BAS interface. The following uses the user whose ID is 353 as an example:
   ```
   [~BRAS] display multicast user-id 353
     User information:
     User ID             :353
     User IPv4 address   :172.16.1.3
     Gateway IPv4 address:172.16.0.1
     BRAS interface      :GigabitEthernet0/1/1.1
     User MAC-address    :00-e0-fc-22-34-56
     MAX program list    :4
   
     User order program:
     Group IP           Source IP
     225.0.0.1          0.0.0.0
   
     Total:1                       
   ```
   
   # Run the **display pim routing-table** command to display PIM routing entries.
   ```
   [~BRAS] display pim routing-table
    VPN-Instance: public net
    Total 1 (*, G) entry; 1 (S, G) entry
   
    (*, 225.0.0.1)
        RP: NULL
        Protocol: pim-sm, Flag: WC NIIF
        UpTime: 01:37:51
        Upstream interface: NULL, Refresh time: 01:37:51
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1(bas)
                Protocol: igmp, UpTime: 01:37:51, Expires: -
   
    (10.1.1.100, 225.0.0.1)
        RP: NULL
        Protocol: pim-sm, Flag: SPT LOC ACT
        UpTime: 04:34:52
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 04:34:52
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1(bas)
                Protocol: pim-sm, UpTime: 01:37:51, Expires: -  
   ```

#### Configuration Files

```
#
sysname BRAS
#
multicast routing-enable
#
ip pool huawei bas local
 gateway 172.16.0.1 255.255.0.0
 section 1 172.16.0.1 172.16.255.255
#
radius-server group shiva                                                       
 radius-server authentication 10.7.66.66 1812 weight 0                                             
 radius-server accounting 10.7.66.66 1813 weight 0                                                        
 radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
 radius-server retransmit 2                                                    
# 
aaa
 #
 authentication-scheme radius
  authentication-mode radius
 #
 accounting-scheme none
  accounting-mode none
 #
 domain ipv4
  authentication-scheme radius
  accounting-scheme none
  radius-server group shiva
  ip-pool huawei
#
interface GigabitEthernet0/1/0
 undo shutdown
 ip address 10.1.1.1 255.255.255.0
 pim sm
#
interface GigabitEthernet0/1/1.1
 user-vlan 2 
 pim sm
 igmp enable
 bas
 #
  access-type layer2-subscriber default-domain authentication ipv4
  authentication-method bind
  multicast copy by-session
#
return  
```