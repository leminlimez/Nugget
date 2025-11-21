import asyncio
import sys
import os

from typing import Optional
from pymobiledevice3.cli.lockdown import async_cli_start_tunnel
from pymobiledevice3.cli.remote import start_tunnel_task, ConnectionType
from pymobiledevice3.lockdown import create_using_usbmux

def create_tunnel(udid: str, out_file: Optional[str] = None, err_file: Optional[str] = None):
    if out_file is not None:
        fout = open(out_file, 'w')
        sys.stdout = fout
    if err_file is not None:
        ferr = open(err_file, 'w')
        sys.stderr = ferr
    # create lockdown service provider and run the tunnel
    if os.name == 'nt':
        service_provider = create_using_usbmux(serial=udid)
        asyncio.run(async_cli_start_tunnel(service_provider, script_mode=True))
    else:
        asyncio.run(start_tunnel_task(connection_type=ConnectionType.USB, secrets=None, udid=udid, script_mode=True))