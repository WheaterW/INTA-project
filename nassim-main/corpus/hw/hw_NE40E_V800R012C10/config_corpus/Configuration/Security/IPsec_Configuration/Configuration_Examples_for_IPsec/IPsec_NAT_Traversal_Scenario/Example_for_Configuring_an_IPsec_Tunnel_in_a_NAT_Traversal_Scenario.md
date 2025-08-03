Example for Configuring an IPsec Tunnel in a NAT Traversal Scenario
===================================================================

Example for Configuring an IPsec Tunnel in a NAT Traversal Scenario

#### Networking Requirements

If a NAT gateway exists between the local and remote devices used for IPsec negotiation, NAT traversal capabilities need to be negotiated between the two ends of the IPsec tunnel to be established. This requires both devices to support NAT traversal.

On the network shown in [Figure 1](#EN-US_TASK_0172372521__fig19433292615), a NAT gateway (NATER) is deployed between DeviceA (egress gateway of the headquarters network) and DeviceB (egress gateway of the branch network). Configure NAT traversal on DeviceA and DeviceB to allow for IPsec tunnel-based communication between them.

Configure ESP as the security protocol for an IPsec proposal. Specify the authentication algorithm SHA2-256 and the encryption algorithm AES-256 for ESP. Configure an IKE proposal, and use the default authentication algorithm and authentication method in the IKE proposal, which are AES-CBC and key pre-share, respectively. In addition, set the DH group identifier used for key negotiation to group14.

**Figure 1** Network diagram for configuring an IPsec tunnel in a NAT traversal scenario![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/1 and GE0/1/2, respectively.


  
![](figure/en-us_image_0000002171890417.png)

#### Configuration Notes

* NATER must be configured to allow for the communication between DeviceA and DeviceB.
* DeviceA, the responder of IPsec negotiation, must use an IPsec policy template.
* NAT traversal must be enabled on both DeviceA and DeviceB.
* The data encapsulation mode can be set to tunnel only.
* IKEv2 negotiation in main mode supports IPsec NAT traversal.
* Configuring DPD is recommended.

#### Procedure

1. Configure DeviceA.
   
   
   ```
   #
    sysname DeviceA //Configure a hostname for the device.
   ```
   ```
   #
   ```
   ```
   service-location 1
   ```
   ```
    location slot 1
   ```
   ```
   #
   ```
   ```
   service-instance-group group1
   ```
   ```
    service-location 1
   ```
   ```
   #
   ike dpd interval 10 10 //Deploying DPD is recommended.
   #
   acl number 3000 //Configure an ACL to define the data flows to be protected.
    rule 0 permit ip source 10.1.0.0 0.0.0.255 destination 10.2.0.0 0.0.0.255
   # 
   ipsec proposal rta //Create an IPsec proposal.
    esp authentication-algorithm sha2-256
    esp encryption-algorithm aes 256
   #
   ike proposal 1 //Configure an IKE proposal.
    dh group14
   #
   ike peer rta //Configure an IKE peer.
    ike-proposal 1
    pre-shared-key cipher %^%#JvZxR2g8c;a9~FPN~n'$7`DEV&=G(=Et02P/%\*!%^%# //Set the pre-shared authentication key to device (displayed in ciphertext).
    local-id-type ip //Specify the IP address format for the IKE ID.
    nat traversal //Enable NAT traversal.
   # 
   ipsec policy-template rta_temp 1 //Create an IPsec policy template.
    ike-peer rta
    proposal rta
    security acl 3000
   #
   ipsec policy rta 1 isakmp template rta_temp //Use the IPsec policy template to create an SA.
   # 
   interface Tunnel1
   ip address 1.1.1.1 24
   tunnel-protocol ipsec
   ipsec policy rta service-instance-group 1
   #
   interface gigabitethernet0/1/1
    ip address 1.1.2.1 255.255.255.0
   #
   interface gigabitethernet0/1/2
    ip address 10.1.0.1 255.255.255.0
   #
   ospf 1
   area 0.0.0.0
     network 1.1.2.0 0.0.0.255
   #
   ip route-static 192.168.0.0 255.255.0.0 Tunnel1 192.168.0.2  //Configure a static route to the network segment 192.168.0.0.
   ip route-static 192.168.0.2 255.255.255.255 1.1.2.2 //Configure a static route destined for the tunnel interface of DeviceB.
   #
   return
   ```
2. Configure DeviceB.
   
   
   ```
   #
    sysname DeviceB //Configure a hostname for the device.
   ```
   ```
   #
   ```
   ```
   service-location 1
   ```
   ```
    location slot 1
   ```
   ```
   #
   ```
   ```
   service-instance-group group1
   ```
   ```
    service-location 1
   ```
   ```
   #
   ike dpd interval 10 10 //Deploying DPD is recommended.
   #
   acl number 3000 //Configure an ACL to define the data flows to be protected.
    rule 0 permit ip source 10.2.0.0 0.0.0.255 destination 10.1.0.0 0.0.0.255
   #
   ipsec proposal rtb //Create an IPsec proposal.
    esp authentication-algorithm sha2-256
    esp encryption-algorithm aes 256
   #
   ike proposal 1 //Configure an IKE proposal.
    dh group14
   #
   ike peer rtb //Configure an IKE peer.
    ike-proposal 1
    pre-shared-key cipher %^%#JvZxR2g8c;a9~FPN~n'$7`DEV&=G(=Et02P/%\*!%^%# //Set the pre-shared authentication key to device (displayed in ciphertext).
   local-id-type ip //Specify the IP address format for the IKE ID.
    remote-address 1.1.1.1 //Specify the IKE peer address.
    nat traversal //Enable NAT traversal.
   #
   ipsec policy rtb 1 isakmp //Configure an IPsec policy.
    security acl 3000
    ike-peer rtb
    proposal rtb
   #
   interface Tunnel1
   ip address 192.168.0.2 24
   tunnel-protocol ipsec
   ipsec policy rtb service-instance-group 1
   #
   interface gigabitethernet0/1/1
    ip address 192.168.1.2 255.255.255.0
   #
   interface gigabitethernet0/1/2
    ip address 10.2.0.1 255.255.255.0
   #
   ospf 1
   area 0.0.0.0
     network 192.168.1.0 0.0.0.255
   #
   ip route-static 10.1.0.0 255.255.255.0 Tunnel1 1.1.1.1 //Configure a static route destined for the network segment 10.1.0.0.
   ip route-static 1.1.1.1 255.255.255.255 192.168.1.1 //Configure a static route destined for the tunnel interface of DeviceA.
   #
   return 
   ```
3. Configure NATER.
   
   
   ```
   #
    sysname NATER //Configure a hostname for the device.
   #
    license
     active nat session-table size 2 slot 1 
     active nat bandwidth-enhance 20 slot 1
   ```
   ```
   #
   ```
   ```
   service-location 1
   ```
   ```
    location slot 1
   ```
   ```
   #
   ```
   ```
   service-instance-group group1
   ```
   ```
    service-location 1
   ```
   ```
   #
   nat instance nat1 id 1
    service-instance-group 1
    nat address-group address-group1 group-id 1 10.34.160.101 10.34.160.105
    nat outbound any address-group address-group1
   #
   acl number 3000 //Configure an ACL to define the data flows to be processed by NAT.
    rule 0 permit ip source 192.168.0.0 0.0.0.255 destination 1.1.1.0 0.0.0.255
   #
   interface gigabitethernet0/1/1
    ip address 1.1.2.2 255.255.255.0
    nat bind acl 3000 instance nat1 //Configure an outbound NAT traffic diversion policy.
   #
   interface gigabitethernet0/1/2
    ip address 192.168.1.1 255.255.255.0
   #
   ospf 1
    import-route unr
    area 0.0.0.0
     network 1.1.2.0 0.0.0.255
     network 192.168.1.0 0.0.0.255
   #
   ip route-static 1.1.1.1 32 1.1.2.1 //Configure a static route destined for the tunnel interface of DeviceA.
   ip route-static 192.168.0.2 32 192.168.1.2 //Configure a static route destined for the tunnel interface of DeviceB.
   #
   return
   ```
4. Verify the configuration.
   
   
   
   Perform a ping operation to trigger IPsec session establishment. Then, run the **display ike sa verbose remote** *ip-address* and **display ipsec sa** commands on DeviceA to check the configuration of the established IPsec tunnel.