Configuring a Device to Redirect IPv4 Public Network Traffic to an SRv6 TE Policy Through Multi-Field Classification
====================================================================================================================

The redirection function can be used to steer IPv4 public network traffic to an SRv6 TE Policy.

#### Prerequisites

Before configuring a device to redirect IPv4 public network traffic to an SRv6 TE Policy through multi-field classification, complete either of the following tasks:

* [Configure an SRv6 TE Policy in controller-based dynamic delivery mode.](dc_vrp_srv6_cfg_all_0116.html)
* [Configure an SRv6 TE Policy in manual configuration mode.](dc_vrp_srv6_cfg_all_0110.html)

#### Context

If some IPv4 public network traffic experiences congestion, QoS multi-field classification can be used to identify and redirect the traffic to an SRv6 TE Policy, resolving the congestion issue. The factors involved in the redirection are an endpoint, color, and SID. If a redirection rule match fails, multi-field classification does not take effect. In this case, the traffic is forwarded over common IP. If the SRv6 TE Policy fails, multi-field classification also fails. In this case, the traffic is also forwarded over common IP.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**traffic classifier**](cmdqueryname=traffic+classifier) *classifier-name* [ **operator** { **and** | **or** } ]
   
   
   
   A traffic classifier is defined and its view is displayed.
3. Configure **if-match** clauses to define matching conditions for IPv4 public network traffic.
   
   
   
   For details, see [Configuring a Traffic Classifier](../ne/dc_ne_qos_cfg_0042.html).
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the traffic classifier view.
5. Run [**traffic behavior**](cmdqueryname=traffic+behavior) *behavior-name*
   
   
   
   A traffic behavior is defined and its view is displayed.
6. Perform either of the following operations to redirect IPv4 public network traffic to an SRv6 TE Policy:
   * Run the [**redirect srv6-te policy**](cmdqueryname=redirect+srv6-te+policy) *endpoint* *color* [ **sid** *sid-ip* ] command to redirect IPv4 public network traffic to a single SRv6 TE Policy.
     
     Note that **sid** *sid-ip* specifies the public network SID of the endpoint of the SRv6 TE Policy.
   
   
   * Run the [**redirect-template srv6-te**](cmdqueryname=redirect-template+srv6-te)*template-name* command to redirect IPv4 public network traffic to a group of SRv6 TE Policies.Before performing this operation, you need to run the following commands in the system view to create an SRv6 TE Policy redirection template and specify an SRv6 TE Policy:
     1. Run the [**redirect template**](cmdqueryname=redirect+template)*template-name* **srv6-te** command to create an SRv6 TE Policy redirection template and enter the template view.
     2. Run the **endpoint** *endpoint* **color** *color* [ **sid** *sid-ip* ] command to redirect IPv4 public network traffic to an SRv6 TE Policy.
        
        This step can be performed multiple times.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can specify the **sid** parameter to redirect IPv4 public network traffic to an IPv4 public network.
   
   The value of *sid-ip* must be an End.DT4 SID, which is configured using the [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt4** or [**opcode**](cmdqueryname=opcode) *func-opcode* **end-dt46** command.
   
   In scenarios where IPv4 public network traffic is redirected to an SRv6 TE Policy, to set a hop limit for IPv6 packets for which a node performs IPv6 encapsulation, run the [**ttl-mode**](cmdqueryname=ttl-mode) { **pipe** | **uniform** } command in the Segment Routing IPv6 view. By default, the **pipe** mode is used.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the traffic behavior view.
8. Run [**traffic policy**](cmdqueryname=traffic+policy) *policy-name*
   
   
   
   A traffic policy is defined and its view is displayed.
9. Run [**classifier**](cmdqueryname=classifier) *classifier-name* **behavior** *behavior-name*
   
   
   
   The traffic behavior is specified for the traffic classifier in the traffic policy.
10. Run [**quit**](cmdqueryname=quit)
    
    
    
    Exit the traffic policy view.
11. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ *.subinterface-number* ]
    
    
    
    The interface view is displayed.
12. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* **inbound**
    
    
    
    The traffic policy is applied to the interface.
13. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.

#### Verifying the Configuration

After configuring the device to redirect IPv4 public network traffic to an SRv6 TE Policy through multi-field classification, perform the following operations to verify the configuration:

* Run the [**display traffic classifier**](cmdqueryname=display+traffic+classifier) { **system-defined** | **user-defined** } [ *classifier-name* ] command to check the traffic classifier configuration.
* Run the [**display traffic behavior**](cmdqueryname=display+traffic+behavior) **user-defined** [ *behavior-name* ] command to check the traffic behavior configuration.
* Run the [**display traffic policy**](cmdqueryname=display+traffic+policy) **user-defined** [ *policy-name* [ **classifier** *classifier-name* ] ] command to check the associations between all traffic classifiers and traffic behaviors or between specified ones in the traffic policy.