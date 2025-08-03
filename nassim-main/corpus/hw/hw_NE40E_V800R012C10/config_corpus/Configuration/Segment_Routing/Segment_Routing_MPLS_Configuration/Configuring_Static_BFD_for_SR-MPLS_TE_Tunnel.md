Configuring Static BFD for SR-MPLS TE Tunnel
============================================

This section describes how to configure static BFD for SR-MPLS TE to detect SR-MPLS TE tunnel faults.

#### Usage Scenario

BFD can be used to monitor to SR-MPLS TE tunnels. If the primary tunnel fails, BFD instructs applications such as VPN FRR to quickly switch traffic, minimizing the impact on services.


#### Pre-configuration Tasks

Before configuring static BFD for SR-MPLS TE, configure SR-MPLS TE tunnels.


#### Procedure

1. Enable BFD globally.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd)
      
      
      
      BFD is enabled globally, and the BFD view is displayed.
      
      You can set BFD parameters only after running the [**bfd**](cmdqueryname=bfd) command to enable BFD globally.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Set ingress BFD parameters.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd) *sessname-value* **bind** **mpls-te** **interface** *tunnel-name*
      
      
      
      BFD for SR-MPLS TE tunnel is configured, and the BFD session view is displayed.
   3. Run [**discriminator**](cmdqueryname=discriminator) **local** *discr-value*
      
      
      
      A local discriminator is configured for the BFD session.
   4. Run [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value*
      
      
      
      A remote discriminator is configured for the BFD session.
      
      
      
      A U-BFD session does not require any remote discriminator.
   5. (Optional) Run [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval*
      
      
      
      The minimum interval at which the local device sends BFD packets is changed.
      
      
      
      This command cannot be run for a U-BFD session.
      
      Actual local interval at which BFD packets are sent = MAX { Locally configured interval at which BFD packets are sent, Remotely configured interval at which BFD packets are received }
      
      Actual local interval at which BFD packets are received = MAX { Remotely configured interval at which BFD packets are sent, Locally configured interval at which BFD packets are received }
      
      Local BFD detection period = Actual local interval at which BFD packets are received x Remotely configured BFD detection multiplier
      
      For example: If on the local device, the intervals at which BFD packets are sent and received are 200 ms and 300 ms, respectively, and the detection multiplier is 4; on the remote device, the intervals at which BFD packets are sent and received are 100 ms and 600 ms, respectively, and the detection multiplier is 5, then:
      * On the local device, the actual interval for sending BFD packets is 600 ms calculated using the formula MAX {200 ms, 600 ms}, the actual interval for receiving BFD packets is 300 ms calculated using the formula MAX {100 ms, 300 ms}, and the actual detection period is 1500 ms (300 ms Ã 5).
      * On the remote device, the actual interval between sending BFD packets is 300 ms calculated using the formula MAX {100 ms, 300 ms}, the actual interval between receiving BFD packets is 600 ms calculated using the formula MAX {200 ms, 600 ms}, and the actual detection period is 2400 ms (600 ms Ã 4).
   6. (Optional) Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
      
      
      
      The minimum interval at which the local device receives BFD packets is changed.
      
      
      
      For a U-BFD session, run the [**min-echo-rx-interval**](cmdqueryname=min-echo-rx-interval) command to set the minimum interval at which the local device receives BFD packets.
   7. (Optional) Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
      
      
      
      The local BFD detection multiplier is changed.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. Set egress BFD parameters.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd) *sessname-value* **bind** **mpls-te** **interface** *tunnel-name*
      
      
      
      BFD is configured to monitor an SR-MPLS TE tunnel.
   3. Run [**discriminator**](cmdqueryname=discriminator) **local** *discr-value*
      
      
      
      A local discriminator is configured for the BFD session.
   4. Run [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value*
      
      
      
      A remote discriminator is configured for the BFD session.
      
      
      
      A U-BFD session does not require any remote discriminator.
   5. (Optional) Run [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval*
      
      
      
      The minimum interval at which the local device sends BFD packets is changed.
      
      
      
      U-BFD sessions do not support this command.
      
      If the reverse link is an IP link, this command cannot be run.
      
      Actual local interval at which BFD packets are sent = MAX { Locally configured interval at which BFD packets are sent, Remotely configured interval at which BFD packets are received }
      
      Actual local interval at which BFD packets are received = MAX { Remotely configured interval at which BFD packets are sent, Locally configured interval at which BFD packets are received }
      
      Local BFD detection period = Actual local interval at which BFD packets are received x Remotely configured BFD detection multiplier
      
      For example: If on the local device, the intervals at which BFD packets are sent and received are 200 ms and 300 ms, respectively, and the detection multiplier is 4; on the remote device, the intervals at which BFD packets are sent and received are 100 ms and 600 ms, respectively, and the detection multiplier is 5, then:
      * On the local device, the actual interval for sending BFD packets is 600 ms calculated using the formula MAX {200 ms, 600 ms}, the actual interval for receiving BFD packets is 300 ms calculated using the formula MAX {100 ms, 300 ms}, and the actual detection period is 1500 ms (300 ms Ã 5).
      * On the remote device, the actual interval between sending BFD packets is 300 ms calculated using the formula MAX {100 ms, 300 ms}, the actual interval between receiving BFD packets is 600 ms calculated using the formula MAX {200 ms, 600 ms}, and the actual detection period is 2400 ms (600 ms Ã 4).
   6. (Optional) Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
      
      
      
      The minimum interval at which the local device receives BFD packets is changed.
      
      
      
      For a U-BFD session, run the [**min-echo-rx-interval**](cmdqueryname=min-echo-rx-interval) command to set the minimum interval at which the local device receives BFD packets.
   7. (Optional) Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
      
      
      
      The local BFD detection multiplier is changed.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After configuring static BFD for SR-MPLS TE, check the configurations.

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) **mpls-te** **interface** *interface-type* *interface-number* [ **verbose** ] command to check BFD session information on the tunnel ingress.
* Check BFD session information on the tunnel egress.
  + To check all BFD sessions' information, run the [**display bfd session**](cmdqueryname=display+bfd+session) **all** [ **for-te** ] [ **verbose** ] command.
  + To check static BFD sessions' information, run the [**display bfd session**](cmdqueryname=display+bfd+session) **static** [ **for-te** ] [ **verbose** ] command.
* Check BFD statistics.
  + To check statistics about all BFD sessions, run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **all** [ **for-te** ] command.
  + To check statistics about static BFD sessions, run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **static** [ **for-te** ] command.
  + To check statistics about BFD sessions, run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **mpls-te** **interface** *interface-type* *interface-number* command.