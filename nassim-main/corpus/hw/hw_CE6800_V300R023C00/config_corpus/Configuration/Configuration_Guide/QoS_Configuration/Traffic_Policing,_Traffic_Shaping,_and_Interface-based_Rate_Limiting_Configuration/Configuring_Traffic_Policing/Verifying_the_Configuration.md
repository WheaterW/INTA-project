Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

| Operation | Command |
| --- | --- |
| Check the configured traffic classifiers. | [**display traffic classifier**](cmdqueryname=display+traffic+classifier) [ *classifier-name* ] |
| Check the configured traffic behaviors. | [**display traffic behavior**](cmdqueryname=display+traffic+behavior) [ *behavior-name* ] |
| Check the configured traffic policy. | [**display traffic policy**](cmdqueryname=display+traffic+policy) [ *policy-name* [ **classifier** *classifier-name* ] ] |
| Check the traffic policy application records. | [**display traffic-policy applied-record**](cmdqueryname=display+traffic-policy+applied-record) |
| Check the traffic statistics after MQC-based traffic policing (level-1 CAR) is enabled. | **[**display traffic-policy statistics**](cmdqueryname=display+traffic-policy+statistics)** |
| Check the CAR profile configuration. | [**display qos car**](cmdqueryname=display+qos+car) [ *car-name* ]  This function is not supported by the CE6885-LL (low latency mode). |