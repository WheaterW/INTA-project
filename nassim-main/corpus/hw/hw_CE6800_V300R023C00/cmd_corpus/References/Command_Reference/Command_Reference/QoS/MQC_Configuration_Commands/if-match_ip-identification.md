if-match ip-identification
==========================

if-match ip-identification

Function
--------



The **if-match ip-identification** command configures a matching rule based on the IP identifier in a traffic classifier.

The **undo if-match ip-identification** command deletes a matching rule based on the IP identifier in a traffic classifier.



By default, no matching rule based on the IP identifier is configured in a traffic classifier.


Format
------

**if-match ip-identification** *ip-id* [ **mask** *ip-id-mask* ]

**undo if-match ip-identification** [ *ip-id* [ **mask** *ip-id-mask* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-id* | Specifies the ID of an IP identifier. | The value is an integer ranging from 0 to 65535. |
| **mask** *ip-id-mask* | Specifies the mask length of the IP identifier. | The value ranges from 0 to ffff, in hexadecimal notation. |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **if-match ip-identification** command to classify packets based on the IP identifier in packets so that the device processes packets matching the same traffic classifier in the same manner.

**Precautions**

If you run the **if-match ip-identification** command in the same traffic classifier view multiple times, only the latest configuration takes effect.


Example
-------

# Configure a matching rule based on the IP identifier of 1 in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier c1 type and
[*HUAWEI-classifier-c1] if-match ip-identification 1

```