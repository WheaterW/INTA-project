http server ip-block reactive
=============================

http server ip-block reactive

Function
--------



The **http server ip-block reactive** command sets the interval after which a locked client IP address is automatically unlocked.

The **undo http server ip-block reactive** command restores the automatic unlocking time of a locked client IP address to the default value.



By default, the automatic unlocking time of a locked client IP address is 5 minutes.


Format
------

**http server ip-block reactive** *reactive-period*

**undo http server ip-block reactive** [ *reactive-period* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *reactive-period* | Specifies the period after which the locked client IP address is automatically unlocked. | The value is an integer ranging from 1 to 1000, in minute. |



Views
-----

Service-RESTCONF view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

You can run this command to set the automatic unlocking time of the locked client IP address. After an IP address is locked, it cannot be used to access the device through HTTP until the automatic unlocking time expires. This effectively prevents brute force cracking.


Example
-------

# Set the interval for automatically unlocking a locked client IP address to 50 minutes.
```
<HUAWEI> system-view
[~HUAWEI] http
[*HUAWEI-http] service restconf
[*HUAWEI-http-service-restconf] http server ip-block reactive 50

```