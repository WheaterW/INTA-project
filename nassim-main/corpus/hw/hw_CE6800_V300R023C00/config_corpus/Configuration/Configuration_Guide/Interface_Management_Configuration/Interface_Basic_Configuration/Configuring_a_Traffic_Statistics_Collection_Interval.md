Configuring a Traffic Statistics Collection Interval
====================================================

Configuring a Traffic Statistics Collection Interval

#### Context

Interface traffic statistics can be collected at a set interval, allowing them to be subsequently analyzed. With the interface traffic statistics, you can take measures to prevent network congestion and service interruption.

* When congestion occurs, you can set the statistics collection interval on an interface to 300 seconds or less (30 seconds if congestion worsens). Then observe traffic distribution on the interface within a short period of time. If data packets cause congestion, take proper measures to control the rate of the packets.
* When the network bandwidth is sufficient and services are running properly, set the statistics collection interval on an interface to more than 300 seconds. If traffic parameters on an interface are out of the specified range, change the statistics collection interval to observe the traffic statistics in real time.

![](public_sys-resources/note_3.0-en-us.png) 

* The interval set in the system view takes effect on all the interfaces that use the default interval.
* The interval set in the interface view takes effect only on this interface.
* The interval set in the interface view takes precedence over the interval set in the system view.


#### Procedure

* Configure a global traffic statistics collection interval in the system view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure a global traffic statistics collection interval.
     
     
     ```
     [set flow-stat interval](cmdqueryname=set+flow-stat+interval) interval
     ```
     
     By default, the global traffic statistics collection interval is 300s.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure a traffic statistics collection interval on an interface.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
     ```
  3. Configure a traffic statistics collection interval on the interface.
     
     
     ```
     [set flow-stat interval](cmdqueryname=set+flow-stat+interval) interval
     ```
     
     By default, the traffic statistics collection interval on an interface is 300s.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```