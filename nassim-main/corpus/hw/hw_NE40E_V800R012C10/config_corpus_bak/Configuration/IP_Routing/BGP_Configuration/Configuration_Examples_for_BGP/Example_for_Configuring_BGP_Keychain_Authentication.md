Example for Configuring BGP Keychain Authentication
===================================================

By configuring keychain authentication between BGP peers, you can enhance the security of BGP connections.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172366409__fig_dc_vrp_bgp_cfg_308501), Device A belongs to AS 100, and Device B belongs to AS 200. BGP runs on the network, and BGP keychain authentication is used to protect EBGP connections against attacks.

**Figure 1** Networking diagram of configuring BGP keychain authentication![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example is GE 0/1/0.


  
![](images/fig_dc_vrp_bgp_cfg_308501.png)

#### Precautions

During the configuration, note the following:

* Keychain authentication must be configured on both BGP peers. The keychains configured at both ends must use the same encryption algorithm and password so that a TCP connection can be set up and BGP messages can be exchanged properly.
* For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish an EBGP connection between Device A and Device B.
2. Configure keychain authentication on Device A and Device B.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs and AS numbers of Device A and Device B
* Name of keychain authentication between Device A and Device B
* Passwords to be encrypted using the HMAC-SHA256 algorithm for the authentication on Device A and Device B

#### Procedure

1. Configure an IP address for each interface. For configuration details, see Configuration Files in this section.
2. Establish an EBGP connection.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 10.20.1.2 as-number 200
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] peer 10.20.1.1 as-number 100
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
3. Configure keychain authentication.
   
   
   
   # Configure Device A.
   
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
   
   # Configure Device B.
   
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
4. Apply keychain authentication on the EBGP connection between Device A and Device B.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] peer 10.20.1.2 keychain AMode
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure Device B.
   
   ```
   [*DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] peer 10.20.1.1 keychain AMode
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
5. Verify the configuration.
   
   
   
   # On Device A, check the BGP connection status after keychain authentication is configured.
   
   ```
   <~DeviceA> display bgp peer
   
    BGP local router ID : 10.20.1.1
    Local AS number : 100
    Total number of peers : 1         Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.20.1.2       4         200       21       24     0 00:00:23      Established    0
   ```
   
   You can view that the status of the BGP connection is Established after keychain authentication is configured.
   
   # Run the [**display keychain**](cmdqueryname=display+keychain) *keychain-name* command on Device A to check the Key-id in **Active** state.
   
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
   
   # Run the [**display bgp peer**](cmdqueryname=display+bgp+peer+verbose) *ipv4-address* **verbose** command to verify that the authentication type configured for the BGP peer is **Keychain(Amode)**.
   
   ```
   <~DeviceA> [display bgp peer](cmdqueryname=display+bgp+peer+verbose) 10.20.1.2 verbose
            BGP Peer is 10.20.1.2,  remote AS 200
            Type: EBGP link
            BGP version 4, Remote router ID 2.2.2.2
            Update-group ID: 3
            BGP current state: Established, Up for 00h03m36s
            BGP current event: KATimerExpired
            BGP last state: OpenConfirm
            BGP Peer Up count: 1
            Received total routes: 0
            Received active routes total: 0
            Advertised total routes: 0
            Port: Local - 179        Remote - 55423
            Configured: Connect-retry Time: 32 sec
            Configured: Min Hold Time: 0 sec
            Configured: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Received  : Active Hold Time: 180 sec
            Negotiated: Active Hold Time: 180 sec   Keepalive Time:60 sec
            Peer optional capabilities:
            Peer supports bgp multi-protocol extension
            Peer supports bgp route refresh capability
            Peer supports bgp 4-byte-as capability
            Address family IPv4 Unicast: advertised and received
    Received: Total 6 messages
                     Update messages                1
                     Open messages                  1
                     KeepAlive messages             4
                     Notification messages          0
                     Refresh messages               0
    Sent: Total 7 messages
                     Update messages                1
                     Open messages                  1
                     KeepAlive messages             5
                     Notification messages          0
                     Refresh messages               0
    Authentication type configured: Keychain(amode)
    Last keepalive received: 2013-08-15 17:51:17+00:00
    Last keepalive sent    : 2013-08-15 17:51:52+00:00
    Last update    received: 2013-08-15 17:48:27+00:00
    Last update    sent    : 2013-08-15 17:48:27+00:00
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

* Device A configuration file
  
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
   ip address 10.20.1.1 255.255.255.0
  #
  bgp 100
   router-id 1.1.1.1
   peer 10.20.1.2 as-number 200
   peer 10.20.1.2 keychain AMode
   #              
   ipv4-family unicast
    undo synchronization
    peer 10.20.1.2 enable
  #
  return
  ```
* Device B configuration file
  
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
   ip address 10.20.1.2 255.255.255.0
  #
  bgp 200
   router-id 2.2.2.2
   peer 10.20.1.1 as-number 100
   peer 10.20.1.1 keychain AMode
   #              
   ipv4-family unicast
    undo synchronization
    peer 10.20.1.1 enable
  #
  return
  ```