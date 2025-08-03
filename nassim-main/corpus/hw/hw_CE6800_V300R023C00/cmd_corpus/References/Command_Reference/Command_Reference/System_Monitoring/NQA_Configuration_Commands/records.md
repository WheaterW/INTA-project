records
=======

records

Function
--------



The **records** command sets the maximum number of history and result records that can be saved for an NQA test instance.

The **undo records** command restores the default maximum value.



By default, the maximum number of history records is 60, the maximum number of result records is 5.


Format
------

**records history** *history-number*

**records result** *result-number*

**undo records history**

**undo records result**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **result** *result-number* | Specifies the maximum number of result records that the device can save for each NQA test instance. | The value is an integer ranging from 1 to 10. |
| **history** *history-number* | Specifies the maximum number of history records that the device can save for each NQA test instance. | The value is an integer ranging from 0 to 1000. |



Views
-----

NQA view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The result and history records of an NQA test instance are recorded in the result table and history table, respectively. You can run the following commands to query the result and history statistics and evaluate network quality.

* The **display nqa results** command displays result records of an NQA test instance.
* The **display nqa history** command displays history records of an NQA test instance.To save more result and history records, run the **records** command to change the maximum number of records in the corresponding table.To prevent a great number of records from consuming memory resources, do not configure an excessively large number. The default value is recommended.

**Configuration Impact**

If the maximum number of records has been configured, running the **records** command overrides the previous configuration.

**Precautions**

If parameters need to be changed during the running of the test instance, the system prompts you whether to terminate the test instance. Press "Y" or "N" as required.

* If you press "Y", the test instance is terminated and parameters changed. The settings take effect after being committed. To restart the test instance, run the **start** command.
* If you press "N", the test instance keeps running, and the parameters fail to be modified.

Example
-------

# Set the maximum number of result records for the test instance named user test to 5.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type  icmp
[*HUAWEI-nqa-user-test] records result 5

```

# Set the maximum number of history records for the test instance named user test to 1000.
```
<HUAWEI> system-view
[~HUAWEI] nqa test-instance user test
[*HUAWEI-nqa-user-test] test-type  icmp
[*HUAWEI-nqa-user-test] records history 1000

```