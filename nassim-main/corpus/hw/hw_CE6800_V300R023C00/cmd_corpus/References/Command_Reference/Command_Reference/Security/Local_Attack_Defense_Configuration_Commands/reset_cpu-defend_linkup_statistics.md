reset cpu-defend linkup statistics
==================================

reset cpu-defend linkup statistics

Function
--------



The **reset cpu-defend linkup statistics** command clears statistics about linkup.




Format
------

**reset cpu-defend linkup statistics** [ **packet-type** *packet-type* ] **slot** *slot-id*

**reset cpu-defend linkup statistics** [ **packet-type** *packet-type* ] **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet-type** *packet-type* | Displays the configuration of rate limiting for packets of a specified type. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ: The options are as follows:   * bgp * bgp4plus * ftp * isis * m-lag * m-lag-sync * ospf * ospfv3 * ssh * telnet * tftp  For the CE6885-LL (low latency mode): The options are as follows:   * bgp * ftp * isis * m-lag * m-lag-sync * ospf * ssh * telnet * tftp |
| **slot** *slot-id* | Displays the configuration of protocol association sessions in a specified slot. | The value must be set according to the device configuration. |
| **all** | Indicates all boards. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To collect statistics about linkup within a period of time, you can run the **reset cpu-defend linkup statistics** command to clear the existing statistics, wait for a period of time, and then run the **display cpu-defend linkup statistics** command to view statistics about linkup.


Example
-------

# Clear statistics about linkup on all devices.
```
<HUAWEI> reset cpu-defend linkup statistics packet-type telnet all

```