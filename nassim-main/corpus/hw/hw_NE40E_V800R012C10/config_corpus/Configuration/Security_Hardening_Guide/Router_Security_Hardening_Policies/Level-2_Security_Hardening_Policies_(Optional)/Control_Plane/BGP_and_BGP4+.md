BGP/BGP4+
=========

BGP/BGP4+

#### Security Policy Overview

* BGP MD5 authentication
  
  BGP uses TCP as its transport layer protocol and considers a TCP packet valid if the source IP address, destination IP address, source port number, destination port number, and TCP sequence number in the packet are correct. Most of the preceding parameters in a TCP packet can be obtained by attackers without much difficulty. To protect BGP from attacks, you can configure MD5 authentication over TCP between BGP peers.
  
  The cleartext passwords configured on both ends must be the same. If the interval between the configuration completions of the two devices is greater than **hold-time**, the peer relationship is interrupted. Otherwise, the peer relationship is not interrupted.
  
  To prevent an MD5 password configured for a BGP peer from being cracked, change the password periodically.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The MD5 algorithm is not recommended if high security is required.
* Keychain authentication
  
  A keychain consists of multiple authentication keys, each of which contains an ID and a password. Each key in a keychain has a lifecycle, and keys are dynamically selected based on the lifecycle of each key. After a keychain with the same rules is configured on the two ends of a BGP session, authentication keys are dynamically selected to enhance BGP attack defense.
* TCP-AO authentication
  
  The TCP authentication option (TCP-AO) is used to authenticate received and to-be sent packets during TCP session establishment and data exchange. It supports packet integrity check to prevent TCP replay attacks. TCP-AO authentication improves the security of the TCP connection between BGP peers and is applicable to the network that requires high security.
* BGP GTSM
  
  GTSM checks TTL values to defend against attacks. Attackers may simulate BGP messages and continuously send them to the Router. After receiving these packets, the interface board on the Router sends these messages directly to the control plane for BGP processing, without validating them, if they are destined for the device. The Router becomes extremely busy, and CPU usage is high because the control plane of the Router needs to process these unchecked messages.
  
  GTSM protects the Router by checking whether the TTL value in the IP packet header is within a pre-defined range to improve system security.
* BGP whitelist
  
  The application layer association module checks protocol packets sent to the CPU and sends protocol packets that match the whitelist at a high rate.
* CP-CAR
  
  For enabled services or protocols, a device can limit the rate at which packets are sent to the CPU, protecting the CPU from attacks and ensuring proper network operating.
* Session-CAR
  
  The function of whitelist session-CAR for BGP sets an independent CAR channel for each BGP session to ensure that the bandwidth of each BGP session is not preempted by other traffic (including traffic from other sessions of the same protocol and traffic from other protocols). When BGP messages suffer a traffic burst, you can adjust the default parameters of whitelist session-CAR for BGP if they do not meet service requirements. This ensures that BGP messages can be sent properly.
* Route over-threshold control
  
  In most cases, a BGP routing table contains a large number of routes. If a lot of routes are received from a peer, excessive system resources may be consumed. To prevent this issue, you can set the maximum number of routes that the local BGP device can accept from the peer.
* Limit on the quantity of AS numbers in the AS\_Path attribute
  
  When a BGP device receives a route, it checks whether the quantity of AS numbers in the AS\_Path attribute exceeds a specified threshold. If the quantity exceeds the threshold, the device discards the route. During route advertisement, the device also checks whether the quantity of AS numbers in the AS\_Path attribute exceeds the threshold. If the quantity exceeds the threshold, the device does not advertise the route, which prevents maliciously constructed error messages with an extra-long AS\_Path from attacking the Router.
* RPKI
  
  Resource Public Key Infrastructure (RPKI) ensures BGP security by verifying the validity of the BGP route source AS, AS\_Path, or route advertiser.
  
  Attackers can steal user data by advertising routes that are more specific than those advertised by carriers. RPKI can resolve this problem. For example, if a carrier advertises a valid route with the destination address of 10.10.0.0/16 to a user and an attacker advertises a route with the destination address of 10.10.153.0/24, the traffic from the user to 10.10.153.0/24 will be stolen by the attacker because the route advertised by the attacker is more specific.
  
  To solve the preceding problem, you can configure Route Origin Authorization (ROA), Autonomous System Provider Authorization (ASPA), or regional validation. This helps ensure BGP security.
* BMP
  
  The BGP Monitoring Protocol (BMP) monitors devices' BGP/BGP4+ running status in real time, such as the establishment and termination status of BGP/BGP4+ peer relationships and route update status.
  
  BMP is mainly applied to the networking where a monitoring server exists and the BGP/BGP4+ running status of devices on the network needs to be monitored. BMP changes the traditional method of obtaining the BGP/BGP4+ running status of devices through manual query and greatly improves the efficiency of network monitoring.
* BGP TLS authentication
  
  The Transport Layer Security (TLS) protocol, as the SSL successor, ensures data integrity and privacy. SSL/TLS authentication can be configured on an SSL server so that BGP messages are encrypted to ensure data transmission security on the network.

#### Attack Methods

* DoS attacks
  
  Attackers can send various types of packets to attack devices. If the packets are multicast protocol packets or the destination IP address is the IP address of an interface (including the loopback interface) on the device, the device sends these packets to the CPU. These packets consume the CPU and system resources, causing DoS attacks. After a BGP session is created, the system sends a whitelist. The application layer association module checks the received protocol packets and sends protocol packets that match the whitelist at a high rate. The module sends protocol packets that do not match the whitelist at the default bandwidth and rate to prevent DoS attacks. In addition, CP-CAR applies to interfaces to limit the transmission rate of BGP packets, to protect the CPU from attacks, and to ensure proper network operations.
* Injection of a large number of BGP routes
  
  BGP runs on various models of devices, such as the IASs on an access network and NE40Es. The number of BGP routes is determined by the CPU and memory of a device. If the number of BGP routes received by a device exceeds the capacity of the device, memory resources of the device will be exhausted, causing the device and services on it to fail to run properly. The maximum number of routes for a single peer can be set. If attackers inject a large number of routes and the quantity exceeds the maximum number of routes for a single peer, the excess routes are discarded to prevent exhaustion of system resources.
* Construction of error BGP messages
  
  Attackers may construct various types of error packets, such as packets with extra-long AS\_Paths, packets with incorrect packet headers, packets with incorrect lengths, and packets with invalid next hops. The attackers use these error packets to attack devices. BGP implements a policy "tolerant on input and strict on output". The device discards error packets without interrupting connections to peers to ensure uninterrupted services. For packets with extra-long AS\_Paths, an AS\_Path limit is set. During route reception or advertisement, if the device finds that the AS\_Path exceeds the limit, it refuses to accept or advertise routes.
  
  A BGP Update message contains various path attributes. If a local device receives Update messages containing malformed path attributes, the involved BGP sessions may flap. To resolve this issue and enhance reliability, run the **peer path-attribute-treat** command to configure a special mode in which the device processes specified path attributes in received BGP Update messages. Special modes indicate those that are not defined in a standard protocol.
* Network packet attacks
  
  It is easy for attackers to obtain the majority of parameters in the 5-tuple of a packet. To protect BGP from attacks, take the following measures:
  
  + Use TCP MD5 authentication between BGP peers to reduce the possibility of being attacked.
  + Configure keychain authentication for BGP sessions to enhance BGP anti-attack performance.
  + Configure the GTSM function to check TTLs in messages to prevent attacks.


#### Procedure

* Configure MD5 authentication.
  
  
  
  An MD5 authentication password is configured for TCP connections, and TCP implements MD5 authentication of BGP. If authentication fails, no TCP connections can be established.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**password**](cmdqueryname=password) { **cipher** *cipher-password* | **simple** *simple-password* }
     
     
     
     An MD5 authentication password is configured.
     
     
     
     The password can be set in either of the following modes:
     
     + **cipher** *cipher-password*: indicates that a password is set using a ciphertext string.
     + **simple** *simple-password*: indicates that a password is set using a cleartext string.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If MD5 authentication is configured in the BGP view, the configuration also takes effect in extended BGP address family views because they use the same TCP connection. BGP MD5 authentication and BGP keychain authentication are mutually exclusive.
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The new password is at least eight characters long and contains at least two of the following types: upper-case letters, lower-case letters, digits, and special characters, except the question mark (?) and space.
     + For security purposes, you are advised to configure a password in ciphertext mode. To further improve device security, periodically change the password.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure keychain authentication.
  
  
  
  Configure keychain authentication on both ends of a BGP peer relationship. In addition, the configured keychains must use the same encryption algorithm and password so that TCP connections can be set up, and BGP messages can be exchanged properly.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } [**keychain**](cmdqueryname=keychain) *keychain-name*
     
     
     
     Keychain authentication is configured.
     
     To ensure the setup of a TCP connection and BGP exchange between on both ends of a BGP connection, configure keychain authentication specified for TCP-based applications and the same password and encryption algorithms on both ends.
     
     *keychain-name* specified in this command must exist; otherwise, the TCP connection cannot be established. For keychain configuration details, see the "Keychain Configuration" chapter in *HUAWEI NE40E-M2 series Configuration Guide - Security*.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + When this command is used in the BGP view, it is also applicable to the extended address family view because they use the same TCP connection.
     + BGP MD5 authentication and BGP keychain authentication are mutually exclusive.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure TCP-AO authentication.
  
  
  
  TCP-AO authentication must be configured on both BGP peers. A TCP-AO authentication password needs to be set for a TCP connection, and the authentication is performed by TCP. If authentication fails, no TCP connections can be established.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**tcp ao**](cmdqueryname=tcp+ao)*tcpaoname*
     
     
     
     A TCP-AO is created, and the TCP-AO policy view is displayed.
  3. Run [**binding keychain**](cmdqueryname=binding+keychain)*kcName*
     
     
     
     The TCP-AO is bound to a keychain.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A keychain must have been created using the **keychain** command before you perform this step.
  4. Run [**key-id**](cmdqueryname=key-id) *keyId*
     
     
     
     A key ID is created for the TCP-AO, and the TCP-AO key ID view is displayed.
  5. Run [**send-id**](cmdqueryname=send-id) *sndId* **receive-id***rcvId*
     
     
     
     The send-id and receive-id are configured for the Key ID.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     The TCP-AO policy view is displayed.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  8. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  9. Run [**peer**](cmdqueryname=peer) *ipv4-address* [**as-number**](cmdqueryname=as-number) *as-number*
     
     
     
     The IP address of a peer and the number of the AS where the peer resides are specified.
  10. Run [**peer**](cmdqueryname=peer) *ipv4-address* **tcp-ao policy** *tcp-ao-name*
      
      
      
      TCP-AO authentication is configured for the TCP connection to be set up between BGP peers.
      
      
      
      The value of the *tcp-ao-name* parameter must be set to the TCP-AO created in step 2.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      For the same peer, the authentication modes TCP-AO, MD5, and keychain are mutually exclusive.
  11. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure the BGP GTSM function.
  
  
  
  GTSM protects Routers from attacks by checking whether the TTL in the header of an IP packet is within the pre-defined range.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **valid-ttl-hops** [ *hops* ]
     
     
     
     The BGP GTSM is configured.
     
     
     
     The valid TTL range of detected packets is [255 â *hops* + 1, 255]. For example, for an EBGP direct route, the value of *hops* is 1. That is, the valid TTL value is 255.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + After GTSM is configured in the BGP view, the configuration also takes effect in the MP-BGP VPNv4 address family view because BGP and MP-BGP VPNv4 share a TCP connection.
     + GTSM and EBGP-max-hop are mutually exclusive because they both affect the TTL values in sent BGP messages. Therefore, only one of them can be used for a peer or peer group.
     
     A BGP device that is enabled with GTSM checks the TTL values in all BGP packets on interface boards. As required by the actual networking, packets whose TTL values are not within the specified range are discarded. In scenarios where GTSM is not configured on a BGP device, the received BGP messages are forwarded if the BGP peer configuration exists. Otherwise, the received BGP messages are discarded. This prevents bogus BGP messages from consuming CPU resources.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the default GTSM action.
  
  
  
  Perform the following steps on a GTSM-enabled Router:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**gtsm default-action**](cmdqueryname=gtsm+default-action) { **drop** | **pass** }
     
     
     
     The default action to be taken for packets that do not match the GTSM policy is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the default action is configured but no GTSM policy is configured, GTSM does not take effect.
     
     This command is supported only on the Admin-VS and cannot be configured in other VSs. This command takes effect on all VSs.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure ROA.
  1. Select one of the following configurations based on the usage scenario:
     
     
     + If the local device needs to obtain data from the ROA database through a connection to be established with an RPKI server, perform the following operations:
       1. Run [**system-view**](cmdqueryname=system-view)
          
          The system view is displayed.
       2. Run [**rpki**](cmdqueryname=rpki)
          
          RPKI is started, and the RPKI view is displayed.
       3. Run [**session**](cmdqueryname=session) *ipv4-address*
          
          An address of the RPKI server is specified for a TCP connection to be set up between the client and RPKI server.
       4. Run [**tcp**](cmdqueryname=tcp) **port** *port-number* [ **password md5** *cipher-password* | **keychain***keychain-name* ] Parameters are configured for the TCP connection between the local device and the RPKI server.
          
          ![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          The MD5 algorithm is not recommended if high security is required.
          
          For security purposes, you are advised to configure a ciphertext password, and change it periodically.
       5. (Optional) Run [**timer**](cmdqueryname=timer) { **aging** *aging-time* | **refresh** *refresh-time* }
          
          Timers are configured for the RPKI session between the client and the RPKI server.
          
          The *aging-time* parameter specifies a value of the validation data age timer, and the *refresh-time* parameter specifies a value of the session update timer. You can configure the timers based on actual requirements on BGP security. Small values are recommended if high BGP security is required. However, frequent data updates consume much network bandwidth.
       6. (Optional) Run [**rpki-limit**](cmdqueryname=rpki-limit) *limit* [ **alert-only** | **idle-forever** | **idle-timeout** *times* ]
          
          The maximum number of Route Origin Authorization (ROA) entries that the device is allowed to accept in a session is configured.
          
          In most cases, a large number of ROA entries exist on an RPKI server. If the device receives a large number of ROA entries from the RPKI server, excessive system resources will be consumed. To prevent this problem, run the [**rpki-limit**](cmdqueryname=rpki-limit) command to configure the maximum number of ROA entries that the BGP device is allowed to accept in a session.
       7. (Optional) Run [**connect-interface**](cmdqueryname=connect-interface) { *interface-name* | *ipv4-source-address* | *interface-type* *interface-number* | *interface-type* *ipv4-source-address* | *interface-type* *interface-number* *ipv4-source-address* }
          
          The source interface for sending RPKI packets is specified.
       8. (Optional) Run [**ssl-policy**](cmdqueryname=ssl-policy) *policy-name*
          
          An SSL policy to be bound to the TCP connection between the device and RPKI server is configured.
       9. Run [**quit**](cmdqueryname=quit)
          
          The RPKI view is displayed.
       10. Run [**quit**](cmdqueryname=quit)
           
           The system view is displayed.
       11. Run [**commit**](cmdqueryname=commit)
           
           The configuration is committed.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If configurations of an RPKI session are changed and you want its new configurations to take effect immediately, run the [**reset rpki session**](cmdqueryname=reset+rpki+session) command to reset the RPKI session.
     + If a static ROA database needs to be configured on the local device, perform the following operations:
       1. Run [**system-view**](cmdqueryname=system-view)
          
          The system view is displayed.
       2. Run [**rpki**](cmdqueryname=rpki)
          
          RPKI is started, and the RPKI view is displayed.
       3. Run [**origin-validation**](cmdqueryname=origin-validation)
          
          A static ROA database is created, and the RPKI origin-validation view is displayed.
       4. Run [**static record**](cmdqueryname=static+record) *ipv4-address* *mask-length* **max-length** *max-mask-length* **origin-as** *as-number*
          
          A record is configured for the static ROA database.
       5. Run [**quit**](cmdqueryname=quit)
          
          The RPKI view is displayed.
       6. Run [**quit**](cmdqueryname=quit)
          
          The system view is displayed.
       7. Run [**commit**](cmdqueryname=commit)
          
          The configuration is committed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Configure inbound or outbound ROA validation as required.
     
     
     + To configure inbound ROA validation (validation results not affecting route acceptance) for the routes received from an EBGP peer, perform the following operations:
       1. Run [**prefix origin-validation enable**](cmdqueryname=prefix+origin-validation+enable)
          
          Origin AS validation of RPKI is enabled.
          
          This function applies only to the routes received from EBGP peers, not to those received from IBGP peers. After origin AS validation is enabled, the device matches the origin AS of each route received from an EBGP peer against that of the matched route in the database and outputs the validation result, which can be Valid, Not Found, or Invalid.
       2. (Optional) Run [**bestroute origin-as-validation**](cmdqueryname=bestroute+origin-as-validation) [ **allow-invalid** ]
          
          The device is configured to apply origin AS validation results of RPKI to BGP route selection.
          
          BGP selects routes in descending order of Valid, Not Found, and Invalid after origin AS validation results are applied to route selection. If **allow-invalid** is not specified in the command, the BGP routes with the validation result being Invalid do not participate in route selection.
       3. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **advertise-ext-community**
          
          The device is configured to advertise extended community attributes to the specified peer.
       4. (Optional) Run [**peer**](cmdqueryname=peer) { *ipv4-address* | *group-name* } **advertise origin-as-validation**
          
          The device is enabled to advertise origin AS validation results of RPKI to the specified BGP peer or peer group.
          
          ![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          Origin AS validation results of RPKI can be advertised only to IBGP peers.
     + To configure outbound ROA validation for the routes to be advertised to an EBGP peer to control route advertisement, perform the following operations:
       
       Run [**peer**](cmdqueryname=peer) { *peerIpv4Addr* | *peerGroupName* } **origin-validation export** [ **include-not-found** [ **external** ] ]
       
       The local device is configured to perform outbound ROA validation on the routes to be advertised to the specified EBGP peer.
       
       After the local device is configured to perform outbound ROA validation on the routes to be advertised to a specified EBGP peer, the device matches the origin ASs of the routes against those of the matched routes recorded in the database. The validation result can be Valid, Not Found, or Invalid. By default, only the routes whose validation result is Valid are advertised. To configure the device to advertise the routes with the validation result being Valid or Not Found, specify the **include-not-found** keyword in the preceding command. To configure the device to advertise the routes with the validation result being Valid or Not Found (if the routes with the result being Not Found were received from another AS), specify the **include-not-found external** keyword in the preceding command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure ASPA.
  1. Select one of the following configurations based on the usage scenario:
     
     
     + If the local device needs to obtain data from the ASPA database through a connection to be established with an RPKI server, perform the following operations:
       1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
       2. Run the [**rpki**](cmdqueryname=rpki) command to start RPKI and enter the RPKI view.
       3. Run the [**session**](cmdqueryname=session) *ipv4-address* command to configure session information for the TCP connection between the local device and the RPKI server.
       4. Run the [**tcp**](cmdqueryname=tcp) **port** *port-number* [ **password md5** *cipher-password* | | **keychain***keychain-name* ] command to configure parameters for the TCP connection between the local device and the RPKI server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
          
          The MD5 algorithm is not recommended if high security is required.
          
          For security purposes, you are advised to configure a ciphertext password, and change it periodically.
       5. Run the **[**version**](cmdqueryname=version)** *version-num* command to configure an RPKI version. RPKIv2 allows a device to receive ASPA data on the condition that both the device and the RPKI server support RPKIv2.
       6. (Optional) Run the [**timer**](cmdqueryname=timer) { **aging** *aging-time* | **refresh** *refresh-time* } command to configure timers for the RPKI session.
          
          The *aging-time* parameter specifies a value of the validation data aging timer, and the *refresh-time* parameter specifies a value of the session update timer. You can configure the timers based on actual requirements on BGP security. Small values are recommended if high BGP security is required. However, frequent data updates consume much network bandwidth.
       7. (Optional) Run the **[**aspa-limit**](cmdqueryname=aspa-limit)** *limit* [ *percentage* ] [ **alert-only** | **idle-forever** | **idle-timeout** **times** ] command to configure the maximum number of ASPA records that the device is allowed to accept in the session.
          
          In most cases, a large number of ASPA records exist on a server. If a BGP device receives a large number of ASPA records from the server, excessive system resources will be consumed. To prevent this problem, run the **aspa-limit** command to configure the maximum number of ASPA records that the device is allowed to accept in the session.
       8. (Optional) Run the [**connect-interface**](cmdqueryname=connect-interface) { *interface-name* | *ipv4-source-address* | *interface-type* *interface-number* | *interface-type* *ipv4-source-address* | *interface-type* *interface-number* *ipv4-source-address* } command to specify the source interface for sending RPKI messages.
       9. (Optional) Run the [**ssl-policy**](cmdqueryname=ssl-policy) *policy-name* command to configure an SSL policy to be bound to the TCP connection between the device and the RPKI server.
       10. Run the [**quit**](cmdqueryname=quit) command to enter the RPKI view.
       11. Run the [**quit**](cmdqueryname=quit) command to enter the system view.
       12. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If configurations of an RPKI session are changed and you want its new configurations to take effect immediately, run the [**reset rpki session**](cmdqueryname=reset+rpki+session) command to reset the RPKI session.
     + If a static ASPA database needs to be configured on the local device, perform the following operations:
       1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
       2. Run the [**rpki**](cmdqueryname=rpki) command to start RPKI and enter the RPKI view.
       3. Run the [**aspa-validation**](cmdqueryname=aspa-validation) command to create a static ASPA database and enter the RPKI ASPA-validation view.
       4. Run the **[**static record**](cmdqueryname=static+record)** **customer-as** **provider** **as-number**{ **ipv4** | **ipv6** } command to configure the static ASPA database.
       5. Run the [**quit**](cmdqueryname=quit) command to enter the RPKI view.
       6. Run the [**quit**](cmdqueryname=quit) command to enter the system view.
       7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
  2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
  3. Configure inbound ASPA validation as required. To configure inbound ASPA validation (validation results not affecting route acceptance) for the routes received from an EBGP peer, perform the following operations:
     
     
     1. Run the **[**peer**](cmdqueryname=peer+role)** { *peerIpv4Addr* | *peerIpv6Addr* } **role** { **provider** | **rs** | **rs-client** | **customer** | **lateral-peer** | **sibling** } command to configure a role for a BGP peer.
     2. Run the **aspa-validation enable** command to enable RPKI-based ASPA validation. After ASPA validation is enabled, the device compares the AS\_Path of a route with the matching ASPA pair recorded in the database and provides the validation results: Valid, NotFound, or Invalid.
     3. (Optional) Run the [**bestroute aspa-validation**](cmdqueryname=bestroute+aspa-validation) [ **allow-invalid** ] command to configure the device to apply ASPA validation results of RPKI to BGP route selection. BGP selects routes in descending order of Valid, Not Found, and Invalid after ASPA validation results are applied to route selection. If **allow-invalid** is not specified in the command, the BGP routes with the validation result being Invalid do not participate in route selection.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure regional validation.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**rpki**](cmdqueryname=rpki)
     
     
     
     RPKI is started, and the RPKI view is displayed.
  3. Run [**region-validation**](cmdqueryname=region-validation)
     
     
     
     Regional validation is enabled, and the region-validation view is displayed.
  4. You can configure regions or regional confederation as required.
     
     
     + Create a region.
       1. Run [**region**](cmdqueryname=region) *region-id*
          
          A region is created.
       2. Run [**description**](cmdqueryname=description) *description-text*
          
          A description is configured for the region.
       3. Run [**as-number**](cmdqueryname=as-number) { *asn* } &<1-100>
          
          An AS number list is configured so that the AS numbers in it can be added to the region.
       4. Run [**quit**](cmdqueryname=quit)
          
          The regional validation view is displayed.
       5. Run [**quit**](cmdqueryname=quit)
          
          The RPKI view is displayed.
       6. Run [**quit**](cmdqueryname=quit)
          
          The system view is displayed.
     + Create a regional confederation.
       1. Run [**region**](cmdqueryname=region) *region-id*
          
          A region is created.
       2. Run [**quit**](cmdqueryname=quit)
          
          The regional validation view is displayed.
       3. Run [**region-confederation**](cmdqueryname=region-confederation) *region-confederation-id*
          
          A regional confederation is created.
       4. Run [**description**](cmdqueryname=description) *description-text*
          
          A description is configured for the regional confederation.
       5. Run [**region**](cmdqueryname=region) { *region-id* } &<1-100>
          
          A region ID list is configured in the regional confederation so that regions in the list are added to the regional confederation.
       6. Run [**quit**](cmdqueryname=quit)
          
          Exit the RPKI regional confederation validation view and enter the regional validation view.
       7. Run [**quit**](cmdqueryname=quit)
          
          The RPKI view is displayed.
       8. Run [**quit**](cmdqueryname=quit)
          
          The system view is displayed.
  5. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  6. Enable the region or regional confederation function as required.
     
     
     + Run [**region-validation**](cmdqueryname=region-validation)
       
       BGP regional validation is enabled.
     + Run [**region-validation confed-check strict**](cmdqueryname=region-validation+confed-check+strict)
       
       Strict BGP regional validation is enabled.
  7. Run [**bestroute region-validation**](cmdqueryname=bestroute+region-validation) [ **allow-invalid** ]
     
     
     
     The device is configured to apply the BGP regional validation results of RPKI to BGP route selection.
     
     
     
     If regional validation succeeds, the route is valid and can participate in route selection. If regional validation fails, the route is invalid and cannot participate in route selection. To allow the routes that fail regional validation to be valid and participate in route selection, configure the **allow-invalid** parameter in the command. The priority of such routes is reduced during route selection.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BMP.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bmp**](cmdqueryname=bmp)
     
     
     
     BMP is enabled, and the BMP view is displayed.
  3. (Optional) Run [**statistics-timer**](cmdqueryname=statistics-timer) *time*
     
     
     
     An interval at which the BMP device sends BGP/BGP4+ running statistics to a monitoring server is set.
     
     
     
     You can set the interval based on the actual requirements on BGP/BGP4+ stability. Usually, a shorter interval is set for a network with higher stability, but this consumes more bandwidth resources because the device sends BGP/BGP4+ running statistics more frequently.
  4. Run [**bmp-session**](cmdqueryname=bmp-session) [ **vpn-instance** *vrf-name* ] { *ipv4-address* | *ipv6-address* } [ **alias** *alias-name* ]
     
     
     
     An IPv4 or IPv6 session address is configured for the TCP connection between the BMP device and the monitoring server.
     
     
     
     **alias** *alias-name* specifies an alias for a BMP session. If the device needs to establish TCP connections with monitoring servers that have the same destination IP address but different destination port numbers, specify different values for the **alias** *alias-name* parameter to differentiate the connections.
  5. Configure the BMP device to send statistics about routes of specific types to the monitoring server.
     
     
     + Configure the BMP device to send the monitoring server the statistics about RIB-in routes (all received routes or only accepted routes) from BGP/BGP4+ peers in a specified address family.
       1. Run one of the following commands to enter the BMP-Monitor view:
          - [**monitor public**](cmdqueryname=monitor+public): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of all BGP/BGP4+ peers in the public network address family to be monitored.
          - [**monitor all-vpn-instance**](cmdqueryname=monitor+all-vpn-instance): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of BGP/BGP4+ peers in all VPN instance address families to be monitored.
          - [**monitor peer**](cmdqueryname=monitor+peer): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of a specified BGP/BGP4+ peer in the public address family to be monitored.
          - [**monitor vpn-instance**](cmdqueryname=monitor+vpn-instance): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of all BGP/BGP4+ peers in a specified VPN instance to be monitored.
          - [**monitor vpn-instance peer**](cmdqueryname=monitor+vpn-instance+peer): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of a specified BGP/BGP4+ peer in a specified VPN instance to be monitored.
       2. Run [**route-mode**](cmdqueryname=route-mode) { **ipv4-family** **unicast** | **ipv4-family** **labeled-unicast** | **ipv4-family** **vpnv4** | **ipv6-family** **unicast** | **ipv6-family** **vpnv6** } **adj-rib-in** { **pre-policy** | **post-policy** }
          
          The BMP device is configured to send statistics about RIB-in routes of BGP/BGP4+ peers in a specified address family to the monitoring server.
          
          To configure the device to send statistics about all received routes to the monitoring server, specify **pre-policy** in the command. To configure the device to send statistics about only the routes that match the import policy (those delivered to the routing table) to the monitoring server, specify **post-policy** in the command.
          
          ![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          If the **pre-policy** parameter is specified in the command, run the [**keep-all-routes**](cmdqueryname=keep-all-routes) command in the BGP view to save information about routes carried in BGP/BGP4+ Update messages that are received from all BGP/BGP4+ peers or peer groups after BGP/BGP4+ connections are established. Alternatively, run the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command to save information about routes carried in the BGP/BGP4+ Update messages that are received from a specified BGP/BGP4+ peer or peer group after the BGP/BGP4+ connection is established.
     + Configure the BMP device to send statistics about RIB-out routes advertised to BGP/BGP4+ peers in a specified address family.Run one of the following commands to enter the BMP-Monitor view:
       - [**monitor public**](cmdqueryname=monitor+public): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of all BGP/BGP4+ peers in the public network address family to be monitored.
       - [**monitor all-vpn-instance**](cmdqueryname=monitor+all-vpn-instance): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of BGP/BGP4+ peers in all VPN instance address families to be monitored.
       - [**monitor peer**](cmdqueryname=monitor+peer): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of a specified BGP/BGP4+ peer in the public address family to be monitored.
       - [**monitor vpn-instance**](cmdqueryname=monitor+vpn-instance): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of all BGP/BGP4+ peers in a specified VPN instance to be monitored.
       - [**monitor vpn-instance peer**](cmdqueryname=monitor+vpn-instance+peer): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of a specified BGP/BGP4+ peer in a specified VPN instance to be monitored.
       
       Run [**route-mode**](cmdqueryname=route-mode) { **ipv4-family** **unicast** | **ipv4-family** **labeled-unicast** | **ipv4-family** **vpnv4** | **ipv6-family** **unicast** | **ipv6-family** **vpnv6** } **adj-rib-out** { **pre-policy** | **post-policy** }
       
       The BMP device is configured to send statistics about RIB-out routes of BGP/BGP4+ peers in a specified address family to the monitoring server.
       
       To configure the device to send statistics about all routes, specify the **pre-policy** parameter in the command. To configure the device to send statistics about only the routes that match the export policy, specify the **post-policy** parameter in the command.
     + Configure the BMP device to send statistics about Local-RIB routes of BGP/BGP4+ peers in a specified address family.
       1. Run one of the following commands to enter the BMP-Monitor view:
          - [**monitor public**](cmdqueryname=monitor+public): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of all BGP/BGP4+ peers in the public network address family to be monitored.
          - [**monitor vpn-instance**](cmdqueryname=monitor+vpn-instance): displays the BMP-Monitor view and allows the BGP/BGP4+ running status of all BGP/BGP4+ peers in a specified VPN instance to be monitored.
       2. Perform the following operations as required:
          - To configure the BMP device to send the monitoring server the statistics about Local-RIB routes of BGP/BGP4+ peers in a specified address family, run the [**route-mode**](cmdqueryname=route-mode) { **ipv4-family** **unicast** | **ipv4-family** **labeled-unicast** | **ipv4-family** **vpnv4** | **ipv6-family** **unicast** | **ipv6-family** **vpnv6** } **local-rib** [ **add-path** | **all** ] [ **path-marking** ] command.
          - To configure the BMP device to send statistics about Local-RIB routes of BGP/BGP4+ peers in the BGP-Flow address family to the monitoring server, run the [**route-mode**](cmdqueryname=route-mode) { **ipv4-family** | **ipv6-family** } **flow** **local-rib** [ **report route-identifier** ] command.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the BMP session view.
  7. Run [**tcp**](cmdqueryname=tcp) **connect** **port** *port-number* [ **password md5** *cipher-password* | **keychain** *keychain-name* ]
     
     
     
     Parameters for the TCP connection to be established between the device and the monitoring server are configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Configuring MD5 is not recommended when high security is required.
  8. (Optional) Run [**ssl-policy name**](cmdqueryname=ssl-policy+name) *policy-name*
     
     
     
     An SSL policy is configured for BMP.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Ensure that the specified SSL policy has been created using the [**ssl policy**](cmdqueryname=ssl+policy) *policy-name* command in the system view.
  9. (Optional) Run [**connect-interface**](cmdqueryname=connect-interface) { *interface-type* *interface-number* | *ip-source-address* | *interface-type* *interface-number* *ip-source-address* }
     
     
     
     The source interface for sending BMP messages is specified.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      After configuring BMP session parameters, run the [**reset bmp session**](cmdqueryname=reset+bmp+session) command to reset the BMP session for the new BMP session parameters to take effect.
* Configure TLS authentication.
  
  
  
  The Secure Sockets Layer (SSL) protocol protects data privacy based on the Internet. It allows a client and a server to communicate in a way designed to prevent eavesdropping. Specifically, to ensure data transmission security on a network, a BGP peer or peer group needs to be configured as an SSL client or as a server, and the SSL data encryption, identity authentication, and message integrity verification mechanisms need to be used.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **ssl-server** **certificate**
     
     
     
     SSL/TLS authentication is enabled on an SSL server.
  4. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **ssl-policy** **name** *ssl-policy-name*
     
     
     
     The SSL policy is applied to the SSL client or server.
  5. Run [**peer**](cmdqueryname=peer) { *group-name* | *ipv4-address* } **ssl-policy** **role** { **client** | **server** }
     
     
     
     A peer or peer group is configured as an SSL client or server.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The [**peer as-number**](cmdqueryname=peer+as-number) command has been run to create a peer.
  
  SSL/TLS authentication can be configured only on the server. BGP MD5 authentication and BGP keychain authentication are mutually exclusive.
  
  The configuration of a peer takes precedence over that of the peer group to which the peer belongs.
  
  SSL/TLS authentication takes effect only after SSL/TLS authentication is enabled on the server (SSL/TLS authentication is not required on the client), the SSL client and server are configured, and SSL policies are applied to the client and server.
  
  TLS authentication can be used in BGP single-instance scenarios rather than in BGP multi-instance scenarios.

#### Result

* Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) [ *ipv4-address* ] **verbose** command to view the authentication information about BGP peers.
* Run the [**display gtsm statistics**](cmdqueryname=display+gtsm+statistics) { *slot-id* | **all** } command to check GTSM statistics.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this command is supported only by the admin VS.
* Run the [**display rpki session**](cmdqueryname=display+rpki+session) *ipv4-address* **verbose** command to check RPKI session configurations.
* Run the [**display rpki table**](cmdqueryname=display+rpki+table) command to check ROA information.
* Run the [**display bmp session**](cmdqueryname=display+bmp+session) [ **vpn-instance** *vrf-name* ] [ *ipv4-address* [ **alias** *alias-name* ] **verbose** ] command to check BMP session configurations.
* Run the [**display bgp bmp-monitor**](cmdqueryname=display+bgp+bmp-monitor) { **all** | { **ipv4** | **vpnv4** **vpn-instance** *vpn-instance-name* | **vpnv4** } *ipv4-address* } command to check information about BGP peers monitored through BMP in all address families or in a specified address family.
* Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **bgp** **statistics** **slot** *slot-id* command to check statistics about BGP whitelist session CAR on a specified interface board.