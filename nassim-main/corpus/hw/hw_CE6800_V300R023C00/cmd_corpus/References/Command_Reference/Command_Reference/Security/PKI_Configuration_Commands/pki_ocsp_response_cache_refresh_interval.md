pki ocsp response cache refresh interval
========================================

pki ocsp response cache refresh interval

Function
--------



The **pki ocsp response cache refresh interval** command sets the interval at which the OCSP response cache is refreshed.

The **undo pki ocsp response cache refresh interval** command restores the interval at which a PKI entity refreshes the OCSP response cache to the default value.



By default, the interval at which a PKI entity refreshes the OCSP response cache is 5 minutes.


Format
------

**pki ocsp response cache refresh interval** *interval*

**undo pki ocsp response cache refresh interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which the OCSP response cache is refreshed. | The value is an integer that ranges from 1 to 1440, in minutes. The default value is 5. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

A PKI entity refreshes the OCSP response cache periodically and deletes the OCSP responses that have expired based on the interval value.


Example
-------

# Set the interval at which the OCSP response cache is refreshed to 30 minutes.
```
<HUAWEI> system-view
[~HUAWEI] pki ocsp response cache refresh interval 30

```