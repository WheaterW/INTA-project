SNMP
====

SNMP is used to manage network devices. Network administrators can use SNMP to obtain data from devices and configure devices. SNMP also provides the trap and inform functions. When the important status changes on a device, the device reports the event to an NMS.

#### Security Policy

SNMPv1, SNMPv2c, and SNMPv3 support different security policies.

SNMPv1 and SNMPv2c support ACLs and the view-based access control model (VACM). Associate an ACL and a MIB view with a community name to limit the NMSs and nodes that can access a device, enhancing system security to some extent. SNMPv1 and SNMPv2c do not support encryption algorithms.

In addition to support for ACLs and VACM, SNMPv3 supports the user-based security model (USM), authentication algorithms, and encryption algorithms. A supported authentication algorithm can be message digest algorithm 5 (MD5) or secure hash algorithm (SHA-1/SHA-2). A supported encryption algorithm can be data encryption standard (DES), 3DES, or Advanced Encryption Standard (AES). SNMPv3 authenticates and encrypts communication data to solve security problems such as message forging, modification, and disclosure.

Configure the lock mechanism for SNMP so that the IP address of a user is locked after the user fails the authentication. (The lock mechanism is enabled by default.)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

To ensure high security, you are advised to use the SHA algorithm as the authentication algorithm. Do not use the DES or 3DES algorithm as the SNMPv3 encryption algorithm.

CPCAR-based security policies can be used to defend against flood attacks. If a device is connected to the public address space of the Internet, the management and control plane of the device may suffer from flood attacks. In this case, you can deploy a CPU attack defense policy to protect the device against traffic attacks.


#### Attack Methods

* User name and password cracking
  
  An attacker continuously sends SNMPv1/v2c community names and SNMPv3 user names and passwords to crack authorized user names and passwords.
* Unauthorized management operations
  
  + An attacker modifies the source IP address of sent packets to obtain the rights of an authorized user and perform unauthorized management operations.
  + An attacker listens to communication between NMSs and SNMP agents to collect information, such as user names, community names, and passwords in order to obtain unauthorized access rights.
  + An attacker intercepts, reorders, delays, or retransmits SNMP messages to affect normal operations and obtain unauthorized operation rights.
* DoS attack
  
  An attacker launches DoS attacks to slow the device response. For example, mass packet attacks result in a full SNMP message cache table and a failure to process requests from the NMS.
* Invalid packet attack
  
  + An attacker sends invalid packets, such as overlong packets, packets with incorrect SNMP version, write-intended packets with the read right, SNMPv3 packets with incorrect contextname field, packets with incorrect security model, and packets with incorrect security level.
  + An attacker sends invalid inform reply packets to the device.
* SNMP GetBulk reply magnifying DoS attack
  
  SNMP packets are transmitted based on UDP, which is connectionless-oriented. To be specific, both the client and server do not record the peer status or implement data verification for the peer. In this case, the source IP address of such request packets sent from the client can be easily spoofed, causing the response packet to be sent to the bogus IP address. The attacker sends a short request packet and triggers response of overlong packets, causing packet flooding.


#### Configuration and Maintenance Methods

For security purposes, disabling the insecure SNMPv1 and SNMPv2c is recommended. Configure SNMPv3 users with authentication and encryption configuration, use an SNMPv3 authentication and encryption mode to manage devices, and associate an ACL and a MIB view with the user to control access rights.

1. Disable the insecure SNMPv1 and SNMPv2c if they are not used.
   
   ```
   [~HUAWEI] undo snmp-agent sys-info version v1 v2c
   ```
   ```
   [*HUAWEI] commit
   ```
2. Configure an ACL numbered 2001 and define a rule to permit some IP addresses and a rule to deny some IP addresses.
   
   ```
   [~HUAWEI] acl 2001
   ```
   ```
   [*HUAWEI-acl4-basic-2001] rule 5 permit
   ```
   ```
   [*HUAWEI-acl4-basic-2001] rule 10 deny source 10.138.90.111 0
   ```
   ```
   [*HUAWEI-acl4-basic-2001] commit
   ```
3. Configure an SNMP ACL.
   
   ```
   [~HUAWEI] snmp-agent acl 2001
   ```
   ```
   [*HUAWEI] commit
   ```
4. Configure a MIB view named **iso-view** to access nodes in the subtree whose root node is **iso**.
   
   ```
   [~HUAWEI] snmp-agent
   ```
   ```
   [*HUAWEI] snmp-agent mib-view included iso-view iso
   ```
   ```
   [*HUAWEI] commit
   ```
5. Configure an SNMPv3 group named **v3group**, associate ACL 2001 with the group, and associate the read view, write view, and notification view named **iso-view** with the group.
   
   ```
   [~HUAWEI] snmp-agent group v3 v3group privacy read-view iso-view write-view iso-view notify-view iso-view acl 2001
   ```
   ```
   [*HUAWEI] commit
   ```
6. Configure an SNMPv3 user named **v3user** and add the user to **v3group**. Set the authentication mode and password to **sha2-256** and **hello-1234**, respectively. Set the encryption mode and password to **aes256** and **Hello-2012**, respectively. Associate ACL 2001 with the user.
   
   ```
   [~HUAWEI] snmp-agent usm-user v3 v3user v3group
   ```
   ```
   [*HUAWEI] snmp-agent usm-user v3 v3user v3group acl 2001
   ```
   ```
   [*HUAWEI] snmp-agent usm-user v3 v3user v3group authentication-mode sha2-256 Hello-1234 privacy-mode aes256 Hello-2012
   ```
   ```
   [*HUAWEI] commit
   ```
7. Check the current SNMP configurations.
   
   ```
   [~HUAWEI] display current-configuration | include snmp
   ```
   ```
   snmp-agent
   snmp-agent acl 2001
   snmp-agent local-engineid 800007DB0338BA376BEA01
   undo snmp-agent sys-info version v3
   snmp-agent group v3 v3group privacy read-view iso-view write-view iso-view notify-view iso-view acl 2001
   snmp-agent mib-view included iso-view iso
   snmp-agent usm-user v3 v3user
   snmp-agent usm-user v3 v3user group v3group
   snmp-agent usm-user v3 v3user authentication-mode sha2-256 cipher %^%#!h7X2jV15~c13:~1|(V-:ea+I&v*X8[V;Z61$y];%^%#
   snmp-agent usm-user v3 v3user privacy-mode aes256 cipher %^%#Ko$vVUNO[A3t4O%KX6I5nv\4N_o%b#GL'K#dYTZ'%^%#
   snmp-agent usm-user v3 v3user acl 2001
   ```

Configure SNMPv1 and SNMPv2c community names. Restrict user access rights using the association between an ACL, a MIB view, and a community name.

1. Configure an ACL numbered 2001 and define a rule to permit some IP addresses and a rule to deny some IP addresses.
   
   ```
   [~HUAWEI-acl-basic-2001] display this
   ```
   ```
   #
   ```
   ```
   acl number 2001
   ```
   ```
    rule 5 permit
   ```
   ```
    rule 10 permit source 10.138.90.111 0
   ```
   ```
   #
   ```
   ```
   return
   ```
   ```
   [~HUAWEI-acl-basic-2001]
   ```
2. Configure a MIB view named **iso-view** to access nodes in the subtree whose root node is **iso**.
   
   ```
   [~HUAWEI] snmp-agent
   ```
   ```
   [*HUAWEI] snmp-agent mib-view included iso-view iso
   ```
   ```
   [*HUAWEI] commit
   ```
3. Configure a read-write community name.
   
   ```
   [~HUAWEI] snmp-agent community read cipher Public-123456 mib-view iso-view acl 2001
   ```
   ```
   [*HUAWEI] snmp-agent community write cipher Private-123456 mib-view iso-view acl 2001
   ```
   ```
   [*HUAWEI] snmp-agent sys-info version all
   ```
   ```
   [*HUAWEI] commit
   ```
4. Check the SNMP configurations.
   
   ```
   [~HUAWEI] display this | include snmp
   ```
   ```
   snmp-agent
   snmp-agent local-engineid 800007DB0338BA376BEA01
   snmp-agent community read cipher %^%#{H1SU1d}/A{%ZQ8eZwr1,7#s<+=_J$q+G8C|_$m5wG62/.GguS`8ur>lpTzGS[hHLQitwV9Ih*MQcC>W%^%# mib-view iso-viewiso acl 2001
   snmp-agent community write cipher %^%#~]`4X&Vz`#6W1^8<h<L*gBDu3T/^IXLQ%]7=O@1<'jHCF4o=-KBCH{,8JC~!"v':C8y'sPCq["-/\29G%^%# mib-view iso-viewiso acl 2001
   snmp-agent sys-info version all
   snmp-agent mib-view included iso-view iso
   ```

Configure CPCAR-based flood attack defense policies.

1. Configure a CPU defense policy.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] cpu-defend policy 10
   ```
   ```
   [*HUAWEI-cpu-defend-policy-10] commit
   ```
2. Configure TCP/IP attack defense.
   
   If the function is disabled, run the following command to enable it:
   
   ```
   [~HUAWEI-cpu-defend-policy-10] ctcpsyn-flood enable
   ```
   ```
   [*HUAWEI-cpu-defend-policy-10] fragment-flood enable
   ```
   ```
   [*HUAWEI-cpu-defend-policy-10] udp-packet-defend enable
   ```
   ```
   [*HUAWEI-cpu-defend-policy-10] abnormal-packet-defend enable
   ```
   ```
   [*HUAWEI-cpu-defend-policy-10] quit
   ```
   ```
   [*HUAWEI] commit
   ```
3. Create an ACL.
   
   Add SNMP to ACL 3341.
   
   ```
   [~HUAWEI] acl number 3341
   ```
   ```
   [*HUAWEI-acl-adv-3341] rule permit udp source 10.20.20.0 0.0.0.255 source-port eq snmp
   ```
   ```
   [*HUAWEI-acl-adv-3341] rule permit udp source 10.20.20.0 0.0.0.255 destination-port eq snmp
   ```
   ```
   [*HUAWEI-acl-adv-3341] rule deny udp destination-port eq snmp
   ```
   ```
   [*HUAWEI-acl-adv-3341] commit
   ```
4. Create a user-defined flow.
   
   After the ACL is used to classify protocol packets, you can apply the ACL to create user-defined flows so that different protocol packets are transmitted through different channels.
   
   ACL 3341 corresponds to user-defined flow 11 and is used to protect SNMP. SNMP traffic is heavy but does not require high real-time performance. Therefore, set the priority to low and bandwidth to 1 Mbit/s.
   
   ```
   [~HUAWEI] cpu-defend policy 10
   ```
   ```
   [*HUAWEI-cpu-defend-policy-10] user-defined-flow 11 acl 3341
   ```
   ```
   [*HUAWEI-cpu-defend-policy-10] car user-defined-flow 11 cir 1000
   ```
   ```
   [*HUAWEI-cpu-defend-policy-10] priority user-defined-flow 11 low
   ```
   ```
   [*HUAWEI-cpu-defend-policy-10] quit
   ```
   ```
   [*HUAWEI] commit
   ```
5. Apply the attack defense policy.
   
   ```
   [~HUAWEI] slot 10
   ```
   ```
   [*HUAWEI-slot-10] cpu-defend-policy 10
   ```
   ```
   [*HUAWEI-slot-10] quit
   ```
   ```
   [*HUAWEI] commit
   ```


#### Configuration and Maintenance Suggestions

* SNMPv1 and SNMPv2c community names are stored in ciphertext. Only high-level commands can query ciphertext community names.
* Store community names and user passwords in ciphertext to effectively protect them from being disclosed.
* Passwords and community names are stored as \*\*\*\*\*\* in the operation logs on the SNMP server, CLI, and NETCONF tool, to prevent user information leaks.
* SNMPv1 and SNMPv2c are not secure. Therefore, using SNMPv3 is recommended.
* Disable SNMP if it is unnecessary on a device. (SNMP is disabled by default.)
* When SNMPv3 is configured, ensure that authentication and encryption passwords meet the password complexity requirements and that the authentication password is different from the encryption password. If SNMPv1 or SNMPv2c is configured, the SNMP community name must pass the complexity check.
* Configure the lock mechanism for SNMP so that the IP address of a user is locked after the user fails the authentication. (The lock mechanism is enabled by default.)
* Configure URPF on the edge devices to prevent response attacks.

#### Verifying the Security Hardening Result

* Run the **display this | include snmp** command in the system view to check the SNMP configuration.
* Run the **display cpu-defend** **tcpip-defend** **statistics** [ **slot** *slot-id* ] command to view information about defense against TCP/IP attacks.