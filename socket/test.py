from sshtunnel import SSHTunnelForwarder
import requests

remote_user         = 'ubuntu'
remote_host         = 'tcoil.info'
remote_port         = 22
local_host          = '127.0.0.1'
local_port          = 5000
private_server      = 'http://example.com'
private_server_port = 80

try:
    with SSHTunnelForwarder(
         (remote_host, remote_port),
         ssh_username=remote_user,
         ssh_private_key='/home/coil/.ssh/id_rsa',
         remote_bind_address=(local_host, local_port),
         local_bind_address=(local_host, local_port),
         ) as server:

        server.start()
        print('server connected')

        r = requests.get(f'{private_server}:{private_server_port}').content
        print(r)

except Exception as e:
    print(str(e))