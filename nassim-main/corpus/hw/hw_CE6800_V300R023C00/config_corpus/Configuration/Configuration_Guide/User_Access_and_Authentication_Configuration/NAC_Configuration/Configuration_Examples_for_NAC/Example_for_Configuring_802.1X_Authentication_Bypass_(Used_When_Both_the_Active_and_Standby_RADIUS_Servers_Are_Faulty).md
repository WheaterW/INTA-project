Example for Configuring 802.1X Authentication Bypass (Used When Both the Active and Standby RADIUS Servers Are Faulty)
======================================================================================================================

Example for Configuring 802.1X Authentication Bypass (Used When Both the Active and Standby RADIUS Servers Are Faulty)

#### Networking Requirements

On the enterprise network shown in [Figure 1](#EN-US_TASK_0000001513160170__fig_dc_cfg_aaa_602301), DeviceA functions as the access device, and two RADIUS servers are deployed for 802.1X and RADIUS authentication of users on the enterprise network. Users can access the Internet only after being successfully authenticated. The administrator has the following user authentication requirements: When the two RADIUS servers are faulty, users bypass authentication and are granted the same network access rights as they are successfully authenticated. After the RADIUS servers recover, users are re-authenticated and re-authorized by the RADIUS servers.

**Figure 1** Network diagram for configuring 802.1X authentication bypass (used when both the active and standby RADIUS servers are faulty)![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001563880337.png)

#### Precautions

* This section describes only NAC configurations on DeviceA. The RADIUS server configurations are not provided here.
* The RADIUS authentication and accounting keys configured on the RADIUS server must be the same as the RADIUS server's shared key configured on the device.
* By default, the outbound interface IP address of the device is used as the source IP address for sending RADIUS packets to the RADIUS server. This source IP address must be the same as the device IP address configured on the RADIUS server. You can run the following commands to change the IP address as required:
  + Run the **radius-server authentication** *ip-address* *port* **source** { *interface-type* *interface-number* | **ip-address** *source-ip-address* } command to configure a RADIUS authentication server and specify the source IP address used for sending RADIUS packets to the RADIUS authentication server.
  + Run the **radius-server accounting** *ip-address* *port* **source**{ *interface-type* *interface-number* | **ip-address** *source-ip-address* } command to configure a RADIUS accounting server and specify the source IP address used for sending RADIUS packets to the RADIUS accounting server.
* When the **authentication event authen-server-up action re-authen** command is configured, you also need to run the **radius-server testuser** command to enable automatic detection. If automatic detection is not enabled and the authentication server status changes from down to up, the device cannot re-authenticate users in authentication bypass state.
* To trigger the RADIUS server down event, run the following commands:
  ```
  [DeviceA] radius-server dead-interval 7
  [DeviceA] radius-server dead-count 1
  ```
  
  Run the [**test-aaa**](cmdqueryname=test-aaa) command four times. The RADIUS server then goes down.

#### Configuration Roadmap

1. Configure network connectivity to ensure that there are reachable routes between devices.
2. Configure AAA to implement RADIUS authentication, authorization, and accounting for users.
3. Configure 802.1X authentication, configure the rights granted to users when the RADIUS servers are faulty, and configure the re-authentication function when the RADIUS servers recover.

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
   [*DeviceA-100GE1/0/2] port link-type hybrid
   [*DeviceA-100GE1/0/2] port hybrid pvid vlan 20
   [*DeviceA-100GE1/0/2] port hybrid untagged vlan 20
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface vlanif 20
   [*DeviceA-Vlanif20] ip address 192.168.2.10 24
   [*DeviceA-Vlanif20] quit
   ```
   
   # Configure a route destined for RADIUS servers. In this example, the next-hop IP address is 192.168.1.1.
   
   ```
   [*DeviceA] ip route-static 10.7.66.0 255.255.255.0 192.168.1.1
   [*DeviceA] commit
   ```
2. Configure AAA.
   
   
   
   # Create the RADIUS server template **controller**.
   
   ```
   [~DeviceA] radius-server template controller
   ```
   
   # Configure IP addresses and port numbers of the active and standby RADIUS authentication and accounting servers, set the algorithm for selecting RADIUS servers to **master-backup**, and set the RADIUS authentication key.
   
   ```
   [*DeviceA-radius-controller] radius-server authentication 10.7.66.66 1812 weight 80
   [*DeviceA-radius-controller] radius-server accounting 10.7.66.66 1813 weight 80
   [*DeviceA-radius-controller] radius-server authentication 10.7.66.67 1812 weight 40
   [*DeviceA-radius-controller] radius-server accounting 10.7.66.67 1813 weight 40
   [*DeviceA-radius-controller] radius-server algorithm master-backup
   [*DeviceA-radius-controller] radius-server shared-key cipher Huawei@123456789
   ```
   
   # Configure automatic detection.
   
   ```
   [*DeviceA-radius-controller] radius-server testuser username test1 password cipher abc@123
   ```
   
   # Configure the automatic detection interval and detection packet timeout period for RADIUS servers in down state. (This example uses the default values.)
   
   ```
   [*DeviceA-radius-controller] radius-server detect-server interval 60
   [*DeviceA-radius-controller] radius-server detect-server timeout 3
   ```
   
   # Configure the number of retransmissions and timeout interval for RADIUS authentication requests. (This example uses the default values.)
   
   ```
   [*DeviceA-radius-controller] radius-server retransmit 3 timeout 5
   [*DeviceA-radius-controller] quit
   [*DeviceA] commit
   ```
   
   # Configure the conditions for setting the RADIUS server to the down state. (This example uses the default values.)
   
   ```
   [~DeviceA] radius-server dead-interval 5
   [~DeviceA] radius-server dead-count 2
   [~DeviceA] radius-server detect-cycle 2
   [~DeviceA] radius-server max-unresponsive-interval 300
   ```
   
   # Configure the authentication scheme **auth** and set the authentication mode to RADIUS authentication.
   
   ```
   [~DeviceA] aaa
   [~DeviceA-aaa] authentication-scheme auth
   [*DeviceA-aaa-authen-auth] authentication-mode radius
   [*DeviceA-aaa-authen-auth] quit
   ```
   
   # Configure the accounting scheme **acc** and set the accounting mode to RADIUS accounting.
   
   ```
   [*DeviceA-aaa] accounting-scheme acc
   [*DeviceA-aaa-accounting-acc] accounting-mode radius
   [*DeviceA-aaa-accounting-acc] quit
   ```
   
   # Configure the domain **example**, and apply the authentication scheme **auth**, accounting scheme **acc**, and RADIUS server template **controller** to the domain.
   
   ```
   [*DeviceA-aaa] domain example
   [*DeviceA-aaa-domain-example] authentication-scheme auth
   [*DeviceA-aaa-domain-example] accounting-scheme acc
   [*DeviceA-aaa-domain-example] radius-server controller
   [*DeviceA-aaa-domain-example] quit
   [*DeviceA-aaa] quit
   [*DeviceA] commit
   ```
3. Configure 802.1X authentication.
   
   # Configure the 802.1X access profile **d1** and set the client authentication timeout period to 30 seconds.
   ```
   [~DeviceA] dot1x-access-profile name d1
   [*DeviceA-dot1x-access-profile-d1] dot1x authentication-method eap
   [*DeviceA-dot1x-access-profile-d1] dot1x timer client-timeout 30
   [*DeviceA-dot1x-access-profile-d1] quit
   ```
   
   # Bind the 802.1X access profile **d1** to the authentication profile, and configure the forcible authentication domain **example** for users using the authentication profile.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After a forcible domain is configured in an authentication profile, users using this authentication profile are authenticated in the domain regardless of whether the user names carry domain names or carry what kind of domain names.
   
   ```
   [~DeviceA] authentication-profile name p1
   [*DeviceA-authen-profile-p1] dot1x-access-profile d1
   [*DeviceA-authen-profile-p1] access-domain example force
   [*DeviceA-authen-profile-p1] quit
   ```
   
   # Configure the rights granted to users when RADIUS servers are faulty, and enable the re-authentication function when the RADIUS servers recover. The following uses VLAN-based authorization for users in bypass state as an example.
   
   ```
   [*DeviceA] authentication-profile name p1
   [*DeviceA-authen-profile-p1] authentication event authen-server-down action authorize vlan 20
   [*DeviceA-authen-profile-p1] authentication event authen-server-up action re-authen
   [*DeviceA-authen-profile-p1] quit
   [*DeviceA] commit
   ```
   
   # Disable the pre-connection function.
   
   ```
   [~DeviceA] undo authentication pre-authen-access enable
   [*DeviceA] commit
   ```
   
   # Bind the authentication profile **p1** to 100GE 1/0/2 and enable 802.1X authentication on 100GE 1/0/2. The configurations of other interfaces connected to terminals are similar.
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] authentication-profile p1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

1. A user starts a terminal and initiates 802.1X authentication. After the authentication is successful, the user can access the Internet.
2. When the active RADIUS server is down, the standby RADIUS server authorizes the user so that the user can access the Internet. When both the active and standby RADIUS servers are down, the user enters the bypass state and can access specified network resources.
3. After the user goes online, you can run the **display access-user mac-address** command on DeviceA to check online user information.

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
undo authentication pre-authen-access enable 
authentication-profile name p1
 dot1x-access-profile d1
 access-domain example force
 authentication event authen-server-down action authorize vlan 20
 authentication event authen-server-up action re-authen
#
vlan batch 10 20
#
aaa
 authentication-scheme auth    
  authentication-mode radius 
 accounting-scheme acc
  accounting-mode radius   
 domain example            
  authentication-scheme auth
  accounting-scheme acc
  radius-server controller        
# 
radius-server template controller
 radius-server shared-key cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!SKvr${[Fs.3t@/5k|BENhEu>W(3\~XG!!D;!!!!!2jp5!!!!!!A!!!!3"pK8qv!}9M#(4$jGWvQF/R[CNe/+:W^jk8HUe&W%+%#
 radius-server accounting 10.7.66.66 1813 weight 80   
 radius-server accounting 10.7.66.67 1813 weight 40 
 radius-server authentication 10.7.66.66 1812 weight 80 
 radius-server authentication 10.7.66.67 1812 weight 40   
 radius-server testuser username test1 password cipher %+%##!!!!!!!!!"!!!!"!!!!*!!!!SKvr${[Fs.3t@/5k|BENhEu>W(3\~XG!!D;!!!!!2jp5!!!!!!A!!!!3"pK8qv!}9M#(4$jGWvQF/R[CNe/+:W^jk8HUe&W%+%#
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
 port link-type hybrid
 port hybrid pvid vlan 20
 port hybrid untagged vlan 20
 authentication-profile p1
#
ip route-static 10.7.66.0 255.255.255.0 192.168.1.1
#
return 
```