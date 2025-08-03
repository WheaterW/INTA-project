display ntp event clock-unsync
==============================

display ntp event clock-unsync

Function
--------

The **display ntp event clock-unsync** command displays the last 10 clock reasons of clock synchronization failures.



Format
------

**display ntp event clock-unsync**



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

To view information about the last 10 reasons of clock synchronization failures, run the **display ntp event clock-unsync** command.



Example
-------

# Display the last 10 reasons of clock synchronization failures.
```
<HUAWEI> display ntp event clock-unsync
 1. Clock source   :  10.1.1.1(vrf1)
    Session type   :  client, configured
    Unsync reason  :  Peer reachability lost
    Unsync time    :  2020-01-30 12:24:44+00:00

 2. Clock source   :  10.2.1.1(vrf2)
    Session type   :  bdcast client (Interface: Eth1/0/1), dynamic
    Unsync reason  :  Authentication failure 
    Unsync time    :  2020-01-30 11:24:44+00:0

 3. Clock source   :  2001:db8::1(vrf1)
    Session type   :  client, configured
    Unsync reason  :  Autokey failure  
    Unsync time    :  2020-01-30 10:24:44+00:00

```


**Table 1** Description of the
**display ntp event clock-unsync** command output

| Item | Description |
| --- | --- |
| Clock source | IP address, NEID or domain name of a server clock. |
| Session type | Session type of the server clock. |
| Unsync reason | Reasons of a synchronization failure. |
| Unsync time | Date and time when clock synchronization failed. |