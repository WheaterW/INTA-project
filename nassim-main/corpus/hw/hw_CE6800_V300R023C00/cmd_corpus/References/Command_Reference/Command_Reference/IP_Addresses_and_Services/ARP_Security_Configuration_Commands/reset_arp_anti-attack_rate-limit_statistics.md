reset arp anti-attack rate-limit statistics
===========================================

reset arp anti-attack rate-limit statistics

Function
--------



The **reset arp anti-attack rate-limit statistics** command clears statistics about ARP packets discarded due to rate limiting on an interface.




Format
------

**reset arp anti-attack rate-limit statistics**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view statistics about ARP packets discarded due to rate limiting on an interface in a specified period, run the **reset arp anti-attack rate-limit statistics** command to clear the existing statistics and then run the display arp anti-attack rate-limit statistics command.

**Precautions**

The deleted packet statistics cannot be restored.


Example
-------

# Clear the statistics on ARP packets.
```
<HUAWEI> reset arp anti-attack rate-limit statistics

```