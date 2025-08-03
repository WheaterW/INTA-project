Configuring BFD Session Authentication
======================================

Configuring BFD Session Authentication

#### Prerequisites

Before configuring BFD session authentication, complete the following tasks:

* Enable BFD globally.
* Create a BFD session.

#### Context

If a network requires high security, you can configure BFD session authentication to improve network security. BFD session authentication verifies BFD packets when a BFD session is created. As shown in [Figure 1 BFD session setup](#EN-US_TASK_0000001478199318__fig1079985816269), the BFD session between DeviceA and DeviceB is in the DOWN state initially. After a device receives a BFD packet with the State field set to DOWN from the peer, the device does not switch the BFD session state to INIT. Instead, it checks whether the authentication information in the packet is the same as the local authentication information. If they are the same, the device sends a BFD packet with the State field set to INIT to the peer. After receiving the packet with the State field set to INIT, the peer device compares the authentication information in the packet with the local authentication information. If the authentication information is the same, it changes the local BFD session state to UP. If the authentication information is different, it discards the packet. This ensures the security of the BFD session.

**Figure 1** BFD session setup  
![](figure/en-us_image_0000001710275361.png)

BFD session authentication applies to single-hop BFD for IP sessions, and multi-hop BFD for IP sessions. After negotiation packet authentication is configured, the BFD packet sender sets the A flag in the packet header to 1. The receiver decapsulates the packet. If the A flag in the packet header is different from the local one, the receiver discards the packet. If they are the same, the receiver checks whether the authentication field is the same as the local configuration. If they are the same, the BFD session is set up.

![](public_sys-resources/note_3.0-en-us.png) 

When configuring session authentication, ensure that the same authentication mode, authentication password, and authentication timeout interval are configured on the sender and receiver.

An authentication password can be configured in cleartext or ciphertext mode. In both modes, the password is displayed in ciphertext in the configuration file.

It is recommended that the password be at least eight characters long and contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters.



#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure BFD session authentication according to the service scenario.
   * BFD sessions in BFD for IP scenarios
     1. Enter the BFD view.
        ```
        [bfd](cmdqueryname=bfd)
        ```
     2. Configure BFD session authentication information in a BFD for IP scenario.
        + Configure authentication information for a single-hop BFD for IPv4 session.
          ```
          [bfd](cmdqueryname=bfd) single-hop peer-ip ip-address [ vpn-instance vpn-name ] authentication-mode met-sha1 key-id key-id-value cipher cipher-text nego-packet
          ```
        + Configure authentication information for a single-hop BFD for IPv6 session.![](public_sys-resources/note_3.0-en-us.png) 
          
          The CE6885-LL in low-latency mode does not support IPv6 functions.
          
          ```
          [bfd](cmdqueryname=bfd) single-hop peer-ipv6 ipv6-address [ vpn-instance vpn-name ] authentication-mode met-sha1 key-id key-id-value cipher cipher-text nego-packet
          ```
        + Configure authentication information for a multi-hop BFD for IPv4 session.
          ```
          [bfd](cmdqueryname=bfd) multi-hop peer-ip ip-address [ vpn-instance vpn-name ] authentication-mode met-sha1 key-id key-id-value cipher cipher-text nego-packet
          ```
        + Configure authentication information for a multi-hop BFD for IPv6 session.![](public_sys-resources/note_3.0-en-us.png) 
          
          The CE6885-LL in low-latency mode does not support IPv6 functions.
          
          ```
          [bfd](cmdqueryname=bfd) multi-hop peer-ipv6 ipv6-address [ vpn-instance vpn-name ] authentication-mode met-sha1 key-id key-id-value cipher cipher-text nego-packet
          ```
3. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display bfd session all verbose**](cmdqueryname=display+bfd+session+all+verbose) command to check the status of the authenticated BFD session.