traffic classifier(IFIT-dcn-instance view)
==========================================

traffic classifier(IFIT-dcn-instance view)

Function
--------



The **traffic classifier** command configures a traffic classifier.

The **undo traffic classifier** command deletes a traffic classifier.



By default, no IFIT traffic classifier is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**traffic classifier** *classifier-name*

**undo traffic classifier** *classifier-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **classifier** *classifier-name* | Specifies the name of a traffic classifier. | The value is a string of 1 to 32 case-sensitive characters, starting with a letter or digit. Spaces and question marks (?) are not supported. |



Views
-----

IFIT dcn-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before configuring IFIT, you can run this command to configure an IFIT traffic classifier. A traffic classifier is used to specify the traffic characteristics of an IFIT measurement domain.

**Prerequisites**

IFIT has been enabled.


Example
-------

# Specify an IFIT traffic classifier.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] traffic classifier class1

```