Configuring ATM Complex Traffic Classification
==============================================

ATM complex traffic classification can be configured to
classify and manage traffic that enters an ATM network or that is
transmitted over an ATM network, and then provide differentiated services.

#### Usage Scenario

You are required to classify
and limit the traffic that enters an ATM network or that flows in
an ATM network, for example:

* To differentiate packet types such as voice packets, video
  packets, and data packets, and provide different bandwidths and latencies
  for those types of packets
* To handle traffic coming from different users and provide different
  bandwidths and priorities for those types of packets

You can classify packets according to parameters such as the
DSCP value, the protocol type, the IP address, or the port number,
and then provide differentiated services and configure QoS traffic
policies based on the ATM complex traffic classification.


#### Pre-configuration Tasks

Before configuring
the ATM complex traffic classification, complete the following tasks:

* Configuring the link attributes of ATM interfaces
* Configuring IP addresses for ATM interfaces
* Configuring PVC or PVP parameters
* Configuring IPoA services

![](../../../../public_sys-resources/note_3.0-en-us.png) 

An ATM interface configured with IPoA services
supports the ATM complex traffic classification whereas an ATM interface
configured with ATM transparent cell transmission services does not
support the ATM complex traffic classification.



#### Configuration Procedures

**Figure 1** Flowchart for Configuring ATM Complex Traffic Classification
  
![](images/fig_dc_ne_qos_cfg_01238801.png)


[Defining Traffic Classifiers](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012390.html)

Before configuring complex traffic classification, you need to define a traffic classifier.

[Defining Traffic Behaviors](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012391.html)

This section describes traffic behaviors and how to configure them.

[Defining Traffic Policies](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012392.html)

After defining traffic classifiers and traffic behaviors, you need to configure traffic policies by associating traffic classifiers with traffic behaviors.

[Applying Traffic Policies](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012393.html)

Class-based traffic policies take effect only after they are applied to interfaces.

[Verifying the Configuration of ATM Complex Traffic Classification](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_qos_cfg_012394.html)

After ATM complex traffic classification is configured, you can view information about the configured traffic classifiers, traffic behaviors, traffic policies in which the specified classifiers and behaviors are associated, and traffic statistics on interfaces.