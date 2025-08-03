peer request-sa-enable
======================

peer request-sa-enable

Function
--------



The **peer request-sa-enable** command enables the Router to send a source active (SA) Request message to a specified Multicast Source Discovery Protocol (MSDP) peer immediately after receiving a new Join message.

The **undo peer request-sa-enable** command restores the default configuration.



By default, when receiving a new Join message, the Router does not send an SA Request messages to an MSDP peer immediately but waits to receive the next SA message from the peer.


Format
------

**peer** *peer-address* **request-sa-enable**

**undo peer** *peer-address* **request-sa-enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of an MSDP peer. | The value is in dotted decimal notation. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a PIM-SM domain, after receiving a new Join message, the rendezvous point (RP) creates a (\*, G) entry and searches for a matching (S, G) entry. If no matching (S, G) entry is found and the SA cache function is disabled, the RP cannot immediately generate a multicast route for this user, so that the RP waits for the next SA message from the remote MSDP peer to obtain corresponding (S, G) information.Generally, the interval for an MSDP peer to send SA messages is set to a large value to reduce traffic load in the PIM-SM domain. This, however, will cause a long delay in joining the source's SPT. To minimize the delay, run the peer request-sa-enable command to enable the local RP to immediately send an SA Request message immediately after receiving a new Join message. In addition, enable the SA cache function on the remote MSDP peer. Then, if the local entries and SA cache do not contain a matching (S, G) entry for a new Join message, the local RP immediately sends an SA Request message to the remote MSDP peer instead of waiting to receive the next SA message from the peer.

**Prerequisites**

SA cache has been disabled on the local router but enabled on the MSDP peer specified by peer-address. This prerequisite enables the local router to immediately send an SA Request message and get a Response message.


Example
-------

# In the public network instance, enable the Router to send an SA Request message to the MSDP peer 10.10.7.6 immediately after receiving a new Join message.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback1
[*HUAWEI-LoopBack1] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 10.10.7.6 connect-interface LoopBack 1
[*HUAWEI-msdp] peer 10.10.7.6 request-sa-enable

```