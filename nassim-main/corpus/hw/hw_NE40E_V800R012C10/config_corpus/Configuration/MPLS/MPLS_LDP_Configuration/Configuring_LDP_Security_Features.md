Configuring LDP Security Features
=================================

LDP security features, such as MD5 authentication, LDP generalized TTL security mechanism (GTSM), and keychain authentication can be configured to meet high network security requirements. By default, no LDP security features are configured. You are advised to configure security features as required. Otherwise, the system may be insecure.

#### Usage Scenario

MD5 authentication, LDP GTSM, or keychain authentication can be configured on an MPLS network to meet network security requirements:![](../../../../public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.

* LDP MD5 authentication
  
  A typical MD5 application is to calculate a message digest to prevent message spoofing. The MD5 message digest is a unique result calculated using an irreversible character string conversion. If a message is modified during transmission, a different digest is generated. After the message arrives at the receiving end, the receiving end can detect the modification after comparing the received digest with a pre-computed digest.
  
  When configuring MD5 authentication, you can configure different authentication modes (plaintext or ciphertext) for the two peers of an LDP session. The passwords on the two peers, however, must be the same.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  As MD5 is insecure, you are advised to use a more secure authentication mode.
* LDP keychain authentication
  
  Keychain, an enhanced encryption algorithm similar to MD5, calculates a message digest for an LDP message to prevent the message from being modified.
  
  Keychain allows users to define a group of passwords to form a password string. Each password is assigned encryption and decryption algorithms, such as MD5 and secure hash algorithm-1 (SHA-1), and a validity period. The system selects a valid password before sending or receiving a packet. Within the validity period of the password, the system uses the encryption algorithm matching the password to encrypt the packet before sending it. The system also uses the decryption algorithm matching the password to decrypt the packet before accepting the packet. In addition, the system automatically uses a new password after the previous password expires, which minimizes password decryption risks.
  
  Before configuring LDP keychain authentication, configure keychain authentication globally. If LDP keychain authentication is configured before global keychain authentication, the LDP session will be disconnected.
* LDP GTSM
  
  The GTSM checks TTL values to defend against attacks. An attacker simulates unicast LDP messages and sends them to nodes. After receiving these messages, an interface board on a node finds that the messages are destined for itself. It directly sends them to the LDP module on the control plane without verifying them. As a result, the node is busy in processing these forged messages on the control plane, leading to high CPU usage.
  
  To address this problem, the GTSM can be configured to check whether the TTL value in the IP header is within a specified range. It protects the nodes from attacks and improves system security.
* Whitelist session-CAR for LDP
  
  When the LDP service suffers a traffic burst, bandwidth may be preempted among LDP sessions. To resolve this problem, you can configure whitelist session-CAR for LDP to isolate bandwidth resources by session.


#### Pre-configuration Tasks

Before configuring LDP security features, complete the following tasks:

* Enable MPLS and MPLS LDP.
* (Optional) Configure keychain authentication globally.


[Configuring LDP MD5 Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0056.html)

LDP authentication can be configured to improve the security of a connection over which an LDP session is established. LDP authentication is configured on LSRs at both ends of an LDP session.

[Configuring LDP Keychain Authentication for a TCP Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0057.html)

LDP keychain authentication can be configured to improve the security of a TCP connection used to establish an LDP session. LDP authentication is configured on LSRs at both ends of an LDP session.

[Configuring LDP Keychain Authentication for a UDP Connection](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0057_new.html)

LDP keychain authentication can be configured to improve the security of a UDP connection used to establish an LDP session. LDP authentication is configured on LSRs at both ends of an LDP session.

[Configuring LDP TCP-AO Authentication](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_tcp-ao.html)

This section describes how to configure LDP TCP-AO authentication to check the integrity of LDP packets and prevent TCP replay attacks.

[Configuring the LDP GTSM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0058.html)

The LDP Generalized TTL Security Mechanism (GTSM) needs to be configured on the LDP peers at both ends of an LDP session.

[Configuring Whitelist Session-CAR for LDP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_session-car.html)

You can configure whitelist session-CAR for LDP to isolate bandwidth resources by session for LDP packets. This configuration prevents bandwidth preemption among LDP sessions in the case of a traffic burst.

[Configuring Micro-Isolation CAR for LDP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_micro-car.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0059.html)

After configuring LDP security features, you can view the configurations of LDP MD5 authentication, LDP GTSM, and LDP keychain authentication.