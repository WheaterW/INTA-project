Example for Configuring the Primary and Secondary RADIUS Servers
================================================================

Example for Configuring the Primary and Secondary RADIUS Servers

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564115729__fig_dc_cfg_aaa_102901), two RADIUS servers are deployed. The enterprise requires that the two RADIUS servers back up each other to ensure user authentication if one server is faulty.

**Figure 1** Configuring the primary and secondary RADIUS servers![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2 and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3 respectively.


  
![](figure/en-us_image_0000001513035854.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a RADIUS server template.
2. Configure authentication and accounting schemes.
3. Apply the RADIUS server template, authentication scheme, and accounting scheme to a domain.

#### Precautions

* Ensure that there are reachable routes between devices before the configuration.
* Ensure that the shared key in the RADIUS server template is the same as that configured on the RADIUS server.
* After the domain is set as the global default domain and the user name of a user contains the domain name or does not contain any domain name, the user uses AAA configuration in the global default domain.
* If the RADIUS server does not support the user name containing a domain name, run the **undo radius-server user-name domain-included** command in the RADIUS server template view to configure the device to send packets that do not contain a domain name to the RADIUS server.
* After the **undo radius-server user-name domain-included** command is run, the device changes only the user name format in the sent packet, without affecting the domain to which the user belongs. For example, after this command is run, the user with the user name **username@huawei.com** still uses AAA configuration in the domain **huawei.com**.

#### Procedure

1. Configure IP addresses for interfaces.
   
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname DeviceA 
   [*DeviceA] commit
   [~DeviceA] vlan batch 10 20 30
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 20
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 30
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 10.1.1.2 255.255.255.0
   [*DeviceA-Vlanif10] quit
   [*DeviceA] interface vlanif 20
   [*DeviceA-Vlanif20] ip address 10.1.6.2 255.255.255.0
   [*DeviceA-Vlanif20] quit
   [*DeviceA] interface vlanif 30
   [*DeviceA-Vlanif30] ip address 10.1.5.2 255.255.255.0
   [*DeviceA-Vlanif30] quit
   [*DeviceA] commit
   ```
2. Configure a RADIUS server template.
   
   
   
   # Configure a RADIUS template named **shiva**.
   
   ```
   [~DeviceA] radius-server template shiva
   ```
   
   # Configure IP addresses and port numbers for the primary RADIUS authentication and accounting server.
   
   ```
   [*DeviceA-radius-shiva] radius-server authentication 10.7.66.66 1812 weight 80
   [*DeviceA-radius-shiva] radius-server accounting 10.7.66.66 1813 weight 80
   ```
   
   # Configure IP addresses and port numbers for the secondary RADIUS authentication and accounting server.
   
   ```
   [*DeviceA-radius-shiva] radius-server authentication 10.7.66.67 1812 weight 40
   [*DeviceA-radius-shiva] radius-server accounting 10.7.66.67 1813 weight 40
   ```
   
   # Set the shared key and maximum number of retransmissions for the RADIUS server, and configure the device not to encapsulate the domain name in the user name when sending RADIUS packets to the RADIUS server.
   
   ```
   [*DeviceA-radius-shiva] radius-server shared-key cipher YsHsjx_202206139
   [*DeviceA-radius-shiva] radius-server retransmit 2
   [*DeviceA-radius-shiva] undo radius-server user-name domain-included
   [*DeviceA-radius-shiva] quit
   [*DeviceA] commit
   ```
3. Configure authentication and accounting schemes.
   
   
   
   # Create an authentication scheme named **auth** and set the authentication mode to RADIUS and local authentication.
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] authentication-scheme auth
   [*DeviceA-aaa-authen-auth] authentication-mode radius local
   [*DeviceA-aaa-authen-auth] quit
   ```
   
   # Create an accounting scheme named **abc**, and set the accounting mode to RADIUS accounting. Configure a policy for the device to keep users online upon accounting-start failures.
   
   ```
   [*DeviceA-aaa] accounting-scheme abc
   [*DeviceA-aaa-accounting-abc] accounting-mode radius
   [*DeviceA-aaa-accounting-abc] accounting start-fail online 
   [*DeviceA-aaa-accounting-abc] quit
   ```
4. Create the domain **huawei**, and apply the authentication scheme **auth**, accounting scheme **abc**, and RADIUS server template **shiva** to the domain.
   
   
   ```
   [*DeviceA-aaa] domain huawei
   [*DeviceA-aaa-domain-huawei] authentication-scheme auth
   [*DeviceA-aaa-domain-huawei] accounting-scheme abc
   [*DeviceA-aaa-domain-huawei] radius-server shiva
   [*DeviceA-aaa-domain-huawei] quit
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```
5. Set the domain **huawei** as the global default administrative domain.
   
   
   ```
   [~DeviceA] domain huawei admin
   [*DeviceA] commit
   ```
6. Configure AAA local authentication. Set the local user name to **user1-huawei**, password to **YsHsjx\_202206**, and privilege level to 3.
   
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] local-user user1-huawei password irreversible-cipher YsHsjx_202206
   [*DeviceA-aaa] local-user user1-huawei service-type ssh
   [*DeviceA-aaa] local-user user1-huawei privilege level 3
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

Run the **display radius-server configuration template** template-name command on DeviceA to check the RADIUS server template configuration.

```
[~DeviceA] display radius-server configuration template shiva
  ------------------------------------------------------------------------------
  Server-template-name          :  shiva
  Server-template-index         :  14                                      
  Protocol-version              :  standard
  Traffic-unit                  :  B
  Shared-secret-key             :  ****************
  Group-filter                  :  class  
  Timeout-interval(in second)   :  5
  Retransmission                :  2
  EndPacketSendTime             :  0
  Dead time(in minute)          :  5
  Domain-included               :  NO
  NAS-IP-Address                :  0.0.0.0
  Calling-station-id MAC-format :  xxxx-xxxx-xxxx
  Called-station-id MAC-format  :  XX-XX-XX-XX-XX-XX
  NAS-Port-ID format            :  New 
  Service-type                  :  - 
  NAS-IPv6-Address              :  ::
  Server algorithm              :  master-backup           
  Detect-interval(in second)    :  60     
  Detect up-server(in second)   :  0              
  Detect timeout(in second)     :  3                               
  Chargeable-user-identity      :  Not Support             
  CUI Not reject                :  No               
  Force framed-ip-addr Attr     :  No 
  Detect-interval(in second)    :  60 
  Authentication Server 1       :  10.7.66.66     Port:1812  Weight:80  [up]
                                   Vrf:- 
                                   Source Interface:NULL                        
                                   Source IP: ::
                                   Shared-key: -
                                   Down time left: -
  Authentication Server 2       :  10.7.66.67     Port:1812  Weight:40  [up]
                                   Vrf:- 
                                   Source Interface:NULL                        
                                   Source IP: ::
                                   Shared-key: -
                                   Down time left: -
  Accounting Server     1       :  10.7.66.66     Port:1813  Weight:80  [up]
                                   Vrf:- 
                                   Source Interface:NULL                        
                                   Source IP: ::
                                   Shared-key: -
                                   Down time left: -
  Accounting Server     2       :  10.7.66.67     Port:1813  Weight:40  [up]
                                   Vrf:- 
                                   Source Interface:NULL                        
                                   Source IP: ::
                                   Shared-key: -
                                   Down time left: -
  ------------------------------------------------------------------------------ 
```
#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
radius-server template shiva
 radius-server shared-key cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!SKvr${[Fs.3t@/5k|BENhEu>W(3\~XG!!D;!!!!!2jp5!!!!!!A!!!!3"pK8qv!}9M#(4$jGWvQF/R[CNe/+:W^jk8HUe&W%+%#
 radius-server authentication 10.7.66.66 1812 weight 80
 radius-server authentication 10.7.66.67 1812 weight 40
 radius-server accounting 10.7.66.66 1813 weight 80
 radius-server accounting 10.7.66.67 1813 weight 40
 radius-server retransmit 2
 undo radius-server user-name domain-included 
#
aaa
 authentication-scheme auth
  authentication-mode radius local
 accounting-scheme abc
  accounting-mode radius
 domain huawei
  authentication-scheme auth
  accounting-scheme abc
  radius-server shiva
 local-user user1-huawei password irreversible-cipher $1d$OwseVRh@LH}ZeTBm$1nH4$ab>d(N{-%0!ab48y=Ic*xEUR4pVhR2"9-~,$
 local-user user1-huawei privilege level 3
 local-user user1-huawei service-type ssh   
#
domain huawei admin
# 
vlan batch 10 20 30
#
interface Vlanif10
 ip address 10.1.1.2 255.255.255.0
#
interface Vlanif20
 ip address 10.1.6.2 255.255.255.0
#
interface Vlanif30
 ip address 10.1.5.2 255.255.255.0
#
interface 100GE1/0/1 
 port link-type trunk
 port trunk allow-pass vlan 10
#
interface 100GE1/0/2 
 port link-type trunk
 port trunk allow-pass vlan 20
#
interface 100GE1/0/3 
 port link-type trunk
 port trunk allow-pass vlan 30
#
return
```