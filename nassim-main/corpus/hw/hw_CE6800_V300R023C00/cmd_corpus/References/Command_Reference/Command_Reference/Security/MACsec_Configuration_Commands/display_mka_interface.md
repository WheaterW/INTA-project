display mka interface
=====================

display mka interface

Function
--------



The **display mka interface** command displays MKA session information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mka interface** { *interface-name* | *interface-type* *interface-number* } [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |
| **verbose** | Displays detailed MKA session information. If this parameter is not specified, brief MKA session information is displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays the MACsec configuration and MKA session information, facilitating fault locating.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed MKA session information on 100GE 1/0/1.
```
<HUAWEI> display mka interface 100GE 1/0/1 verbose
Interface 100GE1/0/1:                                                             
  MKA transmit interval(s)               : 2                                    
  MKA life time(s)                       : 6                                    
  SAK life time(s)                       : 3600                                 
  MACsec capability                      : 3                                    
  MACsec mode                            : Normal                               
  MACsec frame validation                : Strict                               
  MACsec replay protection               : YES                                  
  MACsec replay-window(frame(s))         : 0                                    
  MACsec confidentiality-offset(byte(s)) : 0                                    
  MACsec include SCI                     : NO                                   
  MKA algorithm agility                  : 00-80-C2-01                          
  MACsec cipher suite                    : GCM-AES-128                          
  MKA cryptographic algorithm         : AES-CMAC-128 
  Key server priority                    : 2                                    
  Transmit SCI                           : 2CAB009815D00010                     
    CKN: F1C3B2A4D6D9A7C5B4E1AB56DC21ED79AC97BE533671DCAB2678AC55CF71ACED       
      MKA status           : SUCCEEDED                                          
      MI                   : 3D9EF959E258F43AF9C3AE7C                           
      MN                   : 2678                                               
      Key server           : NO                                                 
      Principal actor      : YES                                                
      Live peers           : 1                                                  
      Potential peers      : 0                                                  
      Latest SAK status    : Rx & Tx                                            
      Latest SAK AN        : 1                                                  
      Latest SAK KI        : C795C32E7B0D37ADEFC2CDDC                           
      Latest SAK KN        : 2                                                  
      Old SAK status       : N/A                                                
      Old SAK AN           : N/A                                                
      Old SAK KI           : N/A                                                
      Old SAK KN           : N/A                                                
      Live peers list      :                                                    
      MI                        MN          Priority  Capability  Rx-SCI        
      C795C32E7B0D37ADEFC2CDDC  2680        1         3           2CAB009815B00010                                                          
      Potential peers list :                                                    
      MI                        MN          Priority  Capability  Rx-SCI        
      --                        --          --        --          --            
  MKA statistics:                                                               
    Rx MKA packets     : 5160                                                   
    Tx MKA packets     : 5159                                                   
    Drop MKA packets   : 18                                                     
    Wrong CKN num      : 1                                                      
    Wrong ICV num      : 0                                                      
    SAK install times  : 6                                                      
    SAK delete times   : 5                                                      
    SAK swap times     : 1                                                      
    Latest SAK reason  : KeyServer start SAK switch

```

**Table 1** Description of the **display mka interface** command output
| Item | Description |
| --- | --- |
| MKA transmit interval(s) | Interval for sending MKA protocol packets, in seconds. |
| MKA life time(s) | MKA session timeout period, in seconds.  To configure this parameter, run the mka timer mka-life command. |
| MKA algorithm agility | MKA algorithm agility, which is used to identify the key and ICV generation algorithms used during MKA session negotiation. |
| MKA cryptographic algorithm | MKA key generation algorithm.  To configure this parameter, run the mka cryptographic-algorithm command. |
| MKA status | MKA session status. This field has the following values:   * IDLE: The MKA session is idle. * ABNORMAL: The MKA session is abnormal. * INITIATED: The MKA session is in the initialized state. * POTENTIAL\_PEER\_ESTABLISHED: The neighbor relationship is being established. * SAK\_READY: The key server is transmitting the SAK. * SAK\_EXPECTED: The device is not the key server and is receiving the SAK. * SUCCEEDED: Negotiation is successful. |
| MKA statistics | MKA statistics. |
| SAK life time(s) | SAK timeout period, in seconds.  To configure this parameter, run the mka timer sak-life command. |
| SAK install times | Number of times the SAK is installed. |
| SAK delete times | Number of times the SAK is deleted. |
| SAK swap times | Number of times the SAK is switched. |
| MACsec capability | MACsec capability value:   * 2: Integrity and confidentiality check is supported. Encryption can be performed only from the packet header. * 3: Integrity and confidentiality check is supported. Encryption can start from the packet header, offset 30 bytes, and offset 50 bytes.   By default, the MACsec capability value is 3.  When the device is connected to another type of device, if the peer device supports only MACsec capability 2, the MACsec capability of the device must be the same as that of the peer device.  If the MACsec capability is set to 2, setting the MACsec encryption offset to 30 or 50 using the macsec confidentiality-offset command does not take effect. In this case, the MACsec encryption offset is always 0. |
| MACsec mode | MACsec encryption mode. This field has the following values:   * none: Neither data encryption nor integrity check is performed. * normal: Both data encryption and integrity check are performed. * integrity-only: Integrity check is performed, and data encryption is not performed.   To configure this parameter, run the macsec mode command. |
| MACsec frame validation | MACsec data packet check mode. This field has a fixed value:   * Strict: indicates the strict check mode. That is, data packets are discarded if the check fails. |
| MACsec replay protection | Whether MACsec replay protection is enabled. This field has a fixed value:   * YES: The replay protection function is enabled. |
| MACsec replay-window(frame(s)) | Size of the MACsec replay protection window.  To configure this parameter, run the macsec replay-window command. |
| MACsec confidentiality-offset(byte(s)) | MACsec encryption offset, in bytes.  To configure this parameter, run the macsec confidentiality-offset command. |
| MACsec include SCI | Whether MACsec data packets carry the SCI. This field has the following values:   * YES: The SCI is carried. * NO: The SCI is not carried.   To configure whether the device adds the SCI in MACsec data packets, run the macsec include-sci command. |
| MACsec cipher suite | MACsec cipher suite, which is used to identify the encryption algorithm used for SAK-encrypted data packets. |
| Key server priority | Key server priority.  To configure this parameter, run the mka keyserver priority command. |
| Key server | Whether the local end is a key server:   * YES. * NO. |
| Transmit SCI | SCI on the local end. |
| MI | Member identifier, in the hexadecimal format. |
| MN | Message number. |
| Principal actor | Whether the connection is active, that is, whether the CKN is in use. This field has the following values:   * YES: active connection. * NO: inactive connection. |
| Live peers | Number of peers that have been learned. |
| Live peers list | List of peers that have been learned. |
| Potential peers | Number of peers under negotiation. |
| Potential peers list | List of peers under negotiation. |
| Latest SAK status | Latest SAK status. This field has the following values:   * Rx: SAK receiving is enabled. * Tx: SAK transmitting is enabled. * Rx & Tx: Both SAK receiving and SAK transmitting are enabled. * N/A: The SAK is invalid.   During SAK switching, SAK transmitting is enabled on the key server and then SAK receiving is enabled, and both SAK receiving and SAK transmitting are enabled on the device that is not the key server. The SAK is used to encrypt and decrypt data packets only when both SAK receiving and SAK transmitting are enabled on both ends. |
| Latest SAK AN | Latest SAK association number. |
| Latest SAK KI | Latest SAK identifier. |
| Latest SAK KN | Latest SAK number. |
| Latest SAK reason | Reason for the latest SAK creation or switchover. The possible values are as follows:   * First engendered: The SAK is generated for the first time. * SAK life time over: The SAK times out. * CAK swap. * Configure new key server priority: indicates that the priority of the key server is changed. * Configure new confidentiality-offset: changes the encryption offset. * Configure MACsec mode: configures the encryption mode. * Local PN exhaust(3/4): The local PNs are about to be exhausted. PN indicates the packet number. * Peer PN exhaust(3/4): The peer PNs are about to be exhausted. (The SAK switchover triggered by non-keyserver configuration changes is reported to the key server through PN exhaustion. In this case, the SAK switchover cause displayed on the key server is that the peer PN is about to be exhausted.). * MI changed: The member identifier is changed. * Configure include-sci or replay-window: The configuration data packet contains SCI or the replay protection window size is changed. * Configure SAK life time: configures the SAK timeout period. * KeyServer start SAK switch: SAK switchover triggered by the key server. * Peer start SAK switch: SAK switchover triggered by the peer. * Configure cipher suite: configures the encryption algorithm for MACsec data packets. * Configure cryptographic algorithm: configures the MKA key generation algorithm. * Configure capability: configures the MACsec capability value. |
| Rx MKA packets | Number of received MKA packets. |
| Tx MKA packets | Number of sent MKA packets. |
| Old SAK status | Last SAK status. This field has the following values:   * Rx: SAK receiving is enabled. * Tx: SAK transmitting is enabled. * Rx & Tx: Both SAK receiving and SAK transmitting are enabled. * N/A: The SAK is invalid.   After the new SAK takes effect during SAK switching, the status of the original SAK changes to N/A, indicating that the original SAK becomes invalid. |
| Old SAK AN | Previous SAK association number. |
| Old SAK KI | Previous SAK identifier. |
| Old SAK KN | Previous SAK number. |
| Priority | Key server priority. |
| Capability | Capability value. |
| Rx-SCI | Received SCI. |
| Drop MKA packets | Number of discarded MKA packets. |
| Wrong CKN num | Number of packets failing the CKN check. |
| Wrong ICV num | Number of packets failing the ICV check. |
| CKN | To configure this parameter, run the mka cak-mode static command.  A CKN is a hexadecimal string consisting of between 2 and 64 characters (must be an even number of characters). It is recommended that you configure a CKN with the maximum length. If the length of the configured CKN is shorter than the maximum length, the device adds 0s at the end of the CKN to make it reach the maximum length. The CKN in this command output contains added 0s. For example, if the configured CKN is abc123, the displayed CKN is abc1230000000000000000000000000000000000000000000000000000000000. |