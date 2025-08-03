Example for Configuring the Primary and Secondary HWTACACS Servers
==================================================================

Example for Configuring the Primary and Secondary HWTACACS Servers

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563875641__fig_dc_cfg_aaa_103001), two HWTACACS servers are deployed. The enterprise requires that the two HWTACACS servers back up each other to ensure user authentication if one server is faulty.

**Figure 1** Configuring the primary and secondary HWTACACS servers![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2 and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3 respectively.


  
![](figure/en-us_image_0000001513155842.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an HWTACACS server template.
2. Configure authentication, authorization, and accounting schemes.
3. Apply the HWTACACS server template, authentication scheme, authorization scheme, and accounting scheme to a domain.

#### Precautions

* Ensure that there are reachable routes between devices before the configuration.
* Ensure that the shared key in the HWTACACS server template is the same as that configured on the HWTACACS server.
* After the domain is set as the global default domain, and the user name of a user contains the domain name or does not contain any domain name, the user uses AAA configuration in the global default domain.
* If the HWTACACS server does not support the user name containing the domain name, run the **undo hwtacacs-server user-name domain-included** command in the HWTACACS server template view to configure the device to send packets that do not contain the domain name to the HWTACACS server.
* After the **undo hwtacacs-server user-name domain-included** command is run, the device changes only the user name format in the sent packet, without affecting the domain to which the user belongs. For example, after this command is run, the user with the user name **username@huawei.com** still uses AAA configuration in the domain **huawei.com**.

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
2. Configure an HWTACACS server template.
   
   
   
   # Create an HWTACACS server template named **ht**.
   
   ```
   [~DeviceA] hwtacacs-server template ht
   ```
   
   # Configure IP addresses and port numbers for the primary HWTACACS authentication, authorization, and accounting servers.
   
   ```
   [*DeviceA-hwtacacs-ht] hwtacacs-server authentication 10.7.66.66 49
   [*DeviceA-hwtacacs-ht] hwtacacs-server authorization 10.7.66.66 49
   [*DeviceA-hwtacacs-ht] hwtacacs-server accounting 10.7.66.66 49
   ```
   
   # Configure IP addresses and port numbers for the secondary HWTACACS authentication, authorization, and accounting servers.
   
   ```
   [*DeviceA-hwtacacs-ht] hwtacacs-server authentication 10.7.66.67 49 secondary
   [*DeviceA-hwtacacs-ht] hwtacacs-server authorization 10.7.66.67 49 secondary
   [*DeviceA-hwtacacs-ht] hwtacacs-server accounting 10.7.66.67 49 secondary
   ```
   
   # Configure a shared key for the HWTACACS server.
   
   ```
   [*DeviceA-hwtacacs-ht] hwtacacs-server shared-key cipher YsHsjx_202206139
   [*DeviceA-hwtacacs-ht] quit
   [*DeviceA] commit
   ```
3. Configure authentication, authorization, and accounting schemes.
   
   
   
   # Create an authentication scheme named **l-h**, and set the authentication mode to HWTACACS and local authentication.
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] authentication-scheme l-h
   [*DeviceA-aaa-authen-l-h] authentication-mode hwtacacs local
   [*DeviceA-aaa-authen-l-h] quit
   ```
   
   # Create an authorization scheme named **hwtacacs**, and set the authorization mode to HWTACACS and local authorization.
   
   ```
   [*DeviceA-aaa] authorization-scheme hwtacacs
   [*DeviceA-aaa-author-hwtacacs] authorization-mode hwtacacs local
   [*DeviceA-aaa-author-hwtacacs] quit
   ```
   
   # Create an accounting scheme named **hwtacacs**, and set the accounting mode to HWTACACS accounting. Configure a policy for the device to keep users online upon accounting-start failures.
   
   ```
   [*DeviceA-aaa] accounting-scheme hwtacacs
   [*DeviceA-aaa-accounting-hwtacacs] accounting-mode hwtacacs 
   [*DeviceA-aaa-accounting-hwtacacs] accounting start-fail online
   ```
   
   # Set the real-time accounting interval to 3 minutes.
   
   ```
   [*DeviceA-aaa-accounting-hwtacacs] accounting realtime 3
   [*DeviceA-aaa-accounting-hwtacacs] quit
   ```
4. Create the domain **huawei**, and apply the authentication scheme **l-h**, authorization scheme **hwtacacs**, accounting scheme **hwtacacs**, and HWTACACS server template **ht** to the domain.
   
   
   ```
   [*DeviceA-aaa] domain huawei
   [*DeviceA-aaa-domain-huawei] authentication-scheme l-h
   [*DeviceA-aaa-domain-huawei] authorization-scheme hwtacacs
   [*DeviceA-aaa-domain-huawei] accounting-scheme hwtacacs
   [*DeviceA-aaa-domain-huawei] hwtacacs-server ht
   [*DeviceA-aaa-domain-huawei] quit
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```
5. Configure the global default administrative domain.
   
   
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

Run the **display hwtacacs-server template** command on DeviceA. The command output shows that the HWTACACS server template configuration meets the requirements.

```
[~DeviceA] display hwtacacs-server template name ht
  ---------------------------------------------------------------------------
  HWTACACS-server template name        : ht
  HWTACACS-server template index       : 1
  Primary-authentication-server        : 10.7.66.66:49 Vrf:- Shared-key:- Status:UP
  Primary-authorization-server         : 10.7.66.66:49 Vrf:- Shared-key:- Status:UP
  Primary-accounting-server            : 10.7.66.66:49 Vrf:- Shared-key:- Status:UP
  Secondary-authentication-server      : 10.7.66.66:49 Vrf:- Shared-key:- Status:-
  Secondary-authorization-server       : 10.7.66.66:49 Vrf:- Shared-key:- Status:-
  Secondary-accounting-server          : 10.7.66.66:49 Vrf:- Shared-key:- Status:-
  Third-authentication-server          : -:0 Vrf:- Shared-key:- Status:-
  Third-authorization-server           : -:0 Vrf:- Shared-key:- Status:-
  Third-accounting-server              : -:0 Vrf:- Shared-key:- Status:-
  Fourth-authentication-server         : -:0 Vrf:- Shared-key:- Status:-
  Fourth-authorization-server          : -:0 Vrf:- Shared-key:- Status:-
  Fourth-accounting-server             : -:0 Vrf:- Shared-key:- Status:-
  Current-authentication-server        : 10.7.66.66:49 Vrf:- Shared-key:- Status:UP
  Current-authorization-server         : 10.7.66.66:49 Vrf:- Shared-key:- Status:UP
  Current-accounting-server            : 10.7.66.66:49 Vrf:- Shared-key:- Status:UP
  Source-IP-address                    : -
  Source-LoopBack                      : -
  Source-Vlanif                        : -
  Shared-key                           : ****************
  Quiet-interval(min)                  : 5
  Response-timeout-Interval(sec)       : 5
  Domain-included                      : Original
  Traffic-unit                         : B
  User name in authen-start message    : No
  ---------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
hwtacacs-server template ht
 hwtacacs-server authentication 10.7.66.66
 hwtacacs-server authentication 10.7.66.67 secondary
 hwtacacs-server authorization 10.7.66.66
 hwtacacs-server authorization 10.7.66.67 secondary
 hwtacacs-server accounting 10.7.66.66
 hwtacacs-server accounting 10.7.66.67 secondary
 hwtacacs-server shared-key cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!SKvr${[Fs."u,S-6a-X1'[X=L"cpF!5Oz`1!!!!!2jp5!!!!!!A!!!!Ix>cM8i{y6!);(8Dr9:dK`&BHfE(H2=.:SH{@pT%+%#
#
aaa
 authentication-scheme l-h
  authentication-mode hwtacacs local
 authorization-scheme hwtacacs
  authorization-mode hwtacacs local
 accounting-scheme hwtacacs
  accounting-mode hwtacacs
  accounting realtime 3
 domain huawei
  authentication-scheme l-h
  accounting-scheme hwtacacs
  authorization-scheme hwtacacs
  hwtacacs-server ht
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
interface  100GE1/0/1 
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