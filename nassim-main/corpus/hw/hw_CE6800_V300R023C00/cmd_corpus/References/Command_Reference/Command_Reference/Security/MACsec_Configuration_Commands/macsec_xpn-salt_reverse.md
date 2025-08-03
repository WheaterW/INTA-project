macsec xpn-salt reverse
=======================

macsec xpn-salt reverse

Function
--------



The **macsec xpn-salt reverse** command enables MACsec to convert the byte order of XPN salt values.

The **undo macsec xpn-salt reverse** command disables MACsec from converting the byte order of XPN salt values.



By default, the byte order of XPN salt values is not converted.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**macsec xpn-salt reverse**

**undo macsec xpn-salt reverse**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When network devices of different brands implement the MACSec function, the salt value delivered in xpn mode uses the network sequence or host sequence. You can configure this command to be compatible with different implementation modes.

1. When CE V300 and LSW V600 are interconnected, the configuration status of macsec xpn-salt reverse must be the same.
2. When the device connects to a device running an earlier version (CE V300R23C00 or earlier than LSW V600R23C00), the macsec xpn-salt reverse command is needed.
3. When the device is connected to a CE V200 device, the macsec xpn-salt reverse command is needed.
4. When the device is connected to the LSW V200, the macsec xpn-salt reverse command is not needed.
5. When the device is connected to a network device of another brand, the macsec xpn-salt reverse command is not needed.

Example
-------

# Enable salt byte order conversion in XPN mode for the MACsec module.
```
<HUAWEI> system-view
[~HUAWEI] macsec xpn-salt reverse

```

# Disable salt byte order conversion in XPN mode for the MACsec module.
```
<HUAWEI> system-view
[~HUAWEI] undo macsec xpn-salt reverse

```