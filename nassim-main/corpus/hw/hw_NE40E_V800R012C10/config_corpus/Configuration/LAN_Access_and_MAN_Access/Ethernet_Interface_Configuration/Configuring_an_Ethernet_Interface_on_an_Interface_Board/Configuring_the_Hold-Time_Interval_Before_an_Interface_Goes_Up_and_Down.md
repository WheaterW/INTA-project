Configuring the Hold-Time Interval Before an Interface Goes Up/Down
===================================================================

When an interface frequently alternates between up and down, flapping may occur. To prevent the problem, you can configure the hold-time interval before an interface goes up or down. If the VS mode is used, this configuration is supported only by the admin VS.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. To configure the hold-time interval before interfaces go up or down globally, perform either of the following configurations as needed.
   
   
   * To set the hold-time interval before interfaces go up globally, run the [**carrier up-hold-time**](cmdqueryname=carrier+up-hold-time) *interval* command.
   * To set the hold-time interval before interfaces go down globally, run the [**carrier down-hold-time**](cmdqueryname=carrier+down-hold-time) *interval* command.
   
   If a non-default hold-time interval is set on an interface, the interval set on the interface takes effect. If an interface uses the default hold-time interval, the global configuration takes effect.
3. To set the hold-time interval on a specified interface, run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
4. Run either of the following commands as needed.
   
   
   * To set the hold-time interval before an interface goes up, run the [**carrier up-hold-time**](cmdqueryname=carrier+up-hold-time) *interval* command.
   * To set the hold-time interval before an interface goes down, run the [**carrier down-hold-time**](cmdqueryname=carrier+down-hold-time) *interval* command.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.