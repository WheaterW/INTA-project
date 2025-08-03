Configuring the OSPF Authentication Mode for DCN Interfaces
===========================================================

Configuring the OSPF Authentication Mode for DCN Interfaces

#### Security Policy

OSPF/OSPFv3 supports packet authentication. Packets are accepted only if they are authenticated. If packets fail to be authenticated, neighbor relationships cannot be established. If area authentication is used, authentication mode and password configurations on all Routers in the same area must be the same. Interface authentication is implemented by setting an authentication mode and password between neighboring Routers. Interface authentication takes precedence over area authentication.

By default, DCN interfaces run the OSPF protocol. On a network that requires high security, you can set the OSPF authentication mode and authentication key for adjacent routers on DCN interfaces to improve network security.


#### Attack Methods

OSPF is attacked mainly through forged packets. To identify and discard these packets, authentication can be configured.

An attacker may use the following methods to initiate attacks:

* Changes the aging time of a packet to the maximum aging time so that all Routers discard this packet.
* Advertises the LSAs with valid Max Sequence Numbers or with sequence numbers close to the Max Sequence Number.
* Changes the sequence number when the state of the encryption sequence number resets during a neighbor Router restart.
* Changes the peer list in Hello packets.

#### Configuration and Maintenance Methods

* Configure OSPF authentication for DCN interfaces.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     The interface view is displayed.
  3. Run [**dcn (interface view)**](cmdqueryname=dcn+%28interface+view%29) or [**dcn mode vlan**](cmdqueryname=dcn+mode+vlan)
     
     DCN is enabled on the DCN serial interface or sub-interface 4094.
  4. Run any of the following commands to configure the OSPF authentication mode for the DCN interface:
     + To configure OSPF simple authentication, run the [**dcn ospf authentication-mode simple**](cmdqueryname=dcn+ospf+authentication-mode+simple) [ [ **plain** ] *plain-text* | [ **cipher** ] *cipher-text* ] command.
     + To configure OSPF ciphertext authentication, run the [**dcn ospf authentication-mode**](cmdqueryname=dcn+ospf+authentication-mode) { **md5** | **hmac-md5** | **hmac-sha256** } [ *key-id* { **plain** *plain-text* | [ **cipher** ] *cipher-text* } ] command.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       - To ensure high security, do not use the MD5 or HMAC-MD5 algorithm. If you need to use the MD5 or HMAC-MD5 algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function. To prevent security risks, you are advised to use the HMAC-SHA256 algorithm.
       - The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
       - For security purposes, you are advised to configure a ciphertext password and change the password periodically.
     + To configure null authentication, run the [**dcn ospf authentication-mode null**](cmdqueryname=dcn+ospf+authentication-mode+null) command. In null authentication mode, OSPF packets are not authenticated.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.

#### Verifying the Security Hardening Result

Run the [**display ospf peer**](cmdqueryname=display+ospf+peer) command to check information about the OSPF neighbor established on the DCN serial interface.