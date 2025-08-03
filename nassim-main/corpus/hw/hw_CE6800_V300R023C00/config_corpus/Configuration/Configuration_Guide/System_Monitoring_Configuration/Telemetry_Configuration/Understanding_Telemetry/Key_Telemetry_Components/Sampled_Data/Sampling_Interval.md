Sampling Interval
=================

Sampling Interval

#### Basic Concept

The sampling interval refers to the interval at which the device proactively sends information such as interface traffic statistics, CPU data, or memory data to the collector.


#### Factors Affecting the Sampling Interval

The accuracy of the sampling interval for static telemetry subscription is affected by the following factors:

* Number of sampling instances: You can run the **display telemetry sensor-path** command to check the minimum sampling interval of each sampling path and the maximum number of instances that can be sampled at the minimum sampling interval. The sampling interval that takes effect can be calculated as follows: (Minimum sampling interval x Actual number of instances on the device)/Maximum number of instances that can be sampled at the minimum sampling interval.
  
  In most cases, the number of instances is related to a sampling path. Take the sampling path huawei-ifm:ifm/interfaces/interface/huawei-ifm-ip-statistics:ip-statistics-peak as an example. It has four layers of subdirectories. The ifm and interfaces subdirectories are container nodes, so they have no instances. The interface subdirectory contains all interfaces on the device. Assume that there are 1000 interfaces on the device and 50 instances in the huawei-ifm-ip-statistics:ip-statistics-peak subdirectory; altogether, there are 1050 instances in this sampling path.
* Sampling intervals of data sources: Some data sources have their own sampling intervals. If the sampling interval of a data source is different from the sampling interval configured in telemetry, the effective sampling interval of the data source is affected by half of the telemetry sampling interval. In this case, you can change the telemetry sampling interval or the data source sampling interval ensure that the two sampling intervals are the same.
  
  For example, if the telemetry sampling interval is 5 minutes and the data source sampling interval is 1 minute, then the effective sampling interval is 3 minutes. The reason is explained as follows: To avoid sending too much or little data, telemetry suppresses the sampling interval for each instance based on half of the configured telemetry sampling interval. In this way, the same sampled data of an instance is not sent repeatedly within half of the telemetry sampling interval, and can only be sent again in the next half of the telemetry sampling interval. In this example, repeated data is not sent within half of the telemetry sampling interval, that is, 2 minutes and 30 seconds. As the sampling interval of the data source is 1 minute, repeated data is not sent for additional 30 seconds. Therefore, the effective sampling interval is 3 minutes.
* CPU usage: When the system CPU is busy, the telemetry sampling interval is prolonged.