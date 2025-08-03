dldp interval
=============

dldp interval

Function
--------



The **dldp interval** command sets the interval at which Advertisement packets are sent.

The **undo dldp interval** command restores the default setting.



The default interval at which Advertisement packets are sent is 5 seconds.


Format
------

**dldp interval** *interval*

**undo dldp interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which Advertisement packets are sent. | The value is an integer ranging from 1 to 100, in seconds. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Running the dldp interval command sets the interval at which Advertisement packets are sent. Setting the interval allows DLDP to detect the existence of unidirectional links promptly in different network environments.Generally, the interval at which Advertisement packets are sent is less than one third of the STP convergence time.

* If the interval is set longer than 5 seconds, STP loop may occur before DLDP shuts down the unidirectional link. Because DLDP has to take much time to detect the existence of a unidirectional link, incorrect traffic is forwarded during the detecting process.
* If the interval is set shorter than 5 seconds, the network transmission is burdened.The default interval is recommended.

**Prerequisites**

DLDP has been enabled globally using the **dldp enable** command.

**Configuration Impact**

If DLDP on the ports on both ends or on one port is operating, the peer entries on both ends are removed to re-start a negotiation after the dldp interval command is run.

**Precautions**

If the interval is set on the local device, ensure that the same interval is set on both ends connected by optical fibers. Otherwise, DLDP cannot operate properly.


Example
-------

# Set the interval at which all DLDP-enabled ports send Advertisement packets to 20 seconds.
```
<HUAWEI> system-view
[~HUAWEI] dldp interval 20

```