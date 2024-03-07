"""
This file contains the mosaik scenario. To start the simulation, just run this
script from the command line::

    $ python scenario.py

"""
import os
import asyncio
import mango

def check_file_descriptors():
    if os.name == 'posix':
        try:
            descs = os.listdir(os.path.join("/proc", str(os.getpid()), "fd"))
            print(f"file descriptors in use: {len(descs)}")
        except:
            pass

class Agent(mango.Agent):
    def __init__(self, container, **params):
        super().__init__(container)

async def _create_container(host, port):
        print('1 container is created')
        return await mango.create_container(addr=(host, port))
    
async def _create_agent(container, **params):
        agent = Agent(container, **params)
        print('1 agent is created')
        return agent

host = '0.0.0.0'
port = 5678
loop = asyncio.get_event_loop()
container = loop.run_until_complete(_create_container(host, port))
agent = loop.run_until_complete(_create_agent(container))
check_file_descriptors()
agent = loop.run_until_complete(_create_agent(container))
check_file_descriptors()