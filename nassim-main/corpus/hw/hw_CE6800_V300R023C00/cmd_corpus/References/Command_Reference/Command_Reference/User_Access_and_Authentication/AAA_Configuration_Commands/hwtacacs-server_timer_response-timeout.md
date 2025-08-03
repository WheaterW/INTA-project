hwtacacs-server timer response-timeout
======================================

hwtacacs-server timer response-timeout

Function
--------

The **hwtacacs-server timer response-timeout** command sets the response timeout interval of an HWTACACS server.

The **undo hwtacacs-server timer response-timeout** command restores the default response timeout interval of an HWTACACS server.

By default, the response timeout interval for an HWTACACS server is 5 seconds.



Format
------

**hwtacacs-server timer response-timeout** *interval*

**undo hwtacacs-server timer response-timeout**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the response timeout interval of an HWTACACS server. | The value is an integer ranging from 1 to 300, in seconds. Default:5 |




Views
-----

HWTACACS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

After the device sends a request packet to the HWTACACS server, if the device does not receive any response packet from the server within the specified response timeout interval:- If only one HWTACACS server is configured, the device does not retransmit the request to this server.- If both active/standby HWTACACS servers are available and the TCP link between them works normally, the device retransmits the request to the standby server after timeout. If the TCP link is broken during the timeout interval, the device immediately retransmits the request to the standby server.This improves reliability of HWTACACS authentication, authorization, and accounting.The default value is recommended.

**Precautions**

You can modify this configuration only when the HWTACACS server template is not in use.



Example
-------

# Set the response timeout interval of an HWTACACS server to 30s.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template test1
[*HUAWEI-hwtacacs-test1] hwtacacs-server timer response-timeout 30

```