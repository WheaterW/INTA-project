Configuring EPGs and Specifying GBPs
====================================

Configuring EPGs and Specifying GBPs

#### Context

On a network, servers can be added to EPGs as needed and GBPs are specified for the packets that match EPGs. Doing this controls traffic between servers.


#### Procedure

1. Configure an EPG.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Create an EPG and enter its view, or enter the view of an existing EPG.
      
      
      ```
      [traffic-segment segment-id](cmdqueryname=traffic-segment+segment-id) id-value [ segment-name name ] [ intra-epg-behavior { permit | deny | none } ]
      ```
      By default, no EPG exists.![](../public_sys-resources/note_3.0-en-us.png) 
      * When setting **intra-epg-behavior**, you can configure the default access policy for members in a specified EPG.
      * If the default access control policy for members in an EPG is set to **none**, access control is not performed for members in an EPG. In this case, the device performs access control for members in the EPG according to the default access control policy configured using the **traffic-segment same-segment** command. If **permit** or **deny** is selected, the default access control policy corresponding to **permit** or **deny** is used for members in the EPG.
   3. (Optional) Configure the description of the EPG.
      
      
      ```
      [description](cmdqueryname=description) desc-string
      ```
   4. Add a specified IP address to the EPG.
      
      
      
      # Add an IPv4 address to the EPG.
      
      
      
      ```
      [segment-member ip](cmdqueryname=segment-member+ip) ip-address { ip-address-netmask | mask-length } [ vpn-instance vpn-instance-name ]
      ```
      
      # Add an IPv6 address to the EPG.
      
      ```
      [segment-member ipv6](cmdqueryname=segment-member+ipv6) ipv6-addr { ipv6-masklen | ipv6-netmask } [ vpn-instance vpn-instance-name ]
      ```
      
      
      
      By default, no member is added to an EPG.
   5. (Optional) Enable the statistics collection function for the EPG.
      
      
      ```
      [segment-statistics enable](cmdqueryname=segment-statistics+enable)
      ```
      
      By default, the statistics collection function is disabled for an EPG.
   6. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   7. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
2. Specify a GBP.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Create a segment classifier and enter its view, or enter the view of an existing segment classifier.
      
      
      ```
      [segment classifier](cmdqueryname=segment+classifier) classifier-name
      ```
      
      By default, no segment classifier is created in the system.
   3. Set an ACL rule in the segment classifier view.
      
      
      ```
      [rule](cmdqueryname=rule) [ priority ] { permit | deny } { source-segment id-value | destination-segment id-value } * [ [ protocol protocol-number-1 ] | [ protocol { tcp | udp | protocol-number-2 } [ source-port { eq port-num | gt gt-port-num | lt lt-port-num | range begin-port-num end-port-num } ] [ destination-port { eq port-num | gt gt-port-num | lt lt-port-num | range begin-port-num end-port-num } ] ] ]
      ```
      
      By default, no ACL rule is configured in the segment classifier view.
   4. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   5. Create a segment behavior and enter its view, or enter the view of an existing segment behavior.
      
      
      ```
      [segment behavior](cmdqueryname=segment+behavior) behavior-name
      ```
      
      By default, no segment behavior is created.
   6. (Optional) Enable traffic statistics collection for a segment policy.
      
      
      ```
      [statistics enable](cmdqueryname=statistics+enable)
      ```
      
      By default, traffic statistics collection is disabled for a segment policy.
   7. Return to the system view.
      
      
      ```
      [quit](cmdqueryname=quit)
      ```
   8. Create and apply a segment policy and enter its view, or enter the view of an existing segment policy.
      
      
      ```
      [segment policy](cmdqueryname=segment+policy) policy-name
      ```
      
      By default, no segment policy is created.
   9. Bind the segment behavior to the segment classifier in the segment policy.
      
      
      ```
      [classifier](cmdqueryname=classifier) classifier-name behavior behavior-name [ precedence precedence-value ]
      ```
   10. Return to the system view.
       
       
       ```
       [quit](cmdqueryname=quit)
       ```
   11. Apply the segment policy.
       
       
       ```
       [segment-policy](cmdqueryname=segment-policy) policy-name
       ```
   12. Commit the configuration.
       
       
       ```
       [commit](cmdqueryname=commit)
       ```

#### Verifying the Configuration

Run the [**display segment-policy applied-record**](cmdqueryname=display+segment-policy+applied-record) command to check the application status of the segment policy.

Run the [**display segment-policy statistics**](cmdqueryname=display+segment-policy+statistics) command to check segment policy statistics.

Run the [**display traffic-segment configured-information**](cmdqueryname=display+traffic-segment+configured-information) command to check the EPG configuration.

Run the [**display traffic-segment member-information**](cmdqueryname=display+traffic-segment+member-information) command to check information about the EPG to which a specified member belongs.

Run the [**display traffic-segment resource-usage**](cmdqueryname=display+traffic-segment+resource-usage) command to check information about chip resources used by an EPG.

Run the [**display traffic-segment segment-information**](cmdqueryname=display+traffic-segment+segment-information) command to check information about a specified EPG.

Run the [**display traffic-segment statistics**](cmdqueryname=display+traffic-segment+statistics) command to check segment group statistics.