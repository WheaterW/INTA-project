c-bsr hash-length(VPN instance PIM view/PIM view of a public network instance)
==============================================================================

c-bsr hash-length(VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **c-bsr hash-length** command sets a global hash mask length for candidate-bootstrap routers (C-BSRs).

The **undo c-bsr hash-length** command restores the default value.



By default, the global hash mask length of C-BSRs is 30.


Format
------

**c-bsr hash-length** *hashLengthValue*

**undo c-bsr hash-length**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hashLengthValue* | Specifies a global hash mask length for C-BSRs. | The value is an integer ranging from 0 to 32. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a PIM-SM network where a rendezvous point (RP) is dynamically elected using the BSR mechanism, each candidate-rendezvous point (C-RP) sends to the BSR an Advertisement message carrying the C-RP address, range of multicast groups that the C-RP serves, and C-RP priority. Then, the BSR collects all those information and the BSR hash mask length as an RP-set, encapsulates the RP-set into a bootstrap message, and advertises the message to all Routers on the network. All Routers use the RP-set and follow the same RP election rules to elect an RP for a specific group.The RP election rules are as follows:

* The C-RP with the highest priority wins (a larger priority value indicates a lower priority).
* If the C-RPs have the same priority, the hash function is started. The C-RP with the largest calculated value is elected as the RP.
* If all C-RPs have the same priority and calculated hash value, the C-RP with the largest address wins the election.To configure a global hash mask length for C-BSRs, run the c-bsr hash-length command.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the c-bsr hash-length command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, set the global hash mask length to 16 for C-BSRs.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] c-bsr hash-length 16

```