peer sa-cache-maximum
=====================

peer sa-cache-maximum

Function
--------



The **peer sa-cache-maximum** command sets a maximum cache number for (S, G) entries learned from a specified Multicast Source Discovery Protocol (MSDP) peer.

The **undo peer sa-cache-maximum** command restores the default configuration.



By default, a maximum of 8192 (S, G) entries can be cached for a specified MSDP peer.


Format
------

**peer** *peer-address* **sa-cache-maximum** *sa-limit*

**undo peer** *peer-address* **sa-cache-maximum**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of an MSDP peer. | The value is in dotted decimal notation. |
| *sa-limit* | Specifies the maximum number of (S, G) entries that can be cached. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To protect a network against deny of service (DoS) attacks, run the peer sa-cache-maximum command to set a maximum cache number for (S, G) entries learned from an MSDP peer. Running this command for all MSDP peers is recommended.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.MSDP peers have been configured, and the SA cache function has been enabled.

**Configuration Impact**

The total number of (S, G) entries that can be cached in the SA cache is limited by the specifications of the SA cache.For (S, G) entries learned from a specific MSDP peer:-If a maximum cache number is not set or is set to a value larger than the default value, a maximum number of the default value (S, G) entries can be cached for this peer.

* If the specified maximum cache number is smaller than the default value, the specified value takes effect. Excess (S, G) entries are not cached or advertised to PIM-SM but can be forwarded through SA messages.

Example
-------

# In the public network instance, specify 100 as the maximum cache number for (S, G) entries learned from the MSDP peer 10.10.7.6.
```
<HUAWEI> system-view
[~HUAWEI] interface loopback1
[*HUAWEI-LoopBack1] quit
[*HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 10.10.7.6 connect-interface LoopBack 1
[*HUAWEI-msdp] peer 10.10.7.6 sa-cache-maximum 100

```