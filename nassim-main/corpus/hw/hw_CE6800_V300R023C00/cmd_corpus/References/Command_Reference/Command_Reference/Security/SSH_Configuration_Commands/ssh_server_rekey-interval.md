ssh server rekey-interval
=========================

ssh server rekey-interval

Function
--------



The **ssh server rekey-interval** command sets the rekey-interval to update the key pair of the SSH server.

The **undo ssh server rekey-interval** command cancels the rekey-interval to update the key pair of the SSH server and restore the default value.



By default, the rekey-interval to update the key pair of the SSH server is zero, which indicates no update.


Format
------

**ssh server rekey-interval** *hours*

**undo ssh server rekey-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hours* | Specifies the rekey-interval to update the key pair of the SSH server. | It is an integer data type. The value ranges from 0 to 24 hours. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The system automatically updates the key pair of the SSH server at the configured interval. If the client is connected with the server, the public key of the server on the client is not immediately updated. The public key of the server on the client is updated only when the client is re-connected with the server.

**Precautions**

This command applies only to the SSHv1 protocol.


Example
-------

# Configure rekey-interval value as 2 hours.
```
<HUAWEI> system-view
[~HUAWEI] ssh server rekey-interval 2

```