reset radius-server accounting-stop-packet
==========================================

reset radius-server accounting-stop-packet

Function
--------



The **reset radius-server accounting-stop-packet** command clears statistics on the remaining buffer information of RADIUS accounting-stop packets.




Format
------

**reset radius-server accounting-stop-packet** { **all** | **ip** *ip-address* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Clears statistics on the remaining buffer information of RADIUS accounting-stop packets. | - |
| **ip** *ip-address* | Clears statistics on the remaining buffer information of RADIUS accounting-stop packets with the specified IPv4 address. | The value of ipv4-address is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

This command can clear statistics on the remaining buffer information of RADIUS accounting-stop packets. The deleted statistics cannot be restored.


Example
-------

# Clear statistics on the remaining buffer information of all RADIUS accounting-stop packets.
```
<HUAWEI> reset radius-server accounting-stop-packet all

```