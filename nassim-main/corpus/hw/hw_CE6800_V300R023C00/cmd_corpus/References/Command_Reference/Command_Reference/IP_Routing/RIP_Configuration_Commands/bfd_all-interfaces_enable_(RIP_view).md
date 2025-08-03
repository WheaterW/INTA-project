bfd all-interfaces enable (RIP view)
====================================

bfd all-interfaces enable (RIP view)

Function
--------



The **bfd all-interfaces enable** command enables BFD on all the interfaces in a RIP process.

The **undo bfd all-interfaces enable** command disables BFD from all the interfaces in a RIP process.



By default, BFD is disabled in a RIP process.


Format
------

**bfd all-interfaces enable**

**undo bfd all-interfaces enable**


Parameters
----------

None

Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

With the development of technologies, voice, video, and other on-demand services are widely used. These services are sensitive to packet loss and delay. RIP detects neighbor faults through the aging timer. Such fault detection takes a long time. As a result, a large amount of data is lost, and carrier-class network reliability requirements cannot be met. BFD can solve this problem and improve link reliability. You can run the **bfd all-interfaces enable** command to enable BFD for RIP to quickly detect link faults and implement fast network convergence.

**Prerequisites**

Before running this command, ensure the following operations have been performed:

* Global BFD has been enabled using the **bfd** command.
* A RIP process has been created and the RIP view has been displayed using the **rip** command.

**Precautions**

The BFD priority set using the **rip bfd enable** command in the interface view is higher than the one set using the **bfd all-interfaces enable** command.If the **rip bfd block** command has been run on a RIP-capable interface, the **bfd all-interfaces enable** command does not take effect. In this situation, run the **rip bfd enable** command to enable BFD.


Example
-------

# Enable BFD on all interfaces in a RIP process.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] quit
[*HUAWEI] rip
[*HUAWEI-rip-1] bfd all-interfaces enable

```