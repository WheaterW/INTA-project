Example for Configuring HWTACACS Authentication, Authorization, and Accounting for Access Users
===============================================================================================

This section provides an example for configuring HWTACACS authentication, authorization, and accounting for users in the domain **huawei** on a network so that the users are authenticated, authorized, and charged using HWTACACS.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371848__fig_dc_vrp_aaa_cfg_102401):

* Access users are first authenticated locally. If local authentication fails, the HWTACACS server is used to authenticate the users.
* HWTACACS authentication is required before the level of access users is upgraded. If HWTACACS authentication fails, local authentication is used.
* HWTACACS authorization is performed for access users.
* All access users need to be charged.
* The HWTACACS server at 192.168.66.66/32 functions as the primary server, with authentication port 49, authorization port 49, and accounting port 49. The HWTACACS server at 192.168.66.67/32 functions as the secondary server, with authentication port 49, authorization port 49, and accounting port 49 by default.

**Figure 1** Configuring HWTACACS authentication, authorization, and accounting for access users  
![](images/fig_dc_vrp_aaa_cfg_102401.png)  


#### Precautions

None


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an HWTACACS server template.
2. Configure authentication, authorization, and accounting schemes.
3. Apply the HWTACACS server template, authentication scheme, authorization scheme, and accounting scheme to a domain.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of the primary and secondary HWTACACS authentication servers
* IP addresses of the primary and secondary HWTACACS authorization servers
* IP addresses of the primary and secondary HWTACACS accounting servers
* Local or HWTACACS authentication is performed for users on DeviceB.

#### Procedure

1. Enable HWTACACS and configure an HWTACACS server template.
   
   
   
   # Enable HWTACACS and configure an HWTACACS server template named **ht**.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] hwtacacs enable
   ```
   ```
   [*HUAWEI] hwtacacs-server template ht
   ```
   
   # Configure IP addresses and port numbers for the primary HWTACACS authentication, authorization, and accounting servers.
   
   ```
   [*HUAWEI-hwtacacs-ht] hwtacacs-server authentication 192.168.66.66 49
   ```
   ```
   [*HUAWEI-hwtacacs-ht] hwtacacs-server authorization 192.168.66.66 49
   ```
   ```
   [*HUAWEI-hwtacacs-ht] hwtacacs-server accounting 192.168.66.66 49
   ```
   
   # Configure IP addresses and port numbers for the secondary HWTACACS authentication, authorization, and accounting servers.
   
   ```
   [*HUAWEI-hwtacacs-ht] hwtacacs-server authentication 192.168.66.67 49 secondary
   ```
   ```
   [*HUAWEI-hwtacacs-ht] hwtacacs-server authorization 192.168.66.67 49 secondary
   ```
   ```
   [*HUAWEI-hwtacacs-ht] hwtacacs-server accounting 192.168.66.67 49 secondary
   ```
   
   # Configure a key for the HWTACACS server.
   
   ```
   [*HUAWEI-hwtacacs-ht] hwtacacs-server shared-key cipher YsHsjx_202206
   ```
   ```
   [*HUAWEI-hwtacacs-ht] commit
   ```
   ```
   [~HUAWEI-hwtacacs-ht] quit
   ```
2. Configure authentication, authorization, and accounting schemes.
   
   
   
   # Enter the AAA view.
   
   ```
   [~HUAWEI] aaa
   ```
   
   # Configure an authentication scheme named **l-h** and allow local authentication to be performed before HWTACACS authentication.
   
   ```
   [~HUAWEI-aaa] authentication-scheme l-h
   ```
   ```
   [*HUAWEI-aaa-authen-l-h] authentication-mode local hwtacacs
   ```
   ```
   [*HUAWEI-aaa-authen-l-h] commit
   ```
   ```
   [*HUAWEI-aaa-authen-l-h] quit
   ```
   
   # Configure an authorization scheme named **scheme2** and set the authorization mode to HWTACACS.
   
   ```
   [*HUAWEI-aaa] authorization-scheme scheme2
   ```
   ```
   [*HUAWEI-aaa-author-scheme2] authorization-mode hwtacacs
   ```
   ```
   [*HUAWEI-aaa-author-scheme2] authorization-cmd hwtacacs
   ```
   ```
   [*HUAWEI-aaa-author-scheme2] commit
   ```
   ```
   [~HUAWEI-aaa-author-scheme2] quit
   ```
   
   # Configure an accounting scheme named **scheme3** and set the accounting mode to HWTACACS.
   
   ```
   [~HUAWEI-aaa] accounting-scheme scheme3
   ```
   ```
   [*HUAWEI-aaa-accounting-scheme3] accounting-mode hwtacacs
   ```
   ```
   [*HUAWEI-aaa-accounting-scheme3]  commit
   ```
   ```
   [~HUAWEI-aaa-accounting-scheme3] quit
   ```
3. Configure a domain named **huawei**, and apply authentication scheme **l-h**, authorization scheme **scheme2**, accounting scheme **scheme3**, and HWTACACS server template **ht** to the domain.
   
   
   ```
   [~HUAWEI-aaa] domain huawei
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] authentication-scheme l-h
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] authorization-scheme scheme2
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] accounting-scheme scheme3
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] hwtacacs-server ht
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] commit
   ```
   ```
   [~HUAWEI-aaa-domain-huawei] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
4. Verify the configuration.
   
   
   
   Run the **display hwtacacs-server template** command on the Router. The command output shows that the HWTACACS server template configurations meet the requirements.
   
   ```
   <HUAWEI> display hwtacacs-server template ht
   ```
   ```
   -------------------------------------------------
    Template Name                  :  ht
    Template ID                    :  0
    Primary Authentication Server  :  192.168.66.66-49:-
    Primary Authorization Server   :  192.168.66.66-49:-
    Primary Accounting Server      :  192.168.66.66-49:- 
    Primary Common Server          :  192.168.66.66-49:-
    Current Authentication Server  :  192.168.66.66-49:-
    Current Authorization Server   :  192.168.66.66-49:-
    Current Accounting Server      :  192.168.66.66-49:-
    Source IP Address              :  0.0.0.0
    Shared Key                     :  ****************
    Quiet-interval (min)           :  5
    Response-timeout-Interval (sec):  5
    Domain-included                :  Yes
    Secondary Authen Server Count  :  1
    Secondary Author Server Count  :  1
    Secondary Account Server Count :  1 
    Secondary Common Server Count  :  1
   -------------------------------------------------
   ```
   
   Run the **display domain** command on the Router. The command output shows that the domain configurations meet the requirements.
   
   ```
   <HUAWEI>display domain huawei
   ```
   ```
   ---------------------------------------------------------------
   Domain-name                 : huawei
   Domain-state                : Active
   Authentication-scheme-name  : l-h
   Authorization-scheme-name   : scheme2
   Accounting-scheme-name      : scheme3
   User-access-limit           : No
   Online-number               : 0
   HWTACACS-server-template    : ht
   RADIUS-server-template      : -
   ---------------------------------------------------------------            
   ```

#### Configuration Files

```
#
```
```
Sysname HUAWEI
```
```
#
```
```
hwtacacs enable
#
hwtacacs-server template ht
 hwtacacs-server authentication 192.168.66.66
 hwtacacs-server authentication 192.168.66.67 secondary
 hwtacacs-server authorization 192.168.66.66
 hwtacacs-server authorization 192.168.66.67 secondary
 hwtacacs-server accounting 192.168.66.66
 hwtacacs-server accounting 192.168.66.67 secondary
 hwtacacs-server shared-key cipher %#%#pbft&Zu2$Z<,,g4=vX~7958dF@U%YGfREMUAQA{:%#%#
 
#
aaa
 #
 authentication-scheme default
 #
 authentication-scheme l-h
  authentication-mode local hwtacacs
 #
 authorization-scheme default
 #
 authorization-scheme scheme2
  authorization-mode hwtacacs
  authorization-cmd hwtacacs
 #
 accounting-scheme default
 #
 accounting-scheme scheme3
  accounting-mode hwtacacs
 #
 domain default
 #
 domain huawei
  authentication-scheme l-h
  authorization-scheme scheme2
  accounting-scheme scheme3
  hwtacacs-server ht
```
```
 #
```
```
return  
```