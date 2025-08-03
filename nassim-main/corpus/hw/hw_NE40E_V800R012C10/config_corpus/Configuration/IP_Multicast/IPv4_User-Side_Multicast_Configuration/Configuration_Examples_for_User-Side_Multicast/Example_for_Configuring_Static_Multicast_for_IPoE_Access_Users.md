Example for Configuring Static Multicast for IPoE Access Users
==============================================================

This section provides an example for configuring static multicast for IPoE access users. The example provides the networking requirements, configuration roadmap, configuration procedure, and configuration files.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172367682__fig_dc_ne_bras-multicast_cac_cfg_000301), PC1 and PC2 are IPoE access users. You are required to configure static multicast to meet the following requirements:

* PC1 and PC2 belong to the IPv4 domain and access the network through GE 0/1/0 on the BRAS in IPoE mode.
* In this example, RADIUS authentication and non-accounting are used.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  + Authentication scheme: RADIUS or none
  + Accounting scheme: RADIUS or none
* Users join multicast groups 225.1.1.1 and 227.1.1.1 after going online.
* The BRAS uses GE 0/1/0 to communicate with the access network device and uses GE 0/1/1 and GE 0/1/2 to communicate with the PIM-SM devices.

**Figure 1** Configuring static multicast for IPoE access users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example is GE 0/1/0.


  
![](images/fig_dc_ne_bras-multicast_cac_cfg_000201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IPv4 address pool.
2. Configure AAA schemes.
3. Configure a domain.
4. Configure the IPoE user access service:
   
   1. Configure an authentication scheme.
   2. Configure a BAS interface and specify a user access type for the interface.
5. Enable multicast traffic replication by session on the BAS interface.
6. Configure basic multicast functions:
   
   1. Enable multicast routing.
   2. Enable PIM-SM on all interfaces of the BRAS.
   3. Enable IGMP on the BRAS interface connected to users.
7. Configure static multicast:
   
   1. Configure multicast program lists in the AAA view.
   2. Configure a multicast profile in the AAA view.
   3. Bind the multicast profile to the AAA domain.

#### Data Preparation

* IPv4 address pool name, address range, and gateway address
* Authentication and accounting schemes (user authentication on the BRAS through RADIUS)
* Name of the domain to which users belong
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
   [~BRAS] ip pool huawei bas local
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
3. Configure a domain.
   
   
   ```
   [~BRAS] aaa
   ```
   ```
   [~BRAS-aaa] domain ipv4
   ```
   ```
   [*BRAS-aaa-domain-ipv4] commit
   ```
   ```
   [~BRAS-aaa-domain-ipv4] authentication-scheme radius
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
4. Configure a BAS interface, specify a user access type for the interface, and configure an authentication scheme.
   
   
   ```
   [~BRAS-GigabitEthernet0/1/0] bas
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0-bas] access-type layer2-subscriber default-domain authentication ipv4
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0-bas] authentication-method bind
   ```
   ```
   [~BRAS-GigabitEthernet0/1/0-bas] quit
   ```
5. Enable multicast traffic replication by session on the BAS interface.
   
   
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
6. Configure basic multicast functions.
   
   
   ```
   [~BRAS] multicast routing-enable
   ```
   ```
   [*BRAS] interface gigabitethernet 0/1/1
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
7. Configure multicast.
   
   
   
   # Configure multicast program lists.
   
   ```
   [~BRAS] aaa
   ```
   ```
   [~BRAS-aaa] multicast-list  list1 group-address 225.1.1.1
   ```
   ```
   [~BRAS-aaa] multicast-list  list2 group-address 227.1.1.1
   ```
   
   # Configure a multicast profile.
   
   ```
   [~BRAS-aaa] multicast-profile profile1
   ```
   ```
   [~BRAS-aaa-mprofile-profile1] multicast-list name list1 static
   ```
   ```
   [~BRAS-aaa-mprofile-profile1] multicast-list name list2 static
   ```
   ```
   [~BRAS-aaa-mprofile-profile1] quit
   ```
   
   # Bind the multicast profile to the AAA domain.
   
   ```
   [~BRAS-aaa] domain ipv4
   ```
   ```
   [~BRAS-aaa-domain-ipv4] multicast-profile profile1
   ```
   ```
   [*BRAS-aaa-domain-ipv4] commit
   ```
   ```
   [~BRAS-aaa-domain-ipv4] quit
   ```
   ```
   [~BRAS-aaa] quit
   ```
8. Verify the configuration.
   
   
   
   # Run the [**display multicast-profile**](cmdqueryname=display+multicast-profile) command to check information about a specified or all multicast profiles.
   
   # Check information about all multicast profiles.
   
   ```
   [~BRAS] display multicast-profile
   ```
   ```
   ---------------------------------------------------------------------
   Index      Multicast-profile-name                 IfAuthentic
   ---------------------------------------------------------------------
       0      profile1                               Yes
   ---------------------------------------------------------------------
   Total: 1
   
   ```
   
   # Check multicast program lists bound to a specified multicast profile.
   
   ```
   [~BRAS] display multicast-profile profile1
    Profile-name                   : profile1
    If-authentic                   : Yes
    Static multicast-list-name     : list1
    Static multicast-list-name     : list2
   
   ```
   
   # Run the [**display multicast-list**](cmdqueryname=display+multicast-list) command to check information about a specified or all multicast program lists.
   
   # Check information about all multicast program lists.
   
   ```
   [~BRAS] display multicast-list
   ```
   ```
   Total: 2
   ---------------------------------------------------------------------
   Multicast-list  name  : list1   
   Index                 : 0   
   Source IP/mask        : 255.255.255.255/32
   Group IP/mask         : 225.1.1.1/32
   Group vpn-instance    : --   
   Multicast-list name   : list2   
   Index                 : 1   
   Source IP/mask        : 255.255.255.255/32
   Group IP/mask         : 227.1.1.1/32
   Group vpn-instance    : --   
   ---------------------------------------------------------------------
   
   ```
   
   # Check information about a specified program list.
   
   ```
   [~BRAS] display multicast-list list1
   ```
   ```
   Total: 1
   ---------------------------------------------------------------------
   Multicast-list  name  : list1   
   Index                 : 0   
   Source IP/mask        : 255.255.255.255/32
   Group IP/mask         : 225.1.1.1/32
   Group vpn-instance    : --   
   ---------------------------------------------------------------------
   
   ```
   
   # Have users go online, and then run the **display access-user** command to check whether user information.
   
   ```
   [~BRAS] display access-user username PC1@ipv4
   ```
   ```
    
   --------------------------------------------------------------------------
    UserID     Username               Interface      IP address       MAC
               Vlan                   IPv6 address   Access type
   --------------------------------------------------------------------------
    1          PC1@ipv4               GE0/1/0           10.0.0.1     00-e0-fc-12-34-56
                  -/-                  -               IPOE
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
    2         PC2@ipv4               GE0/1/0           10.0.0.2        00-e0-fc-22-34-56
                  -/-                 -               IPOE
   --------------------------------------------------------------------------
    Normal users                       : 1
    RUI Local users                    : 0
    RUI Remote users                   : 0
    Total users                        : 1
   
   ```
   
   # Run the **display multicast user-id** command to check the multicast group that a specified user has joined.
   
   ```
   [~BRAS] display multicast user-id 1
   User information:
   User ID             :1
   User IPv4 address   :10.0.0.1
   Gateway IPv4 address:10.0.0.1
   BRAS interface      :GigabitEthernet0/1/0
   User MAC-address    :00-e0-fc-12-34-56
   MAX program list    :4
   
   User static program:
   Group IP           Source IP          Flag
   225.1.1.1          0.0.0.0            Active
   227.1.1.1          0.0.0.0            Active
   
   Total:2
   
   ```
   ```
   [~BRAS] display multicast user-id 2
   User information:
   User ID             :2
   User IPv4 address   :10.0.0.2
   Gateway IPv4 address:10.0.0.1
   BRAS interface      :GigabitEthernet0/1/0
   User MAC-address    :00-e0-fc-22-34-56
   MAX program list    :4
   
   User static program:
   Group IP           Source IP          Flag
   225.1.1.1          0.0.0.0            Active
   227.1.1.1          0.0.0.0            Active
   
   Total:2
   
   ```

#### Configuration Files

```
#
sysname BRAS
#
multicast routing-enable
#
ip pool huawei bas local
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
 multicast-list  list1 index 0 group-address 225.1.1.1 
 multicast-list list1 index 1 group-address 227.1.1.1 
 multicast-profile profile1  
 multicast-list list-index 0 1 static
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
  multicast-profile profile1 
#
interface GigabitEthernet0/1/1
 ip address 10.1.1.1 255.255.255.0
 pim sm
#
interface GigabitEthernet0/1/2
 ip address 10.1.2.1 255.255.255.0
 pim sm
#
interface GigabitEthernet0/1/0
 pim sm
 igmp enable
 bas
 #
  access-type layer2-subscriber default-domain authentication ipv4
  authentication-method bind
  multicast copy by-session
 #
#
return
```