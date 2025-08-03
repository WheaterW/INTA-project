Configuring a Burst Traffic Buffering Mode
==========================================

Configuring a Burst Traffic Buffering Mode

#### Context

The data buffer is allocated in static+dynamic mode. By default, each interface is allocated with some static buffer to ensure the basic forwarding capability of queues, while the remaining buffer is used as a dynamic buffer to ensure the capability of forwarding burst traffic in queues. When burst packets enter a queue, this dynamic buffer can be utilized. [Table 1](#EN-US_TASK_0000001563870689__table16591648195) lists the buffering modes supported by the device.

When multiple interfaces send traffic to an interface, if there is burst traffic with a volume exceeding the maximum allocated buffer, the device discards excess packets. In this case, run the [**qos burst-mode enhanced**](cmdqueryname=qos+burst-mode+enhanced) command to set the burst traffic buffering mode to enhanced to improve the device's capability to forward burst traffic.

**Table 1** Device buffering modes
| Buffering Mode | Description | Application Scenario |
| --- | --- | --- |
| Standard | Each interface reserves some static buffer. When traffic bursts, each interface queue can preempt a small part of the global dynamic buffer. | Light burst traffic exists on an interface. |
| Enhanced | Each interface reserves some static buffer. When traffic bursts, each interface queue can preempt a large part of the global dynamic buffer. | Heavy burst traffic exists on an interface. |
| Shared | An interface has no reserved static buffer. When traffic bursts, each interface queue can preempt a large part of the global dynamic buffer. | Heavy traffic bursts on few interfaces. If heavy traffic bursts on multiple interfaces, the shared buffer may be exhausted. As a result, other interfaces fail to forward packets at the line rate. |
| Extreme | Each interface reserves some static buffer. When traffic bursts, each interface queue can preempt most of the global dynamic buffer. | Extremely heavy burst traffic exists on an interface. |


![](public_sys-resources/note_3.0-en-us.png) 

For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, the device supports the standard, enhanced, and shared buffering modes.

For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, the device supports only the standard and enhanced buffering modes.

The device supports only the enhanced and extreme buffering modes for the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ.



#### Procedure

* Configure a burst traffic buffering mode on the device.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a burst traffic buffering mode.
     
     
     
     For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, run the following command:
     
     ```
     [qos burst-mode](cmdqueryname=qos+burst-mode) enhanced slot slot-id
     ```
     
     For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, run the following command:
     
     ```
     [qos burst-mode](cmdqueryname=qos+burst-mode) { enhanced | shared }
     ```
     
     For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ, run the following command:
     
     ```
     [qos burst-mode](cmdqueryname=qos+burst-mode) { enhanced | extreme } slot slot-id
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a burst traffic buffering mode on an interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-type interface-number | interface-name }
     ```
  3. Configure a burst traffic buffering mode.
     
     
     
     For the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S, run the following command:
     
     ```
     [qos burst-mode](cmdqueryname=qos+burst-mode) enhanced
     ```
     
     For the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, run the following command:
     
     ```
     [qos burst-mode](cmdqueryname=qos+burst-mode) { enhanced | shared }
     ```
     
     For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, CE6863E-48S8CQ, run the following command:
     
     ```
     [qos burst-mode](cmdqueryname=qos+burst-mode) { enhanced | extreme }
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```