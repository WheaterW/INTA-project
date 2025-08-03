reset hwtacacs-server accounting-stop-packet
============================================

reset hwtacacs-server accounting-stop-packet

Function
--------



The **reset hwtacacs-server accounting-stop-packet** command clears statistics about HWTACACS accounting-stop packets.




Format
------

**reset hwtacacs-server accounting-stop-packet** { **all** | **ip** *ip-address* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Clears statistics about all accounting-stop packets. | - |
| **ip** *ip-address* | Clears statistics about accounting-stop packets with the specified IP address. | The value is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

This command can clear statistics on the remaining buffer information of HWTACACS accounting-stop packets. The deleted statistics cannot be restored.


Example
-------

# Clear statistics on the remaining buffer information of all HWTACACS accounting-stop packets.
```
<HUAWEI> reset hwtacacs-server accounting-stop-packet all

```