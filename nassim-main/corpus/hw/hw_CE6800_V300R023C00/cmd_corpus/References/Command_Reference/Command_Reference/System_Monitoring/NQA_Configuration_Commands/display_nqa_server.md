display nqa server
==================

display nqa server

Function
--------



The **display nqa server** command displays the status of an NQA test server.




Format
------

**display nqa server**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Both the server and client must be configured before starting a TCP or UDP jitter test instance. Otherwise, a test instance cannot be started.

* If a TCP test instance is used, run the **nqa server tcpconnect** command to enable a TCP server.
* If a UDP jitter test instance used, run the **nqa server udpecho** command to enable a UDP server.The **display nqa server** command displays the status of a server. Each time a server is enabled, the count of the servers of this type increases by one.


Example
-------

# Display the status of all the NQA test servers.
```
<HUAWEI> display nqa server
NQA Server Max: 5000             NQA Server Num: 2 
NQA Concurrent TCP Server: 1     NQA Concurrent UDP Server: 1 
-----------------------------------------------------------------
Type           VPN         Address        Port       Status        
-----------------------------------------------------------------
tcpconnect     ---         1.1.1.1         22        ACTIVE         udpecho        vpn1        1.1.1.1         22        NOTINSERVICE

```

**Table 1** Description of the **display nqa server** command output
| Item | Description |
| --- | --- |
| NQA Server Max | Maximum number of NQA servers allowed to be configured. |
| NQA Server Num | Total number of existing NQA servers. |
| NQA Concurrent TCP Server | Number of configured TCP servers. |
| NQA Concurrent UDP Server | Number of configured UDP servers. |
| Type | Type of NQA server. |
| VPN | Name of a VPN instance to which an NQA server belongs. |
| Address | IP address of the NQA server for monitoring services. |
| Port | Port number of the NQA server for monitoring services. |
| Status | Status of an NQA server:   * ACTIVE: The NQA server is enabled. * NOTINSERVICE: The NQA server is disabled. |