Example for Configuring 802.1X Authentication (AAA Using RADIUS)
================================================================

Example for Configuring 802.1X Authentication (AAA Using RADIUS)

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564120297__fig_01), terminals in a company's office area are connected to the company's intranet through DeviceA. The downlink interfaces (for example, 100GE 1/0/2) of DeviceA are directly connected to terminals in the office area, and the uplink interface 100GE 1/0/1 of DeviceA is connected to the RADIUS server through the intranet.

To meet the company's high security requirements, 802.1X authentication needs to be configured to authenticate terminals in the office area through the RADIUS server. Additionally, authentication points need to be deployed on DeviceA's interfaces (for example, 100GE 1/0/2) that are directly connected to the terminals.

**Figure 1** Network diagram for configuring 802.1X authentication![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000002209819389.png)

#### Precautions

In the 802.1X authentication scenario, if there is a Layer 2 switch between the 802.1X-enabled device and users, Layer 2 transparent transmission must be enabled for 802.1X authentication packets on the Layer 2 switch; otherwise, users cannot be successfully authenticated. This function needs to be configured on all interfaces through which 802.1X authentication packets pass.


#### Procedure

1. Configure network connectivity.
   
   
   
   # Create VLANs, configure the allowed VLANs on interfaces, and configure IP addresses for interfaces.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] vlan batch 10 20
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface vlanif 10
   [*DeviceA-Vlanif10] ip address 192.168.1.10 24
   [*DeviceA-Vlanif10] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 20
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface vlanif 20
   [*DeviceA-Vlanif20] ip address 192.168.2.10 24
   [*DeviceA-Vlanif20] quit
   [*DeviceA] commit
   ```
2. Configure AAA.
   
   
   
   # Create and configure the RADIUS server template **rd1**.
   
   ```
   [~DeviceA] radius-server template rd1
   [*DeviceA-radius-rd1] radius-server authentication 192.168.1.30 1812
   [*DeviceA-radius-rd1] radius-server shared-key cipher Huawei@123456789
   [*DeviceA-radius-rd1] quit
   [*DeviceA] commit
   ```
   
   # Create the AAA authentication scheme **abc** and set the authentication mode to RADIUS authentication.
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] authentication-scheme abc
   [*DeviceA-aaa-authen-abc] authentication-mode radius
   [*DeviceA-aaa-authen-abc] quit
   [*DeviceA] commit
   ```
   
   # Create the authentication domain **example.com**, and bind the authentication scheme **abc** and RADIUS server template **rd1** to the domain.
   
   ```
   [*DeviceA-aaa] domain example.com
   [*DeviceA-aaa-domain-example.com] authentication-scheme abc
   [*DeviceA-aaa-domain-example.com] radius-server rd1
   [*DeviceA-aaa-domain-example.com] quit
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```
   
   # Check whether a user can pass RADIUS authentication. (The test user **test** and password **Example2012** have been configured on the RADIUS server.)
   
   ```
   [~DeviceA] test-aaa test Example2012 radius-template rd1
   Info: Account test succeeded.
   ```
3. Configure 802.1X authentication.
   
   # Configure the 802.1X access profile **d1**.
   ```
   [~DeviceA] dot1x-access-profile name d1
   [*DeviceA-dot1x-access-profile-d1] dot1x authentication-method eap
   [*DeviceA-dot1x-access-profile-d1] dot1x timer client-timeout 30
   [*DeviceA-dot1x-access-profile-d1] quit
   [*DeviceA] commit
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   By default, an 802.1X access profile uses EAP authentication. Ensure that the RADIUS server supports the EAP protocol. Otherwise, the RADIUS server cannot process 802.1X authentication requests.
   
   
   # Configure the authentication profile **p1**, bind the 802.1X access profile **d1** to the authentication profile, and configure the forcible authentication domain **example.com** for users using the authentication profile.
   
   ```
   [~DeviceA] authentication-profile name p1
   [*DeviceA-authen-profile-p1] dot1x-access-profile d1
   [*DeviceA-authen-profile-p1] access-domain example.com force
   [*DeviceA-authen-profile-p1] quit
   [*DeviceA] commit
   ```
   
   # Bind the authentication profile **p1** to a downlink interface and enable 802.1X authentication on the interface. The following uses 100GE 1/0/2 as an example. Other interfaces have similar configurations.
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] authentication-profile p1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

1. A user starts the 802.1X client on a terminal, and enters the user name and password for authentication.
2. If the user name and password are correct, an authentication success message is displayed on the client page. The user then can access the network.
3. After the user goes online, you can run the **display access-user access-type dot1x** command on the device to check online 802.1X user information.

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
authentication-profile name p1
 dot1x-access-profile d1
 access-domain example.com force
#
vlan batch 10 20
#
aaa
 authentication-scheme abc    
  authentication-mode radius    
 domain example.com            
  authentication-scheme abc     
  radius-server rd1      
#  
radius-server template rd1
 radius-server shared-key cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!SKvr${[Fs.3t@/5k|BENhEu>W(3\~XG!!D;!!!!!2jp5!!!!!!A!!!!3"pK8qv!}9M#(4$jGWvQF/R[CNe/+:W^jk8HUe&W%+%#
 radius-server authentication 192.168.1.30 1812 weight 80
#
dot1x-access-profile name d1
 dot1x timer client-timeout 30
#
interface Vlanif10
 ip address 192.168.1.10 255.255.255.0
#
interface Vlanif20
 ip address 192.168.2.10 255.255.255.0
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10
#
interface 100GE1/0/2
 port default vlan 20
 authentication-profile p1
#
return 
```