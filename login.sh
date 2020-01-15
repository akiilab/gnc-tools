#!/bin/bash

if python login.py $@
then
  open /tmp/launch.ica
fi
