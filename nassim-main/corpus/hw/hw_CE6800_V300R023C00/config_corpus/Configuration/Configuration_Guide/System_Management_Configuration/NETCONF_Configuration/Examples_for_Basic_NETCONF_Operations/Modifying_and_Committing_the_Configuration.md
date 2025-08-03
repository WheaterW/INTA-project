Modifying and Committing the Configuration
==========================================

Modifying and Committing the Configuration

#### Basic Operations

1. Construct the data to be configured, for example, the interface MTU. The corresponding XPath is /ifm/interfaces/interface.
   
   
   ```
   CREATE_INTERFACE = '''<config> 
               <ifm xmlns="urn:huawei:yang:huawei-ifm"> 
                   <interfaces> 
                     <interface> 
                       <name>100GE1/0/1</name>
                       <mtu>1500</mtu> 
                     </interface> 
                   </interfaces> 
                 </ifm> 
   </config>'''
   ```
2. Set the validation mode.
   
   
   * Two-phase validation mode: You need to run the **commit** command for the configuration to take effect after message are delivered.
     1. Deliver an <edit-config> message to modify the <candidate/> configuration database on the server and verify the returned message.
        ```
        rpc_obj = m.edit_config(target='candidate', config=CREATE_INTERFACE)
        _check_response(rpc_obj, 'CREATE_INTERFACE')
        ```
     2. Run the **commit** command to commit the configuration.
        ```
        m.commit()
        ```
   * Trial running mode: You can perform or cancel trial running after messages are delivered.
     1. Deliver an <edit-config> message to modify the <candidate/> configuration database on the server and verify the returned message.
        ```
        rpc_obj = m.edit_config(target='candidate', config=CREATE_INTERFACE)
        _check_response(rpc_obj, 'CREATE_INTERFACE')
        ```
     2. Commit trial running data or discard uncommitted data.
        + Commit trial running data and set a trial running period.
          ```
          m.commit(confirmed=True, timeout='300')
          ```
        + Discard uncommitted data in the <candidate/> configuration database.
          ```
          m.discard_changes()
          ```
        + Commit trial running data and set the **persist** parameter.
          ```
          m.commit(confirmed=True,persist='IQ,d4668')
          ```
        + Cancel a <commit> operation that is being acknowledged.
          ```
          m.cancel_commit(persist_id='IQ,d4668')
          ```In the preceding example, "m" indicates the following:
     ```
     with huawei_connect(host, port=port, user=user, password=password) as m:
     ```
     
     The values of **host**, **port**, **user**, and **password** are those configured for the SSH user.

#### Example

This example shows how to configure a simple Python script to connect to the device and implement configuration.

Deliver the script configuration. In the command, **test\_edit\_config\_running.py** is the script name, **172.16.0.3** is the server address, **client001** is the username, and **YsHsjx\_202206** is the password.

```
$ test_edit_config_running.py 172.16.0.3 22 client001 YsHsjx_202206
RPCReply for CREATE_INTERFACE is <?xml version="1.0" encoding="UTF-8"?>
<rpc-reply message-id="urn:uuid:ad4c7284-49f7-4aef-9d7d-70331de46303" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <ok/>
</rpc-reply>
CREATE_INTERFACE successful
```
The following is an example Python script.
```
# test_edit_config_running.py
import sys
import logging 
from ncclient import manager
from ncclient import operations

log = logging.getLogger(__name__)

CREATE_INTERFACE = '''<config>
                  <ifm xmlns="urn:huawei:yang:huawei-ifm"> 
                     <interfaces> 
                       <interface> 
                         <name>100GE1/0/1</name>
                         <mtu>1500</mtu> 
                       </interface> 
                      </interfaces> 
                   </ifm>
                </config>'''

#Fill the device information and establish a NETCONF session
def huawei_connect(host, port, user, password):
    return manager.connect(host=host,
                           port=port,
                           username=user,
                           password=password,
                           hostkey_verify = False,
                           device_params={'name': "huaweiyang"},
                           allow_agent = False,
                           look_for_keys = False)

def _check_response(rpc_obj, snippet_name):
    print("RPCReply for %s is %s" % (snippet_name, rpc_obj.xml))
    xml_str = rpc_obj.xml
    if "<ok/>" in xml_str:
        print("%s successful" % snippet_name)
    else:
        print("Cannot successfully execute: %s" % snippet_name)      

def test_edit_config_running(host, port, user, password):
    #1.Create a NETCONF session
    with huawei_connect(host, port=port, user=user, password=password) as m:

        #2.Send RPC and check RPC reply
        rpc_obj = m.edit_config(target='running', config=CREATE_INTERFACE)
        _check_response(rpc_obj, 'CREATE_INTERFACE')

if __name__ == '__main__':
    test_edit_config_running(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
```