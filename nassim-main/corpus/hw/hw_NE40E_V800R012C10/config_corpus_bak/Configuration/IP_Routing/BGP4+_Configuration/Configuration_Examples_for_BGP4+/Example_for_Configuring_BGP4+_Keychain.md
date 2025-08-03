Example for Configuring BGP4+ Keychain
======================================

Configuring keychain authentication between BGP4+ peers can enhance the security of BGP4+ connections.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001424386041__fig_dc_vrp_bgp_cfg_308501), DeviceA belongs to AS 100, and DeviceB belongs to AS 200. BGP runs on the network, and BGP4+ keychain is used to protect EBGP connections against attacks.

**Figure 1** Networking diagram for configuring BGP4+ keychain![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GE0/1/0.


  
![](figure/en-us_image_0000001374066252.png)

#### Precautions

During the configuration, note the following:

* Keychain authentication must be configured on both BGP4+ peers. The keychains configured at both ends must use the same encryption algorithm and password so that a TCP connection can be set up and BGP4+ messages can be exchanged properly.
* For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish an EBGP connection between DeviceA and DeviceB.
2. Configure keychain authentication on DeviceA and DeviceB.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs and AS numbers of DeviceA and DeviceB
* Name of keychain authentication between DeviceA and DeviceB
* Passwords to be encrypted using the HMAC-SHA256 algorithm for the authentication on DeviceA and DeviceB

#### Procedure

1. Configure an IP address for each interface. For configuration details, see Configuration Files in this section.
2. Configure EBGP connections.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 2001:db8:1::2 as-number 200
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] peer 2001:db8:1::1 as-number 100
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
3. Configure a keychain.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] keychain AMode mode absolute
   ```
   ```
   [*DeviceA-keychain] tcp-kind 179
   ```
   ```
   [*DeviceA-keychain] tcp-algorithm-id hmac-sha-256 17
   ```
   ```
   [*DeviceA-keychain] receive-tolerance 100
   ```
   ```
   [*DeviceA-keychain] key-id 1
   ```
   ```
   [*DeviceA-keychain-keyid-1] algorithm hmac-sha-256
   ```
   ```
   [*DeviceA-keychain-keyid-1] key-string hello
   ```
   ```
   [*DeviceA-keychain-keyid-1] send-time 11:00 2009-12-24 to 12:00 2009-12-24
   ```
   ```
   [*DeviceA-keychain-keyid-1] receive-time 11:00 2009-12-24 to 12:00 2009-12-24
   ```
   ```
   [*DeviceA-keychain-keyid-1] commit
   ```
   ```
   [~DeviceA-keychain-keyid-1] quit
   ```
   ```
   [~DeviceA-keychain] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] keychain AMode mode absolute
   ```
   ```
   [*DeviceB-keychain] tcp-kind 179
   ```
   ```
   [*DeviceB-keychain] tcp-algorithm-id hmac-sha-256 17
   ```
   ```
   [*DeviceB-keychain] receive-tolerance 100
   ```
   ```
   [*DeviceB-keychain] key-id 1
   ```
   ```
   [*DeviceB-keychain-keyid-1] algorithm hmac-sha-256
   ```
   ```
   [*DeviceB-keychain-keyid-1] key-string hello
   ```
   ```
   [*DeviceB-keychain-keyid-1] send-time 11:00 2009-12-24 to 12:00 2009-12-24
   ```
   ```
   [*DeviceB-keychain-keyid-1] receive-time 11:00 2009-12-24 to 12:00 2009-12-24
   ```
   ```
   [*DeviceB-keychain-keyid-1] commit
   ```
   ```
   [~DeviceB-keychain-keyid-1] quit
   ```
   ```
   [~DeviceB-keychain] quit
   ```
4. Apply keychain authentication on the EBGP connection between DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 2001:db8:1::2 keychain AMode
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] peer 2001:db8:1::1 keychain AMode
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
5. Verifying the Configuration
   
   
   
   # On DeviceA, check the BGP connection status after keychain authentication is configured.
   
   ```
   <~DeviceA> display bgp ipv6 peer
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1         Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:db8:1::2   4         200       4       5     0 00:00:23      Established    1
   ```
   
   You can view that the status of the BGP connection is Established after keychain authentication is configured.
   
   
   
   # Run the [**display keychain**](cmdqueryname=display+keychain) *keychain-name* command on DeviceA to check the Key-id in **Active** state.
   
   ```
   <~DeviceA> display keychain Amode
   Keychain Information:
    ----------------------
    Keychain Name             : amode
      Timer Mode              : Absolute
      Receive Tolerance(min)  : 100
      Digest Length           : 32
      Time Zone               : LMT
      TCP Kind                : 179
      TCP Algorithm IDs       :
        HMAC-MD5              : 5
        HMAC-SHA1-12          : 2
        HMAC-SHA1-20          : 6
        MD5                   : 3
        SHA1                  : 4
        HMAC-SHA-256          : 17
        SHA-256               : 8
        SM3                   : 9
        AES-128-CMAC          : 10
        HMAC-SHA-384          : 11
        HMAC-SHA-512          : 12
    Number of Key IDs         : 1
    Active Send Key ID        : 1
    Active Receive Key IDs    : 01
    Default send Key ID       : Not configured
   
    Key ID Information:
    ----------------------
    Key ID                    : 1
      Key string              : ******
      Algorithm               : HMAC-SHA-256
      SEND TIMER              :
        Start time            : 2013-08-10 10:00
        End time              : 2022-10-28 12:00
        Status                : Active
      RECEIVE TIMER           :
        Start time            : 2013-08-10 10:00
        End time              : 2022-10-28 12:00
        Status                : Active
   ```
   
   # Run the [**display bgp ipv6 peer**](cmdqueryname=display+bgp+ipv6+peer+verbose) *ipv6-address* **verbose** command to check whether the authentication type configured for the BGP peer is **Keychain(Amode)**.
   
   ```
   <~DeviceA> [display bgp ipv6 peer](cmdqueryname=display+bgp+ipv6+peer+verbose) 2001:DB8:1::2 verbose
            BGP Peer is 2001:DB8:1::2,  remote AS 200
            Type: EBGP link
            BGP version 4, Remote router ID 2.2.2.2
            Update-group ID: 3
            BGP current state: Established, Up for 00h06m41s
            BGP current event: KATimerExpired
            BGP last state: OpenConfirm
            BGP Peer Up count: 1
            Received total routes: 1
            Received active routes total: 0
            Advertised total routes: 1
            Port: Local - 179        Remote - 59233
            Configured: Connect-retry Time: 32 sec
            Configured: Min Hold Time: 0 sec
            Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Received  : Active Hold Time: 180 sec
            Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Peer optional capabilities:
            Peer supports bgp multi-protocol extension
            Peer supports bgp route refresh capability
            Peer supports bgp 4-byte-as capability
            Address family IPv6 Unicast: advertised and received
    Received: Total 11 messages
                     Update messages                2
                     Open messages                  1
                     KeepAlive messages             8
                     Notification messages          0
                     Refresh messages               0
    Sent: Total 12 messages
                     Update messages                2
                     Open messages                  2
                     KeepAlive messages             8
                     Notification messages          0
                     Refresh messages               0
    Authentication type configured: Keychain(amode)
    Last keepalive received: 2013-08-15 17:42:11+00:00
    Last keepalive sent    : 2013-08-15 17:42:15+00:00
    Last update    received: 2013-08-15 17:36:08+00:00
    Last update    sent    : 2013-08-15 17:36:08+00:00
    No refresh received since peer has been configured
    No refresh sent since peer has been configured
    Minimum route advertisement interval is 30 seconds
    Optional capabilities:
    Route refresh capability has been enabled
    4-byte-as capability has been enabled
    Peer Preferred Value: 0
    Memory Priority: medium
    Routing policy configured:
    No routing policy is configured
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  keychain AMode mode absolute
   receive-tolerance 100
   tcp-kind 179
   tcp-algorithm-id hmac-sha-256 17
   #
   key-id 1
    algorithm hmac-sha-256
    key-string cipher %#%#e^1}%%w;/C[M)OQc7"j+,2)}%#%#
    send-time 11:00 2009-12-24 to 12:00 2009-12-24
    receive-time 11:00 2009-12-24 to 12:00 2009-12-24
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable
   ipv6 address 2001:db8:1::1 64
  #
  bgp 100
   router-id 1.1.1.1
   peer 2001:db8:1::2 as-number 200
   peer 2001:db8:1::2 keychain AMode
   #
   ipv4-family unicast
    undo synchronization 
   #              
   ipv6-family unicast
    undo synchronization
    peer 2001:db8:1::2 enable
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  keychain AMode mode absolute
   receive-tolerance 100
   tcp-kind 179
   tcp-algorithm-id hmac-sha-256 17
   #
   key-id 1
    algorithm hmac-sha-256
    key-string cipher %#%#ub(70WJ"^=i(kxPK@*fK,)}t%#%#
    send-time 11:00 2009-12-24 to 12:00 2009-12-24
    receive-time 11:00 2009-12-24 to 12:00 2009-12-24
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ipv6 enable
   ipv6 address 2001:db8:1::2 64
  #
  bgp 200
   router-id 2.2.2.2
   peer 2001:db8:1::1 as-number 100
   peer 2001:db8:1::1 keychain AMode
   #
   ipv4-family unicast
    undo synchronization 
   #              
   ipv6-family unicast
    undo synchronization
    peer 2001:db8:1::1 enable
  #
  return
  ```