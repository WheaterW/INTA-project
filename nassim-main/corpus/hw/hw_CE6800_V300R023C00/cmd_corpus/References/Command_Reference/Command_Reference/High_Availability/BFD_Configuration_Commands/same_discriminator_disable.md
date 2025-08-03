same discriminator disable
==========================

same discriminator disable

Function
--------



The **same discriminator disable** command configures the device not to use the same local and remote discriminators of multicast BFD.

The **undo same discriminator disable** command cancels the configuration.



By default, local and remote discriminators of multicast BFD can use the same value.


Format
------

**same discriminator disable**

**undo same discriminator disable**


Parameters
----------

None

Views
-----

BFD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In a multicast BFD scenario, if the local and remote discriminators of a BFD session are the same, multicast packets may be incorrectly received in the Layer 2 broadcast domain. To resolve this problem, run the same discriminator disable command to disallow the local and remote discriminators of a multicast BFD session to be set to the same value.


Example
-------

# Configure the device not to use the same local and remote discriminators.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] same discriminator disable

```