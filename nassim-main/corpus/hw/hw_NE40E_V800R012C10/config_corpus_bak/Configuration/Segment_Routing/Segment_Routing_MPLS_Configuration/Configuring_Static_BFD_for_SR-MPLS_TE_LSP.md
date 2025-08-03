Configuring Static BFD for SR-MPLS TE LSP
=========================================

Static BFD for SR-MPLS TE LSP can be configured to detect faults on SR-MPLS TE LSPs.

#### Usage Scenario

BFD detects the connectivity of SR-MPLS TE LSPs. If a BFD session fails to go up through negotiation, an SR-MPLS TE LSP cannot go up. Static BFD for SR-MPLS TE LSP is configured to rapidly switch traffic from a primary LSP to a backup LSP if the primary LSP fails.


#### Pre-configuration Tasks

Before configuring static BFD for SR-MPLS TE LSP, complete the following task:

* Configure an SR-MPLS TE tunnel.

#### Procedure

1. Enable BFD globally.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd)
      
      
      
      BFD is enabled globally, and the BFD view is displayed.
      
      You can set BFD parameters only after running the [**bfd**](cmdqueryname=bfd) command to enable BFD globally.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
2. Configure BFD parameters on the ingress.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd) *sessname-value* **bind** **mpls-te** **interface** *tunnel-name* **te-lsp** [ **backup** ] [ **one-arm-echo** ]
      
      
      
      BFD is configured to monitor the primary or backup LSP that is bound to an SR-MPLS TE tunnel, and the BFD session view is displayed.
      
      
      
      If **one-arm-echo** is configured, U-BFD is configured for the SR-MPLS TE tunnel.
      
      If the egress does not support BFD for SR-MPLS TE, BFD sessions cannot be created. To address this issue, configure U-BFD for SR-MPLS TE.
   3. Run [**discriminator**](cmdqueryname=discriminator) **local** *discr-value*
      
      
      
      A local discriminator of a BFD session is set.
   4. Run [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value*
      
      
      
      A remote discriminator of a BFD session is set.
      
      
      
      This command does not need to be run if a U-BFD session is established.
   5. (Optional) Run [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval*
      
      
      
      The minimum interval at which the local device sends BFD packets is changed.
      
      
      
      U-BFD sessions do not support this parameter.
      
      Actual local interval at which BFD packets are sent = MAX { Locally configured interval at which BFD packets are sent, Remotely configured interval at which BFD packets are received }
      
      Actual local interval at which BFD packets are received = MAX { Remotely configured interval at which BFD packets are sent, Locally configured interval at which BFD packets are received }
      
      Local BFD detection period = Actual local interval at which BFD packets are received x Remotely configured BFD detection multiplier
      
      For example: If on the local device, the intervals at which BFD packets are sent and received are 200 ms and 300 ms, respectively, and the detection multiplier is 4; on the remote device, the intervals at which BFD packets are sent and received are 100 ms and 600 ms, respectively, and the detection multiplier is 5, then:
      * On the local device, the actual interval for sending BFD packets is 600 ms calculated using the formula MAX {200 ms, 600 ms}, the actual interval for receiving BFD packets is 300 ms calculated using the formula MAX {100 ms, 300 ms}, and the actual detection period is 1500 ms (300 ms Ã 5).
      * On the remote device, the actual interval between sending BFD packets is 300 ms calculated using the formula MAX {100 ms, 300 ms}, the actual interval between receiving BFD packets is 600 ms calculated using the formula MAX {200 ms, 600 ms}, and the actual detection period is 2400 ms (600 ms Ã 4).
   6. (Optional) Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
      
      
      
      The minimum interval at which the local device receives BFD packets is changed.
      
      
      
      For a U-BFD session, run the [**min-echo-rx-interval**](cmdqueryname=min-echo-rx-interval) command to configure the minimum interval at which the local device receives BFD packets.
   7. (Optional) Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
      
      
      
      A local BFD detection multiplier is set.
   8. (Optional) Run [**bit-error-detection**](cmdqueryname=bit-error-detection)
      
      
      
      Bit-error-triggered SR-MPLS TE LSP switching is enabled.
      
      SR-MPLS TE LSP establishment does not require protocols. Therefore, an SR-MPLS TE LSP can be established as long as a label stack is delivered. If an SR-MPLS TE LSP encounters bit errors, upper-layer services may be affected. With the [**bit-error-detection**](cmdqueryname=bit-error-detection) command being executed, if BFD detects bit errors on the primary LSP bound to the SR-MPLS TE tunnel, it instructs the SR-MPLS TE tunnel to switch traffic to the backup LSP, minimizing the impact on services.
   9. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
3. Configure BFD parameters on the egress.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**bfd**](cmdqueryname=bfd) *sessname-value* **bind** **mpls-te** **interface** *tunnel-name* **te-lsp** [ **backup** ] [ **one-arm-echo** ]
      
      
      
      BFD is configured to monitor the primary or backup LSP that is bound to an SR-MPLS TE tunnel.
      
      
      
      If **one-arm-echo** is configured, a U-BFD session is established to monitor an LSP bound to the SR-MPLS TE tunnel. A Huawei device at the ingress cannot use BFD for SR-MPLS TE LSP to communicate with a non-Huawei device at the egress. In this situation, no BFD session can be established. To establish a BFD session to monitor an LSP bound to the SR-MPLS TE tunnel, configure U-BFD.
   3. Run [**discriminator**](cmdqueryname=discriminator) **local** *discr-value*
      
      
      
      A local discriminator of a BFD session is set.
   4. Run [**discriminator**](cmdqueryname=discriminator) **remote** *discr-value*
      
      
      
      A remote discriminator of a BFD session is set.
      
      
      
      This command does not need to be run if a U-BFD session is established.
   5. (Optional) Run the [**min-tx-interval**](cmdqueryname=min-tx-interval) *tx-interval* command to change the minimum interval at which the local device sends BFD packets.
      
      
      
      U-BFD sessions do not support this parameter.
      
      Actual local interval at which BFD packets are sent = MAX { Locally configured interval at which BFD packets are sent, Remotely configured interval at which BFD packets are received }
      
      Actual local interval at which BFD packets are received = MAX { Remotely configured interval at which BFD packets are sent, Locally configured interval at which BFD packets are received }
      
      Local BFD detection period = Actual local interval at which BFD packets are received x Remotely configured BFD detection multiplier
      
      For example: If on the local device, the intervals at which BFD packets are sent and received are 200 ms and 300 ms, respectively, and the detection multiplier is 4; on the remote device, the intervals at which BFD packets are sent and received are 100 ms and 600 ms, respectively, and the detection multiplier is 5, then:
      * On the local device, the actual interval for sending BFD packets is 600 ms calculated using the formula MAX {200 ms, 600 ms}, the actual interval for receiving BFD packets is 300 ms calculated using the formula MAX {100 ms, 300 ms}, and the actual detection period is 1500 ms (300 ms Ã 5).
      * On the remote device, the actual interval between sending BFD packets is 300 ms calculated using the formula MAX {100 ms, 300 ms}, the actual interval between receiving BFD packets is 600 ms calculated using the formula MAX {200 ms, 600 ms}, and the actual detection period is 2400 ms (600 ms Ã 4).
   6. (Optional) Run [**min-rx-interval**](cmdqueryname=min-rx-interval) *rx-interval*
      
      
      
      The minimum interval at which BFD packets are received locally is set.
      
      
      
      For a U-BFD session, run the [**min-echo-rx-interval**](cmdqueryname=min-echo-rx-interval) command to set the minimum interval at which BFD packets are received locally.
   7. (Optional) Run [**detect-multiplier**](cmdqueryname=detect-multiplier) *multiplier*
      
      
      
      A BFD detection multiplier is set locally.
   8. (Optional) Run [**bit-error-detection**](cmdqueryname=bit-error-detection)
      
      
      
      Bit-error-triggered SR-MPLS TE LSP switching is enabled.
      
      SR-MPLS TE LSP establishment does not require protocols. Therefore, an SR-MPLS TE LSP can be established as long as a label stack is delivered. If an SR-MPLS TE LSP encounters bit errors, upper-layer services may be affected. With the [**bit-error-detection**](cmdqueryname=bit-error-detection) command being executed, if BFD detects bit errors on the primary LSP bound to the SR-MPLS TE tunnel, it instructs the SR-MPLS TE tunnel to switch traffic to the backup LSP, minimizing the impact on services.
   9. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Verifying the Configuration

After successfully configuring BFD for SR-MPLS TE LSP, verify the configuration. For example, check whether the BFD session is up.

* Run the [**display bfd session**](cmdqueryname=display+bfd+session) **mpls-te** **interface** *interface-type* *interface-number* **te-lsp** [ **verbose** ] command to check information about BFD sessions on the ingress.
* Run the following commands to check BFD session information about the egress:
  + Run the [**display bfd session**](cmdqueryname=display+bfd+session) **all** [ **for-lsp** ] [ **verbose** ] command to check the configurations of all BFD sessions.
  + Run the [**display bfd session**](cmdqueryname=display+bfd+session) **static** [ **for-lsp** ] [ **verbose** ] command to check the configurations of static BFD sessions.
* Run the following commands to check BFD statistics:
  + Run the [**display bfd statistics**](cmdqueryname=display+bfd+statistics) **session** **all** [ **for-lsp** ] command to check statistics about all BFD sessions.
  + Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **static** [ **for-lsp** ] command to check statistics about static BFD sessions.
  + Run the [**display bfd statistics session**](cmdqueryname=display+bfd+statistics+session) **mpls-te** **interface** *interface-type* *interface-number* **te-lsp** command to check statistics about BFD sessions that monitor LSPs.