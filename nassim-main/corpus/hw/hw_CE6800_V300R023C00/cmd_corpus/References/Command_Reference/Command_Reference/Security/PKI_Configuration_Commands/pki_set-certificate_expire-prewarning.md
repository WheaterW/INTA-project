pki set-certificate expire-prewarning
=====================================

pki set-certificate expire-prewarning

Function
--------



The **pki set-certificate expire-prewarning** command sets the expiration warning date for the local certificate and the CA certificate in the memory.

The **undo pki set-certificate expire-prewarning** command restores the expiration warning date for the local certificate and the CA certificate in the memory to the default value.



By default, the expiration warning date for the local certificate and the CA certificate in the memory is ninety days.


Format
------

**pki set-certificate expire-prewarning** *day*

**undo pki set-certificate expire-prewarning**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *day* | Specifies the expiration warning date. | The value is an integer that ranges from 7 to 180. By default, the value is 90. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After this command is executed, you will be prompted the expiration of a certificate in advance. If the system detects that a certificate in the memory is to expire in less than day, the device sends an expiration warning to the user.


Example
-------

# Set the expiration warning date for the local certificate and the CA certificate in the memory as 30 days.
```
<HUAWEI> system-view
[~HUAWEI] pki set-certificate expire-prewarning 30

```