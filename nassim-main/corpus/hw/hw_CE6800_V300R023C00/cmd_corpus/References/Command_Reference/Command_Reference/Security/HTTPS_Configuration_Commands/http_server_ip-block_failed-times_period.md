http server ip-block failed-times period
========================================

http server ip-block failed-times period

Function
--------



The **http server ip-block failed-times period** command sets the maximum number of consecutive authentication failures and the period before the client IP address is locked by HTTP.

The **undo http server ip-block failed-times period** command restores the default number of consecutive authentication failures and period before the client IP address is locked by HTTP.



By default, the maximum number of consecutive authentication failures before the client IP address is locked is 6, and the period of consecutive authentication failures is 5 minutes.


Format
------

**http server ip-block failed-times** *failed-times-value* **period** *period-value*

**undo http server ip-block failed-times** *failed-times-value* **period** *period-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *failed-times-value* | Specifies the number of consecutive authentication failures within a period before the client IP address is locked by HTTP. | The value is an integer ranging from 1 to 10. |
| *period-value* | Specifies the interval at which authentication fails before the client IP address is locked by HTTP. | The value is an integer ranging from 1 to 120, in minutes. |



Views
-----

Service-RESTCONF view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run this command to set the number of consecutive authentication failures within a specified period before an IP address is locked. After being locked, the IP address cannot be used to access the device through HTTP until the automatic unlocking time expires. This effectively prevents brute force cracking.


Example
-------

# Lock the client IP address if the client IP address fails to be authenticated for three consecutive times within a period of 6 minutes.
```
<HUAWEI> system-view
[~HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] http server ip-block failed-times 3 period 6

```