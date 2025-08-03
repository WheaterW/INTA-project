Example for Configuring Intelligent Monitoring
==============================================

This section provides an example for configuring three intelligent monitoring functions on an IP RAN for fault locating and resource trend prediction.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001390854196__fig145041236111514), intelligent monitoring is enabled on Device (core ABR1) to intelligently identify exceptions, detect log exceptions, and predict resource trends.**Figure 1** IP RAN scenario  
![](figure/en-us_image_0000001457250773.png)
#### Configuration Roadmap

The configuration roadmap is as follows:![](../../../../public_sys-resources/note_3.0-en-us.png) 

Ensure that any required license has been installed on Device before the configuration.

1. Configure static telemetry subscription.
2. Configure intelligent monitoring.
#### Data Preparation

To complete the configuration, you need the following data:

* Collector's IP address: 10.20.2.1; port number: 10001
* Sampling paths for static telemetry subscription:
  + Intelligent exception identification: huawei-eai-service:eai-service/anomaly-identify-datas/anomaly-identify-data
  + Intelligent log exception detection: huawei-eai-service:eai-service/logrecord-detection-recommend-datas/logrecord-detection-recommend-data
  + Intelligent resource trend prediction: huawei-eai-service:eai-service/resource-prediction-datas/resource-prediction-data


#### Procedure

1. Configure static telemetry subscription.
   
   
   
   # Configure a destination collector.
   
   ```
   [~HUAWEI] telemetry
   ```
   ```
   [~HUAWEI-telemetry] destination-group destination1
   ```
   ```
   [*HUAWEI-telemetry-destination-group-destination1] ipv4-address 10.20.2.1 port 10001 protocol grpc no-tls
   ```
   ```
   [*HUAWEI-telemetry-destination-group-destination1] quit
   ```
   
   # Configure sampling paths.
   
   
   
   ```
   [*HUAWEI-telemetry] sensor-group sensor1
   ```
   ```
   [*HUAWEI-telemetry-sensor-group-sensor1] sensor-path huawei-eai-service:eai-service/anomaly-identify-datas/anomaly-identify-data 
   ```
   ```
   [*HUAWEI-telemetry-sensor-group-sensor1-path] quit
   ```
   ```
   [*HUAWEI-telemetry-sensor-group-sensor1] sensor-path huawei-eai-service:eai-service/logrecord-detection-recommend-datas/logrecord-detection-recommend-data
   ```
   ```
   [*HUAWEI-telemetry-sensor-group-sensor1-path] quit
   ```
   ```
   [*HUAWEI-telemetry-sensor-group-sensor1] sensor-path huawei-eai-service:eai-service/resource-prediction-datas/resource-prediction-data
   ```
   ```
   [*HUAWEI-telemetry-sensor-group-sensor1-path] quit
   ```
   ```
   [*HUAWEI-telemetry-sensor-group-sensor1] quit
   ```
   
   # Create a subscription.
   
   ```
   [*HUAWEI-telemetry] subscription subscription1
   ```
   ```
   [*HUAWEI-telemetry-subscription subscription1] sensor-group sensor1 sample-interval 0
   ```
   ```
   [*HUAWEI-telemetry-subscription subscription1] destination-group destination1
   ```
   ```
   [*HUAWEI-telemetry-subscription subscription1] commit
   ```
   ```
   [~HUAWEI-telemetry-subscription subscription1] quit
   ```
   ```
   [~HUAWEI-telemetry] quit
   ```
2. Configure intelligent monitoring.
   
   
   
   # Enter the EAI view.
   
   ```
   [~HUAWEI] eai
   ```
   
   
   
   # Enable intelligent exception identification.
   
   ```
   [~HUAWEI-eai] intelligent-anomaly-identify enable
   ```
   ```
   [*HUAWEI-eai] commit
   ```
   
   # Enable intelligent log exception detection.
   
   ```
   [~HUAWEI-eai] intelligent-logrecord-detection enable
   ```
   ```
   [*HUAWEI-eai] commit
   ```
   
   # Enable intelligent resource trend prediction.
   
   
   
   ```
   [~HUAWEI-eai] intelligent-resource-prediction enable
   ```
   
   
   ```
   [*HUAWEI-eai] commit
   ```

#### Configuration Files

```
#
telemetry
 #
 destination-group destination1
  ipv4-address 10.20.2.1 port 10001 protocol grpc no-tls
 #
 sensor-group sensor1
  sensor-path huawei-eai-service:eai-service/anomaly-identify-datas/anomaly-identify-data
  sensor-path huawei-eai-service:eai-service/logrecord-detection-recommend-datas/logrecord-detection-recommend-data
  sensor-path huawei-eai-service:eai-service/resource-prediction-datas/resource-prediction-data
 #
 subscription subscription1
  sensor-group sensor1 sample-interval 0
  destination-group destination1
#
eai
 #
 intelligent-anomaly-identify enable
 intelligent-logrecord-detection enable
 intelligent-resource-prediction enable
#
return
```