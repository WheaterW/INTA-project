mka timer mka-life
==================

mka timer mka-life

Function
--------



The **mka timer mka-life** command sets the MKA session timeout period.

The **undo mka timer mka-life** command restores the default MKA session timeout period.



By default, the MKA session timeout period is 6 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mka timer mka-life** *life-time*

**undo mka timer mka-life**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *life-time* | Specifies the MKA session timeout period. | The value is an integer that ranges from 6 to 60, in seconds. The default value is 6 seconds. |



Views
-----

mac security profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When MACsec is used for secure communication, devices at both ends perform MKA session negotiation to establish a secure channel. After a secure channel is established, the two devices exchange MKA protocol packets to ensure that the session is alive. The MKA protocol defines an MKA session keepalive timer that specifies the timeout period of an MKA session. The local device starts the timer after receiving MKA protocol packets from the remote device.

* If the local device receives subsequent MKA protocol packets within the timeout period, it restarts the timer.
* If the local device does not receive subsequent MKA protocol packets within the timeout period, it considers the session insecure, deletes the session, and performs MKA session negotiation again.

Example
-------

# Set the MKA session timeout period to 10 seconds in the MACsec profile named test.
```
<HUAWEI> system-view
[~HUAWEI] mac-security-profile name test
[*HUAWEI-macsec-profile-test] mka timer mka-life 10

```