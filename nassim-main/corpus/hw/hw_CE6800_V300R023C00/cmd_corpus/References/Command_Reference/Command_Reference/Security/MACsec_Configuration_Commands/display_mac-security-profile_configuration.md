display mac-security-profile configuration
==========================================

display mac-security-profile configuration

Function
--------



The **display mac-security-profile configuration** command displays the configuration of a MACsec profile.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display mac-security-profile configuration** [ **name** *profile-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *profile-name* | Specifies the name of a MACsec profile. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

This command displays the configuration of a MACsec profile.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all MACsec profiles configured on the device.
```
<HUAWEI> display mac-security-profile configuration
------------------------------------------------------------------------------- 
  ID   Macsec-profile name                                                 
------------------------------------------------------------------------------- 
  0      test                                            
  1      p1                                                                                                                            
------------------------------------------------------------------------------- 
 Total 2, printed 2

```

# Display the configuration of the profile named test.
```
<HUAWEI> display mac-security-profile configuration name test
  Profile Name                           : test         
  MKA life time(s)                       : 6                                                                                        
  SAK life time(s)                       : 3600                                                                                     
  MACsec mode                            : none                                                                                     
  MACsec replay protection               : YES                                                                                      
  MACsec replay-window(frame(s))         : 0                                                                                        
  MACsec confidentiality-offset(byte(s)) : 0                                                                                        
  MACsec include SCI                     : YES                                                                                      
  MACsec cipher suite                    : -                                                                                        
  MKA cryptographic algorithm            : AES-CMAC-128                                                                             
  Key server priority                    : 16
  MACsec capability                      : 3

```

**Table 1** Description of the **display mac-security-profile configuration** command output
| Item | Description |
| --- | --- |
| ID | Profile ID. |
| Macsec-profile name | Name of a MACsec profile. |
| Profile Name | Profile name. |
| MKA life time(s) | MKA session timeout period. |
| MKA cryptographic algorithm | MKA key generation algorithm. |
| SAK life time(s) | SAK timeout period. |
| MACsec mode | MACsec encryption mode. |
| MACsec cipher suite | Encryption algorithm for MACsec data packets. |
| MACsec replay-window(frame(s)) | Replay protection window size. |
| MACsec confidentiality-offset(byte(s)) | MACsec encryption offset. |
| MACsec replay protection | Replay protection window. |
| MACsec include SCI | Whether data packets contain an SCI. |
| MACsec capability | MACsec capability value. |
| Key server priority | MKA key server priority. |