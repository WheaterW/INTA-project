radius-server authorization port
================================

radius-server authorization port

Function
--------



The **radius-server authorization port** command configures the port number of a RADIUS authorization server.

The **undo radius-server authorization port** command restores the default configuration.



By default, the port ID of the RADIUS authorization server is 3799.


Format
------

**radius-server authorization port** *port-id*

**undo radius-server authorization port**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *port-id* | Specifies the port ID of the RADIUS authorization server. | The value is an integer that ranges from 1024 to 55535. The default value is 3799. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Run the **radius-server authorization port port-id** command to configure the source port number that the device uses when sending packets to the RADIUS authorization server. After receiving a CoA or DM request packet from the RADIUS authorization server, the device uses the configured port number as the source port number to send a response packet to the RADIUS authorization server.


Example
-------

# Set the port ID of the RADIUS authorization server to 3700.
```
<HUAWEI> system-view
[~HUAWEI] radius-server authorization port 3700

```