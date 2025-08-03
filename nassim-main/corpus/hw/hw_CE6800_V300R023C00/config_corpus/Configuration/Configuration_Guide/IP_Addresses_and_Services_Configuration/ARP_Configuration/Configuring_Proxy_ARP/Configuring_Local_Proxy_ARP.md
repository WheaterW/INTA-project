Configuring Local Proxy ARP
===========================

Configuring Local Proxy ARP

#### Context

In the EVC model, after receiving packets, the member interfaces of a BD broadcast these packets in the BD. To minimize broadcast traffic, configure split horizon on the member interfaces that do not need to communicate. After the configuration is complete, users who are served by these interfaces are isolated. However, as services become more diverse and keep increasing, users have growing needs for intra-BD communication. To allow isolated users in a BD to communicate, configure local proxy ARP on the VBDIF interface of the BD.

![](public_sys-resources/note_3.0-en-us.png) 

This function is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, and CE6863E-48S8CQ.



#### Procedure

1. Configure an IP address for a VBDIF interface.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the BD view.
      
      
      ```
      [bridge-domain](cmdqueryname=bridge-domain) bd-id
      ```
   3. Exit the BD view.
      
      
      ```
      quit
      ```
   4. Create a VBDIF interface and enter its view.
      
      
      ```
      [interface vbdif](cmdqueryname=interface+vbdif) bd-id
      ```
      
      The number of the VBDIF interface must be the same as the BD ID specified in Step b.
      
      ![](public_sys-resources/note_3.0-en-us.png) 
      
      The VBDIF interface of a BD goes up only if the BD has a Layer 2 sub-interface that is in the up state. To add a Layer 2 sub-interface to a BD, run the [**bridge-domain**](cmdqueryname=bridge-domain) command in the view of the Layer 2 sub-interface.
   5. Configure an IP address for the VBDIF interface.
      
      
      ```
      [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
      ```
   6. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
2. Enable local proxy ARP.
   1. Enter the system view.
      
      
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the VBDIF interface view.
      
      
      ```
      [interface vbdif](cmdqueryname=interface+vbdif) bd-id
      ```
   3. Enable local proxy ARP.
      
      
      ```
      [arp-proxy local enable](cmdqueryname=arp-proxy+local+enable)
      ```
   4. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```

#### Verifying the Configuration

Run the [**display arp interface**](cmdqueryname=display+arp+interface) { *interface-name* | *interface-type* *interface-number* } command to check ARP entries on an interface.