display telemetry sensor-path
=============================

display telemetry sensor-path

Function
--------



The **display telemetry sensor-path** command displays the sampling path of a Telemetry sensor.




Format
------

**display telemetry sensor-path**


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

To view all sampling sensor paths supported, run the display telemetry sensor-path command.

**Precautions**

The sampling path in the command output depends on the service scenario supported by the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all sampling sensor paths supported. (The sampling paths listed here are for reference only. Sampling paths supported on devices may differ from that provided in this example.)
```
<HUAWEI> display telemetry sensor-path
Yang: The path uses the Yang model sample mode. The sampled data is obtained by the Yang model.
Probe: The path uses the probe sample mode. The sampled data is raw data and does not include data that needs to be processed again (for example, interface bandwidth usage).
------------------------------------------------------------------------------------------------------------------
Type          MinPeriod(ms)  MaxEachPeriod  Path
------------------------------------------------------------------------------------------------------------------
Yang          10000          200            huawei-aaa:aaa/access-user-qrys/access-user-qry
Yang          10000          200            huawei-aaa:aaa/access-user-records/access-user-record
Yang          10000          1024           huawei-arp-security:arp-security/arp-snooping-records/arp-snooping-record
Yang          1000           20             huawei-arp:arp/huawei-fwm-resource:forward-table-resources/forward-table-resource
Yang          1000           20             huawei-arp:arp/huawei-fwm-resource:soft-table-resources/soft-table-resource
Yang          10000          1024           huawei-cpu-memory:cpu-memory/board-cpu-core-infos/board-cpu-core-info
Yang          10000          1024           huawei-cpu-memory:cpu-memory/board-cpu-infos/board-cpu-info
Yang          60000          1024           huawei-cpu-memory:cpu-memory/board-cpu-process-infos/board-cpu-process-info
Yang          10000          1024           huawei-cpu-memory:cpu-memory/board-memory-infos/board-memory-info
Yang          10000          1024           huawei-cpu-memory:cpu-memory/board-process-memory-infos/board-process-memory-info
Yang          10000          1024           huawei-cpu-memory:cpu-memory/board-storage-flash-bad-block-infos/board-storage-flash-bad-block-info
Yang          10000          1024           huawei-cpu-memory:cpu-memory/board-storage-flash-erase-infos/board-storage-flash-erase-info
Yang          10000          1024           huawei-cpu-memory:cpu-memory/board-storage-partition-infos/board-storage-partition-info
Yang          10000          200            huawei-devm:devm/chassiss/chassis/huawei-driver:power-supply-attribute
Yang          10000          200            huawei-devm:devm/huawei-driver:driver/fans/fan
Yang          10000          200            huawei-devm:devm/huawei-driver:driver/power-supplys/power-supply
Yang          1000           150            huawei-devm:devm/ports/port/huawei-pic:ethernet
Yang          30000          1600           huawei-devm:devm/ports/port/huawei-pic:optical-module
Yang          10000          200            huawei-driver:driver/area-energyinfos/area-energyinfo
Yang          10000          200            huawei-driver:driver/temperature2s/temperature2
Yang          1000           20             huawei-fib:fib/huawei-fwm-resource:forward-table-resources/forward-table-resource
Yang          1000           20             huawei-fib:fib/huawei-fwm-resource:soft-table-resources/soft-table-resource
Yang          10000          1024           huawei-host-security:host-security/cpu-port-statistics/cpu-port-statistic
Yang          10000          1024           huawei-host-security:host-security/packet-statistics/packet-statistic
Yang          10000          1024           huawei-host-security:host-security/top-packet-statistics/top-packet-statistic
Yang          10000          --             huawei-ifm:ifm/interfaces/interface/common-statistics
Probe         1000           150            huawei-ifm:ifm/interfaces/interface/mib-statistics
Probe         1000           150            huawei-ifm:ifm/interfaces/interface/mib-statistics/huawei-pic:eth-port-err-sts
Yang          1000           20             huawei-ipv6-nd:ipv6-nd/huawei-fwm-resource:forward-table-resources/forward-table-resource
Yang          1000           20             huawei-ipv6-nd:ipv6-nd/huawei-fwm-resource:soft-table-resources/soft-table-resource
Yang          10000          200            huawei-mac:mac/bd-mac-total-numbers/bd-mac-total-number
Yang          10000          200            huawei-mac:mac/mac-statistics/mac-statistic
Yang          300000         --             huawei-network-instance:network-instance/instances/instance/huawei-l3vpn:afs/af/huawei-routing:routing/routing-manage/topologys/topology/routes/ipv4-prefix-statistics
Yang          300000         --             huawei-network-instance:network-instance/instances/instance/huawei-l3vpn:afs/af/huawei-routing:routing/routing-manage/topologys/topology/routes/ipv4-route-statistics/ipv4-route-statistic
Yang          300000         --             huawei-network-instance:network-instance/instances/instance/huawei-l3vpn:afs/af/huawei-routing:routing/routing-manage/topologys/topology/routes/ipv6-prefix-statistics
Yang          300000         --             huawei-network-instance:network-instance/instances/instance/huawei-l3vpn:afs/af/huawei-routing:routing/routing-manage/topologys/topology/routes/ipv6-route-statistics/ipv6-route-statistic
Yang          10000          512            huawei-qos:qos/global-query/acl-bank-resource-usages/acl-bank-resource-usage
Yang          10000          512            huawei-qos:qos/global-query/acl-resource-usages/acl-resource-usage
Probe         100            300            huawei-qos:qos/global-query/port-buffer-usage-statisticss/port-buffer-usage-statistics
Probe         100            2400           huawei-qos:qos/global-query/queue-buffer-usage-statisticss/queue-buffer-usage-statistics
Alarm         --             --             huawei-routing-notification:ipv4-prefix-exceed
Alarm         --             --             huawei-routing-notification:ipv4-prefix-exceed-clear
Alarm         --             --             huawei-routing-notification:ipv6-prefix-exceed
Alarm         --             --             huawei-routing-notification:ipv6-prefix-exceed-clear
Alarm         --             --             huawei-routing-notification:public-ipv6-prefix-exceed
Alarm         --             --             huawei-routing-notification:public-ipv6-prefix-exceed-clear
Alarm         --             --             huawei-routing-notification:vpn-ipv4-route-exceed
Alarm         --             --             huawei-routing-notification:vpn-ipv4-route-exceed-clear
Alarm         --             --             huawei-routing-notification:vpn-ipv6-prefix-exceed
Alarm         --             --             huawei-routing-notification:vpn-ipv6-prefix-exceed-clear
Alarm         --             --             huawei-routing-notification:vpn-ipv6-route-exceed
Alarm         --             --             huawei-routing-notification:vpn-ipv6-route-exceed-clear
Yang          300000         --             huawei-routing:routing/routing-manage/unicast-route-statistics
OnChange      --             --             huawei-syslog:syslog/loginfos/loginfo
Yang          10000          1024           huawei-system-resources-usage:system-resources-usage/resources/resource
Probe         1000           150            openconfig-interfaces:interfaces/interface/state/counters
Yang          1000           120            other paths
------------------------------------------------------------------------------------------------------------------
note:
1. Recommended configuration: Sampling period = (Total number of sampling instances) / (Number of sampling instances in each minimum sampling period) * (Minimum sampling period).
2. MaxEachPeriod indicates the historical maximum value, not the specification.

```

**Table 1** Description of the **display telemetry sensor-path** command output
| Item | Description |
| --- | --- |
| Type | Sampling type.   * Probe: probe sampling. * Yang: YANG modelâbased sampling. * OnChange+: incremental sampling. |
| MinPeriod(ms) | Minimum sampling interval, the unit is millisecond. |
| MaxEachPeriod | Maximum number of instances that can be collected at the minimum sampling interval. If the CPU rate is limited, the maximum number of instances may not be reached. |
| Path | Sampling sensor path. For details about the supported sampling paths, see Telemetry-based Indicator List. |