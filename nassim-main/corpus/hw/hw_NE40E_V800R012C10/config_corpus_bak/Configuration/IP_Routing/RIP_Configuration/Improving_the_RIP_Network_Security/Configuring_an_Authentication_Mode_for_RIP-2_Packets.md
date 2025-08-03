Configuring an Authentication Mode for RIP-2 Packets
====================================================

RIP-2 supports authentication for protocol packets. You are advised to configure authentication to ensure system security.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Perform the following operations as required:
   
   
   * Run [**rip authentication-mode**](cmdqueryname=rip+authentication-mode) **simple** { **plain** *plain-text* | [ **cipher** ] *password-key* }
     
     Simple authentication is configured for RIP-2 packets.
     
     In simple authentication mode, the password in simple text mode is transmitted along with each authentication packet. Therefore, simple authentication is not recommended on networks requiring high security.
   * Run [**rip authentication-mode**](cmdqueryname=rip+authentication-mode) **md5** { **nonstandard** { { **plain** *plain-text* | [ **cipher** ] *password-key* } *key-id* | [**keychain**](cmdqueryname=keychain) *keychain-name* } | **usual** { **plain** *plain-text* | [ **cipher** ] *password-key* } }
     
     Message Digest 5 (MD5) authentication is configured for RIP-2 packets.
     
     In MD5 authentication mode, the MD5 password is used for packet encapsulation and decapsulation. MD5 authentication is more secure than simple authentication.
     
     **nonstandard** supports nonstandard authentication packets.
     
     **usual** supports Internet Engineering Task Force (IETF) standard authentication packets.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For the sake of security, using the HMAC-SHA256 algorithm rather than the MD5 algorithm is recommended.
   * Run [**rip authentication-mode**](cmdqueryname=rip+authentication-mode) **hmac-sha256** { **plain** *plain-text* | [ **cipher** ] *password-key* } *key-id*
     
     Hash Message Authentication Code for Secure Hash Algorithm 256 (HMAC-SHA256) authentication is configured.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   When configuring an authentication password, select the ciphertext mode because the password is saved in the configuration file as a plaintext if you select the plaintext mode, which has a high risk. To ensure device security, change the password periodically.
   
   It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.
   
   For security purposes, you are not advised to use the weak security algorithm in RIP. If you need to use the weak security algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Result

The following section describes the changes in the RIP neighbor relationship and data traffic during the upgrade from RIP-1 to RIP-2 with authentication.

**Scenario 1**: [Figure 1](#EN-US_TASK_0172365870__fig_dc_vrp_rip_cfg_004001) shows a P2P topology, and an upgrade is performed. DeviceA and DeviceB use the default configuration.**Figure 1** RIP neighbor relationship over a P2P link  
![](images/fig_dc_vrp_rip_cfg_004001.png)

With the default configuration, packet sending and receiving on one end of the P2P link are the same as those on the other end.
```
Interface 1 on DeviceA: (Default version or RIP-1-compatible version)
Send: RIP-1
Receive: RIP-1; RIP-2 in broadcast or multicast mode

Interface 2 on DeviceB: (Default version or RIP-1-compatible version)
Send: RIP-1
Receive: RIP-1; RIP-2 in broadcast or multicast mode
```

* Step 1: Configure authentication on interface 1 of DeviceA.
  
  ```
  Interface 1 on DeviceA: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in broadcast or multicast mode, with authentication information
  
  DeviceB: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in broadcast or multicast mode
  ```
  
  Authentication applies to RIP-2 packets, not to RIP-1 packets; however, the packets exchanged between DeviceA and DeviceB are RIP-1 packets. Therefore, the RIP neighbor relationship and data traffic remain unchanged after this step is performed.
* Step 2: Configure the same authentication mode on interface 2 of DeviceB.
  ```
  Interface 1 on DeviceA: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in broadcast or multicast mode, with authentication information
  
  Interface 2 on DeviceB: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in broadcast or multicast mode, with authentication information
  ```
  
  Authentication applies to RIP-2 packets, not to RIP-1 packets; however, the packets exchanged between DeviceA and DeviceB are RIP-1 packets. Therefore, the RIP neighbor relationship and data traffic remain unchanged after this step is performed.
* Step 3: Configure RIP-2 in broadcast mode on interface 1 of DeviceA.
  ```
  Interface 1 on DeviceA: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in broadcast or multicast mode, with authentication information
  
  Interface 2 on DeviceB: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in broadcast or multicast mode, with authentication information
  ```
  
  DeviceA broadcasts RIP-2 packets with authentication information to DeviceB. Because the same authentication mode is configured on DeviceB, DeviceB accepts these packets. DeviceB sends RIP-1 packets without authentication information to DeviceA, which accepts the RIP-1 packets although it runs RIP-2 (in broadcast mode with authentication information).
  
  In this case, the neighbor relationship and data traffic are not affected.
* Step 4: Configure RIP-2 in broadcast mode on interface 2 of DeviceB.
  ```
  Interface 1 on DeviceA: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in broadcast or multicast mode, with authentication information
  
  Interface 2 on DeviceB: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in broadcast or multicast mode, with authentication information
  ```
  
  DeviceA and DeviceB exchange RIP-2 packets carrying authentication information in broadcast mode. Because authentication is configured on both DeviceA and DeviceB, both DeviceA and DeviceB can accept broadcast RIP-2 packets. In this case, the neighbor relationship and data traffic are not affected.
* Step 5: Configure RIP-2 on interface 1 of DeviceA.
  ```
  Interface 1 on DeviceA: (RIP-2 in broadcast mode)
  Send: RIP-2 in multicast mode, with authentication information
  Receive: RIP-2 in broadcast and multicast mode, with authentication information
  
  Interface 2 on DeviceB:
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in broadcast or multicast mode, with authentication information
  ```
  
  DeviceA and DeviceB exchange RIP-2 packets carrying authentication information in multicast mode. Because authentication has been configured on DeviceB, Device B accepts the packets from DeviceA. DeviceB broadcasts RIP-2 packets with authentication information to DeviceA, which accepts the packets although it runs RIP-2. In this case, the neighbor relationship and data traffic are not affected.
* Step 6: Configure RIP-2 on interface 2 of DeviceB.
  ```
  Interface 1 on DeviceA: (RIP-2)
  Send: RIP-2 in multicast mode, with authentication information
  Receive: RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 2 on DeviceB: (RIP-2)
  Send: RIP-2 in multicast mode, with authentication information
  Receive: RIP-2 in multicast or broadcast mode, with authentication information
  ```
  
  DeviceA and DeviceB exchange RIP-2 packets carrying authentication information in multicast mode. Because authentication is configured on DeviceA and DeviceB, they can exchange the multicast RIP-2 packets. In this case, the neighbor relationship and data traffic are not affected.

**Scenario 2**: [Figure 2](#EN-US_TASK_0172365870__fig_dc_vrp_rip_cfg_004002) shows a broadcast topology, and an upgrade from RIP-1 (or RIP-1-compatible version) to RIP-2 is performed on devices.**Figure 2** RIP neighbor relationship over a broadcast link  
![](images/fig_dc_vrp_rip_cfg_004002.png)
```
Interface 2 on DeviceB: (Default version or RIP-1-compatible version)
Send: RIP-1
Receive: RIP-1; RIP-2 in multicast or broadcast mode

Interface 1 on DeviceA: (RIP-1)
Send: RIP-1
Receive: RIP-1

Interface 3 on DeviceC: (RIP-1)
Send: RIP-1
Receive: RIP-1
```
![](../../../../public_sys-resources/note_3.0-en-us.png) 

All devices in the networking use interface-level RIP configuration.


* Step 1: Configure authentication on DeviceA.
  
  ```
  Interface 2 on DeviceB: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in multicast or broadcast mode
  
  Interface 1 on DeviceA: (RIP-1)
  Send: RIP-1
  Receive: RIP-1
  
  Interface 3 on DeviceC: (RIP-1)
  Send: RIP-1
  Receive: RIP-1
  ```
  
  Authentication applies to RIP-2 packets, not to RIP-1 packets. Therefore, the authentication on a RIP-1 interface does not affect RIP-1 packets.
* Step 2: Configure authentication on DeviceC.
  ```
  Interface 2 on DeviceB: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in multicast or broadcast mode
  
  Interface 1 on DeviceA: (RIP-1)
  Send: RIP-1
  Receive: RIP-1
  
  Interface 3 on DeviceC: (RIP-1)
  Send: RIP-1
  Receive: RIP-1
  ```
  
  Authentication applies to RIP-2 packets, not to RIP-1 packets. Therefore, the authentication on a RIP-1 interface does not affect RIP-1 packets.
* Step 3: Configure authentication on DeviceB.
  ```
  Interface 2 on DeviceB: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 1 on DeviceA: (RIP-1)
  Send: RIP-1
  Receive: RIP-1
  
  Interface 3 on DeviceC: (RIP-1)
  Send: RIP-1
  Receive: RIP-1
  ```
  
  Authentication applies to RIP-2 packets, not to RIP-1 packets. Therefore, the authentication on an interface that runs RIP of the default version (RIP-1) does not affect RIP-1 packets. If RIP-2 packets are received, they are accepted only after they are authenticated. No RIP-2 packets are sent in this scenario. Therefore, the RIP neighbor relationships and data traffic remain unchanged after this step is performed.
* Step 4: Run the **undo version** command on DeviceA.
  ```
  Interface 2 on DeviceB: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 1 on DeviceA: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 3 on DeviceC: (RIP-1)
  Send: RIP-1
  Receive: RIP-1
  ```
  
  If the [**undo rip version 1**](cmdqueryname=undo+rip+version+1) command is run on the interface of DeviceB, the interface uses RIP of the default version (RIP-1) or RIP-1-compatible version. All the devices exchange RIP-1 packets in this scenario. Therefore, the RIP neighbor relationships and data traffic remain unchanged after this step is performed.
* Step 5: Run the **undo version** command on DeviceC.
  ```
  Interface 2 on DeviceB: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 1 on DeviceA: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 3 on DeviceC: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  ```
  
  If the [**undo rip version 1**](cmdqueryname=undo+rip+version+1) command is run on the interface of DeviceC, the interface uses RIP-1 (default version) or RIP-1-compatible version. All the devices exchange RIP-1 packets in this scenario. Therefore, the RIP neighbor relationships and data traffic remain unchanged after this step is performed.
* Step 6: Configure RIP-2 in broadcast mode on DeviceA.
  ```
  Interface 2 on DeviceB: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 1 on DeviceA: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 3 on DeviceC: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  ```
  
  If the [**rip version 2 broadcast**](cmdqueryname=rip+version+2+broadcast) command is run on the interface of DeviceA, the interface broadcasts RIP-2 packets with authentication information. Because authentication is configured on other devices, they accept the RIP-2 packets from DeviceA and respond with RIP-1 packets. DeviceA accepts these RIP-1 packets. Therefore, the RIP neighbor relationships and data traffic remain unchanged after this step is performed.
* Step 7: Configure RIP-2 in broadcast mode on DeviceC.
  ```
  Interface 2 on DeviceB: (Default version or RIP-1-compatible version)
  Send: RIP-1
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 1 on DeviceA: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 3 on DeviceC: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  ```
  
  If the [**rip version 2 broadcast**](cmdqueryname=rip+version+2+broadcast) command is run on the interface of DeviceC, the interface broadcasts RIP-2 packets with authentication information. Because authentication is configured on other devices, they accept the RIP-2 packets from DeviceC. Device B still broadcasts RIP-1 packets. Upon receipt of these packets, DeviceA and DeviceC accept them. Therefore, the RIP neighbor relationships and data traffic remain unchanged after this step is performed.
* Step 8: Configure RIP-2 in broadcast mode on DeviceB.
  ```
  Interface 2 on DeviceB: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 1 on DeviceA: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 3 on DeviceC: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  ```
  
  If the [**rip version 2 broadcast**](cmdqueryname=rip+version+2+broadcast) command is run on the interface of DeviceB, the interface broadcasts RIP-2 packets with authentication information. Because authentication is configured on other devices, they accept the RIP-2 packets from DeviceB and also broadcast RIP-2 packets with authentication information. All the devices accept packets from each other. Therefore, the RIP neighbor relationships and data traffic remain unchanged after this step is performed.
* Step 9: Configure RIP-2 on DeviceA.
  ```
  Interface 2 on DeviceB: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 1 on DeviceA: (RIP-2)
  Send: RIP-2 in multicast mode, with authentication information
  Receive: RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 3 on DeviceC: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  ```
  
  If the [**rip version 2**](cmdqueryname=rip+version+2) command is run on the interface of DeviceA, the interface multicasts RIP-2 packets with authentication information. Because authentication is configured on other devices, they accept the RIP-2 packets from DeviceA and broadcast RIP-2 packets with authentication information. All the interfaces accept packets from each other. Therefore, the RIP neighbor relationships and data traffic remain unchanged after this step is performed.
* Step 10: Configure RIP-2 on DeviceC.
  ```
  Interface 2 on DeviceB: (RIP-2 in broadcast mode)
  Send: RIP-2 in broadcast mode, with authentication information
  Receive: RIP-1; RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 1 on DeviceA: (RIP-2)
  Send: RIP-2 in multicast mode, with authentication information
  Receive: RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 3 on DeviceC: (RIP-2)
  Send: RIP-2 in multicast mode, with authentication information
  Receive: RIP-2 in multicast or broadcast mode, with authentication information
  ```
  
  If the [**rip version 2**](cmdqueryname=rip+version+2) command is run on the interface of DeviceC, the interface multicasts RIP-2 packets with authentication information. Because authentication is configured on other devices, they accept the RIP-2 packets from DeviceC. DeviceB broadcasts RIP-2 packets with authentication information, and DeviceA multicasts RIP-2 packets with authentication information. All the devices accept packets from each other. Therefore, the RIP neighbor relationships and data traffic remain unchanged after this step is performed.
* Step 11: Configure RIP-2 on DeviceB.
  ```
  Interface 2 on DeviceB: (RIP-2)
  Send: RIP-2 in multicast mode, with authentication information
  Receive: RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 1 on DeviceA: (RIP-2)
  Send: RIP-2 in multicast mode, with authentication information
  Receive: RIP-2 in multicast or broadcast mode, with authentication information
  
  Interface 3 on DeviceC: (RIP-2)
  Send: RIP-2 in multicast mode, with authentication information
  Receive: RIP-2 in multicast or broadcast mode, with authentication information
  ```
  
  If the [**rip version 2**](cmdqueryname=rip+version+2) command is run on the interface of DeviceB, the interface multicasts RIP-2 packets with authentication information. Because authentication is configured on other devices, they accept the RIP-2 packets from DeviceB and multicast RIP-2 packets with authentication information. All the devices accept packets from each other. Therefore, the RIP neighbor relationships and data traffic remain unchanged after this step is performed.

**Scenario 3**: RIP-2 or RIP-2 in broadcast mode is enabled on all devices.

In this scenario, if RIP authentication is configured on all devices, packets may be discarded in the following cases because authentication configuration synchronization cannot be ensured during authentication:

1. RIP packets with authentication information are received by interfaces without authentication configuration.
2. RIP packets without authentication information are received by interfaces with authentication configuration.

After all the configurations are performed, RIP packets are authenticated and accepted by all interfaces with authentication configuration. When the default timer is used, RIP considers a route invalid only if it does not receive any Update packet within six update intervals. Therefore, if all the configurations are completed within the six update intervals, no traffic is interrupted.