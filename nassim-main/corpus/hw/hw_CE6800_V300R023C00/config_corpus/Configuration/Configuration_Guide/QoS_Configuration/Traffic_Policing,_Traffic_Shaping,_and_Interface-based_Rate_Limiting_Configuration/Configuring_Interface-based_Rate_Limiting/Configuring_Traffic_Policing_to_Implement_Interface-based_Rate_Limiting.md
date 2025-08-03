Configuring Traffic Policing to Implement Interface-based Rate Limiting
=======================================================================

Configuring Traffic Policing to Implement Interface-based Rate Limiting

#### Context

If the rate of traffic sent from users is not limited, burst data continuously sent by users may cause the network to become congested. Therefore, to limit the rate of traffic entering an interface, traffic policing can be configured in the inbound direction of the interface on a network device. When the rate of received packets exceeds the specified traffic policing rate, the device discards excess packets.

![](public_sys-resources/note_3.0-en-us.png) 

This function is not supported by the CE6885-LL (low latency mode).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Disable the device from counting the inter-frame gaps and preambles when the device calculates the traffic policing rate.
   
   
   ```
   [qos car ifg disable](cmdqueryname=qos+car+ifg+disable)
   ```
3. Create and configure a CAR profile.
   
   
   ```
   [qos car](cmdqueryname=qos+car) car-name { [percent](cmdqueryname=percent) percent-value | cir cir-value [ kbps | mbps | gbps ] [ cbs cbs-value [ bytes | kbytes | mbytes ] [ pbs pbs-value [ bytes | kbytes | mbytes ] ] | pir pir-value [ kbps | mbps | gbps ] [ cbs cbs-value [ bytes | kbytes | mbytes ] pbs pbs-value [ bytes | kbytes | mbytes ] ] ] }
   ```
   
   The CAR profile defines the rate limit of traffic policing.
4. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) { interface-type interface-number | interface-name }
   ```
5. Apply the CAR profile to the inbound direction of the interface or the outbound direction of a Layer 2 sub-interface.
   
   
   * Apply the CAR profile to the inbound direction of the interface.
     ```
     [qos car inbound](cmdqueryname=qos+car+inbound) car-name
     ```
     
     After the CAR profile is applied to the inbound direction of the interface, the device rate-limits all incoming service traffic on the interface.
   * Apply the CAR profile to the outbound direction of the interface.
     ```
     [qos car outbound](cmdqueryname=qos+car+outbound) car-name
     ```
     
     After the CAR profile is applied to the outbound direction of the interface, the device rate-limits all outgoing service traffic on the interface.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CAR profile can be applied to the outbound direction of an interface only on the CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, CE8850-HAM, CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL (standard forwarding mode), CE6885-T, and CE6863E-48S8CQ.
     
     Currently, a CAR profile can be applied only to a Layer 2 sub-interface. To enter the Layer 2 sub-interface view, run the [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2** command.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display qos car**](cmdqueryname=display+qos+car) [ *car-name* ] command to check the CAR profile configuration.
* Run the [**display qos car statistics**](cmdqueryname=display+qos+car+statistics) **interface** { *interface-type* *interface-number* | *interface-name* } **inbound** command to check statistics about packets forwarded and discarded on a specified interface on which traffic policing is configured.