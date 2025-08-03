macsec replay-window
====================

macsec replay-window

Function
--------



The **macsec replay-window** command configures the MACsec replay protection window size.

The **undo macsec replay-window** command restores the default MACsec replay protection window size.



By default, the replay protection window size is 0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**macsec replay-window** *window-size*

**undo macsec replay-window**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *window-size* | Specifies the replay protection window size. | The value is an integer that ranges from 0 to 4294967295.  When the encryption algorithm for MACsec data packets is set to GCM-AES-XPN-128 or GCM-AES-XPN-256, the maximum MACsec replay protection window size is 1073741823. |



Views
-----

mac security profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent malicious users from repeatedly sending captured data packets, the receiver discards duplicate or out-of-order data packets by default. In some cases, however, data packets are reordered during transmission because their sending priorities are different. As a result, the data packets are out of order when they reach the receiver. To ensure that these out-of-order data packets can be received normally, configure the replay protection window size.

**Precautions**

Assume that the replay protection window size configured on the device is a. If a packet with the sequence number x is received, the sequence number of the next packet that is allowed to be received must be greater than or equal to (x + 1 - a). Set an appropriate replay protection window size based on the data packet forwarding path on the network. If data packets may be forwarded multiple times, there is a high probability that many of them become out of order. To address this issue, you are advised to increase the replay protection window size. Otherwise, decrease the window size.


Example
-------

# Set the replay protection window size to 100 in the MACsec profile named test.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test] macsec replay-window 100

```