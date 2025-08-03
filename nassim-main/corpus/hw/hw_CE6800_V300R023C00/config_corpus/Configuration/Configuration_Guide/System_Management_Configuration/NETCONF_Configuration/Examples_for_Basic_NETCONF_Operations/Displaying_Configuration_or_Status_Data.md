Displaying Configuration or Status Data
=======================================

Displaying Configuration or Status Data

#### Basic Operations

1. Construct a filtering condition, for example, interface, and then query details about all interfaces. The corresponding XPath is /ifm/interfaces/interface.
   
   
   
   If you do not need to filter query results, skip this step.
   
   ```
   FILTER = '''<ifm xmlns="urn:huawei:yang:huawei-ifm"> 
                   <interfaces> 
                       <interface> 
                           <name/> 
                       </interface> 
                   </interfaces> 
               </ifm>'''
   ```
2. Construct a <get> or <get-config> packet and query current running data.
   
   
   * Construct a <get> packet.
     ```
     get_reply = m.get([FILTER])
     ```
   * Construct a <get-config> packet.
     ```
     get_reply = get_config(source='running', filter=[FILTER], with_defaults="trim")
     ```
   
   In the preceding example, "m" indicates the following:
   
   ```
   with huawei_connect(host, port=port, user=user, password=password) as m:
   ```

#### Example

This example shows how to configure a simple Python script to connect to the device and implement query.

```
# test_get.py
import sys
import logging 
from ncclient import manager
from ncclient import operations

log = logging.getLogger(__name__)

FILTER = '''<ifm xmlns="urn:huawei:yang:huawei-ifm">
                <interfaces>
                    <interface>
                        <name/>
                        <mtu/>
                    </interface>
                </interfaces>
            </ifm>'''

# Fill the device information and establish a NETCONF session
def huawei_connect(host, port, user, password):
    return manager.connect(host=host,
                           port=port,
                           username=user,
                           password=password,
                           hostkey_verify = False,
                           device_params={'name': "huaweiyang"},
                           allow_agent = False,
                           look_for_keys = False)

def test_get(host, port, user, password):
    #1.Create a NETCONF session
    with huawei_connect(host, port=port, user=user, password=password) as m:
        n = m._session.id
        print("The session id is %s." % (n))

        #2.Send get RPC and print RPC reply
        get_reply = m.get([FILTER])
        print(get_reply)

if __name__ == '__main__':
    test_get(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
```