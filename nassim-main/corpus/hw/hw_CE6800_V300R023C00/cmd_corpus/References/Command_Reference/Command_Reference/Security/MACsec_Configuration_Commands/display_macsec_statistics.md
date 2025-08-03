display macsec statistics
=========================

display macsec statistics

Function
--------



The **display macsec statistics** command displays statistics about data packets protected by MACsec.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display macsec statistics interface** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the number of an interface. | - |
| **interface** | Specifies an interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays statistics about data packets protected by MACsec, facilitating fault locating in routine maintenance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about data packets protected by MACsec.
```
<HUAWEI> display macsec statistics interface 100GE 1/0/1
Interface 100GE1/0/1:                                                                                                               
  Input:                                                                                                                            
    Valid packets  : 00019                                                                                                          
    Decrypted bytes: 000401500                                                                                                      
    Errors:                                                                                                                         
      Replay check fail    : 0                                                                                                      
      ICV check fail       : 0                                                                                                      
      Notag                : 0                                                                                                      
      Badtag               : 0 
      Can't find SA        : 0                                                                                                   
  Output:                                                                                                                           
    Protected packets: 00037                                                                                                        
    Encrypted bytes  : 02786

```

**Table 1** Description of the **display macsec statistics** command output
| Item | Description |
| --- | --- |
| Interface | Statistics about data packets protected by MACsec on an interface. |
| Valid packets | Number of valid packets protected by MACsec. |
| Decrypted bytes | Number of decrypted bytes. |
| Replay check fail | Number of packets failing the replay check. |
| ICV check fail | Number of packets failing the ICV check. |
| Notag | Number of discarded packets without MACsec tags. |
| Badtag | Number of discarded packets with error MACsec tags. |
| Can't find SA | Number of packets that are discarded because no SA is matched. |
| Protected packets | Number of sent packets protected by MACsec. |
| Encrypted bytes | Number of encrypted bytes. |
| Input | Statistics about received packets protected by MACsec. |
| Errors | Number of error packets protected by MACsec. |
| Output | Statistics about sent packets protected by MACsec. |