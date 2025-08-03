(Optional) Configuring Timers for a PCE Client
==============================================

The Keepalive timer, Hold timer, and LSP Delegate-hold timer can be set for a PCE client.

#### Usage Scenario

PCEP defines the Keepalive and Hold timers to maintain PCEP sessions. These two types of timers run on both ends of a PCEP session. The local end sends a Keepalive message each time its Keepalive timer expires. If the local end does not receive any Keepalive message from the remote end before the Hold timer expires, the local end considers the session interrupted. Typically, the Keepalive timer value multiplied by 4 is the Hold timer value (Hold timer value = 4 x Keepalive timer value). As such, if the Keepalive timer value is set, the Hold timer value is automatically updated according to the preceding formula. Pay attention to the following restrictions on the Keepalive and Hold timer values:

* The Hold timer value must be greater than or equal to the Keepalive timer value.
* Although Keepalive timer value configuration changes the Hold timer value, Hold timer value configuration does not change the Keepalive timer value.
* If the Keepalive timer value is greater than 63, the Hold timer value is always 255.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The Keepalive (and Hold) timers on both ends of a PCEP session are independent of each other and can be set to different values. In addition, the two ends do not negotiate to use the same value.


If the PCEP connection state becomes idle, the PCE client starts an LSP Delegate-hold timer. Before the LSP Delegate-hold timer expires, the PCE client attempts to restore the PCEP connection to the existing PCE server.

After the LSP Delegate-hold timer expires, the PCE client attempts to select another available PCE server to establish a PCEP session. The PCE client also starts an LSP state timeout timer. Before this timeout timer expires, the delegated LSP status remains. The state of the delegated LSP can change only after the LSP state-timeout timer expires.


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