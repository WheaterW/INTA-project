Example for Establishing an IPsec Tunnel Based on Certificates Obtained in CMPv2 Mode
=====================================================================================

This section provides an example for establishing an IPsec tunnel based on certificates obtained in CMPv2 mode.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372560__fig5769165413571), network A and network B connect to the Internet through DeviceA and DeviceB, respectively. The networking environment is as follows:

* Network A belongs to the subnet 10.1.1.0/24 and connects to DeviceA through GE 0/1/1.
* Network B belongs to the subnet 10.1.2.0/24 and connects to DeviceB through GE0/1/1.
* Routes between DeviceA and DeviceB are reachable.

Configure the devices to establish an IPsec tunnel in IKE auto-negotiation mode, protecting the data flows transmitted between network A and network B. The requirements are as follows:

* DeviceA and DeviceB apply for certificates in CMPv2 mode for mutual identity authentication.
* The tunnel encapsulation mode is used.
* ESP is used as the security protocol.
* The encryption algorithm of ESP is set to AES.
* The authentication algorithm of ESP is set to SHA2-256.
* The integrity algorithm is set to HMAC-SHA2-256.

**Figure 1** Network diagram of IPsec tunnel establishment based on certificates obtained in CMPv2 mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001904741117.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses.
2. Create and configure tunnel interfaces.
3. Configure public network routes (typically static routes).
4. Configure ACL rules to define the data flows to be protected.
5. Configure CMPv2-based certificate application and use the default certificate attributes to control access.
   1. Create public-private key pairs.
   2. Configure entity information.
   3. Configure CMP sessions.
   4. Configure CMPv2-based certificate application.
   5. Configure CRL-related functions.
6. Establish an IPsec tunnel based on security policies.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* ACL rules
* Entity information, PKI domain name, RSA key pairs, CA name, and certificate information for device identity authentication and CMP server URL to be contained in a CMP request
* Security protocol, encryption algorithm, and authentication algorithm to be used in an IPsec proposal; authentication algorithm to be used in an IKE proposal

#### Procedure

1. Configure DeviceA.
   
   
   
   # Configure an IP address for GE 0/1/1.
   
   ```
   <DeviceA> system-view
   [~DeviceA] interface GigabitEthernet 0/1/1
   [~DeviceA-GigabitEthernet0/1/1] ip address 10.1.1.1 24
   [*DeviceA-GigabitEthernet0/1/1] quit
   [*DeviceA] commit
   ```
   
   # Configure an IP address for GE 0/1/2.
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/2
   [~DeviceA-GigabitEthernet0/1/2] ip address 172.16.163.1 24
   [*DeviceA-GigabitEthernet0/1/2] quit
   [*DeviceA] commit
   ```
   
   # Create and configure a tunnel interface.
   
   ```
   [~DeviceA] interface Tunnel 10
   [*DeviceA-Tunnel10] tunnel-protocol ipsec
   [*DeviceA-Tunnel10] ip address 172.19.1.1 24
   [*DeviceA-Tunnel10] quit
   [*DeviceA] commit
   ```
   
   # Configure a static route destined for network B. The outbound interface of the route to network B is Tunnel 10, and the next hop IP address is 172.20.1.2. Assume that the next hop address of DeviceA is 172.16.163.2/24.
   
   ```
   [~DeviceA] ip route-static 10.1.2.0 255.255.255.0 Tunnel 10 172.20.1.2
   [*DeviceA] ip route-static 172.20.1.2 255.255.255.255 172.16.163.2
   [*DeviceA] commit
   ```
   
   # Create an advanced ACL numbered 3000 and configure a rule to define the packets whose source IP address is 10.1.1.0/24 and destination IP address is 10.1.2.0/24 as the packets to be encrypted.
   
   ```
   [~DeviceA] acl 3000
   [*DeviceA-acl-adv-3000] rule permit ip source 10.1.1.0 0.0.0.255 destination 10.1.2.0 0.0.0.255
   [*DeviceA-acl-adv-3000] quit
   [*DeviceA] commit
   ```
   
   # Create a private-public key pair.
   
   ```
   [~DeviceA] rsa pki local-key-pair key-a create
   [*DeviceA] commit
   ```
   
   # Configure entity information.
   
   ```
   [~DeviceA] pki entity entitya
   [*DeviceA-pki-entitya] common-name DeviceA
   [*DeviceA-pki-entitya] quit
   [*DeviceA] commit
   ```
   
   # Configure a CMP session.
   
   ```
   [~DeviceA] pki domain domaina
   [*DeviceA-pki-domaina] pki cmp session session-a
   [*DeviceA-pki-domaina-pki-cmp-session-a] cmp request entity entitya
   [*DeviceA-pki-domaina-pki-cmp-session-a] cmp request rsa local-key-pair key-a regenerate
   [*DeviceA-pki-domaina-pki-cmp-session-a] cmp request ca-name "/C=cn/ST=beijing/L=shangdi/O=BB/OU=BB/CN=AB"
   [*DeviceA-pki-domaina-pki-cmp-session-a] cmp request server url http://172.16.73.168:8080
   [*DeviceA-pki-domaina-pki-cmp-session-a] cmp request authentication-cert cert-a.cer
   [*DeviceA-pki-domaina-pki-cmp-session-a] quit
   [*DeviceA-pki-domaina] pki cmp initial-request
   [*DeviceA-pki-domaina] quit
   [*DeviceA] commit
   ```
   
   # Import the local certificate **session-a\_ir.cer** and CA certificate **session-a\_ca0.cer**.
   
   ```
   [~DeviceA] pki import-certificate local filename session-a_ir.cer
   [~DeviceA] pki import-certificate ca filename session-a_ca0.cer
   ```
   
   # Specify the local certificate in the CMP request for device identity authentication.
   
   ```
   [~DeviceA] pki domain domaina
   [*DeviceA-pki-domaina] pki cmp session session-a
   [*DeviceA-pki-domaina-pki-cmp-session-a] cmp request authentication-cert session-a_ir.cer
   ```
   
   # Configure automatic certificate update.
   
   ```
   [~DeviceA-pki-domaina-pki-cmp-session-a] certificate auto-update enable
   [*DeviceA-pki-domaina-pki-cmp-session-a] quit
   [*DeviceA-pki-domaina] quit
   [*DeviceA] commit
   ```
   
   # Enable CRL check.
   
   ```
   [~DeviceA] pki crl check enable
   [*DeviceA] commit
   ```
   
   # Configure automatic update of CRL.
   
   ```
   [~DeviceA] pki domain domaina
   [*DeviceA-pki-domaina] crl auto-update enable
   [*DeviceA-pki-domaina] crl update-period 3
   [*DeviceA-pki-domaina] crl http
   [*DeviceA-pki-domaina] crl url http://172.18.166.1/crl.crl
   [*DeviceA-pki-domaina] quit
   [*DeviceA] commit
   ```
   
   # Configure an IPsec proposal named **tran1**.
   
   ```
   [~DeviceA] ipsec proposal tran1
   [*DeviceA-ipsec-proposal-tran1] encapsulation-mode tunnel
   [*DeviceA-ipsec-proposal-tran1] transform esp
   [*DeviceA-ipsec-proposal-tran1] esp authentication-algorithm sha2-256
   [*DeviceA-ipsec-proposal-tran1] esp encryption-algorithm aes 256
   [*DeviceA-ipsec-proposal-tran1] quit
   [*DeviceA] commit
   ```
   
   # Configure an IKE proposal.
   
   ```
   [~DeviceA] ike proposal 10
   [*DeviceA-ike-proposal-10] authentication-method rsa-sig
   [*DeviceA-ike-proposal-10] authentication-algorithm sha2-256
   [*DeviceA-ike-proposal-10] integrity-algorithm hmac-sha2-256
   [*DeviceA-ike-proposal-10] dh group14
   [*DeviceA-ike-proposal-10] quit
   [*DeviceA] commit
   ```
   
   # Configure an IKE peer.
   
   ```
   [~DeviceA] ike peer b
   [*DeviceA-ike-peer-b] ike-proposal 10
   [*DeviceA-ike-peer-b] certificate local-filename session-a_ir.cer
   [*DeviceA-ike-peer-b] remote-address 172.20.1.2
   [*DeviceA-ike-peer-b] quit
   [*DeviceA] commit
   ```
   
   # Configure an IPsec policy named **map1**.
   
   ```
   [~DeviceA] ipsec policy map1 10 isakmp
   [*DeviceA-ipsec-policy-isakmp-map1-10] security acl 3000
   [*DeviceA-ipsec-policy-isakmp-map1-10] proposal tran1
   [*DeviceA-ipsec-policy-isakmp-map1-10] ike-peer b
   [*DeviceA-ipsec-policy-isakmp-map1-10] quit
   [*DeviceA] commit
   ```
   
   # Configure an IPsec service instance group named **group1**.
   
   ```
   [~DeviceA] service-location 1
   [*DeviceA-service-location-1] location slot 1
   [*DeviceA-service-location-1] commit
   [~DeviceA-service-location-1] quit
   [~DeviceA] service-instance-group group1
   [*DeviceA-service-instance-group-group1] service-location 1
   [*DeviceA-service-instance-group-group1] commit
   [~DeviceA-service-instance-group-group1] quit
   ```
   
   # Apply the security policy **map1** to the tunnel interface.
   
   ```
   [~DeviceA] interface Tunnel 10
   [~DeviceA-Tunnel10] ipsec policy map1 service-instance-group group1
   [*DeviceA-Tunnel10] quit
   [*DeviceA] commit
   ```
2. Configure DeviceB.
   
   
   
   # Configure an IP address for GE 0/1/1.
   
   ```
   <DeviceB> system-view
   [~DeviceB] interface GigabitEthernet 0/1/1
   [~DeviceB-GigabitEthernet0/1/1] ip address 10.1.2.1 24
   [*DeviceB-GigabitEthernet0/1/1] quit
   [*DeviceB] commit
   ```
   
   # Configure an IP address for GE 0/1/2.
   
   ```
   [~DeviceB] interface GigabitEthernet 0/1/2
   [~DeviceB-GigabitEthernet0/1/2] ip address 172.16.169.1 24
   [*DeviceB-GigabitEthernet0/1/2] quit
   [*DeviceB] commit
   ```
   
   # Create and configure a tunnel interface.
   
   ```
   [~DeviceB] interface Tunnel 10
   [*DeviceB-Tunnel10] tunnel-protocol ipsec
   [*DeviceB-Tunnel10] ip address 172.20.1.2 24
   [*DeviceB-Tunnel10] quit
   [*DeviceB] commit
   ```
   
   # Configure a static route destined for network A. The outbound interface of the route to network A is Tunnel 10, and the next hop address is 172.19.1.1. Assume that the next hop address of DeviceB is 172.16.169.2/24.
   
   ```
   [~DeviceB] ip route-static 10.1.1.0 255.255.255.0 Tunnel 10 172.19.1.1
   [*DeviceB] ip route-static 172.19.1.1 255.255.255.255 172.16.169.2
   [*DeviceB] commit
   ```
   
   # Create an advanced ACL numbered 3000 and configure a rule to define the packets whose source IP address is 10.1.2.0/24 and destination IP address is 10.1.1.0/24 as the packets to be encrypted.
   
   ```
   [~DeviceB] acl 3000
   [*DeviceB-acl-adv-3000] rule permit ip source 10.1.2.0 0.0.0.255 destination 10.1.1.0 0.0.0.255
   [*DeviceB-acl-adv-3000] quit
   [*DeviceB] commit
   ```
   
   # Create a private-public key pair.
   
   ```
   [~DeviceB] rsa pki local-key-pair key-b create
   [*DeviceB] commit
   ```
   
   # Configure entity information.
   
   ```
   [~DeviceB] pki entity entityb
   [*DeviceB-pki-entityb] common-name DeviceB
   [*DeviceB-pki-entityb] quit
   [*DeviceB] commit
   ```
   
   # Configure a CMP session.
   
   ```
   [~DeviceB] pki domain domainb
   [*DeviceB-pki-domainb] pki cmp session session-b
   [*DeviceB-pki-domainb-pki-cmp-session-b] cmp request entity entityb
   [*DeviceB-pki-domainb-pki-cmp-session-b] cmp request rsa local-key-pair key-b regenerate
   [*DeviceB-pki-domainb-pki-cmp-session-b] cmp request ca-name "/C=cn/ST=beijing/L=shangdi/O=BB/OU=BB/CN=AB"
   [*DeviceB-pki-domainb-pki-cmp-session-b] cmp request server url http://172.16.73.168:8080
   [*DeviceB-pki-domainb-pki-cmp-session-b] cmp request authentication-cert cert-b.cer
   [*DeviceB-pki-domainb-pki-cmp-session-b] quit
   [*DeviceB-pki-domainb] pki cmp initial-request
   [*DeviceB-pki-domainb] quit
   [*DeviceB] commit
   ```
   
   # Import the local certificate **session-b\_ir.cer** and CA certificate **session-b\_ca0.cer**.
   
   ```
   [~DeviceB] pki import-certificate local filename session-b_ir.cer
   [~DeviceB] pki import-certificate ca filename session-b_ca0.cer
   ```
   
   # Specify the local certificate in the CMP request for device identity authentication.
   
   ```
   [~DeviceB] pki domain domainb
   [*DeviceB-pki-domainb] pki cmp session session-b
   [*DeviceB-pki-domainb-pki-cmp-session-b] cmp request authentication-cert session-b_ir.cer
   ```
   
   # Configure automatic certificate update.
   
   ```
   [~DeviceB-pki-domainb-pki-cmp-session-b] certificate auto-update enable
   [*DeviceB-pki-domainb-pki-cmp-session-b] quit
   [*DeviceB-pki-domainb] quit
   [*DeviceB] commit
   ```
   
   # Enable CRL check.
   
   ```
   [~DeviceB] pki crl check enable
   [*DeviceB] commit
   ```
   
   # Configure automatic update of CRL.
   
   ```
   [~DeviceB] pki domain domainb
   [*DeviceB-pki-domainb] crl auto-update enable
   [*DeviceB-pki-domainb] crl update-period 3
   [*DeviceB-pki-domainb] crl http
   [*DeviceB-pki-domainb] crl url http://172.18.166.1/crl.crl
   [*DeviceB-pki-domainb] quit
   [*DeviceB] commit
   ```
   
   # Configure an IPsec proposal named **tran1**.
   
   ```
   [~DeviceB] ipsec proposal tran1
   [*DeviceB-ipsec-proposal-tran1] encapsulation-mode tunnel
   [*DeviceB-ipsec-proposal-tran1] transform esp
   [*DeviceB-ipsec-proposal-tran1] esp authentication-algorithm sha2-256
   [*DeviceB-ipsec-proposal-tran1] esp encryption-algorithm aes 256
   [*DeviceB-ipsec-proposal-tran1] quit
   [*DeviceB] commit
   ```
   
   # Configure an IKE proposal.
   
   ```
   [~DeviceB] ike proposal 10
   [*DeviceB-ike-proposal-10] authentication-method rsa-sig
   [*DeviceB-ike-proposal-10] authentication-algorithm sha2-256
   [*DeviceB-ike-proposal-10] integrity-algorithm hmac-sha2-256
   [*DeviceB-ike-proposal-10] dh group14
   [*DeviceB-ike-proposal-10] quit
   [*DeviceB] commit
   ```
   
   # Configure an IKE peer.
   
   ```
   [~DeviceB] ike peer a
   [*DeviceB-ike-peer-a] ike-proposal 10
   [*DeviceB-ike-peer-a] certificate local-filename session-b_ir.cer
   [*DeviceB-ike-peer-a] remote-address 172.19.1.1
   [*DeviceB-ike-peer-a] quit
   [*DeviceB] commit
   ```
   
   # Configure an IPsec policy named **map1**.
   
   ```
   [~DeviceB] ipsec policy map1 10 isakmp
   [*DeviceB-ipsec-policy-isakmp-map1-10] security acl 3000
   [*DeviceB-ipsec-policy-isakmp-map1-10] proposal tran1
   [*DeviceB-ipsec-policy-isakmp-map1-10] ike-peer a
   [*DeviceB-ipsec-policy-isakmp-map1-10] quit
   [*DeviceB] commit
   ```
   
   # Configure an IPsec service instance group named **group1**.
   
   ```
   [~DeviceB] service-location 1
   [*DeviceB-service-location-1] location slot 1
   [*DeviceB-service-location-1] commit
   [~DeviceB-service-location-1] quit
   [~DeviceB] service-instance-group group1
   [*DeviceB-service-instance-group-group1] service-location 1
   [*DeviceB-service-instance-group-group1] commit
   [~DeviceB-service-instance-group-group1] quit
   ```
   
   # Apply the security policy **map1** to the tunnel interface.
   
   ```
   [~DeviceB] interface Tunnel10 
   [~DeviceB-Tunnel10] ipsec policy map1 service-instance-group group1
   [*DeviceB-Tunnel10] quit
   [*DeviceB] commit
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
   sysname DeviceA
  #
  acl number 3000
    rule 5 permit ip source 10.1.1.0 0.0.0.255 destination 10.1.2.0 0.0.0.255
  #
  ike proposal 10
   authentication-method rsa-sig
   encryption-algorithm aes-cbc 256
   dh group14
   authentication-algorithm sha2-256 
   integrity-algorithm hmac-sha2-256
  #
  ike peer b
   ike-proposal 10
   certificate local-filename session-a_ir.cer
   remote-address 172.20.1.2
  #
  service-location 1
   location slot 1
  #
  service-instance-group group1
   service-location 1
  #
  ipsec proposal tran1
   esp authentication-algorithm sha2-256  
   esp encryption-algorithm aes 256
  #                                         
  ipsec policy map1 10 isakmp
   security acl 3000
   ike-peer b
   proposal tran1
  #                                                                               
  interface GigabitEthernet0/1/1 
   ip address 10.1.1.1 255.255.255.0                                                
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   ip address 172.16.163.1 255.255.255.0                                                 
  #                                                                               
  interface Tunnel10
   ip address 172.19.1.1 255.255.255.0                                             
   tunnel-protocol ipsec 
   ipsec policy map1 service-instance-group group1                                                                        
  #
   ip route-static 10.1.2.0 255.255.255.0 Tunnel 10 172.20.1.2
   ip route-static 172.20.1.2 255.255.255.255 172.16.163.2
  #
  pki entity entitya
   common-name DeviceA
  #
  pki domain domaina
   crl auto-update enable
   crl update-period 3
   crl http
   crl url http://172.18.166.1/crl.crl 
   pki cmp initial-request
   #
   pki cmp session session-a
    cmp request entity entitya
    cmp request rsa local-key-pair key-a regenerate
    cmp request ca-name "/C=cn/ST=beijing/L=shangdi/O=BB/OU=BB/CN=AB"
    cmp request server url http://172.16.73.168:8080
    cmp request authentication-cert cert-a.cer
    cmp request authentication-cert session-a_ir.cer
    certificate auto-update enable
  #
  return
  ```
* DeviceB configuration file
  ```
  #
   sysname DeviceB
  #
  acl number 3000
    rule 5 permit ip source 10.1.2.0 0.0.0.255 destination 10.1.1.0 0.0.0.255
  #
  ike proposal 10
   authentication-method rsa-sig
   encryption-algorithm aes-cbc 256
   dh group14
   authentication-algorithm sha2-256 
   integrity-algorithm hmac-sha2-256
  #
  ike peer a
   certificate local-filename session-b_ir.cer
   ike-proposal 10
   remote-address 172.19.1.1
  #
  service-location 1
   location slot 1
  #
  service-instance-group group1
   service-location 1
  #
  ipsec proposal tran1
   transform esp
   esp authentication-algorithm sha2-256
  #
  ipsec policy map1 10 isakmp
   security acl 3000
   ike-peer a
   proposal tran1
  #                                                                               
  interface GigabitEthernet0/1/1 
   ip address 10.1.2.1 255.255.255.0                                                
  #                                                                               
  interface GigabitEthernet0/1/2                                                  
   ip address 172.16.169.1 255.255.255.0                                                 
  #                                                                               
  interface Tunnel10 
   ip address 172.20.1.2 255.255.255.0                                             
   tunnel-protocol ipsec 
   ipsec policy map1 service-instance-group group1                                                                          
  #
   ip route-static 10.1.1.0 255.255.255.0 Tunnel 10 172.19.1.1
   ip route-static 172.19.1.1 255.255.255.255 172.16.169.2
  #
  pki entity entityb
   common-name DeviceB
  #
  pki domain domainb
   crl auto-update enable
   crl update-period 3
   crl http
   crl url http://172.18.166.1/crl.crl
   #
   pki cmp session session-b
    cmp request entity entityb
    cmp request rsa local-key-pair key-b regenerate
    cmp request ca-name "/C=cn/ST=beijing/L=shangdi/O=BB/OU=BB/CN=AB"
    cmp request server url http://172.16.73.168:8080
    cmp request authentication-cert cert-b.cer 
    cmp request authentication-cert session-b_ir.cer
    certificate auto-update enable 
  #
  return
  ```