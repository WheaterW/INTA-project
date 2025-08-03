Example for Configuring IPv6 Static Multicast for IPoE Access Users
===================================================================

This section provides an example for configuring IPv6 static multicast for IPoE access users.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367729__fig_dc_vrp_bras-multicast_cfg_000901), the user PC supports the IPoE access mode. Configure static multicast to allow the PC user to receive the traffic of specific multicast programs without sending join messages.

**Figure 1** Configuring IPv6 static multicast for IPoE access users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 and interface 2 in this example stand for GE 0/1/0 and GE 0/1/1.1, respectively.


  
![](images/fig_dc_vrp_ipv6bras-multicast_cfg_000801_ne.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure AAA schemes.
2. Configure a local IPv6 prefix pool.
3. Configure a local IPv6 address pool and bind the local IPv6 prefix pool to the local address pool.
4. Configure an AAA domain and bind it to the IPv6 address pool.
5. Configure the IPoE access service:
   
   1. Configure an authentication scheme.
   2. Bind a sub-interface to a VLAN.
   3. Configure a BAS interface and specify a user access type for the interface.
6. Configure a multicast replication mode. Multicast replication by interface + VLAN is used as an example.
7. Configure basic multicast functions:
   
   1. Enable IPv6 multicast routing.
   2. Enable IPv6 PIM-SM on the interfaces of the BRAS.
   3. Enable MLD on the BRAS interface connected to the user.
8. Configure static multicast:
   
   1. Configure an IPv6 multicast program list in the AAA view.
   2. Configure a multicast profile in the AAA view.
   3. Bind the multicast profile to the AAA domain.

#### Data Preparation

* Local prefix pool, address prefix, and prefix length parameters
* Local address pool parameters
* Authentication and accounting schemes (user authentication on the BRAS through RADIUS)
* User domain
* BAS interface parameters

#### Procedure

1. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
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
   [~BRAS] aaa
   ```
   ```
   [~BRAS-aaa] authentication-scheme radius
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
2. Configure a local IPv6 prefix pool.
   
   
   ```
   [~BRAS] ipv6 prefix huawei local
   ```
   ```
   [~BRAS-ipv6-prefix-ipv6] prefix 2001:db8:1::/64
   ```
   ```
   [~BRAS-ipv6-prefix-ipv6] quit
   ```
3. Configure a local IPv6 address pool and bind the local IPv6 prefix pool to the local address pool.
   
   
   ```
   [~BRAS] ipv6 pool poolname bas local
   ```
   ```
   [~BRAS-ipv6-pool-ipv6] prefix ipv6
   ```
   ```
   [~BRAS-ipv6-pool-ipv6] quit
   ```
4. Configure a RADIUS server group.
   
   
   
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
5. Configure a domain and bind the local address pool to the domain.
   
   
   ```
   [~BRAS] aaa
   ```
   ```
   [*BRAS-aaa] domain wdomain
   ```
   ```
   [*BRAS-aaa-domain-wdomain] authentication-scheme radius
   ```
   ```
   [*BRAS-aaa-domain-wdomain] accounting-scheme none
   ```
   ```
   [*BRAS-aaa-domain-wdomain] radius-server group shiva
   ```
   ```
   [*BRAS-aaa-domain-wdomain] ipv6-pool poolname
   ```
   ```
   [*BRAS-aaa-domain-wdomain] quit
   ```
   ```
   [*BRAS-aaa] quit
   ```
   ```
   [*BRAS] commit
   ```
6. Bind a sub-interface to a VLAN.
   
   
   ```
   [~BRAS] interface gigabitethernet 0/1/1.1
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] user-vlan 133
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-vlan-133-133] quit
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] commit
   ```
7. Configure a BAS interface, specify a user access type for the interface, and configure an authentication scheme.
   
   
   ```
   [~BRAS-GigabitEthernet0/1/1.1] bas
   ```
   ```
   [~BRAS-GigabitEthernet0/1/1.1-bas] access-type layer2-subscriber default-domain authentication wdomain
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] authentication-method-ipv6 bind
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
8. Enable multicast traffic replication by interface + VLAN on the BAS interface.
   
   
   ```
   [~BRAS] interface gigabitethernet 0/1/1.1
   ```
   ```
   [~BRAS-GigabitEthernet0/1/1.1] bas
   ```
   ```
   [~BRAS-GigabitEthernet0/1/1.1-bas] multicast copy by-vlan
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1-bas] commit
   ```
   ```
   [~BRAS-GigabitEthernet0/1/1.1-bas] quit
   ```
9. Configure basic multicast functions.
   
   
   ```
   [~BRAS] multicast ipv6 routing-enable
   ```
   ```
   [*BRAS] interface gigabitethernet 0/1/0
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::1/64
   ```
   ```
   [*BRAS-GigabitEthernet0/1/0] pim ipv6 sm
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
   [~BRAS-GigabitEthernet0/1/1.1] ipv6 enable
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] ipv6 address auto link-local
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] pim ipv6 sm
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] mld enable
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*BRAS] commit
   ```
10. Configure IPv6 multicast.
    
    
    
    # Configure IPv6 multicast program lists.
    
    ```
    [~BRAS] aaa
    ```
    ```
    [~BRAS-aaa] multicast-list ipv6 listname1 index 0 group-ipv6-address FF1E::1
    ```
    ```
    [~BRAS-aaa] multicast-list ipv6 listname2 index 1 group-ipv6-address FF1E::2
    ```
    
    # Configure an IPv6 multicast profile.
    
    ```
    [~BRAS-aaa] multicast-profile ipv6 name1
    ```
    ```
    [~BRAS-aaa-mprofile-profile1] multicast-list ipv6 listname1 static
    ```
    ```
    [~BRAS-aaa-mprofile-profile1] multicast-list ipv6 listname2 static
    ```
    ```
    [~BRAS-aaa-mprofile-profile1] quit
    ```
    
    # Bind the IPv6 multicast profile to the AAA domain.
    
    ```
    [~BRAS-aaa] domain wdomain
    ```
    ```
    [~BRAS-aaa-domain-wdomain] multicast-profile ipv6 name1
    ```
    ```
    [*BRAS-aaa-domain-wdomain] commit
    ```
    ```
    [~BRAS-aaa-domain-wdomain] quit
    ```
11. Verify the configuration.
    
    
    
    Run the [**display multicast-profile ipv6**](cmdqueryname=display+multicast-profile+ipv6) command to check information about a specified or all IPv6 multicast profiles.
    
    # Check information about all IPv6 multicast profiles.
    ```
    <HUAWEI> display multicast-profile ipv6
    ```
    ```
    ---------------------------------------------------------------------
    Index      Multicast-profile-name-ipv6                 IfAuthentic
    ---------------------------------------------------------------------
        0      name1                                       Yes
       ---------------------------------------------------------------------
    Total: 1
    
    ```
    
    # Check multicast IPv6 program lists bound to a specified multicast profile.
    ```
    <HUAWEI> display multicast-profile ipv6 name1
     Profile-name-ipv6                   : name1
     If-authentic                        : Yes
     Static multicast-list-name-ipv6     : listname1
     Static multicast-list-name-ipv6     : listname2
    ```
    
    Run the [**display multicast-list ipv6**](cmdqueryname=display+multicast-list+ipv6) command to check information about a specified or all IPv6 multicast program lists.
    
    # Check information about all IPv6 multicast program lists.
    
    ```
    <HUAWEI> display multicast-list ipv6 
    ```
    ```
    Total: 2
    ---------------------------------------------------------------------
    Multicast-list ipv6 name : listname1
    Index                    : 0 
    Source IPv6/prefix       : FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF/128 
    Group IPv6/prefix        : FF1E::1/128 
    Multicast-list ipv6 name : listname2 
    Index                    : 1 
    Source IPv6/prefix       : FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF/128 
    Group IPv6/prefix        : FF1E::2/128 
    ---------------------------------------------------------------------
    
    ```
    
    # Check information about a specified IPv6 multicast program list.
    
    ```
    <HUAWEI> display multicast-list  ipv6 listname1
    ---------------------------------------------------------------------
    Multicast-list ipv6 name  : listname1
    Index                     : 0
    Source IPv6/prefix        : FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF/128 
    Group IPv6/prefix         : FF1E::1/128 
    ---------------------------------------------------------------------
    
    ```
    
    # Run the **display access-user domain wdomain** command to check information about users that have gone online. The command output shows that the user with the user ID 65 has gone online in IPoE mode.
    
    ```
    [*BRAS] display  access-user domain wdomain
    ------------------------------------------------------------------------------
    UserID  Username                Interface      IP address       MAC
            Vlan          IPv6 address             Access type
    ------------------------------------------------------------------------------
    65      spirent33@wdomain       GE0/1/1.1      -                00-e0-fc-12-34-56
            133/-         2001:db8:1::10:CC00:200:27E9   IPoE
    ------------------------------------------------------------------------------
    Normal users                       : 1
    RUI Local users                    : 0
    RUI Remote users                   : 0
    Total users                        : 1
    
    ```
    
    # Run the **display multicast user-id 65** command to check information about the IPv6 static multicast group that a user joins after the user goes online.
    
    ```
    [*BRAS] display multicast user-id 65
    User information:
    User ID             :65
    User IPv6 address   :2001:db8:1::10:CC00:200:27E9
    Gateway IPv6 address:FE80::200:14FF:FE00:571
    BRAS interface      :GigabitEthernet0/1/1.1
    User MAC-address    :00-e0-fc-12-34-56
    MAX program list    :4
    User VLAN           :VLAN 133
    
    User static program:
    Group IP           Source IP          Flag
    FF1E::1            ::                 Active  
    FF1E::2            ::                 Active  
    
    Total:1
    ```

#### Configuration Files

```
#
sysname BRAS
#
multicast ipv6 routing-enable      
#
radius-server group shiva                                                       
 radius-server authentication 10.7.66.66 1812 weight 0                                             
 radius-server accounting 10.7.66.66 1813 weight 0                                                        
 radius-server shared-key-cipher %^%#h{FXVBLZX9#`VI]EWUUaOSHGd5E!.1DGeVYEie=%^%                                       
 radius-server retransmit 2                                                    
# 
aaa
 multicast-list ipv6 listname1 index 0 group-ipv6-address FF1E::1 
 multicast-list ipv6 listname2 index 1 group-ipv6-address FF1E::2 
 multicast-profile ipv6 name1
   multicast-list ipv6 list-index 0 1 static
#
 authentication-scheme radius
  authentication-mode radius
#
 accounting-scheme none
  accounting-mode none
#
 domain wdomain
  authentication-scheme radius
  accounting-scheme none
  radius-server group shiva
  ipv6-pool poolname
  multicast-profile ipv6 name1
#
interface GigabitEthernet0/1/0
 ipv6 enable
 ipv6 address 2001:db8:1::1/64
 pim ipv6 sm     
#
interface GigabitEthernet0/1/1.1
 ipv6 enable
 ipv6 address auto link-local
 user-vlan 133
 pim ipv6 sm
 mld enable
 bas
#
  access-type layer2-subscriber default-domain authentication wdomain
  authentication-method-ipv6 bind
  multicast copy by-vlan
#
ipv6 prefix huawei local
 prefix 2001:db8:1::/64
#
ipv6 pool poolname bas local
 prefix ipv6                     
#
return
```