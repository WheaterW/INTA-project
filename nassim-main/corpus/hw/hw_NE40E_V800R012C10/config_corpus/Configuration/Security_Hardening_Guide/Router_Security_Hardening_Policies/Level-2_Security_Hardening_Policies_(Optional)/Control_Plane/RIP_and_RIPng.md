RIP/RIPng
=========

RIP/RIPng

#### Security Policy Overview

Rapid development of networks poses higher network security requirements. Routing protocol packets transmitted over networks may be illegally obtained, changed, or forged, and packet attacks may cause network interruptions. Therefore, measures must be taken to ensure packet transmission security.

* Protocol security mechanism
  
  RIP/RIPng supports the following security policies at the protocol layer:
  
  + TTL/hop limit mechanism:
    
    The scope of RIP/RIPng packet transmission is always one hop from the originator. RIP/RIPng sets the TTL/hop limit to 1 for the RIP/RIPng packets to be transmitted on broadcast or multicast networks.
  + Whitelist security policy:
    
    RIP/RIPng provides whitelist security for neighbor ports to prevent packet loss caused by CP-CAR policies.
  + GTSM security policy
    
    RIP uses GTSM policies to prevent packet attacks through TTL detection. TTL specifies the maximum number of devices through which a packet can pass. The TTL field exists in IP headers. The forwarding plane of a neighbor directly filters out the protocol packets whose TTL values exceed the TTL range, preventing the control plane from being attacked.
  + Authentication policies:
    
    RIP-2 supports a packet authentication mechanism to prevent receiving bad routing data, error packets, and replay attacks from networks.
    
    RIPng does not define any authentication mechanism to prevent receiving bad routing data, error packets, or replay attacks. RIPng supports IPsec authentication for RIPng packets.
  + Route limit
    
    RIP/RIPng limits the maximum number of routes that can be added to the RIP/RIPng database to limit the route information based on the device capacity.
* Policy for defending against attacks using a large number of error packets:
  
  RIP uses the whitelist security policy to prevent attacks from massive error packets.
* Other policies:
  
  The system supports CP-based policies (CAR) on each interface to define the bandwidth for receiving packets from unknown sources.

#### Attack Methods

* DoS attacks:
  
  RIP uses the whitelist security policy to prevent DoS attacks.
  
  When a DoS attack occurs, the device may obtain RIP packets from a remote path. These packets will be processed by an I/O board and sent to a main control board, on which they will be discarded by RIP/RIPng. This wastes bandwidth and CPU resources and reduces system performance.
  
  To prevent the device from processing these packets from unknown sources, RIP/RIPng provides the whitelist function. A whitelist label is created for each known interface so that packets can be exchanged rapidly. This is necessary to ensure quick convergence on the network. If the interfaces that send packets are not in the whitelist, these interfaces are allocated only the default bandwidth, which is limited.
* Injection of massive routing information:
  
  RIP applies to devices of various levels. The CPU and memory of a device determine the number of RIP/RIPng routes that can be processed. If the number of routes received is greater than the device capacity, CPU and memory are overused, causing the device to become unstable. To ensure that the device runs stably, you can set the maximum number of routes that can be accepted by RIP/RIPng.
* Injection of incorrect routing information:
  
  RIP/RIPng will accept any packet from a valid source address that matches the configured network. Direct route data is carried directly in packets. Therefore, the routing data carried in RIP packets may contain invalid or incorrect route information. The incorrect information causes the generated routing database to be incorrect and leads to network failures.
  
  If authentication is configured on the RIP interface on both sides, RIP only accepts packets if they are authenticated in order to prevent accepting routes from unauthenticated devices.
  
  If IPsec is configured on both sides, RIPng will only accept the packets that are authenticated to prevent the device from accepting routes from unauthenticated devices.
* Replay attacks:
  
  RIP supports sequence numbers in MD5 authenticated packets to prevent replay attacks.

#### Procedure

![](../../../../public_sys-resources/note_3.0-en-us.png) 

It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.

* Configure RIP packet authentication.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run **interface** *interface-type* *interface-number*
     
     The interface view is displayed.
  3. Perform the following configurations as required:
     + To configure simple plaintext authentication for RIP-2 packets, run the [**rip authentication-mode**](cmdqueryname=rip+authentication-mode) **simple** { **plain** *plain-text* | [ **cipher** ] *password-key* } command.
       
       In simple authentication mode, the password in plaintext mode is transmitted along with each authentication packet. Therefore, simple authentication is not recommended on networks requiring high security.
     + To configure MD5 authentication for RIP-2 packets, run the [**rip authentication-mode**](cmdqueryname=rip+authentication-mode) **md5** { **nonstandard** { { **plain** *plain-text* | [ **cipher** ] *password-key* } *key-id* | [**keychain**](cmdqueryname=keychain) *keychain-name* } | **usual** { **plain** *plain-text* | [ **cipher** ] *password-key* } } command.
       
       In MD5 authentication mode, an MD5 password is used for packet encapsulation and decapsulation. MD5 authentication is more secure than simple authentication.
       
       **nonstandard** supports nonstandard authentication packets.
       
       **usual** supports Internet Engineering Task Force (IETF) standard authentication packets.
     + To configure Hash Message Authentication Code for Secure Hash Algorithm 256 (HMAC-SHA256) authentication, run the **rip authentication-mode** **hmac-sha256** { **plain** *plain-text* | [ **cipher** ] *password-key* } *key-id* command.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
       
       When configuring an authentication password, select the ciphertext mode because the password is saved in the configuration file as a plaintext if you select the plaintext mode, which has a high risk. To ensure device security, change the password periodically.
  4. Run **commit**
     
     The configuration is committed.

* Configure IPsec authentication for a RIPng process.
  1. Run **system-view**
     
     The system view is displayed.
  2. Run **ripng** [ *process-id* ]
     
     The RIPng view is displayed.
  3. Run **ipsec sa** *sa-name*
     
     IPsec authentication is enabled for RIPng, and the name of the SA is specified.
  4. Run **commit**
     
     The configuration is committed.
* Configure IPsec authentication on a RIPng interface.
  1. Run **system-view**
     
     The system view is displayed.
  2. Run **interface** *interface-type* *interface-number*
     
     The interface view is displayed.
  3. Run **ripng ipsec sa** *sa-name*IPsec authentication is enabled on the interface, and the name of an SA is specified.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**ripng ipsec sa**](cmdqueryname=ripng+ipsec+sa) command takes precedence over the [**ipsec sa**](cmdqueryname=ipsec+sa) command. If IPsec authentication is configured on both the interface and the process and different SA names are specified, only the configuration of the [**ripng ipsec sa**](cmdqueryname=ripng+ipsec+sa) command takes effect.
  4. Run **commit**
     
     The configuration is committed.

* Whitelist security policy:
  
  No special RIP/RIPng configuration is required.

#### Configuration Suggestions

* RIP authentication support:
  
  In MD5 authentication mode, which Huawei implements in compliance with relevant standards, RIP packets will take "checksum" in authentication instead of direct password keys. Nonstandard authentication is based on relevant standards and supports the same packet format described in relevant standards. (MD5 is supported only.)
  
  Configuring keychain authentication improves RIP connection security. Keychain must be configured on both links. Note: The encryption algorithms and passwords configured for keychain authentication must be the same on both peers. Otherwise, the RIP connection cannot be set up between the two ends and RIP packets cannot be transmitted. After keychain authentication is configured, the MD5 algorithm is used as the keychain authentication algorithm.
  
  To improve network security, HMAC-SHA256 authentication is recommended.
* RIPng authentication support using IPsec
  
  RIPng supports IPsec authentication. Before configuring IPsec authentication for RIPng, familiarize yourself with basic IPsec configurations.
* RIP/RIPng interface security:
  
  No special RIP/RIPng configuration is required.
* Whitelist security policy:
  
  RIP adds a neighboring interface to a whitelist when receiving the first response packet sent by the interface, without checking whether the interface is trusted. After authentication is configured on RIP-enabled interfaces, trusted neighboring interfaces are added to the whitelist.
* RIP/RIPng route limit:
  
  The maximum number of routes supported can be set based on device usage scope, memory, and supported CP-CAR values.

#### Verifying the Security Hardening Result

* Run the [**display rip**](cmdqueryname=display+rip) *process-id* **interface** [ *interface-type* *interface-number* ] [ **verbose** ] command to check information about RIP interfaces.
* Run the [**display rip**](cmdqueryname=display+rip) *process-id* command to check the operating status and configuration of a RIP process.
* Run the [**display ripng**](cmdqueryname=display+ripng) *process-id* **interface** [ *interface-type* *interface-number* ] [ **verbose** ] command to check the SA used for IPsec authentication.
* Run the [**display ripng**](cmdqueryname=display+ripng) *process-id* **statistics** **interface** { **all** | *interface-type interface-number* [ **verbose** | **neighbor** *neighbor-ipv6-address* ] } command to check the number of RIPng packets that fail to be authenticated.