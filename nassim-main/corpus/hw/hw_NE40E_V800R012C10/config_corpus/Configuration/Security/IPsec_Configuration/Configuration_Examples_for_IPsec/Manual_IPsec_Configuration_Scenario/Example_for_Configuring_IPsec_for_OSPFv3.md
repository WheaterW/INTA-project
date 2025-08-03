Example for Configuring IPsec for OSPFv3
========================================

Example for Configuring IPsec for OSPFv3

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172372452__fig_dc_vrp_ipsec_cfg_001801), DeviceA and DeviceB are connected over a public network, and OSPFv3 is deployed for their communication.

**Figure 1** Configuring IPsec![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interface1 in this example represents GE 0/1/1.


  
![](images/fig_dc_vrp_ipsec_cfg_001801.png)

If no authentication mechanism is configured, routing protocol packets transmitted between DeviceA and DeviceB may be modified or spoofed by attackers. As a result, their connection may be torn down, or incorrect routes may be imported.

To prevent such attacks, establish an IPsec tunnel between DeviceA and DeviceB to protect OSPFv3 packets transmitted between them. Configure Encapsulating Security Payload (ESP) as the security protocol, and Secure Hash Algorithm 2-256 (SHA2-256) as the authentication algorithm.


#### Configuration Notes

* The encapsulation modes and security protocols on both IPsec peers must be identical.
* The authentication modes and encryption algorithms on the two IPsec peers must be identical.
* The security parameter indexes (SPIs) and authentication keys on the two IPsec peers must be identical.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic OSPFv3 functions on DeviceA and DeviceB.
2. Configure IPsec proposals. Configure ESP as the security protocol, SHA2-256 as the authentication algorithm, and AES-256 as the encryption algorithm.
3. Set SA parameters.
4. Apply SAs to OSPFv3 processes, enabling IPsec to protect OSPFv3 packets transmitted between DeviceA and DeviceB.

#### Data Preparation

To complete the configuration, you need the following data:

| Device Name | Router ID | Process ID | SPI | Authentication Key in String Format |
| --- | --- | --- | --- | --- |
| DeviceA | 1.1.1.1 | 1 | 12345 | abcdef |
| DeviceB | 2.2.2.2 | 1 | 12345 | abcdef |




#### Procedure

1. Configure OSPFv3 on DeviceA and DeviceB.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] ospfv3 1
   ```
   ```
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-ospfv3-1] area 0
   ```
   ```
   [*DeviceA-ospfv3-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceA-ospfv3-1-area-0.0.0.0] quit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] ospfv3 1
   ```
   ```
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-ospfv3-1] area 0
   ```
   ```
   [*DeviceB-ospfv3-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceB-ospfv3-1-area-0.0.0.0] quit
   ```
2. Configure IPv6 addresses for and enable OSPFv3 on interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface gigabitethernet0/1/1
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ipv6 address 2001:db8::1 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] ospfv3 1 area 0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/1] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] interface gigabitethernet0/1/1
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] ipv6 address 2001:db8::2 64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] ospfv3 1 area 0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/1] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/1] quit
   ```
3. Configure security proposals on DeviceA and DeviceB.
   
   
   
   # Configure a security proposal on DeviceA.
   
   ```
   [~DeviceA] ipsec proposal proposal1
   ```
   ```
   [*DeviceA-ipsec-proposal-proposal1] encapsulation-mode transport
   ```
   ```
   [*DeviceA-ipsec-proposal-proposal1] transform esp
   ```
   ```
   [*DeviceA-ipsec-proposal-proposal1] esp encryption-algorithm aes 256
   ```
   ```
   [*DeviceA-ipsec-proposal-proposal1] esp authentication-algorithm sha2-256
   ```
   ```
   [*DeviceA-ipsec-proposal-proposal1] commit
   ```
   ```
   [~DeviceA-ipsec-proposal-proposal1] quit
   ```
   
   # Configure a security proposal on DeviceB.
   
   ```
   [~DeviceB] ipsec proposal proposal2
   ```
   ```
   [*DeviceB-ipsec-proposal-proposal2] encapsulation-mode transport
   ```
   ```
   [*DeviceB-ipsec-proposal-proposal2] transform esp
   ```
   ```
   [*DeviceB-ipsec-proposal-proposal2] esp encryption-algorithm aes 256
   ```
   ```
   [*DeviceB-ipsec-proposal-proposal2] esp authentication-algorithm sha2-256
   ```
   ```
   [*DeviceB-ipsec-proposal-proposal2] commit
   ```
   ```
   [~DeviceB-ipsec-proposal-proposal2] quit
   ```
   
   # Run the [**display ipsec proposal**](cmdqueryname=display+ipsec+proposal) command on DeviceA and DeviceB to check the configuration. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ipsec proposal
   ```
   ```
   Total IPsec proposal number: 1
   IPsec proposal name: proposal1
     encapsulation mode: transport
     transform: esp-new
     ESP protocol: authentication SHA2-HMAC-256, encryption 256-AES
   ```
4. Configure IPsec SAs on DeviceA and DeviceB and apply a proposal to each SA.
   
   
   
   # Configure an IPsec SA on DeviceA and apply a proposal to it.
   
   ```
   [~DeviceA] ipsec sa sa1
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] proposal proposal1
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] commit
   ```
   
   # Configure an IPsec SA on DeviceB and apply a proposal to it.
   
   ```
   [~DeviceB] ipsec sa sa2
   ```
   ```
   [*DeviceB-ipsec-sa-sa2] proposal proposal2
   ```
   ```
   [*DeviceB-ipsec-sa-sa2] commit
   ```
5. # Configure SPIs and authentication keys in string format on DeviceA and DeviceB.
   
   
   
   # Configure SPIs and authentication keys in string format on DeviceA.
   
   ```
   [~DeviceA] ipsec sa sa1
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] sa spi inbound esp 12345
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] sa spi outbound esp 12345
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] sa string-key inbound esp abcdef
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] sa string-key outbound esp abcdef
   ```
   ```
   [*DeviceA-ipsec-sa-sa1] commit
   ```
   ```
   [~DeviceA-ipsec-sa-sa1] quit
   ```
   
   # Configure SPIs and authentication keys in string format on DeviceB.
   
   ```
   [~DeviceB] ipsec sa sa2
   ```
   ```
   [*DeviceB-ipsec-sa-sa2] sa spi outbound esp 12345
   ```
   ```
   [*DeviceB-ipsec-sa-sa2] sa spi inbound esp 12345
   ```
   ```
   [*DeviceB-ipsec-sa-sa2] sa string-key outbound esp abcdef
   ```
   ```
   [*DeviceB-ipsec-sa-sa2] sa string-key inbound esp abcdef
   ```
   ```
   [*DeviceB-ipsec-sa-sa2] commit
   ```
   ```
   [~DeviceB-ipsec-sa-sa2] quit
   ```
6. Apply SAs to OSPFv3 processes.
   
   
   
   # Apply an SA to an OSPFv3 process on DeviceA.
   
   ```
   [~DeviceA] ospfv3 1
   ```
   ```
   [*DeviceA-ospfv3-1] ipsec sa sa1
   ```
   ```
   [*DeviceA-ospfv3-1] commit
   ```
   
   # Apply an SA to an OSPFv3 process on DeviceB.
   
   ```
   [~DeviceB] ospfv3 1
   ```
   ```
   [*DeviceB-ospfv3-1] ipsec sa sa2
   ```
   ```
   [*DeviceB-ospfv3-1] commit
   ```
7. Verify the configuration.
   
   
   
   # Run the **display ipsec sa** command on DeviceA and DeviceB to check the configuration. The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ipsec sa
   ```
   ```
   Total IP security association number: 1
   ```
   ```
     IP security association name: sa1
   ```
   ```
     Number of references: 1
   ```
   ```
       proposal name: proposal1
   ```
   ```
       State: Complete
   ```
   ```
       inbound AH setting: 
   ```
   ```
         AH spi: 
   ```
   ```
         AH string-key: 
   ```
   ```
         AH authentication hex key: 
   ```
   ```
       inbound ESP setting:
   ```
   ```
         ESP spi: 12345 (0x3039)
   ```
   ```
         ESP string-key: %#%#<}jb{br9\zi%X+/Y@:Y>Lw(L\v#*^KsM"/8RaRe$%#%#
   ```
   ```
         ESP encryption hex key: 
   ```
   ```
         ESP authentication hex key:
   ```
   ```
       outbound AH setting: 
   ```
   ```
         AH spi: 
   ```
   ```
         AH string-key:
   ```
   ```
         AH authentication hex key: 
   ```
   ```
       outbound ESP setting:
   ```
   ```
         ESP spi: 12345 (0x3039)
   ```
   ```
         ESP string-key: %#%#<}j/@X4355SE9JZTD0>GQf"}w2@X,k6.E\Z,z\{#%#%#
   ```
   ```
         ESP encryption hex key: 
   ```
   ```
         ESP authentication hex key: 
   ```
   
   
   
   # Run the **display ipsec statistics** command to check statistics about incoming and outgoing protocol packets processed by IPsec and detailed information about dropped protocol packets. If statistics about incoming and outgoing protocol packets processed by IPsec are displayed, the configuration succeeds. For example:
   
   ```
   [~DeviceA] display ipsec statistics
   ```
   ```
     IPv6 security packet statistics:
       input/output security packets: 184/19
       input/output security bytes: 13216/1312
       input/output dropped security packets: 0/0
       dropped security packet detail:
         memory process problem: 0
         can't find SA: 0
         queue is full: 0
         authentication is failed: 0
         wrong length: 0
         replay packet: 0
         too long packet: 0
         invalid SA: 0
         policy deny: 0
     the normal packet statistics:
       input/output dropped normal packets: 0/0
    IPv4 security packet statistics:
        input/output security packets: 0/0
        input/output security bytes: 0/0
        input/output dropped security packets: 0/0
        dropped security packet detail:
          memory process problem: 0
          can't find SA: 0
          queue is full: 0
          authentication is failed: 0
          wrong length: 0
          replay packet: 0
          too long packet: 0
          invalid SA: 0
          policy deny: 0
      the normal packet statistics:
        input/output dropped normal packets: 0/0
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  ipsec proposal proposal1
   encapsulation-mode transport
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec sa sa1
   proposal proposal1
   sa spi inbound esp 12345
   sa string-key inbound esp %#%#<}jb{br9\zi%X+/Y@:Y>Lw(L\v#*^KsM"/8RaRe$%#%#
   sa spi outbound esp 12345
   sa string-key outbound esp %#%#<}j/@X4355SE9JZTD0>GQf"}w2@X,k6.E\Z,z\{#%#%#
  #
  ospfv3 1
   router-id 1.1.1.1
   ipsec sa sa1
   area 0.0.0.0   
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8::1/64
   ospfv3 1 area 0
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  ipsec proposal proposal2
   encapsulation-mode transport
   esp authentication-algorithm sha2-256
   esp encryption-algorithm aes 256
  #
  ipsec sa sa2
   proposal proposal2
   sa spi inbound esp 12345
   sa string-key inbound esp %#%#<}j/@XSE9JZT5]2"T#]2"T<}j/@XSE9JZT5>%#%#
   sa spi outbound esp 12345
   sa string-key outbound esp %#%#)YTP%@nFE7bL^B&WSBiQ1[p#M"/8RaRe%$7$%#%#
  #
  ospfv3 1
   router-id 2.2.2.2
   ipsec sa sa2
   area 0.0.0.0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8::2/64
   ospfv3 1 area 0
  #
  return
  ```