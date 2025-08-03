Related Concepts of Keychains
=============================

A keychain is a chain of keys, known as a series of encryption and authentication rules.

#### Three Elements of a Key

Each key in a keychain consists of three elements:

* Authentication algorithm: supports MD5, SHA-1, HMAC-MD5, HMAC-SHA1-12, HMAC-SHA1-20, HMAC-SHA-256, SHA-256, SM3, HMAC-SHA-384, and HMAC-SHA-512.![](public_sys-resources/note_3.0-en-us.png) 
  
  MD5, HMAC-MD5, and SHA-1 algorithms are not recommended since they are less secure.
* Authentication key string: a character string used for encryption. The same clear text can be encrypted using different key strings to obtain different ciphertexts. The same ciphertext can be obtained only when the same key string is used for encryption.
* Lifetime: indicates the time interval within which a key is valid. If the lifetime of a key expires, the key is replaced by another active key.

![](public_sys-resources/note_3.0-en-us.png) 

When an authentication algorithm and an authentication key string are used for encryption calculation of packets, a string of fixed-length message authentication code (MAC) is generated.



#### Key ID and Category

To better manage keys collectively on a device, the keychain defines key IDs to facilitate differentiation. Keys on the device are classified into two types: the send key and accept key.

* Send key: used by the device to encrypt packets before sending them.
* Accept key: used by the device to decrypt received packets.

![](public_sys-resources/note_3.0-en-us.png) 

* The send key of the local device must be the same as the accept key of the peer device. In this way, the peer device can use the same algorithm and key string as those of the local device to decrypt the received encrypted packets.
* The send key and accept key on a device can be the same or different. In a certain period of time, the key used for encrypting the packets to be sent must be within its send lifetime, and that used for decrypting received packets must be within its accept lifetime.


#### Lifetime of a Key

To better control the use of keys on a device, the keychain defines the key lifetime, which determines the currently valid key, and its validity period and successor.

The lifetime of a key indicates the time interval within which the key is considered valid.

* A key within the send lifetime is the currently valid send key.
* A key in the accept lifetime is the currently valid accept key.

Both the send lifetime and accept lifetime can be defined in either of the following time modes:

* Absolute time mode: A key in a keychain is valid only within a specified time interval, for example, 12:00-18:00 on December 10, 2019.
* Periodic time mode: As shown in [Table 1](#EN-US_CONCEPT_0000001130622922__table199881922164318), a key in a keychain becomes valid periodically within a specified time interval.
  
  **Table 1** Periodic time mode
  | Period | Time Interval |
  | --- | --- |
  | Daily | Specified time interval every day, for example, 12:00-18:00. |
  | Weekly | Specified days every week, for example, Monday, Wednesday, Friday, and Sunday. |
  | Monthly | Specified dates every month, for example, from the third day to the eighth day. |
  | Yearly | Specified months every year, for example, from June to September. |

![](public_sys-resources/note_3.0-en-us.png) 

* Default send key: If no active send key is available within a specified time interval, packets sent by the device cannot be encrypted and security authentication services cannot be provided for applications. To prevent this, the device supports configuration of the default send key, which is valid when no other active send keys are available within a specified time interval.
* Acceptance tolerance: When the send key of the peer device is updated, the accept key of the local device must also be updated accordingly. Otherwise, the local device cannot decrypt the received packets and will therefore discard them. When the keys of the two ends are updated at the same time, due to a time difference in packet transmission, the packets encrypted by the old key from the peer end may arrive at the local end although the local end has started to use a key. In addition, the clocks of the two ends on the network may be asynchronous. To address this, the device supports configuration of the acceptance tolerance to ensure a smooth transition during key rollover. The tolerance limit takes effect only on accept keys. After the tolerance limit is configured, the actual lifetime of an accept key equals its original lifetime plus two tolerance limits, one for the start time and the other for the end time of the accept key.


#### Key Set

A keychain is a set of keys of the same type.

In most cases, the same type refers to the same lifetime mode. For example, a key that has a lifetime of specified months in every year is of a different type from a key that has a lifetime of specified dates in every month. If these two keys are placed in one keychain, time-based key rollover cannot be performed.

Based on service requirements, the device supports multiple keychains for applications to flexibly choose from.

For example, as shown in [Table 2](#EN-US_CONCEPT_0000001130622922__table12933217131715), Key1 and Key3 are of the same type and can be placed in KeychainA; Key2 and Key4 are of the same type and can be placed in KeychainB; Key5 can only be placed independently in KeychainC; and Key6 can only be placed independently in KeychainD.

**Table 2** Example of key sets
| Key | Authentication Algorithm | Authentication Key String | Lifetime | Key Set |
| --- | --- | --- | --- | --- |
| Key1 | HMAC-SHA1-20 | AbCdEfGh | 12:00-15:00 on December 10, 2019 | KeychainA |
| Key2 | HMAC-SHA1-20 | HgFeDcBa | Every Monday, Wednesday, Friday, and Sunday | KeychainB |
| Key3 | HMAC-SHA-256 | AcEgHfDb | 15:00-18:00 on December 10, 2019 | KeychainA |
| Key4 | HMAC-SHA-256 | HeBgDfCa | Every Tuesday, Thursday, and Saturday | KeychainB |
| Key5 | HMAC-SHA-256 | DhAgBfCe | The third day to the eighth day of every month | KeychainC |
| Key6 | HMAC-SHA-256 | EaHgBcFd | June to September every year | KeychainD |