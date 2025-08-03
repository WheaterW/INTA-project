Example for Configuring User-side Multicast CAC for PPPoE Access Users
======================================================================

This section provides an example for configuring user-side multicast CAC for PPPoE access users.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367677__fig_dc_ne_bras-multicast_cac_cfg_000201), PC1 and PC2 are PPPoE access users. You are required to configure user-side multicast CAC to meet the following requirements:

* PC1 and PC2 belong to the IPv4 domain and access the network through GE 0/1/0 in PPPoE mode.
* In this example, RADIUS authentication and non-accounting are used.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + Supported authentication modes: RADIUS, and none
  + Supported accounting modes: RADIUS, and none
* After going online, users order programs with multicast group addresses 235.1.1.1 and 236.1.1.1.
* The BRAS uses GE 0/1/0 to communicate with the access network device and uses GE 0/1/1 and GE 0/1/2 to communicate with the PIM-SM devices.

**Figure 1** Configuring user-side multicast CAC for PPPoE access users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example is GE 0/1/0.

![](images/fig_dc_ne_bras-multicast_cac_cfg_000201.png)



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IPv4 address pool.
2. Configure AAA schemes.
3. Configure a domain.
4. Configure the PPPoE access service:
   
   1. Configure a VT interface.
   2. Bind the VT interface to a GE interface.
   3. Configure the GE interface as a BAS interface and set the user access mode.
5. Enable multicast traffic replication by session on the BAS interface.
6. Configure basic multicast functions:
   
   1. Enable multicast routing.
   2. Enable PIM-SM on interfaces on the BRAS.
   3. Enable IGMP on the BRAS interface connected to users.
7. Configure user-side multicast CAC:
   
   1. Configure a multicast bandwidth limit policy.
   2. Bind the multicast bandwidth limit policy to the AAA domain.
   3. Bind the multicast bandwidth limit policy to the BRAS interface connected to users.
   4. Enable user-side multicast CAC on a specific interface board.

#### Data Preparation

* IPv4 address pool name, address range, and gateway address
* Authentication and accounting schemes (user authentication on the BRAS through RADIUS)
* Name of the domain to which users belong
* VT interface number
* BAS interface parameters

#### Procedure

1. Configure an IPv4 address pool.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname BRAS
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~BRAS] ip pool ipv4 bas local
   ```
   ```
   [*BRAS-ip-pool-ipv4] gateway 10.0.0.1 255.255.0.0
   ```
   ```
   [*BRAS-ip-pool-ipv4] commit
   ```
   ```
   [~BRAS-ip-pool-ipv4] section 1 10.0.0.1 10.0.255.255
   ```
   ```
   [*BRAS-ip-pool-ipv4] quit
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
   [~BRAS-aaa] authentication-scheme radius
   ```
   ```
   [*BRAS-aaa-authen-radius] authentication-mode radius
   ```
   ```
   [*BRAS-aaa-authen-radius] commit
   ```
   ```
   [~BRAS-aaa-authen-radius] quit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~BRAS-aaa] accounting-scheme none
   ```
   ```
   [*BRAS-aaa-accounting-none] accounting-mode none
   ```
   ```
   [*BRAS-aaa-accounting-none] commit
   ```
   ```
   [~BRAS-aaa-accounting-none] quit
   ```
   ```
   [~BRAS-aaa] quit
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
   [~BRAS-aaa] domain ipv4
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
   [*BRAS-aaa-domain-ipv4] commit
   ```
   ```
   [~BRAS-aaa-domain-ipv4] ip-pool ipv4
   ```
   ```
   [~BRAS-aaa-domain-ipv4] quit
   ```
   ```
   [~BRAS-aaa] quit
   ```
5. Configure a VT interface.
   
   
   ```
   [~BRAS] interface virtual-template 100
   ```
   ```
   [*BRAS-Virtual-Template100] ppp authentication-mode chap
   ```
   ```
   [*BRAS-Virtual-Template100] commit
   ```
   ```
   [~BRAS-Virtual-Template100] quit
   ```
6. Bind the VT to an interface.
   
   
   ```
   [~BRAS] interface GigabitEthernet0/1/0
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0] pppoe-server bind virtual-template 100
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] commit
   ```
7. Configure a BAS interface and specify a user access type for the interface.
   
   
   ```
   [~BRAS-GigabitEthernet0/1/0] bas
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0-bas] access-type layer2-subscriber default-domain authentication ipv4
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0-bas] quit
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] commit
   ```
   # Run the **display access-user domain ipv4** command to check information about online users. The command output shows that the users with IDs 1280 and 1281 have gone online in PPPoE mode.
   ```
   [~BRAS] display  access-user domain ipv4
     ------------------------------------------------------------------------------
     UserID  Username       Interface      IP address       MAC
             Vlan           IPv6 address   Access type
     ------------------------------------------------------------------------------
     1280    PC1@ipv4       GE0/1/0          10.0.0.1    00-e0-fc-22-34-56
             -/-            -              PPPoE
     1281    PC2@ipv4       GE0/1/0          10.0.0.2    00-e0-fc-12-34-56
             -/-            -              PPPoE
     ------------------------------------------------------------------------------
     Normal users                       : 2
     RUI Local users                    : 0
     RUI Remote users                   : 0
     Total users                        : 2      
   ```
8. Enable multicast traffic replication by session on the BAS interface.
   
   
   ```
   [~BRAS-GigabitEthernet0/1/0] bas
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0-bas] multicast copy by-session
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0-bas] commit
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0-bas] quit
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0] quit
   ```
9. Configure basic multicast functions.
   
   
   ```
   [~BRAS] multicast routing-enable
   ```
   ```
   [*BRAS] interface GigabitEthernet 0/1/1
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1] ip address 10.1.1.1 255.255.255.0
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1] quit
   ```
   ```
   [*BRAS] interface GigabitEthernet 0/1/2
   ```
   ```
   [*BRAS-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*BRAS-GigabitEthernet0/1/2] ip address 10.1.2.1 255.255.255.0
   ```
   ```
   [*BRAS-GigabitEthernet0/1/2] pim sm
   ```
   ```
   [*BRAS-GigabitEthernet0/1/2] quit
   ```
   ```
   [*BRAS] commit
   ```
   ```
   [~BRAS] interface gigabitethernet 0/1/0
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0] pim sm
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] igmp enable
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] quit
   ```
   ```
   [*BRAS] commit
   ```
10. Verify the configuration.
    
    
    
    # After users go online, run the **display access-user** command to check information about users.
    
    ```
    [~BRAS] display access-user username PC1@ipv4
    ```
    ```
      --------------------------------------------------------------------------
      UserID     Username               Interface      IP address       MAC
                  Vlan                 IPv6 address    Access type
      --------------------------------------------------------------------------
      1          PC1@ipv4               GE0/1/0            10.0.0.1    00-e0-fc-22-34-56
                  -/-                   -               PPPoE
      --------------------------------------------------------------------------
      Normal users                       : 1
      RUI Local users                    : 0
      RUI Remote users                   : 0
      Total users                        : 1      
    
    ```
    ```
    [~BRAS] display access-user username PC2@ipv4
    ```
    ```
      --------------------------------------------------------------------------
      UserID    Username               Interface      IP address       MAC
                 Vlan                  IPv6 address   Access type
      --------------------------------------------------------------------------
      2         PC2@ipv4               GE0/1/0            10.0.0.2    00-e0-fc-12-34-56
                  -/-                   -               PPPoE
      --------------------------------------------------------------------------
      Normal users                       : 1
      RUI Local users                    : 0
      RUI Remote users                   : 0
      Total users                        : 1      
    ```
11. Configure user-side multicast CAC.
    
    
    
    # Configure a multicast bandwidth limit policy globally.
    
    ```
    [~BRAS] multicast bas-policy
    ```
    ```
    [~BRAS-multicast-bas-policy] policy policy1
    ```
    ```
    [~BRAS-multicast-bas-policy-policy1] unspecified-channel permit
    ```
    ```
    [~BRAS-multicast-bas-policy-policy1] channel huawei
    ```
    ```
    [~BRAS-multicast-bas-policy-policy1-channel-huawei] group 235.1.1.1 mask 32 source 1.1.1.1 mask 24 per-bandwidth 1000 level-1
    ```
    ```
    [~BRAS-multicast-bas-policy-policy1-channel-huawei] group 236.1.1.1 mask 32 source 2.1.1.1 mask 24 per-bandwidth 2000 level-1
    ```
    ```
    [~BRAS-multicast-bas-policy-policy1-channel-huawei] quit
    ```
    ```
    [~BRAS-multicast-bas-policy-policy1] quit
    ```
    ```
    [~BRAS-multicast-bas-policy] quit
    ```
    
    # Configure a multicast bandwidth limit policy and limit the bandwidth of each user in the AAA domain.
    
    ```
    [~BRAS] aaa
    ```
    ```
    [~BRAS-aaa] domain ipv4
    ```
    ```
    [~BRAS-aaa-domain-ipv4] multicast bas-policy policy1 out bandwidth 10000 level-1 8000 interface GigabitEthernet
    ```
    ```
    [~BRAS-aaa-domain-ipv4] quit
    ```
    ```
    [~BRAS-aaa] quit
    ```
    
    # Configure a multicast bandwidth limit policy and limit the bandwidth on the interface through which users go online.
    
    ```
    [~BRAS] interface GigabitEthernet0/1/0
    ```
    ```
    [~BRAS-GigabitEthernet0/1/0] multicast bas-policy policy1 out bandwidth 30000 level-1 20000
    ```
    ```
    [~BRAS-GigabitEthernet0/1/0] quit
    ```
    
    # Enable user-side multicast CAC on the interface board through which users go online.
    
    ```
    [~BRAS] slot 1
    ```
    ```
    [~BRAS-slot-1] multicast bas-policy out enable interface gigabitethernet
    ```
    ```
    [~BRAS-slot-1] quit
    ```
12. Verify the configuration.
    
    
    
    # Run the [**display multicast bas-policy policy**](cmdqueryname=display+multicast+bas-policy+policy) command to check information about global policy entries delivered to an interface board.
    
    ```
    <HUAWEI> display multicast bas-policy policy policy1 slot 1
    Policy Index: 1
    Unspecified-Channel Permit: Enable 
    ----------------------------------------------------------------------------------------------
    Channel Index:0
    Group-Address    Mask  Source-Address  Mask  Bandwidth(kbit/s)  Level
    235.1.1.1       32    1.1.1.1       24    1000               1
    236.1.1.1       32    2.1.1.1       24    1000               1
    -----------------------------------------------------------------------------------------------
    ```
    
    # Run the [**display multicast bas-policy out user**](cmdqueryname=display+multicast+bas-policy+out+user) command to check the multicast BAS policy and bandwidth statistics of a specified user.
    
    ```
    <HUAWEI> display multicast bas-policy out user 1
    ```
    ```
    User-ID: 1 
      Policy Index: 1
        Bandwidth(kbit/s): 10000 
        Level-1(kbit/s): 8000
        Level-2(kbit/s): 2000
        Used-Bandwidth(kbit/s): 5000 
        Used-Level-1(kbit/s): 3000
        Used-Level-2(kbit/s): 2000
    
    ```
    
    # Run the [**display multicast bas-policy out interface**](cmdqueryname=display+multicast+bas-policy+out+interface) command to check information about the multicast bandwidth limit policy of a specific interface.
    
    ```
    <HUAWEI> display multicast bas-policy out interface GigabitEthernet0/1/0
    ```
    ```
    Interface: GigabitEthernet0/1/0 
      Policy Index: 1
       Bandwidth(kbit/s): 30000 
       Level-1(kbit/s): 20000 
       Level-2(kbit/s): 10000
       Used-Bandwidth(kbit/s): 10000 
       Used-Level-1(kbit/s): 8000
       Used-Level-2(kbit/s): 2000
    
    ```

#### Configuration Files

```
#
sysname BRAS
#
multicast routing-enable
#
ip pool ipv4 bas local
 gateway 10.0.0.1 255.255.0.0
 section 1 10.0.0.1 10.0.255.255
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
  ip-pool ipv4
  multicast bas-policy policy1 out bandwidth 10000 level-1 8000 interface GigabitEthernet
#
interface Virtual-Template100
 ppp authentication-mode chap
#
interface GigabitEthernet0/1/0
 pppoe-server bind Virtual-Template 100
 pim sm
 igmp enable
 bas
 #
  access-type layer2-subscriber default-domain authentication ipv4
  multicast copy by-session
 #
 multicast bas-policy policy1 out bandwidth 30000 level-1 20000
#
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 10.1.1.1 255.255.255.0
 pim sm
#
interface GigabitEthernet0/1/2
 undo shutdown
 ip address 10.1.2.1 255.255.255.0
 pim sm
#
multicast bas-policy
 policy policy1
  unspecified-channel permit
  channel huawei
   group 235.1.1.1 mask 32 source 1.1.1.1 mask 24 per-bandwidth 1000 level-1
   group 236.1.1.1 mask 32 source 2.1.1.1 mask 24 per-bandwidth 2000 level-1
#
slot 1
 multicast bas-policy out enable interface GigabitEthernet
#
return  
```