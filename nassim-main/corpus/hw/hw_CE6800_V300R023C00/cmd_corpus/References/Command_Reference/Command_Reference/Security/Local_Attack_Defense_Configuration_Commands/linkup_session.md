linkup session
==============

linkup session

Function
--------



The **linkup session anti-attack ratio-threshold** command sets the percentage threshold for triggering punishment by protocol association.

The **undo linkup session anti-attack ratio-threshold** command restores the default percentage threshold for triggering punishment by protocol association.



By default, the percentage threshold for triggering punishment is 50%.


Format
------

**linkup session anti-attack ratio-threshold** *rate-value-percent*

**undo linkup session anti-attack ratio-threshold**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **anti-attack** | Indicates attack defense. | - |
| **ratio-threshold** *rate-value-percent* | Specifies the percentage threshold for triggering punishment by protocol association. The default value is 50. | The value is an integer in the range from 1 to 100. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The CAR value for protocol association is shared by sessions of the same protocol type. When the number of packets of a session increases greatly or the device receives a large number of attack flows matching this session, other sessions of the same protocol may be discarded because the packet rate exceeds the rate limit, data transmission is affected, and services are interrupted. In this case, you can run this command to set the percentage threshold for triggering punishment to ensure that services related to these protocol packets can run properly when attacks occur. The protocol association function triggers penalty detection when the packet rate of a protocol exceeds 80% of the protocol-associated CAR. If the packet rate of a single session exceeds the percentage threshold of the total rate of sessions of the same protocol, the rate of the session is degraded to the CPCAR, which is limited by the CAR value of CPCAR. After that, protocol association is restored periodically, which is limited by the CAR value for protocol association. The percentage threshold for triggering linkup session penalty can be set as required. Only one session can be established for M-LAG and M-LAG-SYNC, and the protocol association penalty function does not take effect. The protocol association penalty function takes effect only when at least two sessions are established for other protocols. The punished session is restored to protocol association after 5 minutes. If the attack persists, the session is punished again.




Example
-------

# In the attack defense policy named test, set the percentage threshold for triggering punishment by protocol association to 20%.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] linkup session anti-attack ratio-threshold 20

```