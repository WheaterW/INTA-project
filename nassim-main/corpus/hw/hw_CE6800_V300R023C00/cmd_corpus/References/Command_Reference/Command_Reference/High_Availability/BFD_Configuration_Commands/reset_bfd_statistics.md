reset bfd statistics
====================

reset bfd statistics

Function
--------



The **reset bfd statistics** command clears statistics about packets received and sent for BFD sessions.




Format
------

**reset bfd statistics** { **all** | **discriminator** *discr-value* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Clears statistics about packets received and sent for all BFD sessions. | - |
| **discriminator** *discr-value* | Clears statistics about packets received and sent for the BFD sessions with a specified discriminator. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To clear statistics about packets received and sent for the BFD sessions, run **reset bfd statistics** command with one of the following parameters:

* If all is configured, statistics about packets received and sent for all BFD sessions are cleared.
* If discriminator discr-value is configured, statistics about packets received and sent for the BFD sessions with a specified discriminator are cleared.

**Configuration Impact**

After clearing statistics about packets received and sent for BFD sessions, you can run the **display bfd statistics** command to view statistics about packets received and sent for BFD sessions within a specified period.

**Precautions**

Statistics about packets received and sent for BFD sessions cannot be restored after being cleared. Exercise caution when running the **reset bfd statistics** command.


Example
-------

# Clear statistics about packets received and sent for BFD sessions.
```
<HUAWEI> reset bfd statistics all

```