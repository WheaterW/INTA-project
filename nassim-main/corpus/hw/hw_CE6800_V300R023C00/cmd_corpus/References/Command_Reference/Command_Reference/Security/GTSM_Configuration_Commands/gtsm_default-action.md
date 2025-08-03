gtsm default-action
===================

gtsm default-action

Function
--------



Using the **gtsm default-action** command, you can set the default action to be taken on the packets that do not match the GTSM policies.



By default, the packets that do not match the GTSM policies can pass the filtering.


Format
------

**gtsm default-action** { **drop** | **pass** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **drop** | Indicates that the packets that do not match the GTSM policies cannot pass the filtering and are dropped. | - |
| **pass** | Indicates that the packets that do not match the GTSM policies can pass the filtering. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The GTSM checks the validity of the TTL value of the IP packets that match the GTSM policies. For the packets that do not match the policies, GTSM takes the default action, that is, sending the packets to the main control board or dropping them.



**Precautions**



For the BGP GTSM or BGP4+ GTSM, if "drop" is set as the default GTSM action for packets, you need to configure TTL values for all the packets sent from valid peers in the GTSM policy. If TTL values are not configured for the packets sent from a peer, the device will discard the packets sent from the peer and cannot establish a connection to the peer. Therefore, GTSM enhances security but reduces the ease of use.If only the private network policy or the public network policy is configured, it is recommended that you set the default action to be taken on the packets that do not match the GTSM policy to pass. This prevents the packets of other instances from being dropped by mistake.




Example
-------

# Set the default action to be taken on the packets that do not match the GTSM policies to Drop.
```
<HUAWEI> system-view
[~HUAWEI] gtsm default-action drop

```