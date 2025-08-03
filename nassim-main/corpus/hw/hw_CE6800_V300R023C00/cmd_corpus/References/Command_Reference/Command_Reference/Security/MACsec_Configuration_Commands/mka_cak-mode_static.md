mka cak-mode static
===================

mka cak-mode static

Function
--------



The **mka cak-mode static** command configures a static Connectivity Association Key Name (CKN) and a Connectivity Association Key (CAK).

The **undo mka cak-mode static** command deletes the configured static CKN and CAK.



By default, no static CKN or CAK is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mka cak-mode static ckn** *string-name* **cak** *string-key*

**undo mka cak-mode static ckn** *string-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cak** *string-key* | Indicates the key associated with secure channel. | The value is a hexadecimal string consisting of between 32 and 64 characters (must be an even number of characters). It must contain at least one digit (0 to 9) and one case-insensitive letter (A to F). The letters are case insensitive and different from ckn. The value can also be a string of 148 to 188 characters in ciphertext, the start and end characters of the ciphertext must be set to %@ %# or %+ %#, and the ciphertext is saved in %+ %# format.  The maximum length is recommended. If the configured CAK is shorter than the maximum length, the device adds 0s to the end of the CAK to reach the maximum length. If the CAKs configured on both ends are the same from the first character to the last non-zero character, the two CAKs are considered the same. |
| **ckn** *string-name* | Specifies a CAK. | The value is a hexadecimal string consisting of between 2 and 64 characters (must be an even number of characters). It must contain at least one digit (0 to 9) and one case-insensitive letter (A to F).  It is recommended that you configure a CKN with the maximum length. If the length of the configured CKN is shorter than the maximum length, the device adds 0s at the end of the CKN to make it reach the maximum length. When two CKNs on two devices are the same from the first character to the last non-zero character, the two CKNs are considered identical. |



Views
-----

100GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The key used for encrypting and decrypting data packets using MACsec is generated and distributed by the key server based on the encryption algorithm defined in the MKA protocol and the configured static CAK. Therefore, you need to configure a CKN and a corresponding CAK on the interface in advance.

**Precautions**

This command is supported only on Layer 2 interfaces.The local and remote interfaces must have the same static CKN and CAK. Otherwise, the two interfaces cannot negotiate an MKA session.After the **undo mka cak-mode static** command is run to delete the configured static CKN and CAK, the original CKN and CAK still take effect before a new MKA session is successfully negotiated.After the configured static CKN and CAK are deleted or modified, the modified configuration in the profile bound to the interface takes effect only after renegotiation succeeds.After this command is configured on the local device, the generated ciphertext cannot be directly copied to the peer device for delivery. Otherwise, the command fails to be delivered to the peer device.


Example
-------

# Set the CKN to 0123456789abcdef987654321fbcad9632587410abcdef7412589630fedabc53 and the CAK to 9af0131568d4567cae202d34789ebcaf on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] mka cak-mode static ckn 0123456789abcdef987654321fbcad9632587410abcdef7412589630fedabc53 cak 9af0131568d4567cae202d34789ebcaf

```