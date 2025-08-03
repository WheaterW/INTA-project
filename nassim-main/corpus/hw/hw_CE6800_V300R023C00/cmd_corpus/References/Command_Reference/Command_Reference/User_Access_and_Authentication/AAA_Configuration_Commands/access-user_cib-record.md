access-user cib-record
======================

access-user cib-record

Function
--------



The **access-user cib-record cache-record-num cache-aging-time** command sets the maximum number of CIB cache entries that can be recorded and the aging time.

The **undo access-user cib-record cache-record-num cache-aging-time** command restores the default maximum number of CIB cache entries that can be recorded and the default aging time.



By default, the maximum number of cached users is 2% of the user specification, and the maximum cache aging time is 48 hours.


Format
------

**access-user cib-record cache-record-num** *cache-record-num* **cache-aging-time** *cache-aging-time*

**undo access-user cib-record cache-record-num** *cache-record-num* **cache-aging-time** *cache-aging-time*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cache-record-num** *cache-record-num* | Maximum number of cached records for a single process. | The value is an integer ranging from 0 to 100.  The value 0 indicates that no record is generated.  For the CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ: The value is an integer ranging from 0 to 100.  The value 0 indicates that no record is generated.  For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S: The value is an integer that ranges from 0 to 4,096.  The value 0 indicates that no record is generated. |
| **cache-aging-time** *cache-aging-time* | Cache aging time. | The value is an integer that ranges from 0 to 240, in hours.  The value 0 indicates that no record is generated. The default value is 48 hours. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

When an access user fails to be authenticated, you need to check the data in the access user cache table to locate the fault. To facilitate fault locating, run this command to specify the maximum number of CIB cache entries that can be recorded and the aging time.


Example
-------

# In the system view, set the number of CIB cache entries that can be recorded and the aging time.
```
<HUAWEI> system-view
[~HUAWEI] access-user cib-record cache-record-num 200 cache-aging-time 24

```