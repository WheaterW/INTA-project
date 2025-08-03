clear-records
=============

clear-records

Function
--------



The **clear-records** command deletes history records and result records of an NQA test instance.




Format
------

**clear-records**


Parameters
----------

None

Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After each test instance is complete, test results and history information will be recorded in result and history tables, respectively. You can run the following commands to view the corresponding data and assess network quality.

* The **display nqa results** command displays the results of an NQA test instance.
* The **display nqa history** command displays history records of an NQA test instance.After several test instances are performed to monitor network quality, there may be too many records in the statistics table. In this case, you can run the **clear-records** command to delete history and result records of an NQA test instance.

Example
-------

# Delete statistics about the NQA test instance named user test.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] clear-records

```