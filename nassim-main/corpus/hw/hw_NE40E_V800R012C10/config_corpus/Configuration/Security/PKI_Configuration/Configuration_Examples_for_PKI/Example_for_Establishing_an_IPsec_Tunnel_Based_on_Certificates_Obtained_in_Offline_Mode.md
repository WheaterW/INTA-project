Example for Establishing an IPsec Tunnel Based on Certificates Obtained in Offline Mode
=======================================================================================

This section provides an example for establishing an IPsec tunnel based on certificates obtained in offline mode.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172372557__fig19886103514551), network A and network B connect to the Internet through DeviceA and DeviceB, respectively. The networking environment is as follows:

* Network A belongs to the subnet 10.1.1.0/24 and connects to DeviceA through GE 0/1/1.
* Network B belongs to the subnet 10.1.2.0/24 and connects to DeviceB through GE 0/1/1.
* Routes between DeviceA and DeviceB are reachable.

Configure the devices to establish an IPsec tunnel in IKE auto-negotiation mode, protecting the data flows transmitted between network A and network B. The requirements are as follows:

* DeviceA and DeviceB apply for certificates in offline mode for mutual identity authentication.
* The tunnel encapsulation mode is used.
* ESP is used as the security protocol.
* The encryption algorithm of ESP is set to AES.
* The authentication algorithm of ESP is set to SHA2-256.
* The integrity algorithm is set to HMAC-SHA2-256.

**Figure 1** Network diagram of IPsec tunnel establishment based on certificates obtained in offline mode![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/1 and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001904735613.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses.
2. Create and configure tunnel interfaces.
3. Configure public network routes (typically static routes).
4. Configure ACL rules to define the data flows to be protected.
5. Configure PKI offline certificate application and use the default certificate attributes to control access.
   
   1. Create public-private key pairs.
   2. Configure entity information.
   3. Obtain certificates.
   4. Configure the default access control policy based on certificate attributes.
6. Establish an IPsec tunnel using security policy auto-negotiation.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of interfaces
* ACL rules
* Entity information, PKI domain, certificate download mode, and access control policy based on certificate attributes
* Security protocol, encryption algorithm, and authentication algorithm to be used in an IPsec proposal; authentication algorithm to be used in an IKE proposal

#### Procedure

1. Configure DeviceA.
   
   
   
   # Disable CRL check.
   
   ```
   <DeviceA> system-view
   [~DeviceA] undo pki crl check enable
   [*DeviceA] commit
   ```
   
   # Configure an IP address for GE 0/1/1.
   
   ```
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
   
   # Create an RSA key pair (a non-default key pair is used in this example).
   
   ```
   [~DeviceA] rsa pki local-key-pair rsa create
   [*DeviceA] commit
   ```
   
   # Configure entity information.
   
   ```
   [~DeviceA] pki entity entitya
   [*DeviceA-entitya] common-name DeviceA
   [*DeviceA-entitya] quit
   [*DeviceA] commit
   ```
   
   # Configure a PKI domain and associate certificate information with the domain.
   
   ```
   [~DeviceA] pki domain domaina
   [*DeviceA-domaina] certificate request entity entitya
   [*DeviceA-pki-domaina] commit
   [~DeviceA] quit
   [~DeviceA] pki domain domaina
   [*DeviceA-pki-domaina] pki cmp session domaina
   [*DeviceA-pki-domaina-cmp-session-domaina] cmp request rsa local-key-pair rsa
   [*DeviceA-pki-domaina-cmp-session-domaina] commit
   [~DeviceA-pki-domaina-cmp-session-domaina] quit
   ```
   
   # Generate a certificate request file named **domaina.req**.
   
   ```
   [~DeviceA] pki request-certificate domain domaina pkcs10
   ```
   
   # Send the certificate request file to the CA server for generating certificates. Assume that the generated local certificate is **local.cer** and the CA certificate is **ca.cer**.
   
   # Manually download the local certificate and CA certificate.
   
   # Import the local certificate and CA certificate into the memory of the device.
   * If a certificate that does not belong to the domain is used for negotiation, import the certificate directly to the memory.
     ```
     [~DeviceA] pki import-certificate local filename local.cer
     [~DeviceA] pki import-certificate ca filename ca.cer
     ```
   * If a certificate that belongs to the domain is used for negotiation, import the certificate to the domain.
     ```
     [~DeviceA] pki import-certificate local domain domaina filename local.cer
     [~DeviceA] pki import-certificate ca domain domaina filename ca.cer
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
   [*DeviceA-ike-peer-b] certificate local-filename local.cer  //Perform this configuration if a certificate that does not belong to the domain is used for negotiation.
   [*DeviceA-ike-peer-b] certificate local pki-domain domaina  //Perform this configuration if a certificate that belongs to the domain is used for negotiation.
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
   
   
   
   # Disable CRL check.
   
   ```
   <DeviceB> system-view
   [~DeviceB] undo pki crl check enable
   [*DeviceA] commit
   ```
   
   # Configure an IP address for GE 0/1/1.
   
   ```
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
   
   # Create an RSA key pair (a non-default key pair is used in this example).
   
   ```
   [~DeviceB] rsa pki local-key-pair rsa create
   ```
   
   # Configure entity information.
   
   ```
   [~DeviceB] pki entity entityb
   [*DeviceB-entityb] common-name DeviceB
   [*DeviceB-entityb] quit
   [*DeviceB] commit
   ```
   
   # Configure a PKI domain and associate certificate information with the domain.
   
   ```
   [~DeviceB] pki domain domainb
   [*DeviceB-domainb] certificate request entity entityb
   [*DeviceB-pki-domaina] commit
   [~DeviceB] quit
   [~DeviceB] pki domain domainb
   [*DeviceB-pki-domainb] pki cmp session domainb
   [*DeviceB-pki-domainb-cmp-session-domaina] cmp request rsa local-key-pair rsa
   [*DeviceB-pki-domainb-cmp-session-domaina] commit
   [~DeviceB-pki-domainb-cmp-session-domaina] quit
   ```
   
   # Generate a certificate request file named **domainb.req**.
   
   ```
   [~DeviceB] pki request-certificate domain domainb pkcs10
   ```
   
   # Send the certificate request file to the CA server for generating certificates. Assume that the generated local certificate is **local.cer** and the CA certificate is **ca.cer**.
   
   # Manually download the local certificate and CA certificate.
   
   # Import the local certificate and CA certificate into the memory of the device.
   * If a certificate that does not belong to the domain is used for negotiation, import the certificate directly to the memory.
     ```
     [~DeviceB] pki import-certificate local filename local.cer
     [~DeviceB] pki import-certificate ca filename ca.cer
     ```
   * If a certificate that belongs to the domain is used for negotiation, import the certificate to the domain.
     ```
     [~DeviceB] pki import-certificate local domain domainb filename local.cer
     [~DeviceB] pki import-certificate ca domain domainb filename ca.cer
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
   [*DeviceB-ike-peer-a] certificate local-filename local.cer  //Perform this configuration if a certificate that does not belong to the domain is used for negotiation.
   [*DeviceB-ike-peer-a] certificate local pki-domain domainb  //Perform this configuration if a certificate that belongs to the domain is used for negotiation.
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
   
   # Apply the IPsec proposal to the tunnel interface.
   
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
  undo pki crl check enable
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
   certificate local-filename local.cer  //Perform this configuration if a certificate that does not belong to the domain is used for negotiation.
   certificate local pki-domain domaina  //Perform this configuration if a certificate that belongs to the domain is used for negotiation.
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
   undo shutdown
   ip address 10.1.1.1 255.255.255.0    
  #  
  interface GigabitEthernet0/1/2
   undo shutdown
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
   certificate request entity entitya
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
   sysname DeviceB
  #
  undo pki crl check enable
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
   certificate local-filename local.cer  //Perform this configuration if a certificate that does not belong to the domain is used for negotiation.
   certificate local pki-domain domainb  //Perform this configuration if a certificate that belongs to the domain is used for negotiation.
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
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec policy map1 10 isakmp
   security acl 3000
   ike-peer a
   proposal tran1
  #  
  interface GigabitEthernet0/1/1 
   undo shutdown
   ip address 10.1.2.1 255.255.255.0    
  #  
  interface GigabitEthernet0/1/2 
   undo shutdown
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
   certificate request entity entityb
  #
  return
  ```