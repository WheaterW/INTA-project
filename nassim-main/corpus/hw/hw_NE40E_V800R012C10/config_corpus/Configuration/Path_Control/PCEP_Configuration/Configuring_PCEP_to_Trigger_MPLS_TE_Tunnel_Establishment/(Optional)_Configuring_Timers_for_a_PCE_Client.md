(Optional) Configuring Timers for a PCE Client
==============================================

The Keepalive timer, Hold timer, PCReq retransmission timer, and LSP Delegate-hold timer can be set for a PCE client.

#### Usage Scenario

PCEP defines the Keepalive and Hold timers to maintain PCEP sessions. Both ends of a PCEP session start these two timers. Each time the Keepalive timer expires, the local end resends a Keepalive message. If no Keepalive message arrives after the Hold timer expires, the local end considers the PCEP session disconnected.

Hold timer value = 4 x Keepalive timer value

After the Keepalive timer is set, the Hold timer value is automatically updated. However, there are restrictions:

* The Hold timer value must be greater than or equal to the Keepalive timer value.
* Although setting the Keepalive timer value changes the Hold timer value, setting the Hold timer value does not change the Keepalive timer value.
* If the Keepalive time is set larger than 63s, the Hold timer remains 255s.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Keepalive and Hold timers on both ends of a PCEP session are independent and can be assigned different values. The two ends do not negotiate for a consistent value.


If a PCEP connection goes Down, a PCE client starts an LSP Delegate-hold timer. Before the LSP Delegate-hold timer expires, the PCE client attempts to restore the PCEP connection to the existing PCE server. After the LSP Delegate-hold timer expires, the PCE client attempts to select another available PCE server to establish a PCEP session. The PCE client also starts an LSP state timeout timer. Before this timeout timer expires, the delegated LSP status remains. After the timeout timer expires, the PCE client is allowed to change the delegated LSP status in the following situations:

* If the [**mpls te pce cleanup lsp-state**](cmdqueryname=mpls+te+pce+cleanup+lsp-state) command is run on the PCE client, the client deletes the delegate LSP status and automatically uses a local path computation function to reestablish an LSP.
* If the [**mpls te pce cleanup lsp-state**](cmdqueryname=mpls+te+pce+cleanup+lsp-state) command is not run on the PCE client, the client keeps attempting to establish a session with a PCE server.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The PCE client view is displayed.
3. Run [**timer**](cmdqueryname=timer) { **keepalive** *keepalive-value* | **hold** *hold-time* | **request** *request-time* | **delegate-hold** *delegate-value* | **state-timeout** *state-timeout-value* }
   
   
   
   Timers are configured for the PCE client.
   
   
   
   The following table describes the meaning of the parameters in the command. Default timer values are recommended.
   
   | Parameter | Description | Value |
   | --- | --- | --- |
   | **keepalive** *keepalive-time* | Sets a Keepalive timer value. | The value is an integer ranging from 0 to 255, in seconds. The default value is 30s. |
   | **hold** *hold-time* | Sets a Hold timer value. | The value is an integer ranging from 0 to 255, in seconds. The default value is 120s. |
   | **request** *request-time* | Sets a value for the PCReq retransmission timer. | The value is an integer ranging from 5 to 300, in seconds. The default value is 30s. |
   | **delegate-hold** *delegate-value* | Sets a value for the LSP Delegate-hold timer. | The value is an integer ranging from 30 to 255, in seconds. The default value is 30s. |
   | **state-timeout** *state-timeout-value* | Sets a value for the LSP state timeout timer. | The value is an integer ranging from 0 to 2147483647, in seconds. The default value is 259200s (or 72 hours). |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.