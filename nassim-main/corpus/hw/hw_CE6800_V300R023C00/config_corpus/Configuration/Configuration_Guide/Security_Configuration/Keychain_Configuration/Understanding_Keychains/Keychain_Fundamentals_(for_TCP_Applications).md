Keychain Fundamentals (for TCP Applications)
============================================

The fundamentals of keychain authentication for TCP applications are similar to those for non-TCP applications. The only difference is that the TCP Enhanced Authentication Option is added for TCP applications.

#### TCP Enhanced Authentication Option

[Figure 1](#EN-US_CONCEPT_0000001130782710__fig198037195582) depicts the format of the TCP Enhanced Authentication Option. The TCP packet header carries this option to provide authentication protection specifically for TCP connections.

**Figure 1** Format of TCP Enhanced Authentication Option  
![](figure/en-us_image_0000001176662479.png)

* Kind: 8 bits, identifies the TCP Enhanced Authentication Option. This value is assigned by IANA.
* Length: 8 bits, specifies the length of the TCP Enhanced Authentication Option, in octets.
* T: 1 bit, specifies whether the TCP Enhanced Authentication Option is included in the TCP header for the purpose of TCP enhanced authentication calculation. A value of 0 indicates that the TCP Enhanced Authentication Option is included. The default value is 0.
* K: 1 bit, reserved for future enhancement. The current value is 0.
* Alg ID: 6 bits, identifies the TCP enhanced authentication algorithm.
* Res: 2 bits, reserved for future use. The current value is 0.
* Key ID: 6 bits, identifies the key for keychain authentication.
* Authentication Data: The length is variable. It contains at least the result of TCP enhanced authentication calculation.

IANA does not define the values of the Kind and Alg ID fields in a unified manner. Therefore, different vendors use different values. To enable devices of different vendors to communicate, the keychain supports configuration of the TCP Kind and TCP Alg ID fields.


#### Encryption Process

**Figure 2** Encryption process for a TCP application using keychain authentication  
![](figure/en-us_image_0000001130622928.png "Click to enlarge")

#### Decryption Process

**Figure 3** Decryption process for a TCP application using keychain authentication  
![](figure/en-us_image_0000001176662475.png "Click to enlarge")