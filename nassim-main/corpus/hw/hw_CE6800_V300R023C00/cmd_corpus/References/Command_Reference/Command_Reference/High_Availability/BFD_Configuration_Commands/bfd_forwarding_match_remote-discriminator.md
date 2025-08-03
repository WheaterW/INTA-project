bfd forwarding match remote-discriminator
=========================================

bfd forwarding match remote-discriminator

Function
--------



The **bfd forwarding match remote-discriminator** command matches the local BFD discriminator configured on the peer end.

The **undo bfd forwarding match remote-discriminator** command disables a device from matching the local BFD discriminator configured on the peer.



By default, no remote discriminator is configured for a BFD session.


Format
------

**bfd forwarding match remote-discriminator** *discriminator-value* [ **to** *discriminator-value* ]

**undo bfd forwarding match remote-discriminator** *discriminator-value* [ **to** *discriminator-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *discriminator-value* | Specifies a minimum remote discriminator for a BFD session. | The value is an integer ranging from 1 to 16384. |
| **to** *discriminator-value* | Specifies a maximum remote discriminator for a BFD session. | The value is an integer ranging from 1 to 16384. |



Views
-----

BFD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a BFD for M-LAG scenario where two devices belong to an M-LAG group, after a one-arm BFD session is set up on the peer device, run the bfd forwarding match remote-discriminator command on the local device to configure a remote discriminator (same as the local discriminator of the BFD session on the peer). This allows the local device to forward BFD packets carrying the remote discriminator to the peer.


Example
-------

# Configure a remote discriminator for a BFD session.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] bfd forwarding match remote-discriminator 11

```