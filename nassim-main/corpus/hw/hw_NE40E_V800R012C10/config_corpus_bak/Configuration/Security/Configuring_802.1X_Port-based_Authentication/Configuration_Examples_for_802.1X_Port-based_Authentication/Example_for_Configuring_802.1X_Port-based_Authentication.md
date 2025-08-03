Example for Configuring 802.1X Port-based Authentication
========================================================

Example_for_Configuring_802.1X_Port-based_Authentication

#### Networking Requirements

On the network as shown in [Figure 1](#EN-US_TASK_0172372671__fig_dc_ne_cfg_8021x_001001), the NE40E connects to a base station through a switch to aggregate and transmit service packets from the base station. Most base stations are placed in unattended equipment rooms (base stations of different carriers may be placed in the same equipment room). Therefore, security measures must be taken to control access to the mobile bearer network. Base stations are required to send 802.1X packets to verify their validity when accessing the network. Only authenticated base stations are allowed to access the network. In addition, MAC-based access control is required.

**Figure 1** Networking for 802.1X port-based authentication![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and interfaces 2 in this example represent GE 0/1/1 and GE0/2/1, respectively.


  
![](images/fig_dc_ne_cfg_8021x_000401.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

* Configure an 802.1X template.
* Configure a RADIUS authentication scheme.
* Configure a forcible authentication domain.
* Enable 802.1X authentication on a specified interface, and set the maximum number of access users on the interface to 1.

#### Data Preparation

To configure 802.1X authentication, you need the following data:

* Name of the 802.1X authentication-enabled interface
* Name of the 802.1X template
* Forcible authentication domain
* Type of the authentication service

#### Procedure

1. Configure an 802.1X template so that the default 802.1X template 1 is not used.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] dot1x-template 10
   ```
   ```
   [*HUAWEI-dot1x-template-10] quit
   ```
2. Configure a RADIUS authentication scheme.
   
   
   
   # Configure a RADIUS server group named **shiva**.
   
   ```
   [~HUAWEI]  radius-server group shiva
   ```
   
   # Configure the IP address and port number for a RADIUS server.
   
   ```
   [*HUAWEI-radius-shiva] radius-server authentication 10.7.66.66 1812
   ```
   ```
   [*HUAWEI-radius-shiva] quit
   ```
   
   # Configure authentication scheme 1, with the **RADIUS** authentication mode.
   
   ```
   [~HUAWEI-aaa] authentication-scheme 1
   ```
   ```
   [*HUAWEI-aaa-authen-1] authentication-mode radius
   ```
   ```
   [*HUAWEI-aaa-authen-1] quit
   ```
   
   # Configure accounting scheme 1, with the **none** accounting mode.
   
   ```
   [~HUAWEI-aaa] accounting-scheme 1
   ```
   ```
   [*HUAWEI-aaa-accounting-1] accounting-mode none
   ```
   ```
   [*HUAWEI-aaa-accounting-1] quit
   ```
3. Configure a forcible authentication domain named **huawei**.
   
   
   ```
   [~HUAWEI-aaa] domain huawei
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] authentication-scheme 1
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] accounting-scheme 1
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] radius-server group shiva
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] dot1x-template 10
   ```
   ```
   [*HUAWEI-aaa-domain-huawei] quit
   ```
   ```
   [~HUAWEI-aaa] quit
   ```
4. Enable 802.1X authentication on GE 0/1/1.
   
   
   ```
   [~HUAWEI] interface GigabitEthernet 0/1/1
   [*HUAWEI-GigabitEthernet0/1/1] dot1x enable
   [*HUAWEI-GigabitEthernet0/1/1] dot1x max-user 1
   [*HUAWEI-GigabitEthernet0/1/1] dot1x force-domain huawei
   [*HUAWEI-GigabitEthernet0/1/1] dot1x port-method mac
   [*HUAWEI-GigabitEthernet0/1/1] dot1x port-control auto
   [*HUAWEI-GigabitEthernet0/1/1] quit
   ```
5. Verify the configuration.
   
   
   ```
   [~HUAWEI] display dot1x interface GigabitEthernet 0/1/1
   ```
   ```
   GigabitEthernet0/1/1
        Dot1x authentication: enable
        Port control method: mac
        Port control type: auto
        Max user num: 1
        Forced-domain:huawei
        Port current status: authorized
        Port current access user num: 1
   
   ```

#### Configuration Files

NE40E configuration file

```
#
system-view
 dot1x-template 10
#
radius-server group shiva
 radius-server authentication 10.7.66.66 1812 weight 0
#
aaa
 authentication-scheme 1
 accounting-scheme 1
  accounting-mode none
 #
 domain huawei
  authentication-scheme 1
  accounting-scheme 1
  radius-server group shiva 
  dot1x-template 10
#
interface GigabitEthernet0/1/1
 undo shutdown
 dot1x enable
 dot1x force-domain huawei
 dot1x max-user 1
#
return
```