certificate update expire-time
==============================

certificate update expire-time

Function
--------



The **certificate update expire-time** command specifies when the certificate starts to update. The time is represented by a percentage of the total validity period.

The **undo certificate update expire-time** command restores the default certificate update time.



By default, the certificate is automatically updated when the validity period is only 50% left.


Format
------

**certificate update expire-time** *valid-percent*

**undo certificate update expire-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *valid-percent* | Specifies the remaining percentage of the validity period. | The value is an integer that ranges from 10 to 100. The default value is 50. |



Views
-----

PKI CMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the automatic certificate update through CMPv2 is enabled, the system sends an update request to the CMPv2 server when the specified updated time is reached. This command sets the time (percentage of the total validity period) to update the certificate.


Example
-------

# Enable the automatic certificate update when the used time is 60% of the validity period of the certificate.
```
<HUAWEI> system-view
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test] certificate update expire-time 60

```