Example for Configuring TCP-AO Authentication for BGP
=====================================================

Example_for_Configuring_TCP-AO_Authentication_for_BGP

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001132697979__fig168879525502), DeviceA and DeviceB communicate through BGP.

To ensure the stability and security of the BGP connection, configure TCP-AO to provide dynamic security authentication services for BGP.

**Figure 1** Network diagram of configuring TCP-AO authentication for BGP![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents GE 0/1/0.


  
![](figure/en-us_image_0000001086919832.png)

To complete the configuration, you need the following data:

* Keychain name
* Tolerance time
* ID of the key in the keychain
* Authentication algorithm HMAC-SHA-256 and authentication key (character string used for encryption) of the key
* Lifetime of the key
* TCP-AO name
* ID of the key in the TCP-AO
* send-id and receive-id in the key

#### Precautions

* Ensure that NTP and BGP have been configured.
* The keychain names configured on DeviceA and DeviceB must be the same.
* The time modes of the keychains configured on DeviceA and DeviceB must be the same.
* The key IDs in the keychains configured on DeviceA and DeviceB must be the same. When multiple keys are configured, the key quantity and IDs must be the same as those on the other end, respectively.
* The authentication algorithm and key string for the same keys configured on DeviceA and DeviceB must be the same.
* The TCP-AO names configured on DeviceA and DeviceB must be the same.
* The key IDs in the TCP-AOs configured on DeviceA and DeviceB must be the same. When multiple keys are configured, the key quantity and IDs must be the same as those on the other end, respectively.
* For the same key, the send-id and receive-id configured on DeviceA must match those configured on DeviceB. That is, the receive-id of DeviceA equals the send-id of DeviceB, and the send-id of DeviceA equals the receive-id of DeviceB.

#### Configuration Roadmap

1. Configure a keychain.
2. Configure a TCP-AO and bind it to the keychain.
3. Configure TCP-AO authentication for BGP.

#### Procedure

1. Configure a keychain.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] keychain huawei mode absolute
   [*DeviceA-keychain-huawei] receive-tolerance 5
   [*DeviceA-keychain-huawei] key-id 1
   [*DeviceA-keychain-huawei-keyid-1] algorithm hmac-sha-256
   [*DeviceA-keychain-huawei-keyid-1] key-string cipher YsHsjx_202206
   [*DeviceA-keychain-huawei-keyid-1] send-time 12:00 2019-12-10 to 15:00 2019-12-10
   [*DeviceA-keychain-huawei-keyid-1] quit
   [*DeviceA-keychain-huawei] key-id 2
   [*DeviceA-keychain-huawei-keyid-2] algorithm hmac-sha-256
   [*DeviceA-keychain-huawei-keyid-2] key-string cipher YsHsjx_202207
   [*DeviceA-keychain-huawei-keyid-2] send-time 15:01 2019-12-10 to 18:00 2019-12-10
   [*DeviceA-keychain-huawei-keyid-2] quit
   [*DeviceA-keychain-huawei] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*DeviceB] keychain huawei mode absolute
   [*DeviceB-keychain-huawei] receive-tolerance 5
   [*DeviceB-keychain-huawei] key-id 1
   [*DeviceB-keychain-huawei-keyid-1] algorithm hmac-sha-256
   [*DeviceB-keychain-huawei-keyid-1] key-string cipher YsHsjx_202206
   [*DeviceB-keychain-huawei-keyid-1] send-time 12:00 2019-12-10 to 15:00 2019-12-10
   [*DeviceB-keychain-huawei-keyid-1] quit
   [*DeviceB-keychain-huawei] key-id 2
   [*DeviceB-keychain-huawei-keyid-2] algorithm hmac-sha-256
   [*DeviceB-keychain-huawei-keyid-2] key-string cipher YsHsjx_202207
   [*DeviceB-keychain-huawei-keyid-2] send-time 15:01 2019-12-10 to 18:00 2019-12-10
   [*DeviceB-keychain-huawei-keyid-2] quit
   [*DeviceB-keychain-huawei] quit
   [*DeviceB] commit
   ```
2. Configure a TCP-AO and bind it to the keychain.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] tcp ao huawei
   [*DeviceA-tcp-ao-huawei] binding keychain huawei
   [*DeviceA-tcp-ao-huawei] key-id 1
   [*DeviceA-tcp-ao-huawei-keyid-1] send-id 1 receive-id 2
   [*DeviceA-tcp-ao-huawei-keyid-1] quit
   [*DeviceA-tcp-ao-huawei] key-id 2
   [*DeviceA-tcp-ao-huawei-keyid-2] send-id 3 receive-id 4
   [*DeviceA-tcp-ao-huawei-keyid-2] quit
   [*DeviceA-tcp-ao-huawei] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] tcp ao huawei
   [*DeviceB-tcp-ao-huawei] binding keychain huawei
   [*DeviceB-tcp-ao-huawei] key-id 1
   [*DeviceB-tcp-ao-huawei-keyid-1] send-id 2 receive-id 1
   [*DeviceB-tcp-ao-huawei-keyid-1] quit
   [*DeviceB-tcp-ao-huawei] key-id 2
   [*DeviceB-tcp-ao-huawei-keyid-2] send-id 4 receive-id 3
   [*DeviceB-tcp-ao-huawei-keyid-2] quit
   [*DeviceB-tcp-ao-huawei] quit
   [*DeviceB] commit
   ```
3. Configure TCP-AO authentication for BGP.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet 0/1/0
   [~DeviceA-GigabitEthernet0/1/0] ip address 192.168.1.1 24
   [*DeviceA-GigabitEthernet0/1/0] quit
   [*DeviceA] bgp 1
   [*DeviceA-bgp] router-id 1.1.1.1
   [*DeviceA-bgp] peer 192.168.1.2 as-number 1
   [*DeviceA-bgp] peer 192.168.1.2 tcp-ao policy huawei
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet 0/1/0
   [~DeviceB-GigabitEthernet0/1/0] ip address 192.168.1.2 24
   [*DeviceB-GigabitEthernet0/1/0] quit
   [*DeviceB] bgp 1
   [*DeviceB-bgp] router-id 2.2.2.2
   [*DeviceB-bgp] peer 192.168.1.1 as-number 1
   [*DeviceB-bgp] peer 192.168.1.1 tcp-ao policy huawei
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

Check whether TCP-AO authentication is configured successfully for BGP. The following example uses the command output on DeviceA.

Run the [**display bgp peer**](cmdqueryname=display+bgp+peer) *ipv4-address* **verbose** command to check that the authentication type configured for the BGP peer is **TCP-AO(huawei)**.

```
<DeviceA> display bgp peer 192.168.1.2 verbose
         BGP Peer is 192.168.1.2,  remote AS 1                                  
         Type: IBGP link                                                        
         BGP version 4, Remote router ID 2.2.2.2                                
         Update-group ID: 3                                                     
         BGP current state: Established, Up for 00h27m26s                       
         BGP current event: RecvKeepalive                                       
         BGP last state: OpenConfirm                                            
         BGP Peer Up count: 2                                                   
         Received total routes: 0                                               
         Received active routes total: 0                                        
         Advertised total routes: 0                                             
         Port: Local - 58168        Remote - 179                                
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
 Received: Total 34 messages                                                    
                  Update messages                1                              
                  Open messages                  1                              
                  KeepAlive messages             32                             
                  Notification messages          0                              
                  Refresh messages               0                              
 Sent: Total 33 messages                                                        
                  Update messages                1                              
                  Open messages                  1                              
                  KeepAlive messages             31                             
                  Notification messages          0                              
                  Refresh messages               0                              
 Authentication type configured: TCP-AO(huawei)                               
 Last keepalive received: 2019-12-10 10:12:29+00:00                             
 Last keepalive sent    : 2019-12-10 10:12:04+00:00                             
 Last update    received: 2019-12-10 09:45:14+00:00                             
 Last update    sent    : 2019-12-10 09:45:14+00:00                             
 No refresh received since peer has been configured                             
 No refresh sent since peer has been configured                                 
 Minimum route advertisement interval is 15 seconds                             
 Optional capabilities:                                                         
 Route refresh capability has been enabled                                      
 4-byte-as capability has been enabled                                          
 Peer Preferred Value: 0                                                        
 Routing policy configured:                                                     
 No routing policy is configured
```

#### Configuration Scripts

* DeviceA
  
  ```
  #
   sysname DeviceA
  #
  keychain huawei mode absolute
   receive-tolerance 5
   #
   key-id 1
    algorithm hmac-sha-256
    key-string cipher %^%#1h29-c>>[H,XTu>Q}##;"}JOQOK#c>TD6>~d-BaJ%^%#
    send-time 12:00 2019-12-10 to 15:00 2019-12-10
   #
   key-id 2
    algorithm hmac-sha-256
    key-string cipher %^%#^<Sn.IK2iK'N%[VnMhv-I)|C4d<K$F$a.6%jEN@K%^%#
    send-time 15:01 2019-12-10 to 18:00 2019-12-10
  #
  tcp ao huawei
   binding keychain huawei
   #
   key-id 1
    send-id 1 receive-id 2
   key-id 2
    send-id 3 receive-id 4
  #
  interface gigabitethernet0/1/0
   ip address 192.168.1.1 255.255.255.0
  #
  bgp 1
   router-id 1.1.1.1
   peer 192.168.1.2 as-number 1
   peer 192.168.1.2 tcp-ao policy huawei
   #
   ipv4-family unicast
    peer 192.168.1.2 enable
  #
  return
  ```
* DeviceB
  
  ```
  #
   sysname DeviceB
  #
  keychain huawei mode absolute
   receive-tolerance 5
   #
   key-id 1
    algorithm hmac-sha-256
    key-string cipher %^%#p8cb/;OMFES0Wx@PY^"Ka{6q2MB;oG|[ZO-_]u}&%^%#
    send-time 12:00 2019-12-10 to 15:00 2019-12-10
   #
   key-id 2
    algorithm hmac-sha-256
    key-string cipher %^%#&Yq4=s*P:L<"8iG-|o1ZB*Qi0qCn%N{Y3a&Z-zuD%^%#
    send-time 15:01 2019-12-10 to 18:00 2019-12-10
  #
  tcp ao huawei
   binding keychain huawei
   #
   key-id 1
    send-id 2 receive-id 1
   key-id 2
    send-id 4 receive-id 3
  #
  interface gigabitethernet0/1/0
   ip address 192.168.1.2 255.255.255.0
  #
  bgp 1
   router-id 2.2.2.2
   peer 192.168.1.1 as-number 1
   peer 192.168.1.1 tcp-ao policy huawei
   #
   ipv4-family unicast
    peer 192.168.1.1 enable
  #
  return
  ```