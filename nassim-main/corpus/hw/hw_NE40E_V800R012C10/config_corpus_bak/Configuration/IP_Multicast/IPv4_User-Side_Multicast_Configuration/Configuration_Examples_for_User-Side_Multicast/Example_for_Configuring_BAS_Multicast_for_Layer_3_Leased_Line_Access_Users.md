Example for Configuring BAS Multicast for Layer 3 Leased Line Access Users
==========================================================================

This section provides an example for configuring multicast services for layer 3 leased line users accessing from BAS interface.

#### Networking Requirement

On the network shown in [Figure 1](#EN-US_TASK_0172367674__fig_dc_vrp_bras-multicast_cfg_001601), multicast users go online through a BAS multicast Layer 3 leased line and order multicast programs.

**Figure 1** Configuring BAS multicast for layer 3 leased line access users![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1, interface 2, and interface 3 in this example stand for GE 0/1/1, GE 0/1/2.1, and GE 0/1/3, respectively.


  
![](images/fig_dc_vrp_bras-multicast_cfg_001601.png)  


#### Configuration Roadmap

The configuration roadmap is as follows (on BRAS device):

1. Configure Authentication, Authorization and Accounting (AAA) schemes.
2. Configure a domain.
3. Configure layer 3 lease line for multicast users.
   
   * Configure BAS interface. (A sub-interface is used as the BAS interface in this example.)
   * Configure user access type for multicast users.
4. Configure basic multicast functions:
   
   1. Enable multicast routing.
   2. Enable PIM-SM on the interface of the BRAS.
   3. Enable IGMP on the CE's interface connected to users.

#### Data Preparation

* Authentication and accounting schemes (user authentication on the BRAS through RADIUS)
* User domain
* BAS interface parameters
* Ciphertext password of a Layer 3 leased line user

#### Procedure

1. Assign an IP address to each interface on the user-side network and configure an IGP route. In this example, OSPF is used as an IGP. For configuration details, see [Configuration Files](#EN-US_TASK_0172367674__configfile).
2. Configure RADIUS server.
   
   
   ```
   [~BRAS] radius enable
   ```
   ```
   [*BRAS] radius-server group rd1
   ```
   ```
   [*BRAS-radius-rd1] radius-server authentication 10.1.4.15 1812
   ```
   ```
   [*BRAS-radius-rd1] radius-server accounting 10.1.4.15 1813
   ```
   ```
   [*BRAS-radius-rd1] quit
   ```
   ```
   [*BRAS-aaa] commit
   ```
3. Configure AAA schemes.
   
   
   
   # Configure an authentication scheme.
   
   ```
   [~BRAS] aaa
   ```
   ```
   [*BRAS-aaa] authentication-scheme 1
   ```
   ```
   [*BRAS-aaa-authen-1] authentication-mode radius
   ```
   ```
   [*BRAS-aaa-authen-1] quit
   ```
   ```
   [*BRAS-aaa] commit
   ```
   
   # Configure an accounting scheme.
   
   ```
   [~BRAS-aaa] accounting-scheme 1
   ```
   ```
   [*BRAS-aaa-accounting-1] accounting-mode radius
   ```
   ```
   [*BRAS-aaa-accounting-1] quit
   ```
   ```
   [*BRAS-aaa] quit
   ```
   ```
   [*BRAS] commit
   ```
4. Configure a domain.
   
   
   ```
   [~BRAS] aaa
   ```
   ```
   [*BRAS-aaa] domain l3
   ```
   ```
   [*BRAS-aaa-domain-l3] authentication-scheme 1
   ```
   ```
   [*BRAS-aaa-domain-l3] accounting-scheme 1
   ```
   ```
   [*BRAS-aaa-domain-l3] radius-server group rd1
   ```
   ```
   [*BRAS-aaa-domain-l3] quit
   ```
   ```
   [*BRAS-aaa] quit
   ```
   ```
   [*BRAS] commit
   ```
5. Configure a BAS interface and specify a user access type for the interface.
   
   
   ```
   [~BRAS-GigabitEthernet0/1/2.1] bas
   ```
   ```
   [*BRAS-GigabitEthernet0/1/2.1-bas] access-type layer3-leased-line user-name layer3 password cipher YsHsjx_202206 default-domain authentication l3
   ```
   ```
   [*BRAS-GigabitEthernet0/1/2.1-bas] quit
   ```
   ```
   [*BRAS-GigabitEthernet0/1/2.1] commit
   ```
6. Configure basic multicast functions.
   
   
   
   Configure basic multicast functions on the BRAS device.
   
   ```
   [~BRAS] multicast routing-enable
   ```
   ```
   [*BRAS] interface gigabitethernet 0/1/1
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
   [~BRAS] interface gigabitethernet 0/1/2.1
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] ip address 10.1.3.1 255.255.255.0
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] pim sm
   ```
   ```
   [*BRAS-GigabitEthernet0/1/1.1] quit
   ```
   ```
   [*BRAS] commit
   ```
   
   Configure basic multicast functions on CE.
   
   ```
   [~CE] multicast routing-enable
   ```
   ```
   [*CE] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/1] ip address 10.1.3.2 255.255.255.0
   ```
   ```
   [*CE-GigabitEthernet0/1/1] pim sm
   ```
   ```
   [*CE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE] interface gigabitethernet 0/1/3
   ```
   ```
   [*CE-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/3] ip address 10.1.5.1 255.255.255.0
   ```
   ```
   [*CE-GigabitEthernet0/1/3] pim sm
   ```
   ```
   [*CE-GigabitEthernet0/1/3] igmp enable
   ```
   ```
   [*CE-GigabitEthernet0/1/3] quit
   ```
   ```
   [*CE] commit
   ```
7. Verify the configuration.
   
   # Run the **display access-user domain l3** command to view information about online users who join multicast groups through the BAS multicast Layer 3 leased line. The command output shows that the user with ID 1280 accesses through layer 3 lease line.
   ```
   [~BRAS] display  access-user domain l3
     ------------------------------------------------------------------------------
     UserID  Username                Interface      IP address       MAC
             Vlan          IPv6 address             Access type
     ------------------------------------------------------------------------------
     1280    layer3@l3               GE0/1/2.1      -           -
             -/-           -                        Layer3_lease_line
     ------------------------------------------------------------------------------
     Normal users                       : 1
     RUI Local users                    : 0
     RUI Remote users                   : 0
     Total users                        : 1
   ```

#### Configuration Files

BRAS configuration file

```
#
sysname BRAS
#
multicast routing-enable
#
radius enable
#
radius-server group rd1
 radius-server authentication 10.1.4.15 1812
 radius-server accounting 10.1.4.15 1813
#
aaa
 #
 authentication-scheme 1
  authentication-mode radius
 #
 accounting-scheme 1
  accounting-mode radius
 #
 domain l3
  authentication-scheme 1
  accounting-scheme 1
  radius-server group rd1
#
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 10.1.1.1 255.255.255.0
 pim sm
#
interface GigabitEthernet0/1/2.1
 undo shutdown
 ip address 10.1.3.1 255.255.255.0
 encapsulation dot1q-termination
 dot1q termination vid 10
 pim sm
 bas
 #
  access-type layer3-leased-line user-name layer3 password cipher %^%#2hXm~)DX,6jjtH#jL!~:Vcg/@e"^Y0bxG default-domain authentication l3
#
interface GigabitEthernet0/1/3
 undo shutdown
 ip address 10.1.4.1 255.255.255.0
#
interface LoopBack0
 ip address 1.1.1.1 255.255.255.255
 pim sm
#
ospf 1
 area 0.0.0.0
  network 10.1.1.0 255.255.255.0
  network 10.1.3.0 255.255.255.0
  network 10.1.4.0 255.255.255.0
  network 1.1.1.1 255.255.255.255
#
pim 
 c-bsr LoopBack0
 c-rp LoopBack0
#
return  
```

CE configuration file

```
#
sysname CE
#
multicast routing-enable
#
interface GigabitEthernet0/1/1
 undo shutdown
 ip address 10.1.3.2 255.255.255.0
 pim sm
#
interface GigabitEthernet0/1/3
 undo shutdown
 ip address 10.1.5.1 255.255.255.0
 pim sm
 igmp enable
#
ospf 1
 area 0.0.0.0
  network 10.1.3.0 255.255.255.0
  network 10.1.5.0 255.255.255.0
#
return
```