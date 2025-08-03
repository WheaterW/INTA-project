macsec mode
===========

macsec mode

Function
--------



The **macsec mode** command configures the MACsec encryption mode.

The **undo macsec mode** command restores the default MACsec encryption mode.



By default, the MACsec mode is normal.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**macsec mode** { **none** | **normal** | **integrity-only** }

**undo macsec mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **none** | Indicates that neither data encryption nor integrity check is performed. | - |
| **normal** | Indicates that both data encryption and integrity check are performed. | - |
| **integrity-only** | Indicates that integrity check is performed and data encryption is not performed. | - |



Views
-----

mac security profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When MACsec is configured on interfaces to protect transmitted data packets, you need to set the encryption mode:

* If the encryption mode of one end is set to none, the encryption mode of the other end must be set to none.
* If the encryption mode of one end is set to normal, the encryption mode of the other end must be set to normal or integrity-only.
* If the encryption mode of one end is set to integrity-only, the encryption mode of the other end must be set to normal or integrity-only.When MACsec is configured on both ends to ensure secure communication, the encryption mode configured on the key server is used.Data encryption and integrity check:
* Data encryption: The sender encrypts data packets and transmits the encrypted packets over a LAN link. The receiver decrypts received packets and processes the decrypted packets.
* Integrity check: The receiver checks the integrity of received packets to determine whether the packets are tampered with. The sender calculates the Integrity Check Value (ICV) based on the data packet and encryption algorithm and adds it to the end of the packet. After receiving the packet, the receiver calculates the ICV based on the packet excluding the ICV and the same encryption algorithm, and compares the obtained ICV with the ICV in the packet. If they are the same, the packet is considered complete and passes the check. Otherwise, the packet is discarded.

**Precautions**

* When you configure MACsec on a network where data traffic is transmitted, set the encryption mode on both ends to none to shorten the traffic interruption time. Then run the **display mka interface** command to check MKA session information on both ends. When the MKA status is displayed as SUCCEEDED, change the encryption mode on both ends to normal.
* When the MACsec mode is set to none, data encryption and integrity check are not performed. To ensure data security, you are advised to set this parameter to normal.
* When the MACsec mode is set to none, changes of configurations such as Keyserver Priority, confidentiality-offset, timer sak-life, include-sci and replay-window do not trigger MACsec renegotiation.

Example
-------

# Set the encryption mode to normal in the MACsec profile named test.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test] macsec mode normal

```