Example for Configuring HWTACACS Authentication and Authorization for Administrators
====================================================================================

This section provides an example for configuring HWTACACS authentication and authorization for administrators.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172371851__fig_dc_vrp_aaa_cfg_103401), Administrator is an administrator of the HUAWEI. To prevent unauthorized administrators from accessing the device, perform HWTACACS authentication and authorization for administrators.

**Figure 1** Configuring HWTACACS authentication and authorization for administrators  
![](images/fig_dc_vrp_aaa_cfg_103401.png)  


#### Precautions

When the type of a user is set to terminal, Telnet, FTP, SNMP, or SSH using the [**local-user service-type**](cmdqueryname=local-user+service-type) command, the user becomes an administrator.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an HWTACACS server template.
2. Configure an HWTACACS authentication scheme and an authorization scheme.
3. Apply the HWTACACS server template, authentication scheme, and authorization scheme to a domain.

#### Data Preparation

To complete the configuration, you need the following data:

* HWTACACS server template name **ht**, authentication scheme name **scheme1**, authorization scheme name **scheme2**
* IP address 172.16.1.1/32 of the primary HWTACACS server, authentication port number 49, and authorization port number 49
* IP address 172.16.1.2/32 of the secondary HWTACACS server, default authentication port number 49, and default authorization port number 49
* HWTACACS authentication is performed for users on DeviceA.

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
   
   # Configure an IP address and port number for the primary HWTACACS authentication and authorization server.
   
   ```
   [*HUAWEI-hwtacacs-ht] hwtacacs-server authentication 172.16.1.1 49
   ```
   ```
   [*HUAWEI-hwtacacs-ht] hwtacacs-server authorization 172.16.1.1 49
   ```
   
   # Configure an IP address and port number for the secondary HWTACACS authentication and authorization server.
   
   ```
   [*HUAWEI-hwtacacs-ht] hwtacacs-server authentication 172.16.1.2 49 secondary
   ```
   ```
   [*HUAWEI-hwtacacs-ht] hwtacacs-server authorization 172.16.1.2 49 secondary
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
2. Configure authentication and authorization schemes.
   
   
   
   # Enter the AAA view.
   
   ```
   [~HUAWEI] aaa
   ```
   
   # Configure an authentication scheme named **scheme1** and set the authentication mode to HWTACACS.
   
   ```
   [~HUAWEI-aaa] authentication-scheme scheme1
   ```
   ```
   [*HUAWEI-aaa-authen-scheme1] authentication-mode hwtacacs
   ```
   ```
   [*HUAWEI-aaa-authen-scheme1] commit
   ```
   ```
   [*HUAWEI-aaa-authen-scheme1] quit
   ```
   
   # Configure an authorization scheme named **scheme2** and set the authorization mode to HWTACACS.
   
   ```
   [*HUAWEI-aaa] authorization-scheme scheme2
   ```
   ```
   [*HUAWEI-aaa-author-scheme2] authorization-mode hwtacacs
   ```
   ```
   [*HUAWEI-aaa-author-scheme2] commit
   ```
   ```
   [~HUAWEI-aaa-author-scheme2] quit
   ```
3. Configure a domain named **huawei**. Apply the HWTACACS authentication scheme **scheme1**, HWTACACS authorization scheme **scheme2**, and HWTACACS server template **ht** to the domain. When a user requests to go online, the username must carry domain name **huawei** so that HWTACACS authentication and authorization can be performed for the user.
   
   
   ```
   [~HUAWEI-aaa] domain huawei
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] authentication-scheme scheme1
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] authorization-scheme scheme2
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
    Primary Authentication Server  :  172.16.1.1-49:-
    Primary Authorization Server   :  172.16.1.1-49:-
    Primary Accounting Server      :  0.0.0.0-0:- 
    Primary Common Server          :  0.0.0.0-0:- 
    Current Authentication Server  :  172.16.1.1-49:-
    Current Authorization Server   :  172.16.1.1-49:-
    Current Accounting Server      :  0.0.0.0-0:-
    Source IP Address              :  0.0.0.0
    Shared Key                     :  ****************
    Quiet-interval (min)           :  5
    Response-timeout-Interval (sec):  5
    Domain-included                :  Yes
    Secondary Authen Server Count  :  1
    Secondary Author Server Count  :  1
    Secondary Account Server Count :  0 
    Secondary Common Server Count  :  0
   -------------------------------------------------
   ```
   
   Run the **display domain** command on the Router. The command output shows that the domain configurations meet the requirements.
   
   ```
   <HUAWEI>display domain
   ```
   ```
   ---------------------------------------------------------------
   Domain-name                 : huawei
   Domain-state                : Active
   Authentication-scheme-name  : scheme1
   Authorization-scheme-name   : scheme2
   Accounting-scheme-name      : -
   User-access-limit           : No
   Online-number               : 0
   HWTACACS-server-template    : ht
   RADIUS-server-template      : -
   ---------------------------------------------------------------            
   ```
   
   When users in the domain **huawei** attempt to access the device, HWTACACS authentication scheme **scheme1** and authorization scheme **scheme2** are used to authenticate and authorize the users.

#### Configuration Files

# DeviceA configuration file

```
#
```
```
sysname HUAWEI
```
```
#
```
```
hwtacacs enable
#
hwtacacs-server template ht
 hwtacacs-server authentication 172.16.1.1
 hwtacacs-server authentication 172.16.1.2 secondary
 hwtacacs-server authorization 172.16.1.1
 hwtacacs-server authorization 172.16.1.2 secondary
 hwtacacs-server shared-key cipher %#%#pbft&Zu2$Z<,,g4=vX~7958dF@U%YGfREMUAQA{:%#%
 
#
aaa
 #
 authentication-scheme default
 #
 authentication-scheme scheme1
  authentication-mode hwtacacs
 #
 authorization-scheme default
 #
 authorization-scheme scheme2
  authorization-mode hwtacacs
 #
 accounting-scheme default
 #
 domain default
 #
 domain huawei
  authentication-scheme scheme1
  authorization-scheme scheme2
  hwtacacs-server ht
```
```
 #
```
```
return  
```