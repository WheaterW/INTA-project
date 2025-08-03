Configuring GRE over IPsec + OSPF for NAT Traversal
===================================================

Configuring_GRE_over_IPsec_+_OSPF_for_NAT_Traversal

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172372524__fig_dc_ar_cfg_vpn_04552301), the headquarters provides IPsec VPN access to multiple branches, and NAT is configured on egress routers of the branches. The headquarters and branches perform NAT traversal. The headquarters uses a security template to establish GRE tunnels with the branches through loopback interfaces. The branches use ACL to establish GRE over IPsec tunnels with the headquarters and branches through loopback interfaces. Configure an IPsec proposal, set the security protocol used for the proposal to ESP, and specify the authentication algorithm SHA2-256 and the encryption algorithm AES 256 for ESP. In addition, configure an IKE proposal and set the authentication algorithm to SHA2-256, the encryption algorithm to AES-CBC-256, and the DH group identifier used for key negotiation to group14.

**Figure 1** Configuring GRE over IPsec + OSPF for NAT traversal![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](figure/en-us_image_0257609448.png)

#### Procedure

1. Configure DeviceA.
   
   
   ```
   #
    sysname DeviceA
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
   router id 172.16.0.1  //Configure a router ID for OSPF.
   #
   ike dpd interval 10 10     //You are suggested to deploy the DPD function.
   #
   acl number 3000  //Configure ACL 3000
    rule 0 permit gre source 172.16.0.1 0 destination 192.168.1.1 0
    rule 0 permit gre source 172.16.0.1 0 destination 192.168.2.1 0
   #
   ipsec proposal default  //Configure the default IPsec proposal.
    esp authentication-algorithm sha2-256
    esp encryption-algorithm aes 192
   #
   ike proposal 1  //Configure the IKE proposal.
    dh group14
   #
   ike peer branch   //Configure the IKE peer for the branch.
    ike-proposal 1
    pre-shared-key cipher %^%#JvZxR2g8c;a9~FPN~n'$7`DEV&=G(=Et02P/%\*!%^%#  //Configure the PSK as 123-branch in ciphertext.
    local-id-type ip
    nat traversal
   #
   ipsec policy-template branch 1  //Configure an IPsec policy template with the number of 1 for the branch.
    security acl 3000
    ike-peer branch
    proposal default
   #
   ipsec policy policy1 1 isakmp template branch    //Create IPsec policy 1 for the IPsec policy template of the branch.
   #
   interface gigabitethernet0/1/2  //Configure the external network interface of the headquarters.
    ip address 1.1.1.60 255.255.255.0
   #
   interface gigabitethernet0/1/1  //Configure the IP address of the internal network interface of the headquarters.
    ip address 172.16.1.1 255.255.255.0
   #
   interface LoopBack0  //Configure the loopback interface used for establishing a GRE connection.
    ip address 172.16.0.1 255.255.255.255
   #
   interface Tunnel0  //Configure a GRE tunnel for branch 1.
    ip address 192.168.0.1 255.255.255.252
    tunnel-protocol gre
    source LoopBack0
    destination 192.168.1.1
   #
   interface Tunnel1  //Configure a GRE tunnel for branch 2.
    ip address 192.168.0.5 255.255.255.252
    tunnel-protocol gre
    source LoopBack0
    destination 192.168.2.1
   #
   interface Tunnel2
   ip address 10.0.1.60 24
   tunnel-protocol ipsec
   ipsec policy policy1 service-instance-group group1
   #
   ospf 1  //Configure routes.
    area 0.0.0.0 
     network 192.168.0.1 0.0.0.3
     network 172.16.1.0 0.0.0.255
     network 192.168.0.5 0.0.0.3
   #
   ip route-static 10.0.1.2 255.255.255.255 1.1.1.61
   ip route-static 10.0.2.2 255.255.255.255 1.1.1.61
   #
   return
   ```
2. Configure DeviceB.
   
   
   ```
   #
    sysname DeviceB
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
   ike dpd interval 10 10     //You are suggested to deploy the DPD function.
   #
   acl number 3000
    rule 0 permit gre source 192.168.1.1 0 destination 172.16.0.1 0
   #
   ipsec proposal default  //Configure the default IPsec proposal.
    esp authentication-algorithm sha2-256
    esp encryption-algorithm aes 192
   #
   ike proposal 1  //Configure the IKE proposal.
    dh group14
   #
   ike peer center   //Configure the IKE peer for the headquarters.
    ike-proposal 1
    pre-shared-key cipher %^%#K{JG:rWVHPMnf;5\|,GW(Luq'qi8BT4nOj%5W5=)%^%#  //Configure the PSK as 123-branch in ciphertext.
    local-id-type ip
    nat traversal
    remote-address 10.0.1.60
   #
   ipsec policy center 1 isakmp  //Configure an IPsec policy with the number of 1 for the headquarters.
    security acl 3000 
    ike-peer center
    proposal default
   #
   interface gigabitethernet0/1/1  //Configure the external network interface for branch 1.
    ip address 10.1.1.2 255.255.255.0
   #
   interface gigabitethernet0/1/2  //Configure the internal network interface for branch 1.
    ip address 192.168.11.1 255.255.255.0
   #
   interface LoopBack0  //Configure a loopback interface used for creating a GRE source and OSPF router ID for the headquarters.
    ip address 192.168.1.1 255.255.255.255 
   #
   interface Tunnel0  //Configure a GRE tunnel for the headquarters.
    ip address 192.168.0.2 255.255.255.252
    tunnel-protocol gre
    source LoopBack0
    destination 172.16.0.1
   #
   interface Tunnel1
    ip address 10.0.1.2 24
    tunnel-protocol ipsec
    ipsec policy center service-instance-group group1
   #  //Configure OSPF routes.
   ospf 1
    area 0.0.0.0
     network 192.168.11.0 0.0.0.255
     network 192.168.0.2 0.0.0.3
   #
   ip route-static 10.0.1.60 255.255.255.255 10.1.1.1
   ip route-static 0.0.0.0 0.0.0.0 Tunnel1 10.0.1.1  //Configure the default route.
   #
   return
   ```
3. Configure DeviceC.
   
   
   ```
   #
    sysname DeviceC
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
    router id 192.168.2.1  //Configure a router ID for OSPF.
   #
   ike dpd interval 10 10     //You are suggested to deploy the DPD function.
   #
   acl number 3000
    rule 0 permit gre source 192.168.2.1 0 destination 172.16.0.1 0
   #
   ipsec proposal default  //Configure the default IPsec proposal.
    esp authentication-algorithm sha2-256
    esp encryption-algorithm aes 192
   #
   ike proposal 1  //Configure the IKE proposal.
    dh group14
   #
   ike peer center   //Configure the IKE peer for the headquarters.
    ike-proposal 1
    pre-shared-key cipher %^%#IRFGEiFPJ1$&a'Qy,L*XQL_+*Grq-=yMb}ULZdS6%^%#  //Configure the PSK as 123-branch in ciphertext.
    local-id-type ip
    nat traversal
    remote-address 10.0.1.60
   #
   ipsec policy center 1 isakmp  //Configure an IPsec policy with the number of 1 for the headquarters.
    security acl 3000
    ike-peer center
    proposal default
   #
   interface gigabitethernet0/1/1  //Configure the external network interface for branch 2.
    ip address 10.1.2.2 255.255.255.0
   #
   interface gigabitethernet0/1/2  //Configure the internal network interface for branch 2.
    ip address 192.168.12.1 255.255.255.0
   #
   interface LoopBack0  //Configure a loopback interface used for creating a GRE source and OSPF router ID for the headquarters.
    ip address 192.168.2.1 255.255.255.255
   #
   interface Tunnel0  //Configure a GRE tunnel for the headquarters.
    ip address 192.168.0.6 255.255.255.252
    tunnel-protocol gre
    source LoopBack0
    destination 172.16.0.1
   #
   interface Tunnel1
    ip address 10.0.2.2 24
    tunnel-protocol ipsec
    ipsec policy center service-instance-group group1
   #  //Configure OSPF routes.
   ospf 1
    area 0.0.0.0
     network 192.168.0.6 0.0.0.3
     network 192.168.12.0 0.0.0.255
   #
   ip route-static 10.0.1.60 255.255.255.255 10.1.2.1
   ip route-static 0.0.0.0 0.0.0.0 Tunnel1 10.0.2.1  //Configure the default route.
   #
   return
   ```
4. Configure NAT1.
   
   
   ```
   #
    sysname NAT1
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
    service-instance-group group1
    nat address-group address-group1 group-id 1 11.11.11.1 11.11.11.10  //Configure a NAT address pool.
   #
   acl number 2000  //Configure the IP address for NAT implementation.
    rule 0 permit source 10.1.2.0 0.0.0.255
   #
   interface gigabitethernet0/1/1  //Configure an external network interface for NAT.
    ip address 3.3.3.3 255.255.255.0
    nat bind acl 2000 instance nat1
   #
   interface gigabitethernet0/1/2  //Configure the interface address of the router for branch 2.
    ip address 10.1.2.1 255.255.255.0
   #
   ip route-static 0.0.0.0 0.0.0.0 1.0.3.2  //Configure the default route.
   #
   return
   ```
5. Configure NAT2.
   
   
   ```
   #
    sysname NAT2
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
    service-instance-group group1
    nat address-group address-group1 group-id 1 12.12.12.1 12.12.12.10  //Configure a NAT address pool.
   #
   acl number 2000  //Configure the IP address for NAT implementation.
    rule 0 permit source 10.1.1.0 0.0.0.255
   # 
   interface gigabitethernet0/1/1  //Configure an external network interface for NAT.
    ip address 2.2.2.2 255.255.255.0
    nat bind acl 2000 instance nat1 
   #
   interface gigabitethernet0/1/2  //Configure the interface address of the router for branch 1.
    ip address 10.1.1.1 255.255.255.0
   #
   ip route-static 0.0.0.0 0.0.0.0 1.0.2.2  //Configure the default route.
   #
   return
   ```
6. Verify the configuration.
   
   
   
   On Device A, Device B, or Device C, run the **display ike sa** command. The command output displays configurations of the IKE SA.
   
   On Device A or Device B, run the **display ip routing-table** command. The command output displays information about routes from the tunnel interface to the user-side interface.
   
   The headquarters and branches can communicate with each other.

#### Precautions

* The deny rule cannot be configured for the ACL of the headquarters. Otherwise, data flows fail to be transmitted over the IPsec tunnel.
* Only one IPsec policy can be created for the headquarters. Each sequence number corresponds to an IKE peer.
* The external routes between the headquarters and branches must be reachable.
* Configure DPD.